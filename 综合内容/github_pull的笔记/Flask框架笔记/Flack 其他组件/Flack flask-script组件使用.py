
flask-script 


"""
安装
"""
pip3 install flask-script 

"""
功能：
"""	
	"""
	增加 runserver
	"""
		from chun import create_app
		from flask_script import Manager


		app = create_app()
		manager = Manager(app)	# 用 Manager 封装一下 

		if __name__ == '__main__':
			# app.run()
			manager.run()
			
			
		# python manage.py runserver 
		# python manage.py runserver -h 127.0.0.1 -p 8001
	
	"""
	执行额外的函数 
		
		位置传参 
	"""
		from chun import create_app
		from flask_script import Manager


		app = create_app()
		manager = Manager(app)

		@manager.command
		def custom(arg):
			"""
			自定义命令
			执行： python manage.py custom 123
			:param arg:
			:return:
			"""
			print(arg)


		if __name__ == '__main__':
			# app.run()
			manager.run()
	
	
		# python manage.py custom 123
	"""
	执行额外的函数 
		
		关键字传参
	"""
		from chun import create_app
		from flask_script import Manager


		app = create_app()
		manager = Manager(app)

		@manager.option('-n', '--name', dest='name')
		@manager.option('-s', '--email', dest='email')
		def cmd(name, email):
			"""
			自定义命令
			执行： python manage.py  cmd -n yangftuo -e xxxx@qq.com
			:param name:
			:param url:
			:return:
			"""
			print(name, email)


		if __name__ == '__main__':
			# app.run()
			manager.run()
			
		# python manage.py cmd -n yangtuo -s xxxx@qq.com
