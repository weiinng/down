# Javascript组成

1. ECMAscript JavaScript的语法（变量、函数、循环语句等语法）

2. DOM 文档对象模型 操作html 的 css的方法。

3. DOM 浏览器对象模型 操作浏览器的一些方法

   

javascript是一种专为与网页交互而设计的脚本语言,由下列三个不同的部分组成:

ECMAScript,由ECMA-262定义,提供核心语言功能;

文档对象模型(DOM),提供访问和操作网页内容的方法和接口;

浏览器对象模型(BOM),提供与浏览器交互的方法和接口;

javascript 的这三个组成部分,在当前五个主要浏览器(IE,Firefox,Chrome,Safari和Opera)中都得到了不同程度的支持.其中,所有浏览器对ECMAScript第三版的支持大体上都还不错,而对ECMAScript 5 的支持程度越来越高,但对DOM的支持则彼此相差比较多.对已经正式纳入HTML5标准的BOM来说,尽管个浏览器都实现了某些众所周知的共同特性,但其他特性还是会因浏览器而异.



Java Script的三个主要组成部分是：ECMAScript(核心)，DOM（文档对象模型），BOM（浏览器对象模型）。

- ECMAScript

ECMA-262没有参照web浏览器，规定了语言的组成部分，具体包括语法、类型、语言、关键字、保留字、操作符、对象。

ECMAScript就是对该标准规定了各个方面内容的语言的描述。

ECMAScript的兼容：

1 支持ECMA-262描述的所有“类型，值，对象，属性，函数，以及程序语法和语义” 。

2 支持Unicode字符标准。

3 添加ECMA-262没有描述的更多“类型，值，对象，属性，函数”，ECMA-262说说的浙西新增特性，主要是指该标准中没有规定的新对象和对象的新属性。

4 支持ECMA-262中没有定义的“程序和正则表达式的语法”。也就是说可以修改和扩展内置的正则表达式语法。

- DOM（文档对象模型）

文档对象模型DOM是针对XML但经过扩展用于HTML的应用程序编程接口（API）。DOM把整个页面映射为一个多层次节点结构。HTML或者XML页面中的每个组成部分都是某种类型的节点，这些节点又包含着不同类型的数据。

在DOM中，页面一般可以用分层节点图表示。 


DOM级别：

DOM1级于1998年10月成为W3C的推荐标准。BOM1由两个模块组成分别是DOM core和DOM HTML。

DOM core：规定如何映射基于XML的文档结构，以便简化对文档中任意部分的访问和操作。

DOM HTML：在DOM core的基础上加以扩展，添加了针对HTML的对象和方法。

DOM2级在原来DOM的基础上有扩充了鼠标和用户界面事件、范围、遍历等细分模块，通过对象接口增加了对css的支持。包括以下模块：

1 DOM Views（DOM视图）：定义了跟踪不同文档视图的接口。

2 DOM Events（DOM事件）：定义了事件与事件处理的接口。

3 DOM Traversal and Range(DOM遍历和范围)：定义了遍历和操作文档的接口。

DOM3级则进一步扩展了DOM，引入了加载和保存模块以统一方式加载和保存文档的方法；新增了DOM验证模块主要还是验证文档的方法。

- BOM浏览器对象模型

BOM处理浏览器窗口和框架，人们习惯上把所有针对浏览器的JavaScript扩展算作是BOM的一部分。包括以下：

1 弹出新浏览器窗口的功能。

2 移动、缩放和关闭浏览器窗口的功能。

3 提供浏览器所加载页面的详细信息的navigator对象。

4 提供浏览器所加载页面的详细信息的location对象。

5 提供用户分辨率详细信息的screen对象。

6 对cookies的支持。

7 像XMLHttpRequest和IE的ActionXobject这样的自定义对象。

<https://baike.baidu.com/item/javascript/321142?fr=aladdin>