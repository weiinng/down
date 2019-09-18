# flask 笔记


"""
基本框架
"""


	from flask import Flask 

	app = Flask(__name__)

	def index():
		return "index"

	if —__name__ == "__main__":
	app.run()


"""
配置文件系统
"""

	"""
	# settings.py
	
	class Base(object):    # 所有的都要有用到的配置更改 
		TEST = True

	class Dev(Base):
		DEV = True

	class Pro(Base):
		PRO = True 
	"""
		# 方式1 
	app.config["要更改的字段"] = True  # 直接更改
		# 方式2 
	# app.config.from_object("settings.Dev")	# 通过另外指定配置文件来保存更改 
	app.config.from_object("settings.Pro")	# 可以指定多套配置文件随意切换 

"""
路由，视图 
"""

	"""
	FBV 方式
	"""
	from flask import Flask ,url_for
	@app.route("/index/<int:nid>",methods=["POST","GET"],endpoint="n1")   # 自己定义的装饰器要放在路由装饰器下面
		"""
		rule 
			/index/<int:nid> 动态路由，路径中可以带参数 ，必须要指定类型 
			仅允许的类型 ：
				默认不指定的时候按str 处理
				string 	字符串
				float 	浮点型
				path 	路径
				int 	整型
				any 	任何
				uuid 	uuid类型 
			默认的不支持正则路由匹配的 
		methods 
			规定只允许的请求方式 
		endpoint 
			类似于django 中的反向解析用的 name=""
			未指定的时候默认是绑定函数名 endpoint="index"
				ps: 
					如果两个函数都用了装饰器，装饰器还没有 wraps
					endpoint 默认等于 函数名。
					会把装饰器内的 inner 作为  endpoint 值导致出问题
					因此如果再加装装饰器一定要加 wraps 
		view_func 
			视图函数名称
		strict_slashes
			对最后的url 的 "/" 是否严格要求	
			默认是严格匹配
		redirect_to="/index/<nid>" 
			重定向，可加参数 
		
		注意事项：  
			endpoint 不能重名 
				源码将 endpoint和函数名一起进行的判断。
				如果一定要重名，拿函数要相同，不然会报错 
				总之不要重名就行了
		
		其他参数 ：
			
			
		"""
	def index(nid):	# 接受 url 中参数 
		
		print(url_for(n1))	 # 返回路径 
		print(url_for("n1",nid=999))	 # 返回带参数的路径 

		return "index"
			
		"""
		通过源码分析。
			@app.route()的本质就是执行了 add_url_rule(rule,endpoint,f,**options) 方法 
			因此这样子也可以添加路由映射  主流并不是用这种。就装饰器就可以了
		"""
	add_url_rule("/index",None,index)
		
		
	"""
	CBV 方式
		一般情况下还是以FBV居多 
	"""
	class UserView(views.MethodView):
		methods = ["GET"]  		# 限制只允许的请求方式 
		decorators = [wrapper,]	# 加装装饰器 ，会对所有的内部方法加上
		
		def get(self,*args,**kwargs):
			return "get"
		def post(self,*args,**kwargs):
			return "post"
		""" 
		因为无法加装饰器了。只能用 add_url_rule 的方法了
		add_url_rule(rule,endpoint,f,**options)
		as_view 中的参数为 endpoint值
		"""
	add_url_rule("/index",None,UserView.as_view("endpoint")) 
	
	"""
	动态匹配 URL 相关操作 
	"""
		"""
		整个流程
			1. 用户发送请求
			2. flask内部进行正则匹配
			3. 调用to_python(正则匹配的结果)方法
			4. to_python方法的返回值会交给视图函数的参数
		"""
	# 步骤一：定制类
	from werkzeug.routing import BaseConverter
	class RegexConverter(BaseConverter):
		"""
		自定义URL匹配正则表达式
		"""
		def __init__(self, map, regex):
			super(RegexConverter, self).__init__(map)
			self.regex = regex	# 自动帮你匹配正则

		def to_python(self, value):
			"""
			路由匹配时，匹配成功后传递给视图函数中参数的值
			:param value:
			:return:
			"""
			return int(value)

		def to_url(self, value):
			"""
			使用url_for反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
			:param value:
			:return:
			"""
			val = super(RegexConverter, self).to_url(value)
			return val

	# 步骤二：添加到转换器 
	app.url_map.converters['reg'] = RegexConverter

	# 步骤三：使用自定义正则
	@app.route('/index/<reg("\d+"):nid>') # 类型就用自定义的就可以了
	def index(nid):
		print(nid,type(nid))	# 默认是字符串，通过to_python转换成数字

		print(url_for('index',nid=987))	# 反向解析的时候先执行 to_url 方法，还原出来url 再匹配 
		return "index"

	if __name__ == '__main__':
		app.run()	
	
	"""
	请求，响应的参数和类性
	"""
	def index(nid):
		"""
		请求相关信息
		
		* request.method 
		* request.args
		* request.form
		* request.values
		* request.cookies
		* request.headers
		request.path
		request.full_path
		request.script_root
		request.url
		request.base_url
		request.url_root
		request.host_url
		request.host
		request.files
		obj = request.files['the_file_name']
		obj.save('/var/www/uploads/' + secure_filename(f.filename))
		"""
		dic = {"k1":"v1"}
		"""
		返回响应体的4种形式 
			字符串
			jsonify
			模板
			url 
		"""
		return "index"
		return jsonify(dic)
		return render_template("xxx.html",dic=dic)	# 可带数据传递
		return redirect(url_for("index"))	# 跳转通过 url_for 反向解析 
		"""
		定制响应头的时候构造响应体用到 make_response
		"""
		from flask import make_response,headers,set_cookie
		obj = make_response(jsonify(dic))
		obj.headers["xxxxx"] = "123"
		obj.set_cookie("key","value")
		return obj
		
	


