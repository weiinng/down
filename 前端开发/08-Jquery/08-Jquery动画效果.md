# juqery特殊效果

##### **fadeIn()   淡入**

##### **fadeOut()    淡出**

##### **fadeToggle()     切换淡入淡出**

##### **hide()    隐藏元素**

##### **show()     显示元素**

##### **goggle()        向下展开**

##### **slideUp()        向上卷起**

**slideToggle()       一次展开或者卷起某个元素**

```python
$('#btn').click(function(){
  $('.box').fadeIn(1000,     //操作动画需要的时间1000/1秒
                   'swing',     //操作的样式
                   function(){alert('动画完了！')});//回调函数，动画执行完之后要做的事情
})
```



**fadeIn(1000/1ms（操作所需要的时间），'swing'效果 ， function() 回调函数)**

**在这里只举一个例子，其他的效果用法与此相同。**

  

```html
<!DOCTYPE html>
<html>
	<meta name=""charset="utf-8" content=""/>
<head>
	<title>Document</title>
</head>
	
	<style type="text/css">
		.box{
			widows: 300px;
			height: 300px;
			background-color: gold;
			/*是否显示  none 隐藏*/
			display: none;
		}
	</style>
	<script type="text/javascript" src="js\jquery-1.12.4.min.js"></script>
	<script type="text/javascript">
		$(function(){
			$('#btn').click(function(){

				// $('.box').fadeIn(1000,'swing',function(){
				// 	alert('动画完了！！')
				// });
				$('.box').fadeToggle(1000,'swing',function(){
				});
			})


		})
	</script>
	<!-- 
	fadeIn()淡入
	fadeOut（）淡出
	fadeTogle()切换淡入淡出
	fadeIn(1000/1ms（操作所需要的时间），'swing'效果 ， function() 回调函数)
	
	hide() 隐藏元素
	show()显示元素
	toggle()切换元素显示的可见状态
	slideDown（）向下展开
	slideUp() 向上卷起
	slideTogge() 依次展开或者卷起某个元素
	-->

<body>
	<input type="button" name="" value="动画" id='btn'>
	<div class="box">111</div>
</body>
</html>
```

