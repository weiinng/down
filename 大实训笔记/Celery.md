title: celery 概念及操作

Date: 2017-08-11 10:20

Modified: 2017-08-11 19:30
Category: 技术
Tags: pelican, publishing
Slug: git
Authors: 夏伟

Tags:celery

Celery是一个异步任务的调度工具。

Celery 是 Distributed Task Queue，分布式任务队列，分布式决定了可以有多个 worker 的存在，队列表示其是异步操作，即存在一个产生任务提出需求的工头，和一群等着被分配工作的码农。

在 Python 中定义 Celery 的时候，我们要引入 Broker，中文翻译过来就是“中间人”的意思，在这里 Broker 起到一个中间人的角色。在工头提出任务的时候，把所有的任务放到 Broker 里面，在 Broker 的另外一头，一群码农等着取出一个个任务准备着手做。

这种模式注定了整个系统会是个开环系统，工头对于码农们把任务做的怎样是不知情的。所以我们要引入 Backend 来保存每次任务的结果。这个 Backend 有点像我们的 Broker，也是存储任务的信息用的，只不过这里存的是那些任务的返回结果。我们可以选择只让错误执行的任务返回结果到 Backend，这样我们取回结果，便可以知道有多少任务执行失败了。

Celery(芹菜)是一个异步任务队列/基于分布式消息传递的作业队列。它侧重于实时操作，但对调度支持也很好。Celery用于生产系统每天处理数以百万计的任务。Celery是用Python编写的，但该协议可以在任何语言实现。它也可以与其他语言通过webhooks实现。Celery建议的消息队列是RabbitMQ，但提供有限支持Redis, Beanstalk, MongoDB, CouchDB, 和数据库（使用SQLAlchemy的或Django的 ORM） 。Celery是易于集成Django, Pylons and Flask，使用 django-celery, celery-pylons and Flask-Celery 附加包即可。

在Celery中几个基本的概念，需要先了解下，不然不知道为什么要安装下面的东西。概念：Broker、Backend。

## 什么是broker？

broker是一个消息传输的中间件，可以理解为一个邮箱。每当应用程序调用celery的异步任务的时候，会向broker传递消息，而后celery的worker将会取到消息，进行对于的程序执行。好吧，这个邮箱可以看成是一个消息队列。其中Broker的中文意思是 经纪人 ，其实就是一开始说的 消息队列 ，用来发送和接受消息。这个Broker有几个方案可供选择：RabbitMQ (消息队列)，Redis（缓存数据库），数据库（不推荐），等等

## 什么是backend？

通常程序发送的消息，发完就完了，可能都不知道对方时候接受了。为此，celery实现了一个backend，用于存储这些消息以及celery执行的一些消息和结果。Backend是在Celery的配置中的一个配置项 CELERY_RESULT_BACKEND ，作用是保存结果和状态，如果你需要跟踪任务的状态，那么需要设置这一项，可以是Database backend，也可以是Cache backend，具体可以参考这里： CELERY_RESULT_BACKEND 。

对于 brokers，官方推荐是 rabbitmq 和 redis，至于 backend，就是数据库。为了简单可以都使用 redis或者rabbitmq

Celery的架构由三部分组成，消息中间件（message broker），任务执行单元（worker）和任务执行结果存储（task result store）组成。

## 消息中间件

Celery本身不提供消息服务，但是可以方便的和第三方提供的消息中间件集成。包括，RabbitMQ, Redis, MongoDB (experimental), Amazon SQS (experimental),CouchDB (experimental), SQLAlchemy (experimental),Django ORM (experimental), IronMQ

## 任务执行单元

Worker是Celery提供的任务执行的单元，worker并发的运行在分布式的系统节点中。

## 任务结果存储

Task result store用来存储Worker执行的任务的结果，Celery支持以不同方式存储任务的结果，包括AMQP, redis，memcached, mongodb，SQLAlchemy, Django ORM，Apache Cassandra, IronCache 等。

因为涉及到消息中间件（在Celery帮助文档中称呼为中间人），为了更好的去理解文档中的例子，可以安装两个中间件，一个是RabbitMQ,一个redis。

具体操作：

<https://v3u.cn/a_id_99>



# python3.7+Tornado5.1.1+Celery3.1+Rabbitmq3.7.16实现异步队列任务

```
#安装服务
brew install rabbitmq
#启动服务
brew services start rabbitmq
```



  Win10系统就要下载安装包进行安装了，由于rabbitmq是基于erlang的，所以要首先安装erlang

​    1、首先，下载并运行Erlang for Windows 安装程序 （地址：http://www.erlang.org/downloads）下载完毕并安装（注    意：安装目录请选择默认目录）