"""
装饰器方法实现中间件功能
"""


	# 版本一：
	@app.route('/index')
	def index():
		if not session.get('user'):
			return redirect(url_for('login'))
		return render_template('index.html',stu_dic=STUDENT_DICT)
	
	# 版本二：
	import functools
	def auth(func):
		@functools.wraps(func)
		def inner(*args,**kwargs):
			if not session.get('user'):
				return redirect(url_for('login'))
			ret = func(*args,**kwargs)
			return ret
		return inner

	@app.route('/index')
	@auth
	def index():
		return render_template('index.html',stu_dic=STUDENT_DICT)

	# 应用场景：比较少的函数中需要额外添加功能。
	
	# 版本三：before_request 全局 
	@app.before_request
	def xxxxxx():
		if request.path == '/login':
			return None

		if session.get('user'):
			return None

		return redirect('/login')



"""
模板渲染 
"""
	- 基本数据类型：可以执行python语法，如：dict.get()  list['xx']
	- 传入函数
		- django，自动执行
		- flask，不自动执行
	- 全局定义函数
		@app.template_global()
		def sb(a1, a2):
			# {{sb(1,9)}}
			return a1 + a2

		@app.template_filter()
		def db(a1, a2, a3):
			# {{ 1|db(2,3) }}
			return a1 + a2 + a3
	- 模板继承
		layout.html
			<!DOCTYPE html>
			<html lang="zh-CN">
			<head>
				<meta charset="UTF-8">
				<title>Title</title>
				<meta name="viewport" content="width=device-width, initial-scale=1">
			</head>
			<body>
				<h1>模板</h1>
				{% block content %}{% endblock %}
			</body>
			</html>
		
		tpl.html
			{% extends "layout.html"%}


			{% block content %}
				{{users.0}}
				

			{% endblock %}	
	- include 


		{% include "form.html" %}
		
		
		form.html 
			<form>
				asdfasdf
			</form>
	- 宏
		{% macro ccccc(name, type='text', value='') %}
			<h1>宏</h1>
			<input type="{{ type }}" name="{{ name }}" value="{{ value }}">
			<input type="submit" value="提交">
		{% endmacro %}

		{{ ccccc('n1') }} 

		{{ ccccc('n2') }}
		
	- 安全
		- 前端： {{u|safe}}
		- 前端： MarkUp("asdf")


"""
session 
"""
	加密后放在用户浏览器的 cookie 中  
		流程 
			请求到来
			视图函数
			请求结束
		默认 31天的保存时间
	当请求刚到来：flask读取cookie中session对应的值：eyJrMiI6NDU2LCJ1c2VyIjoib2xkYm95，将该值解密并反序列化成字典，放入内存以便视图函数使用。
	视图函数：
		@app.route('/ses')
		def ses():
			session['k1'] = 123
			session['k2'] = 456
			del session['k1']

			return "Session"
	
				session['xxx'] = 123
				session['xxx']
				
	当请求结束时，flask会读取内存中字典的值，进行序列化+加密，写入到用户cookie中。

"""
闪现
"""
	在session中存储一个数据，读取时通过pop将数据移除。
	from flask import Flask,flash,get_flashed_messages
	@app.route('/page1')
	def page1():

		flash('临时数据存储','error') # 取一次之后就没有了
		flash('sdfsdf234234','error') # 设置分类 
		flash('adasdfasdf','info')

		return "Session"

	@app.route('/page2')
	def page2():
		print(get_flashed_messages(category_filter=['error'])) # 按照分类取出数据
		return "Session"
	

"""
中间件
"""
	基本上不会用，还是用装饰器的方法比较方便

	- call方法什么时候出发？
		- 用户发起请求时，才执行。
	- 任务：在执行call方法之前，做一个操作，call方法执行之后做一个操作。
		class Middleware(object):
			def __init__(self,old):
				self.old = old

			def __call__(self, *args, **kwargs):
				ret = self.old(*args, **kwargs)
				return ret


		if __name__ == '__main__':
			app.wsgi_app = Middleware(app.wsgi_app)
			app.run()
		
"""
特殊装饰器 
"""


	1. before_request	谁先定义谁先执行
	执行多个 before 的时候如果再中间有返回值，对于after 的执行直接执行最后一次定义的那个
		
	2. after_request	谁后定义谁执行 
	
		示例：
			from flask import Flask
			app = Flask(__name__)


			@app.before_request
			def x1():
				print('before:x1')
				return '滚'

			@app.before_request
			def xx1():
				print('before:xx1')


			@app.after_request
			def x2(response):
				print('after:x2')
				return response

			@app.after_request
			def xx2(response):
				print('after:xx2')
				return response



			@app.route('/index')
			def index():
				print('index')
				return "Index"


			@app.route('/order')
			def order():
				print('order')
				return "order"


			if __name__ == '__main__':

				app.run()
	
	3. before_first_request
	
		from flask import Flask
		app = Flask(__name__)

		@app.before_first_request
		def x1():
			print('123123')


		@app.route('/index')
		def index():
			print('index')
			return "Index"


		@app.route('/order')
		def order():
			print('order')
			return "order"


		if __name__ == '__main__':

			app.run()

	
	4. template_global
	
	5. template_filter
	
	6. errorhandler
		@app.errorhandler(404)
		def not_found(arg):
			print(arg)
			return "没找到"












