css选择器：
将css添加到<head>与</head>之间，并用<style></style>标记声明的一种样式。
语法如下：
<style>
这里写css内容
</style>

全局选择器：设置所有标签使用同一样式，用*表示
语法：*{}
例如：*{color:red;}  所有字体都为红色

标签选择器：用于声明标记采用的样式
语法：p{color:red;} 所有p标签里的文字都是红色

类选择器：用来为一系列标签定义相同的样式
语法： .类名{color:red;}
例如：
<p class="a">我是你爸爸</p>
<div class="a">我是你爸爸</div>
在<style> .a{color:red;} </style>  p标签和div标签里的文字都为红色

ID选择器：ID选择器和类选择器类似，但要注意同一id名在同一个页面中只能出现一次。（具有唯一性）
id选择器的语法：#id名{}
例如：
<style> #a{color:red;} </style>
<p id="a">我是你爸爸</p>
该p标签里的文字为红色

伪类选择器：
a :link(未被访问过，访问之前的状态）
a :hover(鼠标滑过)
a :active(鼠标按下)
a:visited(访问过后)
伪类选择器：用伪类定义的样式并不是作用在标记上，而是作用在标记的状态上
我们这里只要求掌握超链接的伪类a:hover
伪类选择器的语法：
a:hover{}

优先级：
id>class>标签>全局


