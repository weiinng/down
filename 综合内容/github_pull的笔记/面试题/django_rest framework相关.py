notepad ++ 快速折叠快捷键 alt+0  alt+shift+0


django rest framework
	"""
	帮助我们快速搭建基于 restful 规范的接口的功能组件
	"""
	
什么是接口?
	"""
	- URL	python 中
	- Jave/c# 	A接口里面有个 a 方法，B类继承了A接口，B里面就必须要有 a 方法
	"""
	
restful 规范
	"""
	1 根据method 不同，进行不同的操作
		原来都是在 url 中设置。这样可以大大减少 url 的数量
		GET/POST/PUT/DELETE/PATCH
	2 面向资源编程
		视 URL 为资源
		http://www.yangtuo.com
	3 体现版本
		http://v1.yangtuo.com
		http://v2.yangtuo.com
	4 体现是 API
		http://api.yangtuo.com
		http://yangtuo.com/api/salary
	5 建议使用 https 更安全
		https://www.yangtuo.com
	6 响应式设置状态码
		200 300 400 500
		return HttpResponse("text_data",status=300)
	7 条件
		http://yangtuo.com/v2/api/salary?page=1&size=10
	8 返回值
		http://yangtuo.com/v2/api/salary
			GET:	返回所有的列表
				[
					{"id":1,"title":"lala"},
					{"id":2,"title":"wawa"},
					{"id":3,"title":"kaka"},
				]
			POST:	返回新增的数据
				{"id":1,"title":"tuotuo"}

			PUT:	更新全部的数据  返回更新数据

			PATCH: 	更新少量数据  返回更新数据

			DELETE:	删除数据  返回空
	9 返回错误信息
		{code:10000,
		error:"xxx错了"}
	10 Hypermedia API
		返回信息的时候加上 api

	记忆方式
		URL 5个
			https（推荐用https）://v2（版本）/yangtuo.com（域名为资源）/api（体现api）/salary?page=1&size=10（有条件）
		请求 1 个
			根据method 不同，进行不同的操作
		返回 4个
			返回值 响应式设置状态码 返回错误信息 返回信息的时候加上api
	"""

django rest faramework 框架组件 （10）
	"""
	- 权限
	- 认证
	- 频率限制
		面试题：如何实现的访问频率控制？
			匿名用户：无法控制，因为用户可以换代理IP
				{192.168.1.1:[1521223123.232, 1521223122.232, 1521223121.232],
				192.168.1.2:[1521223123.232, 1521223122.232, 1521223121.232],
				192.168.1.3:[1521223123.232, 1521223122.232, 1521223121.232],
				192.168.1.4:[1521223123.232, 1521223122.232, 1521223121.232],
				192.168.1.5:[1521223123.232, 1521223122.232, 1521223121.232],
				192.168.1.6:[1521223123.232, 1521223122.232, 1521223121.232],}
			登录用户：如果有很多账号，也无法限制
				{alex:[1521223123.232, 1521223122.232, 1521223121.232],
				eric:[1521223123.232, 1521223122.232, 1521223121.232],}
			参考源码：from rest_framework.throttling import SimpleRateThrottle
	- 序列化 （最重要）
		- 对于对象和 queryset对象序列化的区别
			- queryset对象 序列化的时候需要加 many=True
		-  many=True ？内部原理是什么呢？
			- 实例化的时候在 调用 init 之前先调用了 new 方法
				- new 方法基于 queryset对象返回的是 ListSerializer 对象
				- 基于普通对象返回的就是本身
	- 路由
	- 视图
		面试题：你的写的类都继承过哪些类？
			from rest_framework.views import APIView # *  所有的方法都在这里
			from rest_framework.generics import GenericAPIView # 数据库链接以及数据传入
			from rest_framework.viewsets import GenericViewSet # 期待as_view可以带参数的时候必须要继承这个类
			from rest_framework.viewsets import ModelViewSet # 重写增删改查的时候要继承这个类
	- 分页
	- 解析器
	- 渲染器
		规定页面显示的效果，没什么卵用
	- 版本
	"""

谈谈你对 django rest framework 框架的认识？
	"""
	- 路由， 
		- 可以通过as_view传参数，根据请求方式不同执行相应的方法
		- 可以在url中设置一个结尾，类似于： .json 
	- 视图，
		- 帮助开发者提供了一些类，并在类中提供了多个方法以供我们使用。
	- 版本，
		- 在url中设置version参数，用户请求时候传入参数。在request.version中获取版本，根据版本不同做不同处理
	- 认证，
		-  写一个类并注册到认证类，在类的的authticate方法中编写认证逻辑。
			- 认证成功（user,auth）
			- raise AuthticateFaild(....)
			- None 
	- 权限
		-  写一个类并注册到权限类，在类的的has_permission方法中编写认证逻辑。
			- True 
			- False 
	- 频率限制
		-  写一个类并注册到频率类，在类的的 allow_request/wait 方法中编写认证逻辑。
			allow_request
				- True 
				- False  如果返回False，那么就要执行wait			
	- 解析器，
		- 根据ContentType请求头，选择不同解析器对 请求体中的数据进行解析。
			POST /index/ http1.1.\r\nhost:11.11.11.11\r\nContent-Type:url-formendo.... \r\n\r\nuser=alex&age=123
			POST /index/ http1.1.\r\nhost:11.11.11.11\r\nContent-Type:application/json\r\n\r\n{....}
	- 分页 
		- 对从数据库中获取到的数据进行分页处理: SQL -> limit offset 
			- 根据页码：http://www.luffycity.com/api/v1/student/?page=1&size=10
			- 根据索引：http://www.luffycity.com/api/v1/student/?offset=60&limit=10
			- 根据加密：http://www.luffycity.com/api/v1/student/?page=erd8
			
		提问：页码越大速度越慢，为什么以及如何解决？
			  原因：页码越大向后需要扫描的行数越多，因为每次都是从0开始扫描。
			  解决：
					- 限制显示的页数
					- 记录当前页数据ID最大值和最小值，再次分页时，根据ID现行筛选，然后再分页。
	- 序列化
		- 对queryset序列化以及对请求数据格式校验。
	- 渲染器
		- 根据URL中传入的后缀，决定在数据如何渲染到到页面上。
	"""
	
django rest framework生命周期：
	"""
	发送请求-->
	Django的wsgi-->
	中间件-->
	路由系统_执行CBV的as_view()，就是执行内部的dispath方法-->
	在执行dispath之前，有版本分析 和 渲染器-->
	在dispath内，对request封装-->
	版本-->
	认证-->
	权限-->
	频率-->
	视图-->
	如果视图用到缓存( request.data or   request.query_params )就用到了 解析器-->
	视图处理数据，用到了序列化(对数据进行序列化或验证) -->
	视图返回数据可以用到分页
	"""

