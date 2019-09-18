django 请求生命周期
	"""
		--> 执行遵循 wsgi 协议的模块 （socket 服务端）
			---> wsgi在这里请求数据进行初次封装
			---> django框架进行第二次封装成我们习惯的数据（request 对象）
		--> 中间件
			---> 在请求对象中进行其他操作，例如：csrf session
		--> 路由匹配
		--> 视图函数 （业务处理，ORM，模板渲染）
		--> 中间件
			---> 对响应的数据进行处理，例如：缓存
		--> wsgi
			---> 将响应内容发给浏览器
	"""

wsgi 是什么？
	"""
	中文 web服务网关接口，wsgi 是一个协议
	
	实现该协议的模块：
		- wsgiref	默认单线程 性能会稍微差一点
		- werkzurg	默认单线程 性能会稍微差一点
		- uwsig 	性能更高一些 
	
	实现其协议的模块本质上就是socket服务端用于接受用户请求
	
	一般web 框架都是基于 wsgi 来实现。从而实现关注点分离
		框架关注 请求的逻辑处理。 wsgi关注 拿请求
		
		wsgiref示例：
			from wsgiref.simple_server import make_server
 
			def run_server(environ, start_response):
				start_response('200 OK', [('Content-Type', 'text/html')])
				return [bytes('<h1>Hello, web!</h1>', encoding='utf-8'), ]
			 
			 
			if __name__ == '__main__':
				httpd = make_server('127.0.0.1', 8000, run_server)
				httpd.serve_forever()
		
		werkzeug示例：
			from werkzeug.wrappers import Response
			from werkzeug.serving import run_simple

			def run_server(environ, start_response):
				response = Response('hello')
				return response(environ, start_response)

			if __name__ == '__main__':
				run_simple('127.0.0.1', 8000, run_server)

		Flask源码入口：
			from werkzeug.wrappers import Response
			from werkzeug.serving import run_simple

			class Flask(object):
				def __call__(self,environ, start_response):
					response = Response('hello')
					return response(environ, start_response)

				def run(self):
					run_simple('127.0.0.1', 8000, self)
	"""

中间件是什么？
	"""
		介于request与response处理之间的一道轻量级处理过程，用于全局改变django 的输入输出
		
		里面有5个方法
			process_request(self,request)
			process_view(self, request, callback, callback_args, callback_kwargs)
			process_template_response(self,request,response)
			process_exception(self, request, exception)
			process_response(self, request, response)
		
		都用中间件做过什么？
			登陆验证
				装饰器方法对每个页面验证改成用中间件来做省去代码冗余
			权限
				当用户登陆获取当前用户的权限放入session
				访问目标页面的时候对目标页面的url在session中匹配
			跨域
				-jsonp 基于script标签的src 属性然后动态创建script标签来实现
				-core 设置响应头
				应用：本地开始前后端分离的时候使用
	"""

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
	
request.POST 获取不到值的原因 ？ 如何解决？
	"""
	发送数据格式：
		方式一：
			request.post(
				url='xx',
				data={'k1':'v1,'k2':'v2'}
			)
			#数据：  POST /  http1.1\r\nContent-type:urlencode-form.......\r\n\r\nk1=v1&k2=v2
			保证以下条件 request.POST  必然可取到值
				- content-type: urlencode-form
				- 数据格式：k1=v1&k2=v2

		方式二：
			request.post(
				url='xx',
				json={'k1':'v1,'k2':'v2'}
			)
			#数据：  POST /  http1.1\r\nContent-type:application/json....\r\n\r\n{'k1':'v1,'k2':'v2'}
			只能在 request.body  中取值
				取值的时候要 转换字符串 以及 反序列化
					字节 = {'k1':'v1,'k2':'v2'}
					字节转换字符串
					反序列化字符串 -> 字典 
		
	如何判断发生的是 data 还是 json 格式的数据？
		在 chrome 浏览器中可以查看回应的数据 ->
			Form Data:
				phone=861513125555&password=12312312312&oneMonth=1
				
				reqeusts.post(
					url=url,
					data={
						phone:123123123123,
						password:asdfasdf
					}
				)
			
			Request Payload:
				{"BaseRequest":{"Uin":981579400,"Sid":"zWvteTWqBop4heoT","Skey":"@crypt_2ccf8ab9_a710cf413c932e201987599558063c8e","DeviceID":"e358217921593270"},"Msg":{"Type":1,"Content":"test","FromUserName":"@60eef3f2d212721fda0aae891115aa7a","ToUserName":"@@6a5403f510a3192454ed1afebd78ec6033d5057c9038d7b943b201f0a74987d4","LocalID":"15300708105840758","ClientMsgId":"15300708105840758"},"Scene":0}
			
				reqeusts.post(
					url=url,
					json={
						phone:123123123123,
						password:asdfasdf
					}
				)
				
				reqeusts.post(
					url=url,
					data=bytes(json.dumps({
						phone:123123123123,
						password:asdfasdf
					}),encoding=utf-8)
				)
		在 火狐 浏览器中可以查看回应的数据 中文显示更明显 
			表单数据
			Json 
	"""









































