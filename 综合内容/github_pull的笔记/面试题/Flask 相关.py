谈谈你对django 和 flask 的认识 
	"""
		django 内容比较丰富 大型项目推荐用django
		
		flask 更加精练 直接导入就可以使用 但是扩展性很强 小型的轻量级的项目推荐用 flask 
		
		最大的不同 
			request 
				django  通过参数传递
				flask 	通过模块导入
			session 
				django  依附在request 里面 
				flask 	通过模块导入
	"""

django 和 flask 哪个好呢 ？
	"""
		没有好坏之分，只是两种实现方式，两种都好 
	"""

flask 中的配置文件？
	"""
	技术点：
		- rsplit 		从后方切最后的字段
		- importlib		基于字符串引入模块
		- getattr 		反射方法
	
	类似于django 的中间件
	"""

flask 中的蓝图？
	"""
	
	"""
	
flask 中的装饰器？
	"""
	
	"""

flask 中的路由系统
	"""
	基于装饰器实现的路由系统
	技术点： 
		- functions.wraps(func) 	保留原函数元信息
	"""

flask 中的视图系统
	"""
	FBV  CBV
	技术点： 
		- 反射方法
		
	请求：request 

	响应：response 
	
	
	"""

flask 上下文理解 ？
	"""
		上下文管理是 flask 独有的，对比django是没有的上下文管理的
		
		flask 的上下文管理分为两种
			请求上下文管理
			应用上下文管理 
		
		具体的实现机制，两种管理都是一样的
			基本流程：
				请求到来的时候
					将 request相关 和session相关的数据 封装到 RequestContext 
						ctx = RequestContext(request,session)
					将 app 和 g 封装到 AppContext 
						app_ctx = AppContext(app,g)
					再将这两个对象 交给 Locakstark 对象 
					再由 Locakstark 对象将数据 放在 Locak 对象中 
				视图函数获取数据的时候
					可以直接通过 Locakstark 对象直接 对 ctx 进行操作，但是操作较为繁琐
					也可以直接通过 Locakproxy 对象+偏函数 调用 Locakstark 去 Locak 中获取 ctx，app_ctx封装的值
				请求结束的时候
					调用 Locakstark 的 pop 方法 将 ctx 和 app_ctx 进行移除
			
				
			Locak 是什么？ 作用？
				基于协程 对每个协程进行标识
				为每个协程分配内存空间
				从而实现数据基于协程的空间隔离
			
			Locak 中 存储的数据结构是怎么样子的呢？
				storage = {
						1231:{},
						1221:{},
					}
		
			Locakstark 是什么? 作用？
				将 Locak 中的数据结构维护成这样：
					storage = {
						1231:{stack:[app_ctx(app,g),]}
					}
					storage = {
						1231:{stack:[ctx(request,session),]}
					}
				对 __storage__ 中的 栈 进行数据操作 
					具体操作 由 push 和 pop
			
			为什么要维护成一个栈呢？
			
			
			为什么要分成两个呢？ctx 和 app_ctx 的必要性是什么? 
				ctx = RequestContext(request,session) 
				app_ctx = AppContext(app,g)
					ctx 封装了 request 和 session 
					app_ctx 封装了 app 和 g 
				
				在使用离线脚本的时候，比如 SQLAlchemy 的创建表的时候
				ctx 用不上的，我们需要用到的是 app_ctx里面的 app 
			
			这个 g 是干什么的呢？
				g 相当于一个仅对一次请求生效的全局变量
				自请求到来诞生，也随请求结束而被销毁
				
			为什么每次导入 request 就能使用?
				每次执行request.xx方法时，会触发LocalProxy对象的__getattr__等方法，
				由方法每次动态的使用LocalStack去Local中获取数据。
			
			Locak 有几个? Locakstark 有几个？
				Locak只有两个， 一个请求 Locak 一个 app Locak 
				Locakstark 只有两个 ，一个请求 Locakstark 一个 app Locakstark
				不论是单线程还是多线程都是只有两个 
				而且在单 app 情况下，stack 里面的值只有一个 app_ctx 
				在离线脚本的时候，多个app 的时候 
					请求 Locak 里没有 值，因为用不大
					app Locak 里的 stack 里面可能有多个 app_ctx
	"""

thread.Local 的作用？
	"""
		基于协程 对每个协程进行标识
		为每个协程分配内存空间
		从而实现数据基于协程的空间隔离
		
		在哪里用过呢?
			UButils 中对每个线程创建的时候用到 
			flask 的上下文管理中的 Locak 类更加高级
			SQLAlchemy  的多线程创建数据库链接操作的时候
	"""

beforerequest 的实现原理？ 
"""
	将要循环使用的视图加入到了一个列表
	执行时机是 在视图函数执行之前 
	循环那个列表进行相应的操作 
	
	
	afterrequest 和 beforerequest 一样
	但是在循环列表的时候 reversed 反转了一下
	
"""





















