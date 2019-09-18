flask-migrate
		"""
		安装 
			
			依赖：flask-script 需要先导入这个
		"""
		pip3 install flask-script 
		pip3 install flask-migrate 
		
	
		"""
		使用
		"""
		from chun import create_app	
		from chun import db	

		from flask_script import Manager
		from flask_migrate import Migrate, MigrateCommand

		app = create_app()
		manager = Manager(app)
		Migrate(app, db)

		"""
		# 数据库迁移命名
			python manage.py db init    	# 初始化 会增加一个 mirations 的目录 作用同 django中的一样 
			python manage.py db migrate		# 同 makemirations
			python manage.py db upgrade		# 同 migrate
		"""
		manager.add_command('db', MigrateCommand)


		if __name__ == '__main__':
			manager.run()
			# app.run()
