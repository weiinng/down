# Jquery循环

**对jquery选择的对象集合分别进行操作，需要用到jquery循环操作，此时可以用对象上面的each方法。**

```html
<html>
	<head>
		<title></title>
		<meta name="" charset="utf-8" content=""/>
		<script src="js/jquery-1.12.4.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				var $li = $('.list li');
				
				$li.each(function(i){
					
					if($(this).index()%2 ==0){
						$(this).css({
							'backgroundColor':'red',
						})
					}
					else{
						$(this).css({
							'backgroundColor':'pink'
						})
					}
				
				})
				
			})
			
		</script>
	</head>
	<body>
		<ul class="list">
			<li>1</li>
			<li>2</li>
			<li>3</li>
			<li>4</li>
			<li>5</li>
			<li>6</li>
			<li>7</li>
			<li>8</li>
		</ul>
		
	</body>
</html>
```

