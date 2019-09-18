在form 表单对象里面对钩子函数的重写 


# 重写全局的钩子函数，对确认密码做校验
from django.core.exceptions import ValidationError


def clean(self):
	password = self.cleaned_data.get("password")
	re_password = self.cleaned_data.get("re_password")
	if re_password and re_password != password:
		self.add_error("re_password", ValidationError("两次密码不一致"))
	return self.cleaned_data
	


	
# 重写局部钩子函数 对名字字段的敏感字符进行判断
from django.core.exceptions import ValidationError


def clean_name(self):
	value = self.cleaned_data.get("name")
	if "金瓶梅" in value:
		raise ValidationError("不符合社会主义核心价值观!")
	return value




关于 form is_vaild() 的执行顺序
	form is_vaild()
		判断是否有数据 以及 是否有错误
			是否有数据直接可以判断
			进行错误信息的判断
				默认的错误信息为 none 定义在 init 中
				执行 full_clean()方法
	full_clean()
		创建一个 保存错误信息的 空字典 	 
			self._error = ErroDict()
		创建一个 保存校验通过数据的 字典 
			self.cleaned_data = {}
		然后执行下面的三个方法
			_clean_fields()
			
			
				for 循环每个字段(self.fields.items())分别校验(利用的是内置的校验规则)
					如果有错误		在 self._error[] 中 在 add_error 中可以捕获到 ValidationError 异常进行处理
					如果没有报错 	在cleaned_date[] 中 加入已经通过校验的字段 
				
				for 循环结束后  进行一次反射 查询是否有 clean_%s %name 的方法 进行调用后执行
					如果有错误		在 self._error[] 中 在 add_error 中可以捕获到 ValidationError 异常进行处理
					如果没有报错 	在cleaned_date[] 中 加入已经通过校验的字段 
					
					即 这个 clean_%s 的方法为一个钩子函数 此钩子可以帮我们解决什么问题呢?
						这是个局部变量的钩子 可以对局部变量内部进行一定程度的操作 比如对变量的值进行操作

				for 循环走完了之后往下面执行 _clean_form() 方法
			
			_clean_form()
					调用对象的 .clean()方法,默认的继承的 .clean() 是什么都不做的
						因此可以利用这个clean方法进行 重写 自定义想要的校验操作
							即 .clean() 为一个全局的钩子  可以对所有的变量进行操作 比如两个变量的对比等
			post_clean()
		
	
	通过上面的流程可以发现.不论是使用全局钩子还是局部钩子都是对已经校验通过的数据进行操作
	即是说 在调用 def clean_name(self): 或者 def clean(self): 的时候
		self.cleaned_data 里面已经装好了校验通过的数据对象 
			在调用 def clean(self):  		的时候 直接 全部拿来用即可
			在调用 ddef clean_name(self):   的时候 通过get("name") 也可以拿到当前的局部变量对象
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	