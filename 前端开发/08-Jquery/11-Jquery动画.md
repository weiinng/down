# Jquery动画

通过**animate**方法可以设置元素某属性值上的动画，可以设置一个或者多个属性值，动画执行完成后会执行第一个函数。

-------------

**animate方法：**

```html
$(selector).animate({params},speed,callback);
```

必需的 params 参数定义形成动画的 CSS 属性。

可选的 speed 参数规定效果的时长。它可以取以下值："slow"、"fast" 或毫秒。

可选的 callback 参数是动画完成后所执行的函数名称。



------



```html
$('#div').animate({
	width:300,
	height:300,
}),1000,'swing',function(){
	alert('done!!')
}
```

参数可以写成数字表达式：

```html
$('#div').animate({
	width:"+=100",
	height:300,
}),1000,'swing',function(){
	alert('done!!')
}
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
//				$('#btn1').click(function(){
//					$('#div').stop()animate({         //在这种多次点击的动画加上stop() 可以防止恶意点击
//						width:"+=100",
//						height:300,
//					}),1000,'swing',function(){
//						alert('done!!')
//					}
//				})


				$("#btn1").click(function(){         //形成点击事件并赋予一个函数提供调用
					$('#div').animate({            //给选择的对象加上一个动画
						'width':"300px",						//给对象加上动画需要执行的内容
						'height':'300px',           
					},1000,function(){            //每个函数提供了回调函数，使用回调函数会在上一个函数结束之后下一个函数会继续运行
						$('#div').animate({       //继续指定某个div使用动画
							'opacity':'0'        //动画效果
						},5000)             //动画持续的时间
					})
				})
				
			})
		</script>
		<style type="text/css">
			div{
				width: 100px;
				height: 100px;
				background-color: red;
			}
		</style>
	</head>
	<body>
		<div id="div">我是你爸爸！！</div>
		<button id='btn1'>按钮</button>
	</body>
</html>

```

