# 条件语句

## switch语句

**多重if else语句可以切换成更高性能的switch语句**

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<script type="text/javascript">
			window.onload = function(){
				//通过控制 iWeek 的值来实现网页换肤的效果！
				var iWeek = 2;
				//获取到 body01
				var oBody = document.getElementById("body01")
				
				switch(iWeek){
					case 1:
						oBody.style.backgroundColor = 'gold';
						break;             //结束网页运行，不然会接着向下匹配
					
					case 2:
						oBody.style.backgroundColor = 'palegoldenrod';
						break;
						
					case 3:
						oBody.style.backgroundColor = 'pink';
						break;
					
					case 4:
						oBody.style.backgroundColor = 'red';
						break;
						
					case 5:
						oBody.style.backgroundColor = 'gold';
						break;
						
					case 6:
						oBody.style.backgroundColor = rgba(0,0,0,0.3);
						break;
						
					case 7:
						oBody.style.backgroundColor = 'blanchedalmond';
						break;
						
					case 8:
						oBody.style.backgroundColor = 'black';
						break;
						
					case 9:
						oBody.style.backgroundColor = 'yellow';
						break;
					//如果以上条件都不满足可以写这个 相当于 else的作用，这个语句不用写 break
					default:
						oBody.style.backgroundColor = 'aqua';
						
				}
			}
		</script>
	</head>
	<body id='body01'>
	</body>
</html>

```







