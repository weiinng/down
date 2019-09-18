	
# 启动流程 

# 启动入口简约版代码  
from werkzeug.wrappers import Response
from werkzeug.serving import run_simple

class Flask(object):
	def __call__(self,environ, start_response):
		response = Response('hello')
		return response(environ, start_response)

	def run(self):
		run_simple('127.0.0.1', 8000, self)




from flask import Flask 

"""
1 实例化对象 app 
""" 
app = Flask(__name__)

"""
2 设置路由
	将路由关系放在 app.url_map = {} 中
"""
@app.route("/index")
def index():
	return "index"

if —__name__ == "__main__":
"""
3 启动socket服务端 
"""
	app.run()

"""
4 用户请求到来就会执行 __call__ 方法 
"""




"""
run_simple(host,port,self,**options) 
	会对第三个传入的参数加()进行执行
	第三个参数如果是对象就执行其 __call__ 方法
"""

	
def __call__(self,environ, start_response):
	# environ 请求相关的所有数据 第一手的数据，由wsgi进行的初步封装
	# start_response 用于设置响应相关数据 
	return wsgi_app(environ,start_response)

def wsgi_app(environ,start_response):

	ctx = self.request_context(environ) 
		"""
		def request_context(...)
			return RequestContext(self, environ)

		RequestContext()
			def __init__(...)
				...
				request = app.request_class(environ)
				self.request = request	# 创建 request
				self.session = None	# 创建 session 

		request_class = Request  
		"""
	...
	ctx.push() 
		...
		_request_ctx_stack = LocalStack()
		"""
		class LocalStack(object):
		    def __init__(self):
				self._local = Local()
				
		class Local(object):
			__slots__ = ('__storage__', '__ident_func__')

			def __init__(self):
				object.__setattr__(self, '__storage__', {})
				object.__setattr__(self, '__ident_func__', get_ident)
			def __delattr__(self, name):
			def __setattr__(self, name, value):
			def __getattr__(self, name):
		"""
		
		self.session = session_interface.open_session()
		"""
			 # 取写 session 

		def open_session(...):
			val = request.cookies.get(app.session_cookie_name)	# 通过配置文件的session_cookie_name来取
		"""
		
		
	response = self.full_dispatch_request()
		"""
		def full_dispatch_request(self): 
			rv = self.dispatch_request() # 调用视图函数 
			return self.finalize_request(rv) # 进行善后工作 


		def finalize_request(...):
			response = self.process_response(response)

		def process_response(...):
			self.session_interface.save_session(....) 
			

		def save_session(...):
			val = self.get_sighing_serializer(app).dumps(dict(session))
			response.set_cookie( # 写入cookie 
			...
			val 
			)
		"""









"""
以上就是所有的Flack 的源码流程 
"""

__call__() -> 对 environ 第一次封装 
wsgi_app () ->  
	request_context() ->  environ第二次封装 ，具体实现 ： 封装了 request 以及 session（空的）
		RequestContext() -> init 初始化  1.通过 request_class 创建了 Request 对象 2 .创建空的 self.session
			request_class() ->  创建 Request 对象具体操作实现 
	push -> 1. 将 ctx Localstack对象，再由Localstack对象传给 Local 对象保存起来 
			2. 执行 open_session 将self.session 重新赋值
		LocalStack--> 传 ctx 给 Local
			Local--> 对 ctx 的操作 
			
		open_session -->通过配置文件的 配置名字 取到 session 然后解密反序列化生成字典重新赋值 ctx.session 的具体操作实现
	full_dispatch_request --> 1.调用执行视图函数  2.善后工作 
		dispatch_request--> 调用执行视图函数具体操作 
			finalize_request--> 善后工作具体操作
				process_response-->
					save_session-->	写入cookie的具体操作  


 上下文管理（第一次）
		请求到来时候：
			# ctx = RequestContext(self, environ) # self是app对象，environ请求相关的原始数据
			# ctx.request = Request(environ)
			# ctx.session = None
			
			# 将包含了request/session的ctx对象放到“空调”
				{
					1232：{ctx:ctx对象}
					1231：{ctx:ctx对象}
					1211：{ctx:ctx对象}
					1111：{ctx:ctx对象}
					1261：{ctx:ctx对象}
				}
		视图函数：
			from flask import reuqest,session 
			
			request.method 
			
			
		请求结束：
			根据当前线程的唯一标记，将“空调”上的数据移除。


		Local 中如何存储？
			__storage__ = {
				线程/协程id:{}
			}
		Localstack 做了什么？ 
			__storage__ = {
				线程/协程id:{stack:[ctx]}  # 维护成一个栈 
			}	# 都是通过 Localstack 来操作 local 里面的数据结构


"""
第一阶段：请求到来
    将request和Session相关数据封装到ctx=RequestContext对象中。
    再通过LocalStack将ctx添加到Local中。
    __storage__ = {
        1231:{'stack':[ctx(request,session)]}
    }
第二阶段：视图函数中获取request或session
    方式一：直接找LocalStack获取
            from flask.globals import _request_ctx_stack
            print(_request_ctx_stack.top.request.method)
            
    方式二：通过代理LocalProx获取
            from flask import Flask,request
            print(request.method)
"""

1. 上下文管理：LocalProxy对象
	2. 上下文管理：
			- 请求上下文（ctx=RequestContext()）：request/session
			-  App上下文（app_ctx=AppContext()）: app/g
			
		- 程序启动：
			两个Local：
				local1 = {
				
				}
				
				local2 = {
				
				}
		
			两个LocalStack:
				_request_ctx_stack
				_app_ctx_stack
		- 请求到来
			对数据进行封装：
				ctx = RequestContext(request,session)
				app_ctx = AppContext(app,g)
			保存数据
				将包含了(app,g)数据的app_ctx对象，利用 _app_ctx_stack（LocalStack()）将app_ctx添加到Local中
					storage = {
						1231:{stack:[app_ctx(app,g),]}
					}
				将包含了request,session数据的ctx对象，利用_request_ctx_stack（LocalStack()），将ctx添加到Local中
					storage = {
						1231:{stack:[ctx(request,session),]}
					}
					
		- 视图函数处理：
			
			
			from flask import Flask,request,session,current_app,g

			app = Flask(__name__)


			@app.route('/index')
			def index():
				# 去请求上下文中获取值 _request_ctx_stack
				request.method # 找小东北获取值
				session['xxx'] # 找龙泰获取值
				
				# 去app上下文中获取值：_app_ctx_stack 
				print(current_app)
				print(g)
				
				return "Index"


			if __name__ == '__main__':
				app.run()
				app.wsgi_app
		
		- 结束
			_app_ctx_stack.pop()
			_request_ctx_stack.pop()



































	