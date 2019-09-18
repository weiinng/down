### 事件函数列表

- biur()    元素失去焦点
- focus()   元素获得焦点
- click()         鼠标点击
- mouseover()           鼠标进入（进入子元素也触发）
- mouseout()        鼠标离开（离开子元素也触发）
- mouseenter()        鼠标进入（进入子元素不触发）
- mouseleave()       鼠标离开（离开子元素不触发）
- hover()             同时为mouseenter 和 mouseleave 事件指定处理函数
- ready()         DOM加载完成
- resize()          刘拉你窗口的发小发生改变
- scroll()          滚动条的位置发生变化
- submit()                用户递交表单



### 绑定事件的其他方式

```python
$(function(){
  $('#div').bind('click mouseover',function(event){
    alert($(this).html())
  })
})
```





### 取消绑定事件

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<script src="js/jquery-1.12.4.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				
				//普通的点击事件
//				$('#btn').click(function(){
//					alert('点击事件的提交！！')
//				})

				//点击或者鼠标移入的时候都执行这个匿名函数
				$('#btn').bind('click mouseover',function(){
					alert('触发事件绑定的函数！');
					
					
					//当实行完毕这个绑定事件之后同时解除绑定
					$(this).unbind('mouseover click')
				})				
			})			
		</script>
	</head>
	<body>
		<button type="button" name="" value="按钮" id='btn'>提交绑定的事件</button>
	</body>
</html>

```



### 鼠标移入移出

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<script src="js/jquery-1.12.4.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			
			$(function(){
				$('.con').mouseover(function(){
					alert('鼠标移入！');
//					return false;
				})
				$('.con').mouseout(function(){
					alert('鼠标移出！');
				})
				
			//	---------------------------------
				//mouseenter 方法不涉及子元素，只对当前元素有效
				$('.con2').mouseenter(function(){
					alert('鼠标移入！');
					
//					return false;
				})
				$('.con2').mouseleave(function(){
					alert('鼠标移出！');
				})
				
				
			// hover ----------------------------------
			$('.con3').hover(function(){
				alert('移入！！')
				
				
			},function(){
				alert('移出！')
				
			})
			
				
			})
		</script>
		<style type="text/css">
			.con,.con2,.con3{
				width: 200px;
				height: 200px;
				background-color: gold;
			
			}
			.box,.box2,.box3{
				width: 100px;
				height: 100px;
				background-color: green;
			}
		</style>
	</head>
	<body>
		<div class="con">
			<div class="box">mouseover</div>
		</div>
		
		<br />
		<div class="con2">
			<div class="box2">mouseenter</div>
		</div>
		
		<br />
		<div class="con3">
			<div class="box3">hover</div>
		</div>
	</body>
</html>

```





### submit提交

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<script src="js/jquery-1.12.4.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				
				//在获得焦点的时候做什么事情
//				$('#input01').focus(function(){
//					alert('获得'+$(this)+'的焦点')
//				
//				})
				
				//一般用来让input元素开始就获得焦点，如果两个元素同时有获取焦点的属性，最后只能有最后一个元素获取焦点
				$('#input01').focus();
				
				$('#input01').blur(function(){
					var sval  = $(this).val()
					
					alert('失去焦点并获取到了：'+sval)	
				});
        
				//通过submit提交
				$('#form1').submit(function(){
					alert('提交')
					
					
					//阻止默认行为，通过ajax发送数据。
					return false;
				})
				
			})
		</script>
	</head>
	<body>
		<form id='form1' action="http://www.baidu.com">
			<input type="text" name="" id="input01" value="" />
			<input type="text" name="" id="input02" value="" />
			<input type="submit" name="" id="sub" value="提交" />
		</form>
	</body>
</html>

```



### resize事件

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<script src="js/jquery-1.12.4.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			
			//resize是一个高频触发的事件
			$(window).resize(function(){
				var $w = $(window).width();
				
				document.title = $w;
				
				
				
			})
			
			
			
		</script>
	</head>
	<body>
		
	</body>
</html>

```















# jQuery 参考手册 - 事件

