# Jquery链式调用

<font color='red' size='5px'>
jquery对象的方法会在执行完这个返回的jquery对象之后，所有jquery对象的方法可以连接起来
</font>



**$('#div1')                   //id为div1的元素**
**.children('ul')                   //该元素下面的ul子元素**
**.slideDown('fast')                   //高度从零变到实际高度来显示ul元素**
**.parent()                         //跳到ul父级元素平级的所有兄弟元素**
**.siblings()                        //跳到div1 元素平级的所有兄弟元素**
**.childer('ul')                     //这些兄弟元素中的ul子元素**
**.slideUp('fast');                    /高度实际高度变换到零来隐藏ul元素**



## 层级菜单

```html
<!DOCTYPE html>
<html>
<head>
		<meta name=""charset="utf-8" content=""/>
	<title>层级菜单</title>
	<style type="text/css">
		


	</style>
	<script type="text/javascript" src="js\jquery-1.12.4.min.js"></script>
	<script type="text/javascript">
		$(function(){
			$('.level1').click(function(){
				// 当前点击的元素紧挨着的同辈元素向下展开，再跳到次元素的父级（li）,再跳到此父级的其他同辈元素(li),选择其他同辈元素(li)的子元素(li),然后他向上收起。


				// 通过stop() 可以解决多次点击持续动画的问题。
				$(this).next().stop().slideToggle().parent().siblings().children('ul').slideUp();
			})
		})
		


	</script>
</head>

<body>
	<!-- 
$('#div1') //id为div1的元素
.children('ul') //该元素下面的ul子元素
.slideDown('fast') //高度从零变到实际高度来显示ul元素
.parent() //跳到ul父级元素平级的所有兄弟元素
.siblings() //跳到div1 元素平级的所有兄弟元素
.childer('ul') //这些兄弟元素中的ul子元素
.slideUp('fast'); //高度实际高度变换到零来隐藏ul元素
	 -->

	<ul class="meun">
		<li>
			<a href="#" class="level1">水果</a>
			<ul class="current">
				<l1><a href="#">苹果</a></l1><br>
				<l1><a href="#">梨子</a></l1><br>
				<l1><a href="#">葡萄</a></l1><br>
				<l1><a href="#">火龙果</a></l1><br>
			</ul>
		</li>
		<li>
			<a href="#" class="level1">水果</a>
			<ul class="current">
				<l1><a href="#">苹果</a></l1><br>
				<l1><a href="#">梨子</a></l1><br>
				<l1><a href="#">葡萄</a></l1><br>
				<l1><a href="#">火龙果</a></l1><br>
			</ul>
		</li>
		<li>
			<a href="#" class="level1">水果</a>
			<ul class="current">
				<l1><a href="#">苹果</a></l1><br>
				<l1><a href="#">梨子</a></l1><br>
				<l1><a href="#">葡萄</a></l1><br>
				<l1><a href="#">火龙果</a></l1><br>
			</ul>
		</li>		
	</ul>
</body>
</html>
```

