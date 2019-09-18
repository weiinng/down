Django 路由系统
	基本格式
		from django.conf.urls import url
			urlpatterns = [
				 url(正则表达式, views视图函数，参数，别名),
			]

		参数说明
			正则表达式：一个正则表达式字符串
			views视图函数：一个可调用对象，通常为一个视图函数或一个指定视图函数路径的字符串
			参数：可选的要传递给视图函数的默认参数（字典形式）
			别名：一个可选的name参数

	路由匹配方式
		1. 正则表达式的模糊匹配
		2. 分组匹配     	()  				 	--> 相当于给视图函数传递位置参数
		3. 分组命名匹配   	(?P<name>正则表达式) 	--> 相当于给视图函数传递关键字参数

		注意：
			1. 分组匹配和分组命名匹配不能混合使用			
			2. URLconf 匹配的位置
				无视域名和参数
					http://www.example.com/myapp/ 请求中，URLconf 将查找myapp/。
					在http://www.example.com/myapp/?page=3 请求中，URLconf 仍将查找myapp/。	
			3. URLconf 不检查请求的方法				
			4. 捕获的参数永远都是字符串			
			5. 视图函数中指定默认值	
				# urls.py中
				from django.conf.urls import url
				from . import views
				urlpatterns = [
					url(r'^blog/$', views.page),
					url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
				]
				# views.py中，可以为num指定默认值
				def page(request, num="1"):
					pass

	正则表达式详解
		基本示例
			from django.urls import re_path
			from app01 import views	 
			urlpatterns = [
				re_path(r'articles/2003/$', views.special_case_2003), # 静态路由
				re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive), # 动态路由
				re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive), # 动态路由
				re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail), # 动态路由
			]　
		
		注意事项
			urlpatterns中元素按照从上往下逐一匹配正则表达式，匹配成功则不再继续。
			若要从URL中捕获一个值，只需要在它周围放置一对圆括号（分组匹配）。
			最前面不需要加一个反斜线
			每个正则表达式前面的'r' 是可选的但是建议加上。
		
		补充说明：
			# 是否开启URL访问地址后面不为/跳转至带有/的路径的配置项
			APPEND_SLASH=True
			
			Django settings.py配置文件中默认没有 APPEND_SLASH 这个参数，
			但 Django 默认这个参数为 APPEND_SLASH = True。 其作用就是自动在网址结尾加'/'。
			其效果就是：
				我们定义了urls.py：
					from django.conf.urls import url
					from app01 import views
					urlpatterns = [
							url(r'^blog/$', views.blog),
					]
					访问 http://www.example.com/blog 时，默认将网址自动转换为 http://www.example/com/blog/ 。
				如果在settings.py中设置了 APPEND_SLASH=False，
				此时我们再请求 http://www.example.com/blog 时就会提示找不到页面。
	
	分组命名匹配
		基本语法
			(?P<name>pattern)
		实现功能
			捕获的值作为关键字参数而不是位置参数传递给视图函数。
		示例
			urls中：
				url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
			views中：
				views.month_archive(request, year="2017", month="12")	
	
	include 路由分流
		引入其他 urls.py 文件
			当多个app的时候可以再 各app内部创建自己 urls.py 
			在总的urls 中需要 导入分流的各app内部的urls.py
		引入方式
			from django.cinf.url import url,include
		工作原理
			当请求来了由主urls进行匹配,匹配到子urls后由子urls进行下一步匹配
		示例
			from django.conf.urls import include, url
			from app01 import url
			urlpatterns = [
				url(r'^admin/', admin.site.urls),
				url(r'^app01/', include('urls')),  # 可以包含其他的URLconfs文件
			]
			# 当一个 app01/xxxx 的路径请求来了之后 会首先匹配到 ^app01/ 而后转向 app01.url 继续下一步匹配
		
	反向解析 URL 
		本质上就是给url匹配模式起别名，然后用过别名拿到具体的URL路径
		起别名
			在url匹配模式中，定义name="别名"
			url(r'^home', views.home, name='home'),  			# 给我的url匹配模式起名为 home
			url(r'^index/(\d*)', views.index, name='index'),    # 给我的url匹配模式起名为index
		
		通过别名拿到具体路径
			1. 模板语言中：
				直接取到路径
					{% url "别名" %}  // 通过别名拿到具体路径
				如果urls中有位置参数或者关键字参数
					{% url "别名"  2018 "nb" %}
			2. 视图函数中
				首先要导入
					django.utils import reverse
				直接取到路径:
					reverse("别名")	 # 通过别名拿到具体路径
				如果urls中有位置参数或者关键字参数,依然可以传值
					传位置参数：
						reverse("别名", args=(2018, "nb"))	
					传关键字参数：
						reverse("别名" kwargs={"year": 2018, "title": "nb"})
	
	命名空间 	
		即使不同的APP使用相同的URL名称，URL的命名空间模式也可以让你唯一反转命名的URL
		
		示例:
			project中的urls.py
				from django.conf.urls import url, include
				urlpatterns = [
					url(r'^app01/', include('app01.urls', namespace='app01')),
					url(r'^app02/', include('app02.urls', namespace='app02')),
				]
			
			app01中的urls.py
				from django.conf.urls import url
				from app01 import views			 
				app_name = 'app01'
				urlpatterns = [
					url(r'^(?P<pk>\d+)/$', views.detail, name='detail')
				]

			app02中的urls.py
				from django.conf.urls import url
				from app02 import views			 
				app_name = 'app02'
				urlpatterns = [
					url(r'^(?P<pk>\d+)/$', views.detail, name='detail')
				]
		工作原理:
			app01 和 app02 中都有相同的 别名 "detail" 
			为了区分,在总的 urls 上做命名空间,
			在原有的别名基础上需要加上命名空间的预定值才可以正确取到路径
				模板中使用：
					{% url 'app01:detail' pk=12 pp=99 %}
				views中的函数中使用
					v = reverse('app01:detail', kwargs={'pk':11})
				 这样即使app中URL的命名相同，我也可以反转得到正确的URL了。

				
				
				
				
				
				
				
				
				
				
				