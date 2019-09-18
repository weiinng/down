# 蓝图 目录结构 

"""
crm 
	crm
		view
			account.py
			user.py
		static
		templates
			login.html
		__init__.py
	manage.py
"""



# __init__.py

from flask import Flask
from .views.account import ac
from .views.user import us
def create_app():
	app = Flack(__name__)
	
	 
	@app.before_request   # 对全局的视图有效 
	def xx():
		print("app.before_request")
	
	app.register_blueprint(ac)
	app.register_blueprint(us)
	
	return app 


	
# manage.py
from crm import create_app 
if __name__ == "__main__":
	app.run()
	
	
# account.py
from flask import Blueprint,render_template
ac = Blueprint("ac" ,__name__，template_folder="xxxx",static_url_path="xxxx")
# template_folder 优先在 templates 文件夹找。找不到再去 xxxx 里找
# static_url_path 优先在 static 文件夹找。找不到再去 xxxx 里找
# url_prefix="/xx" 为当前蓝图的url里加前缀 
@ac.route("/login")
def login():
	return render_template("login.html")


# user.py	
from flask import Blueprint	
us = Blueprint("ac" ,__name__)

@us.before_request   # 仅对当前的视图有效
def xx():
	print("us.before_request")

@us.route("/user")
def user():
	return "user"
	
	
	
	
	
	
	