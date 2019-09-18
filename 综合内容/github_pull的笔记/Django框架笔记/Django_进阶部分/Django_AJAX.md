JSON
	概念
		JSON 指的是 JavaScript 对象表示法（JavaScript Object Notation）
		JSON 是轻量级的文本数据交换格式
		JSON 独立于语言 *
		JSON 具有自我描述性，更易理解
	示例
		["one", "two", "three"]
		{ "one": 1, "two": 2, "three": 3 }
		{"names": ["张三", "李四"] }
		[ { "name": "张三"}, {"name": "李四"} ]　
		
		格式不正确的示例
			{ name: "张三", 'age': 32 }  					// 属性名必须使用双引号
			[32, 64, 128, 0xFFF] 							// 不能使用十六进制值
			{ "name": "张三", "age": undefined }  			// 不能使用undefined
			{ "name": "张三",
			  "birthday": new Date('Fri, 26 Aug 2011 07:13:10 GMT'),
			  "getName":  function() {return this.name;} 	// 不能使用函数和日期对象
			}
	相关方法
		JavaScript中关于JSON对象和字符串转换的两个方法：
			JSON.parse(): 用于将一个 JSON 字符串转换为 JavaScript 对象　
				JSON.parse('{"name":"Q1mi"}');
				JSON.parse('{name:"Q1mi"}') ;   // 错误
				JSON.parse('[18,undefined]') ;   // 错误
			JSON.stringify(): 用于将 JavaScript 值转换为 JSON 字符串。　
				JSON.stringify({"name":"Q1mi"})
	和XML的比较	
		书写简单
		一目了然
		可以由解释引擎直接处理
		无需另外添加解析代码

AJAX
	概念
		使用Javascript语言与服务器进行异步交互进行传输的数据的传输
		在不重新加载整个页面的情况下，可以与服务器交换数据并更新部分网页内容。
		无需要任何浏览器插件，但需要用户允许JavaScript在浏览器上执行。
			同步交互：客户端发出一个请求后，需要等待服务器响应结束后，才能发出第二个请求；
			异步交互：客户端发出一个请求后，无需等待服务器响应结束，就可以发第二个请求
		
	示例
	
	常见应用情景
		搜索引擎根据用户输入的关键字，自动提示检索关键字。
		注册时候的用户名的查重	
			整个过程中页面没有刷新，只是刷新页面中的局部位置
			当请求发出后，浏览器还可以进行其他操作，无需等待服务器的响应
	
	AJAX的优缺点
		优点：
			AJAX使用JavaScript技术向服务器发送异步请求；
			AJAX请求无须刷新整个页面；
			因为服务器响应内容不再是整个页面，而是页面中的部分内容,更加专一
		缺点:
			请求杂乱且数量增加,对服务器的压力增加
		
	jQuery实现的AJAX
		HTML部分
			<script>
			  $("#ajaxTest").click(function () {
				$.ajax({
				  url: "/ajax_test/",
				  type: "POST",
				  data: {username: "Q1mi", password: 123456},
				  success: function (data) {
					alert(data)
				  }
				})
			  })
			</script>
		
		views.py部分			
			def ajax_test(request):
				user_name = request.POST.get("username")
				password = request.POST.get("password")
				print(user_name, password)
				return HttpResponse("OK")
		
		urls.py部分
			urlpatterns = [
				...
				url(r'^ajax_test/', views.ajax_test),
				...   
			]
		
		注意:
			$.ajax 参数
				data参数中的键值对，如果值值不为字符串，需要将其转换成字符串类型。
				$("#b1").on("click", function () {
					$.ajax({
					  url:"/ajax_add/",
					  type:"GET",
					  data:{
						"i1":$("#i1").val(),
						"i2":$("#i2").val(),
						"hehe": JSON.stringify([1, 2, 3])},
					  success:function (data) {
						$("#i3").val(data);
					  }
					})
				  })
	
	AJAX请求如何设置csrf_token		
		form 表单提提交数据必须要带scrfToken,哪怕在ajax里面提交也许带这一字段才可以
		
		通过获取隐藏的input标签中的csrfmiddlewaretoken值，放置在data中发送。
		$.ajax({
		  url: "/cookie_ajax/",
		  type: "POST",
		  data: {
			"username": "Q1mi",
			"password": 123456,
			"csrfmiddlewaretoken": $("[name = 'csrfmiddlewaretoken']").val()  // 使用jQuery取出csrfmiddlewaretoken的值，拼接到data中
		  },
		  success: function (data) {
			console.log(data);
		  }
		})
				
		单独写一个CSS文件里面写下面代码
			每次有AJAX 的时候就页面引用一下,其他什么都不用做了.
			function getCookie(name) {
				var cookieValue = null;
				if (document.cookie && document.cookie !== '') {
					var cookies = document.cookie.split(';');
					for (var i = 0; i < cookies.length; i++) {
						var cookie = jQuery.trim(cookies[i]);
						// Does this cookie string begin with the name we want?
						if (cookie.substring(0, name.length + 1) === (name + '=')) {
							cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
							break;
						}
					}
				}
				return cookieValue;
			}
			var csrftoken = getCookie('csrftoken');			
			
			function csrfSafeMethod(method) {
			  // these HTTP methods do not require CSRF protection
			  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
			}

			$.ajaxSetup({
			  beforeSend: function (xhr, settings) {
				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				  xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			  }
			});	
				

	ajax 对于 上传文件的时候一样 有特殊的操作
		
		需要加两个参数
			processData: false,
            contentType: false,
	
		data 必须是 FormDate 类型 
		
序列化
	Django内置的serializers
	可以更加便携进行序列化,当然可以用 json 模块完成
		def books_json(request):
			book_list = models.Book.objects.all()[0:10]
			
			from django.core import serializers
			ret = serializers.serialize("json", book_list)	# 第一个参数为转换的格式,后一个参数为被转换的变量
			return HttpResponse(ret)		
	
	待补充 这个方法是内置的比较粗糙的,实际上很少被使用.
				
				
				
				
				
				