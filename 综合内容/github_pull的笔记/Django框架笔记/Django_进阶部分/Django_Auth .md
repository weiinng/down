auth
	概念
		Django自带的用户认证系统  
		可简单的执行:用户注册、用户登录、认证、注销、修改密码等功能
		默认使用 auth_user  表来保存用户数据
	
	模块导入
		from django.contrib import auth
	内置方法
		authenticate()   
			用于用户认证功能，即验证用户名以及密码是否正确，
			一般需要username 、password两个关键字参数。
			认证成功(用户名和密码正确有效 )返回一个 User 对象 
				返回的对象是无法直接获取其内部的值得需要用到 login方法加载出来
			认证失败返回匿名用户  所有的字段都为 ""
				user = authenticate(username='theuser',password='thepassword')
		
		login(HttpRequest, user)　　
			该函数接受一个HttpRequest对象，以及一个被authenticate()认证通过的 User对象。
			该函数实现一个用户登录的功能。它本质上会在后端为该用户生成相关session数据。
			在没有login()之前的User对象是无法获取到其属性的
			from django.contrib.auth import authenticate, login
			   
			def my_view(request):
			  username = request.POST['username']
			  password = request.POST['password']
			  user_obj = authenticate(username=username, password=password)
			  if user_obj:
				login(request, user_obj)
				# Redirect to a success page.
				...
			  else:
				# Return an 'invalid login' error message.
				...
			
			login(request, user_obj)之后，
			request.user就能拿到当前登录的用户对象。
			否则request.user得到的是一个匿名用户对象（AnonymousUser Object）。
				匿名函数的所有字段都是 ""
		
		logout(request) 
			该函数接受一个HttpRequest对象，无返回值。
			当调用该函数时，当前请求的session信息会全部清除。
			该用户即使没有登录，使用该函数也不会报错。
			from django.contrib.auth import logout	   
			def logout_view(request):
			  logout(request)
			  # Redirect to a success page.	
			
			
		is_authenticated()
			用来判断当前请求是否通过了认证。
			def my_view(request):
				if not request.user.is_authenticated():	
					return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path)
			
		login_requierd()
			auth 给我们提供的一个装饰器工具，用来快捷的给某个视图添加登录校验。
				from django.contrib.auth.decorators import login_required	  
				@login_required
				def my_view(request):
				  ...
			若用户没有登录，则会跳转到django默认的 登录URL '/accounts/login/ ' 并传递当前访问url的绝对路径 (登陆成功后，会重定向到该路径)。
			如果需要自定义登录的URL，则需要在settings.py文件中通过LOGIN_URL进行修改。
				LOGIN_URL = '/login/'  # 这里配置成你项目登录页面的路由	
						
		create_user()
			auth 提供的一个创建新用户的方法，需要提供必要参数（username、password）等。
				from django.contrib.auth.models import User
				user = User.objects.create_user（username='用户名',password='密码',email='邮箱',...）
		
		create_superuser()
		
			auth 提供的一个创建新的超级用户的方法，需要提供必要参数（username、password）等。
				from django.contrib.auth.models import User
				user_obj = User.objects.create_superuser（username='用户名',password='密码',email='邮箱',...）
						
			也可以通过 teminal 创建
				python manage.py createsuperuser 
			
		check_password(raw_password)
			auth 提供的一个检查密码是否正确的方法，需要提供当前请求用户的密码。
			密码正确返回True，否则返回False。
				ok = user_obj.check_password('密码')
			或者直接针对当前请求的user对象校验原密码是否正确：
				ok = request.user.check_password(raw_password='原密码')
		
		set_password(raw_password)
			auth 提供的一个修改密码的方法，接收 要设置的新密码 作为参数。
				user_obj.set_password("tuotuo")
				user_obj.save() # 修改后必须要保存
			注意：设置完一定要调用用户对象的save方法！！！	
			
	扩展auth 的自定义属性
		可以将自建的表通过继承的方式在可以使用auth的属性情况下添加自定义属性,实现auth表的扩展
			from django.contrib.auth.models import AbstractUser
			class UserInfo(AbstractUser):
				nid = models.AutoField(primary_key=True)
				phone = models.CharField(max_length=11, null=True, unique=True)
		但是需要注意一定要在 settings.py 中加入一行
			AUTH_USER_MODEL = 'app名字.UserInfo'
		
		扩展后的auth 表会被删除的.将会被你自己的表代替,在操作的时候则 不需要用 reques.user 的方式去取
		而是用平时的 models.UserInfo 方式去取即可 ,
		但是依然可以使用 auth 的相关方法和属性,比如创建用户依然是 create_user 什么的
		只是表的源头发生了改变.
		
			
			
			
			
			
			
			
			
			
			