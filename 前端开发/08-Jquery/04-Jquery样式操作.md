# jquery样式操作



## jquery用法思想二

**同一个函数完成取值和赋值**



## 操作行间样式

```python
//获取div的样式
$('div').scc('width');
$('div').css('color');


//设置div样式
$('div').scc('width','30px');
$('div').scc('height','30px');
$('div').scc({'fontSize':'30px','color':'red'});
```

**特别注意**

选择器获取多个元素，获取信息获取的是第一个，比如：

```python
$('div').scc('width');
```

获取的是第一个div的width.

**jquery可以读取到行间没有定义的属性。**

**JavaScript无法读取到行间没有定义的属性。**



## 操作样式名

```python
$('#div1').addClass('divClass2')  //为id的div1的对象追加样式divClass2
$('#div1').removeClass('divClass') //移除id为div1对象的class名为divClass的样式
$('#div1').removeClass('divClass1 divClass2')   //移除多个样式元素
$('#div1').toggleClass('anotherClass')  //重复切换anotherClass 样式			
```

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<script src="js/jquery-1.12.4.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				
//				//获取div的样式
//				$('div').scc('width');
//				$('div').css('color');
//				
//				
//				//设置div样式
//				$('div').scc('width','30px');
//				$('div').scc('height','30px');
//				$('div').scc({'fontSize':'30px','color':'red'});
				
//				var $div = $('#box');
//				var sTr = $div.scc('fontSize');
				
//				$('#div1').addClass('divClass2')  //为id的div1的对象追加样式divClass2
//				$('#div1').removeClass('divClass') //移除id为div1对象的class名为divClass的样式
//				$('#div1').removeClass('divClass1 divClass2')   //移除多个样式元素
//				$('#div1').toggleClass('anotherClass')  //重复切换anotherClass 样式

				
				
			})
		</script>
	</head>
	<body>
	</body>
</html>

```

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<script src="js/jquery-1.12.4.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				var div1 = $('.box');
				
//				div1.addClass('big') //在原来样式名的基础上加上big样式
				
				div1.addClass('big red');  //在原来基础上加上 big 和 red多种样式
				
				div1.removeClass('red');   //在原来基础上删除red样式名 |可以批量删除方法同添加
				
			})
			
		</script>
		<style type="text/css">
			.box{
				width: 100px;
				height: 100px;
				background-color: gold;
			}
			.big{
				font-size: 30px;
			}
			.red{
				color: red;
			}
		</style>
	</head>
	<body>
		<div class="box">div元素</div>
	</body>
</html>

```

