# 函数传参

```html
<script type="text/javascript">
  window.onload = function(){
    function aAlter(a){
      alert(a)
    };
    aAlter('我是张卫宁！')
  }
</script>
```

## 案例：

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<script type="text/javascript">
			window.onload = function(){
				//定义一个函数。
				function fnMyalert(num1,num2){
					
					var Sum = num1 + num2;
					
					alert(Sum);
					return Sum;
					//弹出
					alert('hello !!');
				}
				fnMyalert(50,30);
				
				function fnChangestyle(mystyle,val){
					var oDiv =document.getElementById("div1");
					oDiv.style[mystyle] = val;
					
				};
				fnChangestyle('fontSize','30px');
				fnChangestyle('color','red');
				fnChangestyle('backgroundColor','pink');
				
			}
		</script>
	</head>
	<body>
		<div id="div1">看到了吗？？这个字体变大了!通过传参！</div>
	</body>
</html>

```



# 函数return关键字

函数中return关键字的作用：

- 返回函数执行的结果。
- 结束函数的运行。
- 阻止默认行为。

## 案例：

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<script type="text/javascript">
			window.onload = function(){
				
				function fnAdd(a,b){
					var c = a + b ;
					//出发return 之后后面的函数就不会执行了，起到一个终止的作用，
					return c;
//					alert(c)
				};
				var iResult = fnAdd(2,5);
				
				//如果不设置返回值 结果就是ondefault
				alert(iResult);
			}
		</script>
	</head>
	<body>
	</body>
</html>

```

