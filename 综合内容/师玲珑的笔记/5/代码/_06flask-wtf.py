from flask import Flask,request,render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

app=Flask(__name__)
app.config['SECRET_KEY']='asd'

class Reg(FlaskForm):
    username=StringField('用户名：',validators=[DataRequired()])
    password=PasswordField('密码：',validators=[DataRequired()])
    password2=PasswordField('确认密码：',validators=[DataRequired(),EqualTo('password',message='两次密码不一致')])
    submit=SubmitField('提交')

@app.route('/',methods=['GET','POST'])
def show():
    reg=Reg()
    if request.method=='POST':
        if reg.validate_on_submit():
            flash('登录成功')
        else:
            flash('登录失败')
    return render_template('8.html',reg=reg)

if __name__ == '__main__':
    app.run(debug=True)



















# from flask  import Flask,render_template,request,flash
# # 导入验证层
# from flask_wtf import FlaskForm
# # 导入需要的字段的包
# from wtforms import StringField,PasswordField
# # 导入验证字段的包
# from wtforms.validators import DataRequired,EqualTo
# app = Flask(__name__)
# app.config['SECRET_KEY'] = "asdfdcs"
# # 继承验证类就能使用验证类的很多方法 对传递过来的字段进行验证
# class RegisterForm(FlaskForm):
#     username = StringField('用户名',validators=[DataRequired(message='用户名不能为空')]) # 通过StringField生成字符串，再通过validators参数传递多个验证规则，列表类型
#     password = PasswordField('密码',validators=[DataRequired(message='密码不能为空')])
#     password2 = PasswordField('确认密码',validators=[DataRequired(message='确认密码不能为空'),EqualTo('password',message='两次密码不一样')])
#
#
# @app.route('/',methods=['POST','GET'])
# def reg():
#     register_form = RegisterForm()
#     if request.method=='POST':
#         if register_form.validate_on_submit():
#             flash("注册成功")
#         else:
#             flash("注册失败")
#     return render_template('7.html',register_form = register_form)
#
# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask,render_template,request,flash
# from flask_wtf import FlaskForm
# from wtforms.validators import DataRequired,EqualTo
# from wtforms import StringField,PasswordField,SubmitField
#
# app=Flask(__name__)
# app.config['SECRET_KEY']='asd'
# class Reg(FlaskForm):
#     username = StringField('用户名', validators=[DataRequired(message='用户名不能为空')])
#     username2=StringField('用户名2',validators=[DataRequired(),EqualTo('username')])
#     password = PasswordField('密码', validators=[DataRequired(message='密码不能为空')])
#     password2=PasswordField('确认密码',validators=[DataRequired(message='确认密码不能为空'),EqualTo('password',message='两次密码不一致')])
#     submit=SubmitField('登录')
#     # username = StringField('用户名', validators=[DataRequired(message='用户名不能为空')])  # 通过StringField生成字符串，再通过validators参数传递多个验证规则，列表类型
#     # password = PasswordField('密码', validators=[DataRequired(message='密码不能为空')])
#     # password2 = PasswordField('确认密码',validators=[DataRequired(message='确认密码不能为空'), EqualTo('password', message='两次密码不一样')])
#
#
#
# @app.route('/',methods=['POST','GET'])
# def show():
#     reg=Reg()
#     if request.method=='POST':
#         if reg.validate_on_submit():
#             flash('登录成功')
#         else:
#             flash('登录失败')
#     return render_template('7.html',register_form=reg)
#
# if __name__ == '__main__':
#     app.run(debug=True)










# from flask import Flask,render_template
#
# app=Flask(__name__)
#
# @app.template_filter('lireverse')
# def do_listreverse(li):
#     #通过原列表创建一个新列表
#     temp_li=list(li)
#     temp_li=sorted(temp_li,key=lambda x:len(x),reverse=False)
#     return temp_li
# @app.template_filter('s')
# def a(li):
#     new=list(li)
#     new=sorted(new,key=lambda x:x['age'],reverse=True)
#     return new
#
# name='<b>哈哈</b>'
# dict2=[{'name':'小明','age':10},{'name':'小红','age':20},{'name':'校长','age':15}]
# list2=['asd','q','as','zxas']
# @app.route('/')
# def a():
#     return render_template('4.html',name=name,list=list2,dict=dict2)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)



















# from flask_wtf import FlaskForm
# from wtforms import StringField,PasswordField,SubmitField
# from flask import Flask,render_template,request,flash
# from wtforms.validators import DataRequired,EqualTo
#
# app=Flask(__name__)
# app.secret_key='itheima'
# app.config.from_pyfile('settings.ini')
#
# class Login_form(FlaskForm):
#     username=StringField('用户名:',validators=[DataRequired()])
#     password=PasswordField('密码:',validators=[DataRequired()])
#     password2=PasswordField('确认密码:',validators=[DataRequired(),EqualTo(password,'两次密码不一致')])
#     submit=SubmitField('提交')
#
# @app.route('/',methods=['GET','POST'])
# def login():
#     login_form=Login_form()
#     if request.method=='POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         password2 = request.form.get('password2')
#
#         if login_form.validate_on_submit():
#             print(username,password,password2)
#             return 'success'
#         else:
#             flash('参数有误')
#     return render_template('3.html',form=login_form)
#
# if __name__ == '__main__':
#     app.run(port=80)