# rabbitmq

**RabbitMQ**是实现了高级消息队列协议（AMQP）的开源消息代理软件（亦称面向消息的中间件）。RabbitMQ服务器是用[Erlang](https://baike.baidu.com/item/Erlang)语言编写的，而集群和故障转移是构建在[开放电信平台](https://baike.baidu.com/item/%E5%BC%80%E6%94%BE%E7%94%B5%E4%BF%A1%E5%B9%B3%E5%8F%B0)框架上的。所有主要的编程语言均有与代理接口通讯的客户端[库](https://baike.baidu.com/item/%E5%BA%93)。 

## 简介

**RabbitMQ**是实现了高级消息队列协议（AMQP）的开源消息代理软件（亦称面向消息的中间件）。RabbitMQ服务器是用[Erlang](https://baike.baidu.com/item/Erlang)语言编写的，而群集和故障转移是构建在[开放电信平台](https://baike.baidu.com/item/%E5%BC%80%E6%94%BE%E7%94%B5%E4%BF%A1%E5%B9%B3%E5%8F%B0)框架上的。所有主要的编程语言均有与代理接口通讯的客户端[库](https://baike.baidu.com/item/%E5%BA%93)。 

## 历史

Rabbit科技有限公司开发了RabbitMQ，并提供对其的支持。起初，Rabbit科技是LSHIFT和CohesiveFT在2007年成立的合资企业，2010年4月被[VMware](https://baike.baidu.com/item/VMware)旗下的SpringSource收购。RabbitMQ在2013年5月成为GoPivotal的一部分。 

## 基本概念

RabbitMQ是一套开源（MPL）的消息队列服务软件，是由 LShift 提供的一个 Advanced Message Queuing Protocol (AMQP) 的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 写成。 

## 主要特性

- 可伸缩性：集群服务
- 消息持久化：从内存持久化消息到硬盘，再从硬盘加载到内存 



## 安装

Erlang与RabbitMQ，安装路径都应不含空格符。

Erlang使用了环境变量HOMEDRIVE与HOMEPATH来访问配置文件.erlang.cookie，应注意这两个环境变量的有效性。需要设定环境变量ERLANG_HOME，并把%ERLANG_HOME%\bin加入到全局路径中。

RabbitMQ使用本地computer name作为服务器的地址，因此需要注意其有效性，或者直接解析为127.0.0.1

可能需要在本地网络防火墙打开相应的端口。