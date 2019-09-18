# 绑定click事件

click是点击事件，JavaScript的用法是onclick,

jquery就得比人家少些一点，所以是  click。

**给元素绑定click事件，可以用如下方法：**

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<script src="js/jquery-1.12.4.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				
				//jquery方法
				var btn1 = $('#btn1');
				btn1.click(function(){
					alert('点击成功！，jquery方法')
				});
				
				
				//JavaScript方法
				var btn2 = document.getElementById("btn2");
				btn2.onclick = function(){
					alert('JavaScript方法！！')
				}
			
			});
				
		</script>
	</head>
	<body>
		<input type="button" name="btn1" id="btn1" value="jquery" />
		<input type="button" name="" id="btn2" value="javascrapy" />
	</body>
</html>

```

**click加toggleClass实现点击变化效果**

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<script src="js/jquery-1.12.4.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				//使用普通的方法来实现点击变化
//				$('#btn1').click(function(){
//					if($('.box').hasClass('col01')){      //hasClass判断是否有colo1
//						$('.box').removeClass('col01')
//					}
//					else{
//						$('.box').addClass('col01')
//					}		
//				})
				
				
				//使用toggleClass方法可以实现点击变化的效果
				$('#btn1').click(function(){
					$('.box').toggleClass('col01');
				})
		
			});
				
		</script>
		<style type="text/css">
			.box{
				width: 500px;
				height: 500px;
				background-color: royalblue;
			}
			.col01{
				background-color: green;
			}
		</style>
	</head>
	<body>
		<input type="button" name="btn1" id="btn1" value="jquery" />
		<div class="box">div元素</div>
	</body>
</html>

```

