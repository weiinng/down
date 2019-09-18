# Node.js Server之三：业务框架实战

此文是Node.js Server分享系列中的第三篇，[上篇文章](https://amsimple.com/blog/article/58.html)讲述了自己对业务框架的理解，在文章末尾提到用代码写一个简单的业务框架，具体实现的指导思想在前文讲过了，这篇就不再重复，这篇主要关注从代码层面如何实现，同时限于时间与篇幅，框架尽量精简，功能点到为止。

特意为此文写的[示例代码](https://github.com/Shasharoman/fw-example)放在Github上，此文的基础也基于该代码，有兴趣的朋友可能要花个10-20分钟看一遍，才能理解后文的讲述。

## 目录

精简版代码的目录结构如下：

```
example
├── app
│   ├── demo
│   │   ├── controller.js
│   │   ├── init.js
│   │   ├── manifest.json
│   │   └── service.js
│   └── exp
│       ├── controller.js
│       ├── init.js
│       ├── manifest.json
│       └── service.js
├── fw
│   ├── app.js
│   ├── appManage.js
│   ├── bootstrap.js
│   ├── httpServer.js
│   └── index.js
└── package.json
```

fw中是业务框架代码，目前完成了启动server，注册路由，以及提供跨模块调用，app中是两个最最简单应用举例。如果只看app中的代码，你无从得知它们是如何有效工作的，但如果让你写一个简单API，大概也能猜出要做些什么：

> - 在manifest.json中的routes里面填写path、method、impl
> - 然后在controller中实现impl指定的方法，并将结果用Promise.resolve返回

当我第一次在egg.js下面写API时，与第一次在app中写API是一样的感觉，只不过是egg.js非常强大，而上述的fw则弱的不行，但本质上它们都是业务框架，提供写业务代码的约束和实现指导。

## fw

fw中的4个文件，其中app、appManage、bootstrap在前一篇文章中有详细描述，这里的httpServer是将express做了一层包装，可以选择其他Node.js Http基础框架，或者自己实现也是OK的。

### App

App目前只实现了路由注册与外部服务调用，缺少中间件注册与restart、reload等生命周期方法的实现。

如果你理解了routes的注册逻辑，那中间件的实现，照着抄就行，比如在manifest中指定route所生效的中间件，然后start的过程中通过server.use进行注册即可。

### AppManage

AppManage中缺少中间件注册和生命周期方法的问题与App是类似的，就不展开了。

但AppManage中的serviceCall是可以进行扩展的，目前利用appManage持有所有app的引用完成跨模块调用，这个可以扩展成利用RPC框架完成这个功能，具体是什么意思呢？

拿这个最基础的例子来说，exp下有一个route: `/api/exp/random`，它跨模块调用了demo模块下的echo服务，如果demo和exp部署在不同实例，那这个跨模块调用就会失败，而把RPC集成进来的话，这个调用就能实现。

有一个概念叫“微服务”，serviceCall如果做成RPC，也就是往这方面靠吧，但自己也缺乏经验，难以窥视微服务的本质，就不继续展开了。

### bootstrap

目前bootstrap在这里没体现什么重要作用，只是简单作为桥梁用来启动Server。

### manifest.json

manifest.json现在看起来有些简单，但已经体现出了其核心作用，剥离应用对底层框架甚至业务框架的依赖。

初看示例代码，会觉得manifest.json是依赖业务框架的，其实恰恰相反，manifest.json才是起点，每一个想要业务框架实现的功能与特性，第一步都是考虑manifest.json中应该如何表达，最终manifest.json是可以独立存在的，业务框架不过是将manifest.json翻译了一遍，有必要的话可以随时更改翻译的方式，只需保持manifest.json的含义得到体现。

目前示例代码中的manifest.json是相对简单的，如果有能力喜欢折腾的话，它一定会变复杂，比如下面这个：

```
{
    "name": "fsfl",
    "path": "/fsfl/api",
    "init": "init",
    "converters": [{
        "mode": "dev",
        "name": "user.mockClient"
    }],
    "routes": [{
        "name": "pay notify",
        "comment": "微信支付成功回调",
        "path": "pay/notify",
        "method": "post",
        "handler": "applet.payNotify",
        "body": "text/xml",
        "res": "text/xml"
    }],
    "child": [{
        "name": "fsfl-admin",
        "path": "admin",
        "converters": ["user.admin"],
        "interceptors": ["auth.noAdminUser"],
        "child": [{
            "name": "fsfl-admin-upload",
            "path": "upload",
            "routes": ["admin/upload"]
        }, {
            "name": "fsfl-admin-goods",
            "path": "goods",
            "routes": ["admin/goods"]
        }...]
    }, {
        "name": "fsfl-client",
        "path": "client",
        "converters": ["user.clientTicket", "user.client"],
        "interceptors": ["auth.noAppletTicket"],
        "child": [{
            "name": "fsfl-client-goods",
            "path": "goods",
            "routes": ["client/goods"]
        }, {
            "name": "fsfl-client-prize",
            "path": "prize",
            "routes": ["client/prize"]
        }...]
    }],
    "services": [{
        "name": "closeOrderById",
        "impl": "order.closeById"
    }, {
        "name": "finishOrderById",
        "impl": "order.finishById"
    }, {
        "name": "pushCheckInNotify",
        "impl": "push.pushCheckInNotify"
    }, {
        "name": "onlineBanner",
        "impl": "star.onlineBanner"
    }...]
}
```

## 总结

已经有很多成熟的框架了，为什么还要去捣鼓这些？可以说是为了学习，但也不单单是为了学习，我觉得这就像是windows与linux，我更喜欢linux。