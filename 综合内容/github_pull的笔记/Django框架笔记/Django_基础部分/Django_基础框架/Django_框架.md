Python web框架的本质:
	收发socket消息    			   --> 按照HTTP协议消息格式去解析消息		
	路径和要执行的函数的对应关系   --> 主要的业务逻辑		
	字符串替换                     --> 模板(特殊符号 --> 数据)
		
	一个完整得请求流程:
		0. 启动服务端,等待客户端(用户的浏览器)来连接
		1. 在浏览器地址栏输入URL,与服务端建立连接,浏览器发送请求
		2. 服务端收到请求消息,解析请求消息,根据路径和函数的对应关系,找到将要执行的函数
		3. 执行函数,打开HTML文件,进行字符串替换,得到一个最终要返回的HTML内容
		4. 按照HTTP协议的消息格式要求,把HTML内容回复给用户浏览器(发送响应)
		5. 浏览器收到响应的消息之后,按照HTML的规则渲染页面
		6. 关闭连接

socket服务端功能划分:
			a. 负责与浏览器收发消息(socket通信)  --> wsgiref/uWsgi/gunicorn...			
			b. 根据用户访问不同的路径执行不同的函数		
			c. 从HTML读取出内容,并且完成字符串的替换  --> jinja2(模板语言)
			
		 Python中 Web框架的分类:
			 按上面三个功能划分:
				1. 框架自带a,b,c                 --> Tornado
				2. 框架自带b和c,使用第三方的a    --> Django
				3. 框架自带b,使用第三方的a和c    --> Flask
			 按另一个维度来划分:
				1. Django   --> 大而全(你做一个网站能用到的它都有)
				2. 其他     --> Flask 轻量级

新建Django项目
	Django安装
		pip3 install django==1.11.11		
		pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ django==1.11.11	
		PyCharm安装的时候:
			注意不要勾选那个选项 (你们懂得)

	 Django项目的启动:	
		命令行启动
			在项目的根目录下(也就是有manage.py的那个目录),运行:
			python3 manage.py runserver IP:端口--> 在指定的IP和端口启动
			python3 manage.py runserver 端口   --> 在指定的端口启动
			python3 manage.py runserver        --> 默认在本机的8000端口启动
		
		PyCharm启动
			点绿色的小三角,直接可以启动Django项目(前提是小三角左边是你的Django项目名)
	
	配置相关   项目名/settings.py文件
		Templates(存放HTML文件的配置)       <-- 告诉Django去哪儿找我的HTML文件
		
		静态文件(css/js/图片)
			# 静态文件保存目录的别名
			STATIC_URL = '/static/'

			# 所有静态文件(css/js/图片)都放在我下面你配置的文件夹中
			STATICFILES_DIRS = [
				os.path.join(BASE_DIR, "static"),
			]
	APP
		app目的：
			分支项目下的应用，方便我们在一个大的Django项目中,管理实现不同的业务功能.
			project  --> 项目  
			APP      --> 应用  
				
		创建APP的命令
			命令行,在Django项目的根目录输入:
				python3 manage.py startapp app名字	
	
	ORM: 
		优点:
			简单,不用自己写SQL语句
			开发效率高
		缺点:
			记忆你这个特殊的语法
			相对于大神些的SQL语句,肯定执行效率有差距
		
		ORM的对应关系:
			类          --->      数据表
			对象        --->      数据行
			属性        --->      字段

		ORM能做的事儿:
			操作数据表    --> 创建表/删除表/修改表
				操作models.py里面的类
			
			操作数据行    --> 数据的增删改查
				
		ORM做不到的事：	
			不能创建数据库,自己动手创建数据库
	
	使用Django的ORM详细步骤:
		自己动手创建数据库
			create database 数据库名;
		在Django项目中设置连接数据库的相关配置(告诉Django连接哪一个数据库)
			# 数据库相关的配置
			DATABASES = {
				'default': {
					'ENGINE': 'django.db.backends.mysql',  # 连接的数据库类型
					'HOST': '127.0.0.1',  # 连接数据库的地址
					'PORT': 3306,  # 端口
					'NAME': "day61",  # 数据库名称
					'USER': 'root',  # 用户
					'PASSWORD': '123456'  # 密码
				}
			}
		告诉Django用pymysql代替默认的MySQLDB 连接MySQL数据库
			在项目/__init__.py文件中,写下面两句:
				import pymysql
				# 告诉Django用pymysql来代替默认的MySQLdb
				pymysql.install_as_MySQLdb()
		在app下面的models.py文件中定义一个类,这个类必须继承models.Model
			class 类名(models.Model):
				...
		执行两个命令
			python3 manage.py makemigrations	# 创建执行命令
			python3 manage.py migrate			# 上传执行命令


















		