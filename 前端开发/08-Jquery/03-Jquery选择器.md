# jquery选择器

## jquery用法想一

选择某个页面元素，然后对他进行某种操作。

## jquery选择器

jquery选择器可以快速地选择标签，选择规则和css样式相同，使用length属性判断是否选择成功！

```python
    $('#myId')         //选择id为myID的网页元素
    $('.myClass')      //选择class为 Class的元素
    $('li')          //选择所有为li的元素
    $('#ul1 li span')    //选择id为ul1元素下所有li下的span元素
    $('input[name=first]')   //选择name 属性等于first的input属性
```



## 对选择集进行过滤

```python
    $('div').has('p');  //选择包含p元素的div标签
    $('div').not('.myClass');    //选择class不等于 myClass 的div元素
    $('div').filter('myClass');   //选择class等于myClass 的div元素
    $('div').eq(5);           //第6个div元素，下标为5
```

## 选择器转移

```python
$('div').prev();      //选择div元素前面紧挨着的同辈元素
$('div').prevAll(); //选择div元素之前所有的同辈元素。
$('div').next()   //选择div元素紧挨着的同辈元素
$('div').nextAll();    //选择div元素后面的同辈元素
$('div').parent();   //选择div的父元素
$('div').children();    //选择div所有的子元素
$('div').siblings();   //选择div的同级元素
$('div').find('.myClass');   //选择div内的class 等于myClass的元素
```

## 判断是否选择到了元素

juqey有容错机制，机试没有找到元素，也不会出错，可以利用lenght属性来判断是否找到了元素，lenght等于0，就是没有选择到元素，lenght大于0，就是选择到了元素。

**lenght是返回否个值的长度函数。**

```python
var $div1 = $('#div1');
var $div2 = $('#div2');
alert($div1.length);   //弹出1
alert($div2.length);   //弹出0

...............
<div id='div1'>这是一个DIV元素</div>
```

