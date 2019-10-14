# RPC简介及框架选择

​	简单介绍RPC协议及常见框架，对比传统restful api和RPC方式的优缺点。常见RPC框架，gRPC及序列化方式Protobuf等 。



### HTTP协议

​	http协议是基于tcp协议的，tcp协议是流式协议，包头部分可以通过多出的\r\n来分界，包体部分如何分界呢？这是协议本身要解决的问题。目前一般有两种方式，第一种方式就是在包头中有个content-Length字段，这个字段的值的大小标识了POST数据的长度，服务器收到一个数据包后，先从包头解析出这个字段的值，再根据这个值去读取相应长度的作为http协议的包体数据。
​	 浏览器connect 80端口

 

### RESTful API (http+json)

 网站即软件，而且是一种新型的软件，这种"互联网软件"采用客户端/服务器模式，建立在分布式体系上，通过互联网通信，具有高延时（high latency）、高并发等特点。
 　　它首次出现在 2000 年 Roy Fielding 的博士论文中，他是 HTTP 规范的主要编写者之一。Representational State Transfer，翻译是”表现层状态转化”，通俗来讲就是：资源在网络中以某种表现形式进行状态转移。
 总结一下什么是RESTful架构：
 　　（1）每一个URI代表一种资源；
 　　（2）客户端和服务器之间，传递这种资源的某种表现层，比如用JSON，XML，JPEG等；
 　　（3）客户端通过四个HTTP动词，对服务器端资源进行操作，实现"表现层状态转化"。

URL定位**资源**，用HTTP动词（GET,POST,DELETE,DETC）描述操作。
 用HTTP协议里的动词来实现资源的添加，修改，删除等操作。即通过HTTP动词来实现资源的状态扭转：
 　　GET 用来获取资源，
 　　POST 用来新建资源（也可以用于更新资源），
 　　PUT 用来更新资源，
 　　DELETE 用来删除资源。

### RPC

进程间通信（IPC，Inter-Process Communication），指至少两个进程或线程间传送数据或信号的一些技术或方法。进程是计算机系统分配资源的最小单位。每个进程都有自己的一部分独立的系统资源，彼此是隔离的。为了能使不同的进程互相访问资源并进行协调工作，才有了进程间通信。这些进程可以运行在同一计算机上或网络连接的不同计算机上。 进程间通信技术包括消息传递、同步、共享内存和远程过程调用。 IPC是一种标准的Unix通信机制。

有两种类型的进程间通信(IPC)。

- 本地过程调用(LPC)LPC用在多任务操作系统中，使得同时运行的任务能互相会话。这些任务共享内存空间使任务同步和互相发送信息。
- 远程过程调用(RPC)RPC类似于LPC，只是在网上工作。RPC开始是出现在Sun微系统公司和HP公司的运行UNIX操作系统的计算机中。

为什么RPC呢？就是无法在一个进程内，甚至一个计算机内通过本地调用的方式完成的需求，比如比如不同的系统间的通讯，甚至不同的组织间的通讯。由于计算能力需要横向扩展，需要在多台机器组成的集群上部署应用

RPC的核心并不在于使用什么协议。RPC的目的是让你在本地调用远程的方法，而对你来说这个调用是透明的，你并不知道这个调用的方法是部署哪里。通过RPC能解耦服务，这才是使用RPC的真正目的。RPC的原理主要用到了动态代理模式，至于http协议，只是传输协议而已。简单的实现可以参考spring remoting，复杂的实现可以参考dubbo。

简单的说，

- RPC就是从一台机器（客户端）上通过参数传递的方式调用另一台机器（服务器）上的一个函数或方法（可以统称为服务）并得到返回的结果。
- RPC 会隐藏底层的通讯细节（不需要直接处理Socket通讯或Http通讯） RPC 是一个请求响应模型。
- 客户端发起请求，服务器返回响应（类似于Http的工作方式） RPC 在使用形式上像调用本地函数（或方法）一样去调用远程的函数（或方法）。

 

####  RPC通信过程

