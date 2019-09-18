# AJAX 教程

 

AJAX = Asynchronous JavaScript and XML（异步的 JavaScript 和 XML）。

AJAX 不是新的编程语言，而是一种使用现有标准的新方法。

AJAX 最大的优点是在不重新加载整个页面的情况下，可以与服务器交换数据并更新部分网页内容。

AJAX 不需要任何浏览器插件，但需要用户允许JavaScript在浏览器上执行。

[**现在开始学习 AJAX !**](https://www.runoob.com/ajax/ajax-intro.html)

------

## 阅读本教程前，您需要了解的知识：

阅读本教程，您需要有以下基础：

- HTML 和 CSS 基础
- JavaScript 基础

如果您想学习这些基础知识，您可以在我们的首页找到相应的教程[菜鸟教程](https://www.runoob.com/)。

------

## AJAX 应用

- 运用XHTML+CSS来表达资讯；
- 运用JavaScript操作DOM（Document Object Model）来执行动态效果；
- 运用XML和XSLT操作资料;
- 运用XMLHttpRequest或新的Fetch API与网页服务器进行异步资料交换；
- 注意：AJAX与Flash、Silverlight和Java Applet等RIA技术是有区分的。

# AJAX 简介

------

AJAX 是一种在无需重新加载整个网页的情况下，能够更新部分网页的技术。

------

## 您应当具备的基础知识

在继续学习之前，您需要对下面的知识有基本的了解：

- HTML / XHTML
- CSS
- JavaScript / DOM

如果您希望首先学习这些项目，请在我们的[首页](http://w3cschool.cc/)访问这些教程。

------

## 什么是 AJAX ？

AJAX = 异步 JavaScript 和 XML。

AJAX 是一种用于创建快速动态网页的技术。

通过在后台与服务器进行少量数据交换，AJAX 可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。

传统的网页（不使用 AJAX）如果需要更新内容，必需重载整个网页面。

有很多使用 AJAX 的应用程序案例：新浪微博、Google 地图、开心网等等。

## AJAX 工作原理

![](../img\ajax工作原理.gif)



![](..\img\ajax工作流程中文版.png)



----

## AJAX是基于现有的Internet标准

AJAX是基于现有的Internet标准，并且联合使用它们：

- XMLHttpRequest 对象 (异步的与服务器交换数据)
- JavaScript/DOM (信息显示/交互)
- CSS (给数据定义样式)
- XML (作为转换数据的格式)

 **AJAX应用程序与浏览器和平台无关的！**



## Google Suggest

在 2005 年，Google 通过其 Google Suggest 使 AJAX 变得流行起来。

Google Suggest 使用 AJAX 创造出动态性极强的 web 界面：当您在谷歌的搜索框输入关键字时，JavaScript 会把这些字符发送到服务器，然后服务器会返回一个搜索建议的列表。

------

## 今天就开始使用 AJAX

AJAX 基于已有的标准。这些标准已被大多数开发者使用多年。

请阅读下一章，看看 AJAX 是如何工作的！



# AJAX 实例

------

为了帮助您理解 AJAX 的工作原理，我们创建了一个小型的 AJAX 应用程序:

------

## AJAX 实例解析

上面的 AJAX 应用程序包含一个 div 和一个按钮。

div 部分用于显示来自服务器的信息。当按钮被点击时，它负责调用名为 loadXMLDoc() 的函数：

```html
<div id="myDiv"><h2>使用 AJAX 修改该文本内容</h2></div>
<button type="button" onclick="loadXMLDoc()">修改内容</button>
```

接下来，在页面的 head 部分添加一个 <script> 标签。该标签中包含了这个 loadXMLDoc() 函数： 

```javascript
<head>
<script>
function loadXMLDoc()
{
    .... AJAX 脚本执行 ...
}
</script>
</head>
```



















