# Node.js Server之一：概述

最近忙于工作，将近一个月没写博客，为了能快速写些东西，打算把自己业余在使用的Node.js Server通过一系列文章向大家讲述，本文是第一篇，主要做一个整体概述。

Server中部分内容也许有现成的轮子，但自己出于学习兴趣与程序员“瞎折腾”性格，都尽量自己实现。

## 前言

这个Server所用到的技术以及设计理念，目的不是为了做一个博客，更多的是作为通用业务框架来使用。从第一份工作后就一直作为自己学习和实践的场地，前前后后差不多三年历史，把其中一些核心内容通过文章分享出来，希望对大家有些帮助。

这篇概述主要包含内容:

- 理念与经验

> 两个简单的指导思想：基于配置、先分模块再分层

- 业务框架

> 不裸着使用基础HTTP Server框架，在其上构建一个业务框架

- 模块

> 通过配置文件描述模块

- 路由

> 通过配置文件进行模块路由描述

- HTTP Server

> 从学习角度出发，实现类Express基础功能的HTTP Server

## 理念与经验

### 基于配置

大概一年多前，跟一位大厂的工程师聊天，他描述自己的一位同事：“超喜欢通过配置来写代码”，自己当时可能理解50%，现在觉得有80%了。基于配置写代码的潜台词：“系统部分行为基于配置内容，可以通过不同的配置项达到不同的目的”，看看nginx的配置项就能体会我说的意思。

灵活、可扩展、统一等基于配置的优点，是自己做系统设计时选择“基于配置”的主要原因。在自己的Server中，路由行为通过配置文件描述是核心特点。

### 分模块与分层

分模块和分层是系统降解复杂度的最有效方式，分模块是垂直方向，分层则是水平。

分模块的重点是“边界”，这是一个麻烦的问题，没有绝对正确的答案。比如这个博客站点大致划分了如下几个模块：帐号、博客、备忘录、统计、SEO、视图，但自己做另外一个系统时，采用的是粒度更粗的划分方式，日后有机会在单独分享。

分层一般是技术性的，与业务无关通常也比较稳定，这个站点的博客模块大致有以下几个层：

- handler(controller)

> HTTP request处理入口

- service

> 服务层，提供与request无关业务逻辑接口，可为handler提供接口，同时作为跨模块调用的入口

- proxy

> 跟数据打交道，提供细粒度的数据查询接口

- model

> MySQL建表，定义数据schema等

分模块和分层还有一个重要抉择：“顺序”，通过目录结构可以体现，以下是两种典型的目录结构。

先分层再分模块：

```
app
├── handler
│   ├── account.js
│   └── blog.js
├── model
│   ├── account.js
│   └── blog.js
├── proxy
│   ├── account.js
│   └── blog.js
└── service
    ├── account.js
    └── blog.js
```

先分模块再分层：

```
app
├── account
│   ├── handler.js
│   ├── model.js
│   ├── proxy.js
│   └── service.js
└── blog
    ├── handler.js
    ├── model.js
    ├── proxy.js
    └── service.js
```

前后者各有优缺点，Node.js业界HTTP框架的新手指引通常都倾向前者，而我认为前者更多的是适用中小型项目，面对大型项目后者更有优势。自己个人项目是一个超长期项目，所以选择后者作为指导思路，主要解决问题：基础框架，模块边界，模块间通信等。

## 业务框架

Express、Koa、Egg等HTTP框架属于技术型框架，根据业务特点结合自己的想法在基础框架上搭建一个业务框架可以带来更多的灵活性与扩展性，同时也可以屏蔽底层HTTP框架差异，为业务做更多的定制。

业务框架的主要功能与作用：

> - 复用
> - 加载基础配置
> - 加载模块配置
> - 路由注册
> - 提供模块间通信能力
> - 第三方库抽象与代理，如mysql、oss、redis等
> - 非业务util

以上提到的功能，在后续系列文章中再做详细讲解。

## 模块

模块是业务框架中重要的概念，这里只展示项目中一个模块的目录结构和配置文件，讲解留给系列后面的文章。

模块的目录结构：

