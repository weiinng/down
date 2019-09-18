**通过节点操作，事件委托，选择器 等功能实现的一个计划表案例，这是一个简单的Demo,如果你还想添加更多功能清发挥自己的想象力！**

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			.list_con{
				width: 600px;
				margin: 50px auto 0;
			}
			.inputtxt{
				width: 550px;
				height: 30px;
				border: 1px solid #ccc;
				padding: 0px;
				text-indent: 10px;
			}
			.inputbtn{
				width: 40px;
				height: 32px;
				padding: 0;
				border: 1px solid #ccc;
			}
			.list{
				margin: 0;
				padding: 0;
				list-style: none;
				margin-top: 20px;
			}
			.list li{
				height: 40px;
				line-height: 40px;
				border-bottom: 1px solid #ccc;
			}
			.list li span{
				float: left;
			}
			.list li a{
				float: right;
				text-decoration: none;
				margin: 0 10px;
			}
		</style>
		<script src="js/jquery-1.12.4.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				
				var $inputtext = $('#txt1');
				var $btn = $('#btn1');
				var $ul = $('#list');
				
				$btn.click(function(){
					// 获取输入框的内容
					var $val = $inputtext.val()
					if($val == ''){
						alert('请输入内容！！')
						return;
					}
					var $li = $('<li><span>'+ $val +'</span><a href="javascript:;" class="up">↑</a><a href="javascript:;" class="down">↓</a><a href="javascript:;" class="del">删除</a></li>') 
					
//					var $a = $li.find('.del');
//					$a.click(function(){
//						$(this).parent().remove();
//					})
					
					// 这里有两种方式
					//1.将A元素添加到B元素。
					$li.appendTo($ul)
					
					//2.为B元素添加A元素。
//					$ul.append($li)
					
					//清空
					$inputtext.val('');
				})
				
//				$('.del').click(function(){
//					$(this).parent().remove()
//				})
				
				$ul.delegate('a','click',function(){
					var $handler = $(this).prop('class');
					if($handler =='del'){
						$(this).parent().remove();
					}
					if($handler == 'up'){
						
						//prev() 选择紧挨这个元素前面的同辈元素
						if($(this).parent().prev().length==0){
							alert('已经到顶了')
						}
						else{
							$(this).parent().insertBefore($(this).parent().prev())
						}
					}
					if($handler == 'down'){
						
						//prev() 选择紧挨这个元素后面的同辈元素
						
						if($(this).parent().next().length==0){
							alert('已经到底了')
						}
						else{
							$(this).parent().insertAfter($(this).parent().next())
						}
					}
					
				})
			})
		</script>
	</head>
	<body>
		<div class="list_con">
			<h1>to do list</h1>
			<input type="text" name="" id="txt1" value="" class="inputtxt" />
			<input type="button" name="" id="btn1" value="添加" id='btn' class="inputbtn" />
			
			<ul id="list" class="list">
				<li>
					<span>学习html</span>
					<a href="javascript:;" class="up">↑</a>
					<a href="javascript:;" class="down">↓</a>
					<a href="javascript:;" class="del">删除</a>
				</li>
				<li>
					<span>学习scc</span>
					<a href="javascript:;" class="up">↑</a>
					<a href="javascript:;" class="down">↓</a>
					<a href="javascript:;" class="del">删除</a>
				</li>
				<li>
					<span>学习javascript</span>
					<a href="javascript:;" class="up">↑</a>
					<a href="javascript:;" class="down">↓</a>
					<a href="javascript:;" class="del">删除</a>
				</li>
			</ul>
			
			<!--# 默认会链接到页面顶部-->
			<!--<a href='#'>链接</a>-->
			
			<!--<a href="javascript:alert('OK')">弹框！</a>-->
			
			<!--如果javascriot里面什么都不放就是拥有a标签的样式但是不执行任何操作-->
			<!--<a href="javascrpt:;">拥有a标签的样式但是不执行任何操作</a>-->
			
			
		</div>
	</body>
</html>

```