​    ![img](https://v3u.cn/v3u/Public/js/editor/attached/image/20190731/20190731092117_21738.png)
​    2、下载 RabbitMQ，（地址：http://www.rabbitmq.com/download.html ）（注意：安装目录请选择默认目录）
​    ![img](https://v3u.cn/v3u/Public/js/editor/attached/image/20190731/20190731092131_65666.png)

​    安装成功后，启用web管理UI，进入RabbitMQ Serverrabbitmq_server-3.6.6sbin，输入命令rabbitmq-plugins enable rabbitmq_management

​    在系统的开始菜单里找到RabbitMQ的启动菜单，启动服务

​    浏览器输入，http://localhost:15672/，使用默认用户guest/guest进入网页端控制台：

​    ![img](https://v3u.cn/v3u/Public/js/editor/attached/image/20190731/20190731092415_65324.png)

​    代表没有问题了

​    然后安装tornado和celery，注意指定版本号



```
pip3 install tornado==5.1.1
pip3 install celery ==3.1
pip3 install pika ==0.9.14
pip3 install tornado-celery
pip3 install flower
```

 需要注意一点，由于python3.7中async已经作为关键字存在，但是有的三方库还没有及时修正，导致它们自己声明的变量和系统关键字重名，所以我们要深入三方库的源码，帮他们修改async关键字为async_my，需要修改的文件夹和文件包含但不限于：

​    /site-packages/pika/adapters/libev_connection.py

​    /site-packages/celery下面的文件

​    /site-packages/kombu下面的文件夹

​    在tornado项目下新建一个任务队列文件task.py：



```
import time
from celery import Celery
from func_tool import mail

C_FORCE_ROOT=True

celery = Celery("tasks", broker="amqp://guest:guest@localhost:5672")
celery.conf.CELERY_RESULT_BACKEND = "amqp"


@celery.task
def sleep(seconds):
    time.sleep(float(seconds))
    return seconds

@celery.task
def sendmail(title,text,tomail):
    mail(title,text,tomail)
    return '发送邮件成功'

if __name__ == "__main__":
    celery.start()
```

然后编写服务端代码: 



```
from celery import Celery
from tornado import gen
import tcelery
sys.path.append("..")
import task

#异步任务
class CeleryHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        response = yield gen.Task(task.sendmail.apply_async,args=['你好','非常好','164850527@qq.com'])
        self.write('ok')
        self.finish()
```

路由器代码:



```
import tornado.web
from views import Index
import config


#路由 

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/celery", Index.CeleryHandler)
        ]
        super(Application,self).__init__(handlers,**config.setting)
```

程序入口代码server.py: 



```
import tornado.ioloop
import tornado.httpserver
import config
 
from application import Application
 
 
 
 
if __name__ == "__main__":
    print('启动...')
    app = Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    # httpServer.listen(8888)
    #绑定端口
    httpServer.bind(config.options['port'])
    #开启5个子进程（默认1，若为None或者小于0，开启对应硬件的CPU核心数个子进程）
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()
```

进入项目目录，分别启动tornado服务，celery服务，以及flower服务 



```
python server.py
celery -A task worker --loglevel=info
celery flower -A task --broker=amqp://guest:guest@localhost:5672//
```





**RabbitMQ**是实现了高级消息队列协议（AMQP）的开源消息代理软件（亦称面向消息的中间件）。RabbitMQ服务器是用[Erlang](https://baike.baidu.com/item/Erlang)语言编写的，而群集和故障转移是构建在[开放电信平台](https://baike.baidu.com/item/%E5%BC%80%E6%94%BE%E7%94%B5%E4%BF%A1%E5%B9%B3%E5%8F%B0)框架上的。所有主要的编程语言均有与代理接口通讯的客户端[库](https://baike.baidu.com/item/%E5%BA%93)。  



## MQ概述

消息队列技术是分布式应用间交换信息的一种技术。

消息队列可驻留在内存或磁盘上,队列存储消息直到它们被应用程序读走。

通过消息队列，应用程序可独立地执行--它们不需要知道彼此的位置、或在继续执行前不需要等待接收程序接收此消息。

MQ主要作用是接受和转发消息。你可以想想在生活中的一种场景：当你把信件的投进邮筒，邮递员肯定最终会将信件送给收件人。我们可以把MQ比作 邮局和邮递员。

MQ和邮局的主要区别是,它不处理消息,但是,它会接受数据、存储消息数据、转发消息。





# Celery框架

异步任务任务队列。 

tornado  默认的机制是同步机制， 要以异步的方式。

Celery框架原理：

由上往下 顺序执行就是同步形式，把同步的 代码，帮你异步化， 以同步的形式，写异步的代码，开发效率还在高的水平线上， 性能还没有损失。 

celery ，就是服务员的角色，celery本身需要集成消息中间件--> rabbitmq 和redis， 

broker ：可以理解为tracker（调度） 收集任务再分发过去。 



！！！自我描述！！！

celery  框架  把同步的代码异步化，同时性能无损失。

celery 作为中间人的存在 ，实际需求中是发邮件。 如果注册邮件多，容易阻塞，就是在发邮件之前celery介入， broker 是厨师跟服务员之间的，selery进行分发。selery本身需要消息中间件，消息到底发成功没需要消息存贮rabbitmq。python3.6需要改源码， 

selery 可以理解为服务员，发邮件的逻辑是炒菜的， 注册的是消费者， broker 是厨师跟服务员之间的。





