默认socket通信。本地机器的RPC框架反序列化出执行结果，函数return这个结果 

![](C:\Users\ASUS\Desktop\md用图\RPC通信过程.webp)

### RPC和restful api对比

REST是一种设计风格，它的很多思维方式与RPC是完全冲突的。 RPC的思想是把本地函数映射到API，也就是说一个API对应的是一个function，我本地有一个getAllUsers，远程也能通过某种约定的协议来调用这个getAllUsers。至于这个协议是Socket、是HTTP还是别的什么并不重要； RPC中的主体都是动作，是个动词，表示我要做什么。 而REST则不然，它的URL主体是资源，是个名词。而且也仅支持HTTP协议，规定了使用HTTP Method表达本次要做的动作，类型一般也不超过那四五种。这些动作表达了对资源仅有的几种转化方式。
 RPC的根本问题是耦合。RPC客户端以多种方式与服务实现紧密耦合，并且很难在不中断客户端的情况下更改服务实现。RPC更偏向内部调用，REST更偏向外部调用。

Web 服务应该算是 RPC 的一个子集，理论上 RPC 能实现的功能， 用 Web 服务也能实现，甚至很多 RPC 框架选用 HTTP 协议作为传输层。
 现在很多网站的 API 都是以 HTTP 服务的形式提供的，这也算是 RPC 的一种形式。

区别主要在这 2 个东西设计的出发点不太一样：

- HTTP 是面向浏览器设计的应用层协议，操作的核心在**资源。**我们更多的用 Web 服务在做网站。
- RPC 是为了在像在本地调用一个函数那样调用远程的代码而设计的，所以更关注减少本地调用和远程调用的差异，像 SOAP(简单对象访问协议) 这种东西是可以把对象当参数传的。

我们讨论 RPC 和 Web 的区别，其实是在谈论 2 个东西：序列化协议和传输协议。序列化协议比如常见的 XML，JSON 和比较现代的 Protocol Buffers、Thrift。 传输协议比如 TCP、UDP 以及更高层的 HTTP 1.1、HTTP 2.0。

一般我们考虑用 RPC 而不是 HTTP 构建自己的服务，通常是考虑到下面的因素：

- 接口是否需要 Schema 约束
- 是否需要更高效的传输协议（TCP，HTTP 2.0）
- 是否对数据包的大小非常敏感

比如 HTTP 是基于文本的协议，头部有非常多冗余（对于 RPC 服务而言）。HTTP 中我们用的最多就是 RESTful ，而 RESTful 是个弱 Schema 约束，大家通过文档沟通，但是如果我就是不在实现的时候对接口文档约定的参数做检查，你也不能把我怎么样。这个时候 Thrift 这种序列化协议的优势就体现出来了，由于 Schema 的存在，可以保证服务端接受的参数和 Schema 保持一致。

 

 

###  RPC框架

- Call ID映射。我们怎么告诉远程机器我们要调用Multiply，而不是Add或者FooBar呢？在本地调用中，函数体是直接通过函数指针来指定的，我们调用Multiply，编译器就自动帮我们调用它相应的函数指针。但是在远程调用中，函数指针是不行的，因为两个进程的地址空间是完全不一样的。所以，在RPC中，所有的函数都必须有自己的一个ID。这个ID在所有进程中都是唯一确定的。客户端在做远程过程调用时，必须附上这个ID。然后我们还需要在客户端和服务端分别维护一个 {函数 <--> Call ID} 的对应表。两者的表不一定需要完全相同，但相同的函数对应的Call ID必须相同。当客户端需要进行远程调用时，它就查一下这个表，找出相应的Call ID，然后把它传给服务端，服务端也通过查表，来确定客户端需要调用的函数，然后执行相应函数的代码。
- 序列化和反序列化。客户端怎么把参数值传给远程的函数呢？在本地调用中，我们只需要把参数压到栈里，然后让函数自己去栈里读就行。但是在远程过程调用时，客户端跟服务端是不同的进程，不能通过内存来传递参数。甚至有时候客户端和服务端使用的都不是同一种语言（比如服务端用C++，客户端用Java或者Python）。这时候就需要客户端把参数先转成一个字节流，传给服务端后，再把字节流转成自己能读取的格式。这个过程叫序列化和反序列化。同理，从服务端返回的值也需要序列化反序列化的过程。
- 网络传输。远程调用往往用在网络上，客户端和服务端是通过网络连接的。所有的数据都需要通过网络传输，因此就需要有一个网络传输层。网络传输层需要把Call ID和序列化后的参数字节流传给服务端，然后再把序列化后的调用结果传回客户端。只要能完成这两者的，都可以作为传输层使用。因此，它所使用的协议其实是不限的，能完成传输就行。尽管大部分RPC框架都使用TCP协议，但其实UDP也可以，而gRPC干脆就用了HTTP2。Java的Netty也属于这层的东西。

