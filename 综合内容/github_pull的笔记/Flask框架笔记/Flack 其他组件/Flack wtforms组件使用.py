# https://www.cnblogs.com/wupeiqi/articles/8202357.html 参考博客 


from flask import Flask,request,render_template,session,current_app,g,redirect
from wtforms import Form
from wtforms.fields import simple # 通常用这个
from wtforms.fields import html5
from wtforms.fields import core

from wtforms import widgets	
from wtforms import validators

app = Flask(__name__)



# 简单实例 
class LoginForm(Form):
    name = simple.StringField(
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
            # validators.Length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'placeholder':'请输入用户名'} # 提示信息 
    )
    pwd = simple.PasswordField(
        validators=[
            validators.DataRequired(message='密码不能为空.'),
			"""
			# 其他的一些错误类型 
            validators.Length(min=8, message='用户名长度必须大于%(min)d'),
            validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
                               message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')
			"""
        ],
        render_kw={'placeholder':'请输入密码'}
    )
	
	# 重写钩子函数 
	def validate_name(self, field):
        """
        自定义name字段规则
        :param field:
        :return:
        """
        # 最开始初始化时，self.data中已经有所有的值
        print('钩子函数获取的值',field.data)
        if not field.data.startswith('old'):
            raise validators.ValidationError("用户名必须以old开头") # 继续后续验证
            # raise validators.StopValidation("用户名必须以old开头")


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "GET":
        form = LoginForm()
        # print(form.name,type(form.name)) # form.name是StringField()对象, StringField().__str__
        # print(form.pwd,type(form.pwd))   # form.pwd是PasswordField()对象,PasswordField().__str__
        return render_template('login.html',form=form)

    form = LoginForm(formdata=request.form) 
    if form.validate():
        print(form.data) 
        return redirect('https://www.baidu.com')
    else:
        print(form.errors)
        return render_template('login.html', form=form)
		"""
		login.html
		
		<body>
			<form method="post" novalidate>
				<p>用户名：{{form.name}}  {{form.name.errors[0]}}</p>
				<p>密码：{{form.pwd}}  {{form.pwd.errors[0]}} </p>
				<p><input type="submit" value="提交"  ></p>
			</form>
		</body>
		"""
# --------------------------------------分割线----------------------------

# 常用的 字段类型 注册实例 
class RegisterForm(Form):
    name = simple.StringField(
        label='用户名', # 标签前的文本提示
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),	# 标签类型 
        render_kw={'class': 'form-control'}, # 添加额外字段
        default='alex' # 默认值 
    )

    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    pwd_confirm = simple.PasswordField(
        label='重复密码',
        validators=[
            validators.DataRequired(message='重复密码不能为空.'),
			# 支持检测重复 ，指定对比字段名称 以及错误提示 
            validators.EqualTo('pwd', message="两次密码输入不一致")
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),
        render_kw={'class': 'form-control'}
    )

    gender = core.RadioField(
        label='性别',
        choices=(
            (1, '男'),
            (2, '女'),
        ),
        coerce=int # int("1") 将上传的字符串类型 转换成 int 
    )
    city = core.SelectField(
        label='城市',
        choices=(
            ('bj', '北京'),
            ('sh', '上海'),
        )
    )

    hobby = core.SelectMultipleField(
        label='爱好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        coerce=int
    )

    favor = core.SelectMultipleField(
        label='喜好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        default=[1, ] 
    )


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegisterForm()
        return render_template('register.html', form=form)

    form = RegisterForm(formdata=request.form)
    if form.validate(): # 校验数据 
        print(form.data)
        return redirect('https://www.luffycity.com/home')

    return render_template('register.html', form=form)
	"""
		register.html 支持 循环创建标签 
		
		<body>
			<form method="post" novalidate>

				{% for field in form %}
				<p>{{field.label}}: {{field}}   {{field.errors[0]}}</p>
				{% endfor %}

				<input type="submit" value="提交">
			</form>
		</body>
	"""


# -----------------------------------------分割线------------------------------

import helper
class UserForm(Form):
    city = core.SelectField(
        label='城市',
        choices=(),
        coerce=int
    )
    name = simple.StringField(label='姓名')
	
	# 通过重写 父类的 __init__ 方法重新获取数据，从而避免每次都要重启服务器的尴尬
    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
		# 动态的在数据库中获取 标签内容 
        self.city.choices=helper.fetch_all('select id,name from tb1',[],type=None)


@app.route('/user')
def user():
    if request.method == "GET":
		# 支持在创建的时候传入数据，当作默认值来使用 
        form = UserForm(data={'name':'alex','city':3})
        return render_template('user.html',form=form)
	"""
		user.html
	
		<body>
			<form method="post">
				{% for field in form %}
				<p>{{field.label}}: {{field}}   {{field.errors[0]}}</p>
				{% endfor %}
				<input type="submit" value="提交">
			</form>
		</body>
	"""








if __name__ == '__main__':
    app.run()
	
	
	
	
	
	
	
	