Django 视图系统
	概念
		一个视图函数，简称视图，是一个简单的Python函数，用于接受Web请求并返回Web响应。
		通常将视图函数写在project或app目录中的名为views.py文件中
	简单的实例
		from django.http import HttpResponse
		import datetime
		def current_datetime(request):
			now = datetime.datetime.now()
			html = "<html><body>It is now %s.</body></html>" % now
			return HttpResponse(html)
	定义方式
		CBV
			可读性更加强,将post 和 get请求分开用两个方法定义
				记得更改urls中的调用方式
			实例
				# CBV版添加班级
				from django.views import View
				class AddClass(View):
					def get(self, request):
						return render(request, "add_class.html")
					def post(self, request):
						class_name = request.POST.get("class_name")
						models.Classes.objects.create(name=class_name)
						return redirect("/class_list/")
				# urls.py中
				url(r'^add_class/$', views.AddClass.as_view()),
			
			
		FBV
			代码更加简洁,但是可读性差,urls 中的调用方式简单
			实例
				def add_class(request):
					if request.method == "POST":
						class_name = request.POST.get("class_name")
						models.Classes.objects.create(name=class_name)
						return redirect("/class_list/")
					return render(request, "add_class.html")
	
	给视图加装饰器
		使用装饰器装饰FBV
			FBV本身就是一个函数，所以和给普通的函数加装饰器无差：
			示例:	
				def wrapper(func):
					def inner(*args, **kwargs):
						start_time = time.time()
						ret = func(*args, **kwargs)
						end_time = time.time()
						print("used:", end_time-start_time)
						return ret
					return inner
				# FBV版添加班级
				@wrapper
				def add_class(request):
					if request.method == "POST":
						class_name = request.POST.get("class_name")
						models.Classes.objects.create(name=class_name)
						return redirect("/class_list/")
					return render(request, "add_class.html")
		
		使用装饰器装饰CBV
			类需要特殊的装饰器进行一次封装才行
				from django.utils.decorators import method_decorator
				@method_decorator(wrapper)
	
			给CBV加装饰器可以有多种方式
				给 类 加装饰器
					from django.utils.decorators import method_decorator
					@method_decorator(check_login, name="get")
					@method_decorator(check_login, name="post")
					class HomeView(View):
						def dispatch(self, request, *args, **kwargs):
							return super(HomeView, self).dispatch(request, *args, **kwargs)
						def get(self, request):
							return render(request, "home.html")
						def post(self, request):
							print("Home View POST method...")
							return redirect("/index/")
				给 post 或者 get 加装饰器
					from django.utils.decorators import method_decorator
					class HomeView(View):
						def dispatch(self, request, *args, **kwargs):
							return super(HomeView, self).dispatch(request, *args, **kwargs)
						def get(self, request):
							return render(request, "home.html")
						@method_decorator(check_login)
						def post(self, request):
							print("Home View POST method...")
							return redirect("/index/")
				给 dispatch 加装饰器
					CBV中首先执行的就是dispatch,这样相当于给get和post方法都加上了装饰器
						from django.utils.decorators import method_decorator
						class HomeView(View):
							@method_decorator(check_login)
							def dispatch(self, request, *args, **kwargs):
								return super(HomeView, self).dispatch(request, *args, **kwargs)
							def get(self, request):
								return render(request, "home.html")
							def post(self, request):
								print("Home View POST method...")
								return redirect("/index/")
				
	常用对象
		request对象
			常用的
				path_info     返回用户访问url，不包括域名
				method        请求中使用的HTTP方法的字符串表示，全大写表示。
				GET              包含所有HTTP  GET参数的类字典对象
				POST           包含所有HTTP POST参数的类字典对象
				body            请求体，byte类型 request.POST的数据就是从body里面提取到的
			不常用的特么好多
				属性
					上传文件示例
				请求方法
		HttpResponse对象
			属性
				HttpResponse.content：响应内容
				HttpResponse.charset：响应内容的编码
				HttpResponse.status_code：响应的状态码
			通常用来传递基本字符串信息
				response = HttpResponse("Here's the text of the Web page.")
				response = HttpResponse("Text only, please.", content_type="text/plain")
		
		render对象
			结合返回一个网页对象,必须带参数request,且可以加其他自定义参数
				return render(request, 'myapp/index.html', {'foo': 'bar'})
			render 渲染的到底是什么?
				render渲染的是一个html文件
				html文件中有什么东西 render 自己是不会在意的而且他也不认识你什么html还是js代码
				只(注意是"只"!)会将html文件中的所有的{{ }}{% %}的部分进行相应的渲染替换成所传的值
		
		redirect对象
			重定向
				return redirect('/some/url/')
				return redirect('http://example.com/')
		
		JsonResponse对象
		
			HttpResponse的子类，用来生成JSON编码的响应。
				from django.http import JsonResponse
				response = JsonResponse({'foo': 'bar'})
				print(response.content)		# b'{"foo": "bar"}'
			默认只能传递字典类型，如果要传递非字典类型需要设置一下safe关键字参数。
				response = JsonResponse([1, 2, 3], safe=False)
	
	
	
	
	
	
	
	
	
	