目前有很多Java的RPC框架，有基于Json的，有基于XML，也有基于二进制对象的。

论复杂度，RPC框架肯定是高于简单的HTTP接口的。但毋庸置疑，HTTP接口由于受限于HTTP协议，需要带HTTP请求头，导致传输起来效率或者说安全性不如RPC

 

 ![](C:\Users\ASUS\Desktop\md用图\RPC框架封装.webp)

## 常用RPC框架

支持Java最多，golang

- Netty - Netty框架不局限于RPC，更多的是作为一种网络协议的实现框架，比如HTTP，由于RPC需要高效的网络通信，就可能选择以Netty作为基础。
- brpc是一个基于protobuf接口的RPC框架，在百度内部称为“baidu-rpc”，它囊括了百度内部所有RPC协议，并支持多种第三方协议，从目前的性能测试数据来看，brpc的性能领跑于其他同类RPC产品。
- Dubbo是Alibaba开发的一个RPC框架，远程接口基于Java Interface, 依托于Spring框架。
- gRPC的Java实现的底层网络库是基于Netty开发而来，其Go实现是基于net库。
- Thrift是Apache的一个项目([http://thrift.apache.org](http://thrift.apache.org/))，前身是Facebook开发的一个RPC框架，采用thrift作为IDL (Interface description language)。
- jsonrpc

## JSON-RPC

[python web接口实现（restful方式、jsonrpc方式）](https://www.jianshu.com/p/545acae57e27)
 区块链项目中用的较多？资料不是很多
 JSON-RPC是一种序列化协议。JSON 是 JS 对象的字符串表示法，它使用文本表示一个 JS 对象的信息，本质是一个字符串。
 非常简单，方便，速度慢
 相关Python 包(直接集成到flask和django)
 Flask-JSONRPC,django-json-rpc；jsonrpcserver,jsonrpcclient

## thrift

[Python RPC 之 Thrift](https://www.jianshu.com/p/82a6bdaabcd3)
 Facebook开源的跨语言RPC框架。

## gRPC

[gRPC 官方文档中文版](http://doc.oschina.net/grpc?t=56831)
 [深入了解gRPC协议-知乎](https://zhuanlan.zhihu.com/p/27595419)

1. tensorflow分布式与tensorflow serving底层通信都是是用的grpc
    序列化用protobuf，通信使用http2
2. latest Google APIs will have gRPC versions of their interfaces, letting you easily build Google functionality into your applications.
3. 支持 C, C++, Node.js, Python, Ruby, Objective-C,PHP and C#

## HTTP2

[一文读懂 HTTP2 特性 - 又拍云的文章 - 知乎](https://zhuanlan.zhihu.com/p/26559480)
 [HTTP/2 和 HTTP/1 速度对比](https://link.zhihu.com/?target=https%3A//http2.akamai.com/demo)
 <http://www.http2demo.io/>
 [HTTP/2](https://hpbn.co/http2/)
 HTTP/2 是 HTTP 协议自 1999 年 HTTP 1.1 发布后的首个更新，主要基于 SPDY 协议。
 HTTP/2的主要目标是通过启用完整请求和响应复用来减少延迟，通过有效压缩HTTP头字段来最大限度地降低协议开销，并添加对请求优先级和服务器推送的支持;多路复用(同一tcp,多个流)，头部压缩，服务推送。

## Protobuf

[常用的跨语言通信方案](https://www.cnblogs.com/doit8791/p/4979465.html)
 [Google Protocol Buffer 的使用和原理](https://www.ibm.com/developerworks/cn/linux/l-cn-gpb/index.html)
 [Protobuf 语法指南](http://colobu.com/2015/01/07/Protobuf-language-guide/)
 Protocol Buffers 是一种轻便高效的结构化数据存储格式，可以用于结构化数据串行化，或者说序列化。它很适合做数据存储或 RPC 数据交换格式。可用于通讯协议、数据存储等领域的语言无关、平台无关、可扩展的序列化结构数据格式。目前提供了 C++、Java、Python 三种语言的 API。
 同 XML 相比， Protobuf 的主要优点在于性能高。它以高效的二进制方式存储，比 XML 小 3 到 10 倍，快 20 到 100 倍。

## 框架选择

[gRPC vs Thrift](https://blog.csdn.net/dazheng/article/details/48830511)
 [RPC框架性能基本比较测试](http://www.useopen.net/blog/2015/rpc-performance.html)
 [怎么看待谷歌的开源 RPC 框架 gRPC？ - 知乎](https://www.zhihu.com/question/30027669)
 [微服务的服务间通信与服务治理](https://zhuanlan.zhihu.com/p/35427150)
 [最佳实践 | 7大维度看国外企业为啥选择gRPC打造高性能微服务？](https://zhuanlan.zhihu.com/p/33623693)

##### 如何选择

**什么时候应该选择gRPC而不是Thrift**
 　　需要良好的文档、示例
 　　喜欢、习惯HTTP/2、ProtoBuf
 　　对网络传输带宽敏感
 **什么时候应该选择Thrift而不是gRPC**
 　　需要在非常多的语言间进行数据交换
 　　对CPU敏感
 　　协议层、传输层有多种控制要求
 　　需要稳定的版本
 　　不需要良好的文档和示例

总的来说，Python rpc框架选择较少，thrift性能最好，grpc性能比thrift稍差，原因是多了http2，而thrift直接基于tcp，但grpc序列化方案更通用(protobuf)优秀，文档较好；
 jsonrpc 本身基于http/1进行通信，速度最慢，相对于之前速度无提升，只是接口和数据格式更为统一；

### gRPC不足

1）GRPC尚未提供连接池
 2）尚未提供“服务发现”、“负载均衡”机制
 3）因为基于HTTP2，绝大部多数HTTP Server、Nginx都尚不支持，即Nginx不能将GRPC请求作为HTTP请求来负载均衡，而是作为普通的TCP请求。（nginx将会在1.9版本支持）

 

微服务是目前比较火的技术，现在都提倡业务的解耦， 我们公司是使用的的是thrif框架。像传统的http接口是靠xml或者json来进行数据的传输，传统方式是以key:value进行传输，而微服务呢是以二进制的方式来对数据进行传输，省去了key,大大提高了传输效率。

thrift框架里有一个.thrift文件，这个文件呢，前端有一套，后端有一套，除了能定位Value，还能前后端一致，传统http的问题是单方面篡该，如果单方面去改参数，没有告诉前端的话就会出问题，如果使用thrift框架，要改接口或者 改功能的话，必须要改 .thrift文件，这样前端能看到我改的数据，这样就是接口文件的好处。thrift文件可以定义接口名称，接口参数，定义接口返回值，数据类型用string。

thrift轮询有哪些数据类型。



docker是基于linux下的容器技术， docker解耦性很强，相当于一个集装箱。

docker的三大核心， 镜像，容器和仓库。 镜像就相当于我们python的一个类可以创建多个容器，容器相当于类下面的实例，容器之间是相互隔离的，而仓库分为公有仓库和私有仓库。共有仓库用来存放项目源码， 私有仓库只有自己可见。

docker-compose



 

 

 

 

 

 

 

 

 

 

 