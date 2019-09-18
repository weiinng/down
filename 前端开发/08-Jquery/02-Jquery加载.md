

**原生js的加载速度比jquery要慢一点，因为jquery加载是标签加载完之后就去执行，原生js加载是标签和页面选完完毕之后采取运行**

```html
<!DOCTYPE html>
<html>
<head>
	<title>使用原生的js和 jquery 写出的代码格式和语法</title>

<script type="text/javascript" src="../static/js/jquery-1.12.4.min.js"></script>
<script type="text/javascript">


//	window.onload = function () {
//	    var oDiv = document.getElementById();
//	    alert('原生弹出的'+oDiv)
//    }

    //ready 比 window.onload 要快：
	//原因是：window.onload是等标签加载完后，在渲染完毕之后再去运行的。
	//ready是等标签加载完毕之后就运行。

//ready 的完整写法
//	$(document).ready(function () {
//	    var $div = $('#div1');
//		alert('juqery弹出的'+$div)
//    })


//	ready的简写
	$(function () {
	    var $div = $('#div1');
	    alert('aaaaaaaa'+$div)

    })

</script>
</head>
<body>

<div id="div1">hellw </div>
</body>

</html>
```