```
blog/
├── asset(静态资源)
│   └── css/
├── component(中间件)
│   └── converter/
├── constant(常量)
│   └── index.js
├── handler(request入口)
│   ├── article.js
│   ├── index.js
│   ├── topic.js
│   └── view.js
├── init(初始化)
│   └── index.js
├── manifest.json(模块表征配置描述)
├── model(数据定义)
│   └── index.js
├── proxy(数据库查询)
│   ├── article.js
│   ├── index.js
│   └── topic.js
├── route(配合manifest的路由文件)
│   ├── article.json
│   ├── topic.json
│   └── view.json
├── service(服务，跨模块调用入口)
│   ├── article.js
│   ├── index.js
│   └── topic.js
└── view(视图模版)
    ├── article/
    ├── index.ejs
    ├── partial/
    └── topic/
```

模块manifest：

```
{
    "name": "blog",
    "init": "init",
    "path": "/blog",
    "routes": [{
        "name": "404",
        "path": "404",
        "interceptors": [{
            "mode": "dev",
            "name": "asset.file",
            "options": {
                "dir": "app/blog/asset",
                "skip": "/blog"
            }
        }],
        "handler": "notFound"
    }, "view"],
    "child": [{
        "name": "blog-api",
        "path": "api",
        "routes": [
            "article",
            "topic"
        ]
    }],
    "links": [{
        "path": "index",
        "target": "index.html"
    }, {
        "path": "/index",
        "target": "index.html"
    }, {
        "path": "/index.html",
        "target": "index.html"
    }],
    "services": []
}
```

## 路由

路由在manifest.json中已经体现，使用routes进行定义，在逐步发展的过程中，发现manifest.json过长影响阅读，所以拆分了routes定义方式，routes中的字符串会从模块route目录加载对应文件内容，然后合并到routes，以下是route/article.json的内容：

```
{
    "path": "article",
    "routes": [{
        "name": "list article",
        "path": "list",
        "method": "get",
        "handler": "article.list"
    }, {
        "name": "list article group by topic",
        "path": "list-group-by-topic",
        "method": "get",
        "handler": "article.listGroupByTopic"
    }, {
        "name": "article detail by id",
        "path": "detail/id:(\\d+)",
        "method": "get",
        "handler": "article.detailById"
    }, {
        "name": "download article by id ",
        "path": "download/id:(\\d+)",
        "method": "get",
        "interceptors": ["auth.notAdmin"],
        "handler": "article.downloadById"
    }, {
        "name": "article meta",
        "path": "meta/id:(\\d+)",
        "method": "get",
        "interceptors": ["auth.notAdmin"],
        "handler": "article.metaInfoById",
        "res": {
            "title": "string",
            "keywords": "string",
            "tags": "string"
        }
    }]
}
```

内容太长，删减了一部分，这里的核心是将每个route定义在配置文件中，其中handler是实现入口，interceptors是中间件的一种。

manifest与route/*为什么选择json而不是用js，主要原因是因为json是一种与语言无关的数据格式，在配置这个层级的抽象，脱离语言环境可以降低配置的复杂性，如果配置使用js，就会不自觉的把逻辑写入其中，从而提高配置复杂度。

## HTTP Server

HTTP Server存在于业务框架之下，业务开发者不了解是具体是Express、Koa、Egg中的哪一个，或者根本不是三者之一。

HTTP Server这块，初期一直是用Express，有一天，出于学习的目的兴致高昂，然后花了两周时间，自己动手撸出一堆渣渣代码，实现了Sever的基础功能，简单使用没什么问题，但目前还存在些问题和重构任务待完成，后面也拿出来与大家分享。

自己实现HTTP Server的核心思路是将server抽象成一棵树，每个request对应树中唯一的一条节点路径，路径中的每个树节点按序分阶段（convert, redirect, intercept, interfere, handle, finish）进行处理，最终得到响应结果，完成一次请求。

## 工具

工具与Sever本身没什么关系，但针对“基于配置”的理念，也可以玩出一些小花样，目前主要用来：

> - 生成API文档
> - 将业务框架＋模块进行打包发布
> - 博客管理客户端