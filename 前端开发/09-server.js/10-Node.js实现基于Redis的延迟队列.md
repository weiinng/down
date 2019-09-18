# Node.js实现基于Redis的延迟队列

写代码的过程中，偶尔会因为业务需求而用到延迟队列，经典场景如：订单的超时关闭，签到提醒等，之前一般选择现成的云服务，但这次本着学习的目的就尝试自己实现了一番。实现的指导思想来自[有赞延迟队列设计](https://tech.youzan.com/queuing_delay/)这篇文章，对于延迟队列使用场景、作用不太清楚的朋友可以通过这篇文章补一补。

核心流程与设计理念照有赞的文章来，自己这篇文章主要讲实现的方式与过程中遇到的问题，所以在看本文之前建议先阅读一遍有赞原文。

[代码](https://gist.github.com/Shasharoman/2b3255e0d2c663a58a874b92a5da6fc5)依赖所在的业务框架环境所以无法独立运行，但核心逻辑都包含在内，请与文字结合理解。

## 接口

由于自己的目的不是独立运行一个延迟队列的服务，所以接口方面就没有做成标准的：添加、获取、完成、删除，而是与业务绑定，具体下来主要就两个接口：

- pushTask(id, topic, delay, ttr, body)

> 往topic中push一个task，延迟delay秒后执行，ttr指的是task从ready中被取走而没有被确认消费成功，间隔多久又会变成ready，body是业务决定的消息内容

> // 之所以不用job，是因为task在视觉上比job好看

- onTopic(topic, fn, frequency)

> 等待task就绪，当某topic中有就绪的task时，会调用fn，fn返回一个Promise，成功则会从队列中移除task并保存到mysql，frequency是onTopic获取就绪task消费完成后取下一个的间隔时间

这两个接口分别对应生产者和消费者使用，拿关闭订单举例，负责关闭订单的模块调用onTopic，而其他产生订单的地方则调用pushTask即可。

## 遇到的问题

自己读了两遍有赞的那篇文章后没开始写之前，觉得理论设计已经到位，那实现应该会比较简单，但在真正撸代码的过程中，还是冒出一些问题，挑重要的与大家分享：

### Redis数据结构选择

能实现这个延迟队列，基本全靠Redis，那不同数据应该决定使用何种数据结构？

我们用定时器扫描delay task，发现task到期了，就将其移动到ready中，在这一步针对delay task的数据结构选择，需要着重考虑扫描的效率，如以下两个方案：

> A方案：使用Hash，taskId => timestamp，每次在代码内扫描整个Hash列表，挑选到期的放入ready中

> B方案：使用Sorted Set，(member: taskId，score: timestamp)，每次使用zrangebyscore获取timestamp在(now - before，now)之间的数据，然后移动到ready中

根据常识，B方案的扫描效率应该远高于A，所以在这里我选择用B方案存储delay task。其他诸如ready、pool等数据应该选用何种数据结构存储，这里就不做具体分析了，但可以肯定的是选择不同结构对后续的实现会带来不同影响。

### task如何由delay转变成ready

当我们选择Sorted Set作为delay task的存储数据结构后，假如ready task选的是List，接下来面临的问题是如何将扫描到的到期task移动到ready中。

这里的核心问题是保证事务，为了保证task只存在delay或ready中，我们不能用代码从delay中删除然后再添加到ready中，因为这样的两个步骤无法保证事务，可能你刚从delay中取出一个task，然后应用因为异常导致重启，如果没有其他措施，那这个task就丢失了。

我在这里想了两个方案：

- A方案：利用Redis multi

> Redis multi支持一串命令保证事务，具体做法是先用zrangebyscore扫描delay得到一个taskId，然后通过multi做两个操作：从delay中移除，添加到ready

> 这个方案依赖zrangebyscore先扫描出taskId，然后再做操作，这就不支持多个实例同时扫描，因为可能导致一个taskId被插入到ready多次，而如果要支持多实例扫描，就需要引入锁

- B方案：借助lua脚本

> A方案之所以不支持多实例，是因为Redis multi中的指令不能获取前一条指令的执行结果，借助lua脚本能满足这一点，也就可以避免锁的引入同时支持多实例

为避免使用锁，自己在这里选择了B方案。

### 如何从ready中消费task

问题与上一个类似，重点依旧是事务，但有一定差别，前者从delay => ready都是Redis中的操作，可以借助Redis的事务特性，而从ready中消费task，是Redis + 代码执行，这是无论如何都无法保证事务的，所以只能是尽量考虑周全，不要出现task丢失、重复等问题，出现的话也尽量保持有记录，可以挽救。

目前在这一步我自己想了一个方案：

除用Redis-List结构存储ready task外，再加入一个用Redis-List结构存储的buffer，每次从ready中消费task时，借助Redis的rpoplpush操作，保证task从ready中移出的同时加入buffer，然后程序再针对取出的task进行处理，如果程序异常，buffer中的task不会受到影响，可为后续补救修复提供条件。

## Redis数据结构

分析了几个问题后，在这里把存数据所用到的Redis结构全部列出来，讲述具体实现逻辑时还会涉及这些数据，不懂的可以翻到这里再看一下。

自己这次存储在Redis中的六个数据，其Redis结构分别如下：

- pool

> Hash，taskId => JSON.stringify(task)，taskId对应的task({id, topic, timestamp, ttr, body}) JSON stringify后内容

- status

> Hash，taskId => status(delay|ready|ok)，taskId对应的task状态，状态一共三种：delay(等待时间满足)、ready(等待被消费)、ok(消费完成)

- topic

> Hash，taskId => taskTopic，taskId对应的task topic，为了在lua脚本中获取taskId对应的topic而设计

- delay

> Sorted Set，(member: taskId，score: timestamp)，taskId与task到期的绝对时间戳，这个结构是为了快速扫描到可转换为ready的task

- ready:{topic}

> List，[taskId]，已经就绪的taskId，onTopic就是从这个结构里面取数据

- buffer

> List，[taskId]，辅助作用，从ready:{topic}中取task时，为避免因应用异常导致task丢失，因而每次获取ready task时，使用rpoplpush保证buffer中有一个备份

我觉得有经验的朋友，在看完所有的Redis数据结构后，已经能基本预测我的实现逻辑了。如果你看完这些结构，还是不清楚应该如何实现，那就继续往下看一下核心逻辑吧。

## 核心逻辑

### 主流程

从pushTask开始到task消费完成来看，整个Q的主要流程：

> - Q收到task，设置task对应的Redis数据pool、status、topic、delay
> - 定时器间隔轮询delay列表发现task满足条件（时间、状态），将其移动到ready中，同时设置其status为ready
> - 定时器间隔轮询ready发现task，使用rpoplpush的方式取出task并移动到buffer中
> - 将task按ttr继续添加到delay中并设置status为delay
> - 消费者处理task
> - 处理失败：不做任何处理，等待ttr时间过后，会再次被消费者处理
> - 处理成功：设置task status为ok，随后持久化该task，并删除redis中与该task相关数据
> - 定时器间隔轮询buffer，若pool中不存在或status为ok则删除，否则rpoplpush自己

### pushTask(id, topic, delay, ttr, body)

pushTask实现比较简单，就是组织task的结构，然后将数据存入Redis中。

```
let task = {...};

redis.multi
    hset pool task.id JSON.stringify(task)
    hset status task.id 'delay'
    hset topic task.id task.topic
    zadd delay task.timestamp task.id
redis.exec
```

### onTopic(topic, fn, frequency)

onTopic是消费者接收task的入口，内部实现比pushTask复杂一些，下面的伪代码没有做任何异常处理，转换为真代码时，仔细分析里面的可能异常，会有不少收获。

```
pop task: topic 
    taskId = redis.rpoplpush ready:{topic} buffer
    task = redis.get pool taskId
    update timestamp with task.ttr && add to delay again
    return task

finish task: taskId
    redis.hset status {taskId} ok
    insert task to mysql
    redis.multi
        hdel status {taskId}
        hdel topic {taskId}
        hdel pool {taskId}
        zrem delay {taskId}
    redis.exec        
        
task = pop task: {topic}
if {fn}(task) is ok
    finish task: task.id
setTimeout onTopic {topic, fn, frequency}
```

定时扫描delay task与清理buffer task，这两件事都通过Redis eval + lua脚本完成，详细细节请在[非完整代码](https://gist.github.com/Shasharoman/2b3255e0d2c663a58a874b92a5da6fc5)中查看。

## 优化

自己实现的这个Q，简单使用可以但还差一点健壮性，具体有以下几点：

### 缺乏task重试次数限制

目前task从ready中被取出后，会按其ttr再次放入delay中，这其中如果某消费者持续异常，会导致这个task一直在队列中经历这个循环。

但目前delay的扫描可以决定时间间隔，比如每次都只扫描
*n**o**w* − 3600*s*，*n**o**w*
之间的就绪task，可以部分缓解这种情况。

加入一些辅助结构和逻辑，可以支持task消费次数限制特性，但目前觉得不是非常必要。

### 针对buffer的处理不完善

设计buffer是为了避免task丢失，但目前并没有利用起来，目前异常的task会一直在buffer中堆积，但没有相关逻辑去进行处理。

此处我认为可以弄一个低频定时任务对buffer做全扫描，然后将异常task进行归档或上报。

### finishTask缺乏异常补救措施

目前finishTask的逻辑除了设置status为ok外，还包含持久化task与清除task在Redis中的数据，但如果这两个后续步骤发生异常，会导致数据遗留在Redis中，缺少重试机制。

这里我认为也可以弄一个低频定时任务做异常修复。

## 总结

这个队列核心代码不到200行，但整体弄下来花了数小时，有些事不去尝试，就不知道会遇到什么问题，既然做了，做好填坑准备，如果哪位朋友发现有BUG，欢迎邮件，谢谢。

// 通过实现这个队列，感觉有些事没有想象的那么复杂，但同样不简单～