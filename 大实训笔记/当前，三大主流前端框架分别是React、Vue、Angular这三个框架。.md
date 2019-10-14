Title: 当前，三大主流前端框架分别是React、Vue、Angular这三个框架。
Date: 2016-08-08 10:20
Modified: 2016-08-08 19:30
Category: 技术
Tags: React 起源于 Facebook 的内部项目，用来架设 Instagram 的网站， 并于 2013年 5 月开源。React 拥有较高的性能，代码逻辑非常简单，越来越多的人已开始关注和使用它。它有以下的特性：

1.声明式设计：React采用声明范式，可以轻松描述应用。

2.高效：React通过对DOM的模拟，最大限度地减少与DOM的交互。

3.灵活：React可以与已知的库或框架很好地配合。



优点：

\1. 速度快：在UI渲染过程中，React通过在虚拟DOM中的微操作来实现对实际DOM的局部更新。

\2. 跨浏览器兼容：虚拟DOM帮助我们解决了跨浏览器问题，它为我们提供了标准化的API，甚至在IE8中都是没问题的。

\3. 模块化：为你程序编写独立的模块化UI组件，这样当某个或某些组件出现问题是，可以方便地进行隔离。

\4. 单向数据流：Flux是一个用于在JavaScript应用中创建单向数据层的架构，它随着React视图库的开发而被Facebook概念化。

\5. 同构、纯粹的javascript：因为搜索引擎的爬虫程序依赖的是服务端响应而不是JavaScript的执行，预渲染你的应用有助于搜索引擎优化。

6.兼容性好：比如使用RequireJS来加载和打包，而Browserify和Webpack适用于构建大型应用。它们使得那些艰难的任务不再让人望而生畏。

缺点：

React本身只是一个V而已，并不是一个完整的框架，所以如果是大型项目想要一套完整的框架的话，基本都需要加上ReactRouter和Flux才能写大型应用。





Vue是一个构建数据驱动的Web界面的库，准确来说不是一个框架，它聚焦在V（view）视图层。

它有以下的特性：

1.轻量级的框架

2.双向数据绑定

3.指令

4.插件化



优点：

\1. 简单：官方文档很清晰，比 Angular 简单易学。

\2. 快速：异步批处理方式更新 DOM。

\3. 组合：用解耦的、可复用的组件组合你的应用程序。

\4. 紧凑：~18kb min+gzip，且无依赖。

\5. 强大：表达式 无需声明依赖的可推导属性 (computed properties)。

\6. 对模块友好：可以通过 NPM、Bower 或 Duo 安装，不强迫你所有的代码都遵循 Angular 的各种规定，使用场景更加灵活。

缺点：

\1. 新生儿：Vue.js是一个新的项目，没有angular那么成熟。

\2. 影响度不是很大：google了一下，有关于Vue.js多样性或者说丰富性少于其他一些有名的库。

\3. 不支持IE8





Angular是一款优秀的前端JS框架，已经被用于Google的多款产品当中。

它有以下的特性：

1.良好的应用程序结构

2.双向数据绑定

3.指令

4.HTML模板

5.可嵌入、注入和测试



优点：

\1. 模板功能强大丰富，自带了极其丰富的angular指令。

\2. 是一个比较完善的前端框架，包含服务，模板，数据双向绑定，模块化，路由，过滤器，依赖注入等所有功能；

\3. 自定义指令，自定义指令后可以在项目中多次使用。

\4. ng模块化比较大胆的引入了Java的一些东西（依赖注入），能够很容易的写出可复用的代码，对于敏捷开发的团队来说非常有帮助。

\5. angularjs是互联网巨人谷歌开发，这也意味着他有一个坚实的基础和社区支持。

缺点：

\1. angular 入门很容易 但深入后概念很多, 学习中较难理解.

\2. 文档例子非常少, 官方的文档基本只写了api, 一个例子都没有, 很多时候具体怎么用都是google来的, 或直接问misko,angular的作者.

\3. 对IE6/7 兼容不算特别好, 就是可以用jQuery自己手写代码解决一些.

\4. 指令的应用的最佳实践教程少, angular其实很灵活, 如果不看一些作者的使用原则,很容易写出 四不像的代码, 例如js中还是像jQuery的思想有很多dom操作.

\5. DI 依赖注入 如果代码压缩需要显示声明.



**MVX框架模式：MVC+MVP+MVVM**

1.MVC：Model(模型)+View(视图)+controller(控制器)，主要是基于分层的目的，让彼此的职责分开。

View通过Controller来和Model联系，Controller是View和Model的协调者，View和Model不直接联系，基本联系都是单向的。

用户User通过控制器Controller来操作模板Model从而达到视图View的变化。

2.MVP：是从MVC模式演变而来的，都是通过Controller/Presenter负责逻辑的处理+Model提供数据+View负责显示。

在MVP中，Presenter完全把View和Model进行了分离，主要的程序逻辑在Presenter里实现。

并且，Presenter和View是没有直接关联的，是通过定义好的接口进行交互，从而使得在变更View的时候可以保持Presenter不变。

MVP模式的框架：Riot,js。

3.MVVM：MVVM是把MVC里的Controller和MVP里的Presenter改成了ViewModel。Model+View+ViewModel。

View的变化会自动更新到Model, Model的变化也会自动同步到View上显示。

这种自动同步是因为ViewModel中的属性实现了Observer，当属性变更时都能触发对应的操作。



**在大型超大型web应用开发上，看好Angular** 

**小型应用上，看好vue** 

**个性化需求、中型应用，更倾向react** 
Slug: my-super-post
Authors: 夏伟