- [jQuery 选择器](http://www.w3school.com.cn/jquery/jquery_ref_selectors.asp)
- [jQuery 效果](http://www.w3school.com.cn/jquery/jquery_ref_effects.asp)

## jQuery 事件方法

事件方法会触发匹配元素的事件，或将函数绑定到所有匹配元素的某个事件。

触发实例：

```
$("button#demo").click()
```

上面的例子将触发 id="demo" 的 button 元素的 click 事件。

绑定实例：

```
$("button#demo").click(function(){$("img").hide()})
```

上面的例子会在点击 id="demo" 的按钮时隐藏所有图像。

| 方法                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [bind()](http://www.w3school.com.cn/jquery/event_bind.asp)   | 向匹配元素附加一个或更多事件处理器                           |
| [blur()](http://www.w3school.com.cn/jquery/event_blur.asp)   | 触发、或将函数绑定到指定元素的 blur 事件                     |
| [change()](http://www.w3school.com.cn/jquery/event_change.asp) | 触发、或将函数绑定到指定元素的 change 事件                   |
| [click()](http://www.w3school.com.cn/jquery/event_click.asp) | 触发、或将函数绑定到指定元素的 click 事件                    |
| [dblclick()](http://www.w3school.com.cn/jquery/event_dblclick.asp) | 触发、或将函数绑定到指定元素的 double click 事件             |
| [delegate()](http://www.w3school.com.cn/jquery/event_delegate.asp) | 向匹配元素的当前或未来的子元素附加一个或多个事件处理器       |
| [die()](http://www.w3school.com.cn/jquery/event_die.asp)     | 移除所有通过 live() 函数添加的事件处理程序。                 |
| [error()](http://www.w3school.com.cn/jquery/event_error.asp) | 触发、或将函数绑定到指定元素的 error 事件                    |
| [event.isDefaultPrevented()](http://www.w3school.com.cn/jquery/event_isdefaultprevented.asp) | 返回 event 对象上是否调用了 event.preventDefault()。         |
| [event.pageX](http://www.w3school.com.cn/jquery/event_pagex.asp) | 相对于文档左边缘的鼠标位置。                                 |
| [event.pageY](http://www.w3school.com.cn/jquery/event_pagey.asp) | 相对于文档上边缘的鼠标位置。                                 |
| [event.preventDefault()](http://www.w3school.com.cn/jquery/event_preventdefault.asp) | 阻止事件的默认动作。                                         |
| [event.result](http://www.w3school.com.cn/jquery/event_result.asp) | 包含由被指定事件触发的事件处理器返回的最后一个值。           |
| [event.target](http://www.w3school.com.cn/jquery/event_target.asp) | 触发该事件的 DOM 元素。                                      |
| [event.timeStamp](http://www.w3school.com.cn/jquery/event_timeStamp.asp) | 该属性返回从 1970 年 1 月 1 日到事件发生时的毫秒数。         |
| [event.type](http://www.w3school.com.cn/jquery/event_type.asp) | 描述事件的类型。                                             |
| [event.which](http://www.w3school.com.cn/jquery/event_which.asp) | 指示按了哪个键或按钮。                                       |
| [focus()](http://www.w3school.com.cn/jquery/event_focus.asp) | 触发、或将函数绑定到指定元素的 focus 事件                    |
| [keydown()](http://www.w3school.com.cn/jquery/event_keydown.asp) | 触发、或将函数绑定到指定元素的 key down 事件                 |
| [keypress()](http://www.w3school.com.cn/jquery/event_keypress.asp) | 触发、或将函数绑定到指定元素的 key press 事件                |
| [keyup()](http://www.w3school.com.cn/jquery/event_keyup.asp) | 触发、或将函数绑定到指定元素的 key up 事件                   |
| [live()](http://www.w3school.com.cn/jquery/event_live.asp)   | 为当前或未来的匹配元素添加一个或多个事件处理器               |
| [load()](http://www.w3school.com.cn/jquery/event_load.asp)   | 触发、或将函数绑定到指定元素的 load 事件                     |
| [mousedown()](http://www.w3school.com.cn/jquery/event_mousedown.asp) | 触发、或将函数绑定到指定元素的 mouse down 事件               |
| [mouseenter()](http://www.w3school.com.cn/jquery/event_mouseenter.asp) | 触发、或将函数绑定到指定元素的 mouse enter 事件              |
| [mouseleave()](http://www.w3school.com.cn/jquery/event_mouseleave.asp) | 触发、或将函数绑定到指定元素的 mouse leave 事件              |
| [mousemove()](http://www.w3school.com.cn/jquery/event_mousemove.asp) | 触发、或将函数绑定到指定元素的 mouse move 事件               |
| [mouseout()](http://www.w3school.com.cn/jquery/event_mouseout.asp) | 触发、或将函数绑定到指定元素的 mouse out 事件                |
| [mouseover()](http://www.w3school.com.cn/jquery/event_mouseover.asp) | 触发、或将函数绑定到指定元素的 mouse over 事件               |
| [mouseup()](http://www.w3school.com.cn/jquery/event_mouseup.asp) | 触发、或将函数绑定到指定元素的 mouse up 事件                 |
| [one()](http://www.w3school.com.cn/jquery/event_one.asp)     | 向匹配元素添加事件处理器。每个元素只能触发一次该处理器。     |
| [ready()](http://www.w3school.com.cn/jquery/event_ready.asp) | 文档就绪事件（当 HTML 文档就绪可用时）                       |
| [resize()](http://www.w3school.com.cn/jquery/event_resize.asp) | 触发、或将函数绑定到指定元素的 resize 事件                   |
| [scroll()](http://www.w3school.com.cn/jquery/event_scroll.asp) | 触发、或将函数绑定到指定元素的 scroll 事件                   |
| [select()](http://www.w3school.com.cn/jquery/event_select.asp) | 触发、或将函数绑定到指定元素的 select 事件                   |
| [submit()](http://www.w3school.com.cn/jquery/event_submit.asp) | 触发、或将函数绑定到指定元素的 submit 事件                   |
| [toggle()](http://www.w3school.com.cn/jquery/event_toggle.asp) | 绑定两个或多个事件处理器函数，当发生轮流的 click 事件时执行。 |
| [trigger()](http://www.w3school.com.cn/jquery/event_trigger.asp) | 所有匹配元素的指定事件                                       |
| [triggerHandler()](http://www.w3school.com.cn/jquery/event_triggerhandler.asp) | 第一个被匹配元素的指定事件                                   |
| [unbind()](http://www.w3school.com.cn/jquery/event_unbind.asp) | 从匹配元素移除一个被添加的事件处理器                         |
| [undelegate()](http://www.w3school.com.cn/jquery/event_undelegate.asp) | 从匹配元素移除一个被添加的事件处理器，现在或将来             |
| [unload()](http://www.w3school.com.cn/jquery/event_unload.asp) | 触发、或将函数绑定到指定元素的 unload 事件                   |