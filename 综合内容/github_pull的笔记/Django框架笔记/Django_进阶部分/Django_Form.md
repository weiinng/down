Form
	概念 
		内置的Django form组件操作更加简单
		form组件的主要功能:
			生成页面可用的HTML标签
			对用户提交的数据进行校验
			保留上次输入内容
	普通的方式创建 form 表单
		views.py
			def register(request):
				error_msg = ""
				if request.method == "POST":
					username = request.POST.get("name")
					pwd = request.POST.get("pwd")
					# 对注册信息做校验
					if len(username) < 6:
						# 用户长度小于6位
						error_msg = "用户名长度不能小于6位"
					else:
						# 将用户名和密码存到数据库
						return HttpResponse("注册成功")
				return render(request, "register.html", {"error_msg": error_msg})
		login.html
			<!DOCTYPE html>
			<html lang="en">
			<head>
				<meta charset="UTF-8">
				<title>注册页面</title>
			</head>
			<body>
			<form action="/reg/" method="post">
				{% csrf_token %}
				<p>
					用户名:
					<input type="text" name="name">
				</p>
				<p>
					密码：
					<input type="password" name="pwd">
				</p>
				<p>
					<input type="submit" value="注册">
					<p style="color: red">{{ error_msg }}</p>
				</p>
			</form>
			</body>
			</html>
		
	使用form组件实现注册功能
		form.py	
			(通常会将 form 表单的操作在 一个单独的文件里面写 这样和model.py同级便于区分)
			先定义好一个RegForm类：
				from django import forms
				# 按照Django form组件的要求自己写一个类
				class RegForm(forms.Form):
					name = forms.CharField(label="用户名")
					pwd = forms.CharField(label="密码")
		
		views.py
				# 使用form组件实现注册方式
				def register2(request):
					form_obj = RegForm()
					if request.method == "POST":
						# 实例化form对象的时候，把post提交过来的数据直接传进去
						form_obj = RegForm(request.POST)
						# 调用form_obj校验数据的方法
						if form_obj.is_valid():
							return HttpResponse("注册成功")
					return render(request, "register2.html", {"form_obj": form_obj})

		login2.html
			<!DOCTYPE html>
			<html lang="en">
			<head>
				<meta charset="UTF-8">
				<title>注册2</title>
			</head>
			<body>
				<form action="/reg2/" method="post" novalidate autocomplete="off">
					{% csrf_token %}
					<div>
						<label for="{{ form_obj.name.id_for_label }}">{{ form_obj.name.label }}</label>
						{{ form_obj.name }} {{ form_obj.name.errors.0 }}
					</div>
					<div>
						<label for="{{ form_obj.pwd.id_for_label }}">{{ form_obj.pwd.label }}</label>
						{{ form_obj.pwd }} {{ form_obj.pwd.errors.0 }}
					</div>
					<div>
						<input type="submit" class="btn btn-success" value="注册">
					</div>
				</form>
			</body>
			</html>		
		
	常用字段与插件
		initial
			初始值，input框里面的初始值。
			class LoginForm(forms.Form):
				username = forms.CharField(
					min_length=8,
					label="用户名",
					initial="张三"  # 设置默认值
				)
				pwd = forms.CharField(min_length=6, label="密码")

		error_messages
			重写错误信息。
			class LoginForm(forms.Form):
				username = forms.CharField(
					min_length=8,
					label="用户名",
					initial="张三",
					error_messages={
						"required": "不能为空",
						"invalid": "格式错误",
						"min_length": "用户名最短8位"
					}
				)
		
		password
			密码类型input标签
			class LoginForm(forms.Form):
				pwd = forms.CharField(
					min_length=6,
					label="密码",
					widget=forms.widgets.PasswordInput(attrs={'class': 'c1'}, render_value=True)
				)
							
		radioSelect
			单选Select 值为字符串
			class LoginForm(forms.Form):
				gender = forms.fields.ChoiceField(
					choices=((1, "男"), (2, "女"), (3, "保密")),
					label="性别",
					initial=3,
					widget=forms.widgets.RadioSelect()
				)					
			
			多选Select
			class LoginForm(forms.Form):
				hobby = forms.fields.MultipleChoiceField(
					choices=((1, "篮球"), (2, "足球"), (3, "双色球"), ),
					label="爱好",
					initial=[1, 3],
					widget=forms.widgets.SelectMultiple()
			)	
			
			单选checkbox
			class LoginForm(forms.Form):
				keep = forms.fields.ChoiceField(
					label="是否记住密码",
					initial="checked",
					widget=forms.widgets.CheckboxInput()
				)	
			
			多选checkbox
			class LoginForm(forms.Form):
				...
				hobby = forms.fields.MultipleChoiceField(
					choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
					label="爱好",
					initial=[1, 3],
					widget=forms.widgets.CheckboxSelectMultiple()
				)	
				
				choice字段注意事项	
					choices的选项可以配置从数据库中获取，但是由于是静态字段 获取的值无法实时更新，需要重写构造方法从而实现choice实时更新。
					方式一:
					from django.forms import Form
					from django.forms import widgets
					from django.forms import fields

					 
					class MyForm(Form):
					 
						user = fields.ChoiceField(
							# choices=((1, '上海'), (2, '北京'),),
							initial=2,
							widget=widgets.Select
						)
					 
						def __init__(self, *args, **kwargs):
							super(MyForm,self).__init__(*args, **kwargs)
							# self.fields['user'].choices = ((1, '上海'), (2, '北京'),)
							# 或
							self.fields['user'].choices = models.Classes.objects.all().values_list('id','caption')
					
					方式二:
					from django import forms
					from django.forms import fields
					from django.forms import models as form_model

					 
					class FInfo(forms.Form):
						authors = form_model.ModelMultipleChoiceField(queryset=models.NNewType.objects.all())  # 多选
						# authors = form_model.ModelChoiceField(queryset=models.NNewType.objects.all())  # 单选
				


	重写钩子函数 对全局或者局部 的验证或修改
		
				
				
				
				