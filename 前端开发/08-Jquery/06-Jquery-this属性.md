# jQuery中this与$(this)的区别总结

这里就谈谈this与$(this)的区别。

### 1、jQuery中this与$(this)的区别

```
   $("#textbox").hover(   
      function() {   
           this.title = "Test";   
      },   
      fucntion() {   
          this.title = "OK”;   
      }   
); 
```

**这里的this其实是一个html 元素(textbox)，textbox有text属性，所以这样写是完全没有什么问题的。** 
**但是如果将this换成(this)就不是那回事了，报Error了。this与(this)的区别在此。**

```
\\Error Code：   
$("#textbox").hover(   
       function() {   
          $(this).title ＝ "Test";   
       },   
       function() {   
          $(this).title = "OK";   
       }   
); 
```

 

$()这是jQuery的一个函数，也是最核心最基本的函数

功能一：传入一个选择器字符串，获得这个选择器对应的dom内容，保存在[]中，也就是俗称的jQuery对象。例如

('#id')(‘.class’) $(‘tag’) 
功能二：传入一个匿名函数，例如

$(function(){})//这个匿名函数在网页载入完成后开始执行 
功能三：将JavaScript对象包装成为jQuery对象。例如

```
$(this)
$({a:1,b:2,c:3})
$(document.getElementById('idstr'))
```

this是javascript**自身的** 语法关键字，它指向一个javascript对象，所以可以使用所指向的目标javascript对象所拥有的方法, 但他自己不是一个普通的变量，所以你无法自己定义一个变量叫this

所以为了使用jQuery对象的方法，你必须传入jQuery函数$(this), 将javascript 对象包装成为一个jquery对象。

这里的$(this)是一个JQuery对象，而jQuery对象沒有title 属性，因此这样写是错误的。

JQuery拥有attr()方法可以get/set DOM对象的属性，所以正确的写法应该是这样：

正确的代码：

```
$("#textbox").hover(   
      function() {   
         $(this).attr(’title’, ‘Test’);   
      },   
      function() {   
         $(this).attr(’title’, ‘OK’);   
      }   
); 
```

使用jQuery的好处是它包裝了各种浏览器版本对DOM对象的操作，因此统一使用$(this)而不再用this应该是比较不错的选择。

jQuery中this与$(this)的区别就介绍到这里。

### 2、典型错误与注意点

```
var node = $('#id');
node.click(function(){
　　this.css('display','block');　　//报错  this是一个html元素，不是jquery对象，因此this不能调用jquery                             的css()方法
　　$(this).css();　　　　　　//正确　　　$(this)是一个jquery对象，不是html元素，可以用css()方法
　　this.style.display = 'block';　　//正确  this是一个html元素，不是jquery对象，因此this不能调用jquery的css()方法,但是可以用javascript来更改style属性

});
```

### 不要滥用$(this)

如果不了解javasrcipt中基本的DOM属性和方法的话，很容易滥用jQuery对象。比如：

```
$(‘#someAnchor’).click(function() {

    alert( $(this).attr(‘id’) );

});
```

 

如果你只是通过jQ对象获取简单的dom元素的属性比如id，那么你完全可以使用js原生的方法：

```
$(‘#someAnchor’).click(function() {

    alert( this.id );

});
```

诸如“src,” “href,” 和“style.”等一些属性在老版本的ie中使用了getAttribute方法。