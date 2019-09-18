# flask-sqlalchemy 的使用 

"""
	目录结构：
		chun	项目名
			
			chun	与项目名同名的文件夹 
				
				static	静态文件相关
				
				templates	模板文件相关
				
				view	视图函数
				
					acctount.py		具体视图函数
					
					user.py		具体视图函数
					
				__init__.py		初始化文件
				
				models.py	数据库相关
			
			create_table.py		数据库创建离线脚本
			
			settings.py		配置文件 
			
"""


"""chun.chun.__init__.py """
from flask import Flask
from flask_session import Session


from flask_sqlalchemy import SQLAlchemy # 
db = SQLAlchemy() # 

from .views.account import ac
from .views.user import us


from .models import *

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.ProConfig')
    app.register_blueprint(ac)
    app.register_blueprint(us)

    db.init_app(app) # 

    return app

"""chun.settings.py"""
from redis import Redis

class BaseConfig(object):

	# 
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/s9day122?charset=utf8"
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_MAX_OVERFLOW = 5
    SQLALCHEMY_TRACK_MODIFICATIONS = False
	# 
    pass

"""chun.chun.models.py"""
# 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer,String,Text,Date,DateTime
from sqlalchemy import create_engine
from chun import db
#
class Users(db.Model): #  
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
   

"""chun.create_table.py"""
from chun import db,create_app

app = create_app()			
app_ctx = app.app_context() 
with app_ctx: 
    db.create_all() 

class ProConfig(BaseConfig):
    pass


"""chun.chun.views.user.py"""
from flask import Blueprint
from chun import db
from chun import models
us = Blueprint('us',__name__)


@us.route('/index')
def index():
    # 使用SQLAlchemy在数据库中插入一条数据
    # db.session.add(models.Users(name='高件套',depart_id=1))
    # db.session.commit()
    # db.session.remove()
    result = db.session.query(models.Users).all()
    print(result)
    db.session.remove()

    return 'Index'



"""
步骤详解
"""

	"""
	下载安装
	"""
		pip3 install flask-sqlalchemy
	"""
	导入并实例化SQLAlchemy
	"""
		# chun.__init__.py 
		from flask_sqlalchemy import SQLAlchemy
		db = SQLAlchemy()
		
			注意事项：必须在导入蓝图之前 
	"""
	导入models.py  
	"""	
		from .models import *
	
	"""
	初始化
	"""
		db.init_app(app)
	"""	
	在配置文件中写入配置
	"""
		# ##### SQLALchemy配置文件 #####
		SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/s9day122?charset=utf8"
		SQLALCHEMY_POOL_SIZE = 10
		SQLALCHEMY_MAX_OVERFLOW = 5
	"""
	创建models.py中的类（对应数据库表）
	"""
		chun/models.py 
			from sqlalchemy.ext.declarative import declarative_base
			from sqlalchemy import Column
			from sqlalchemy import Integer,String,Text,Date,DateTime
			from sqlalchemy import create_engine
			from chun import db


			class Users(db.Model):
				__tablename__ = 'users'
				id = Column(Integer, primary_key=True)
				name = Column(String(32), index=True, nullable=False)
				depart_id = Column(Integer)
	"""
	生成表（使用app上下文）
	"""
		from chun import db,create_app

		app = create_app()
		app_ctx = app.app_context() 	# app_ctx = app/g
		with app_ctx: 					# __enter__,通过LocalStack放入Local中
			db.create_all() 			# 调用LocalStack放入Local中获取app，再去app中获取配置

	"""		
	基于ORM对数据库进行操作。
	"""
		from flask import Blueprint
		from chun import db			# 这个里面啥都有	
		from chun import models
		us = Blueprint('us',__name__)


		@us.route('/index')
		def index():
			# 使用SQLAlchemy在数据库中插入一条数据
			# db.session.add(models.Users(name='高件套',depart_id=1))
			# db.session.commit()
			# db.session.remove()
			result = db.session.query(models.Users).all()
			print(result)
			db.session.remove()

			return 'Index'









