谈谈你对面向对象的认识
"""
	先随便扯些和别的语言的对比
		python 本身是支持函数式编程 和 面向对象式编程
		c，java是只能基于面向对象
	
	在简单说下面向对象的主要特点和好处
		- 基础：面向对象本身拥有基础的三大特性
			 

				封装
					将方法封装到类中
						体现在 功能类上的整合
					将数据封装到对象中 
						体现在类的对象初始化赋值等
				
				继承
					python 是支持多继承的 是python的一个特色，java c# 是不支持的
						基于 mro 的顺序来决定继承顺序
					多个类的对共同方法的，为避免重复编写，封装到父（基）类中
					应用 ： rest framework 中的视图类的继承非常多
					
				多态
					python 作为强类型的动态脚本语言，不支持多态，但是也不需要支持多态
					在c# java里面必须要指定类型，当然也可以通过接口类实现目的
					鸭子类型：
						python 中的参数可以传入任何类型的对象，不会对类型进行强制限制
					说法：
						如果我有个类，这个类的传入参数是不会有类型限制的 这体现了多态
						我有多个类，这些都有个 send 方法 每个类的分别的实例化对象在调用 send 的时候
						都是obj.send() 的一样的调用方式，但是却是执行的他内部的自己的 send 方法，这体现了多态性

		- 进阶：魔法方法 
			
			__init__  		初始化
			__new__			创建对象
			__call__		对象() 	
			__str__			print(对象)	
			__repr__			
			__iter__		含有此方法且返回迭代器 代表此对象可迭代	
			
			__getattr__		对象.xx
			__setattr__		
			__delattr__		对象.del
			
			__setiter__		对象["xx"]
			__getiter__
			__deliter__
			
			__mro__			查看成员顺序 
			__dict__		查看成员顺序 
			
			__add__			对象相加的时候触发
			__...__			对象相减的时候触发
			__...__			对象相乘的时候触发
			__...__			对象相除的时候触发
			
			__enter__		with 对象的开始前触发
			__exit__		with 对象的结束时触发
				应用： 在 SQLAlchemy 中有使用
			
		- 高阶：metaclass 
			
			类的创建两种方法：
				class Foo():pass
				type("Foo",(object,),{ })
			
			指定创建类的 mtype 
				class Foo(metaclass=MyType):	# python 3 
					# __metaclass__ = MyType # python 2 
					pass 
				
				MyType('Foo',(object,),{})
				# 如果一类自己或基类中指定了metaclass
				# 那么该类就是由metaclass指定的type或mytype创建。
			
			对于源码的阅读需要注意 是否指定了 metaclass 
				未指定直接看 __new__ 然后 __init__ 即可
				如果指定了需要注意：
					创建类
						MyType.__init__ 
					创建对象 
						MyType.__call__ 
						MyType.__new__ 
						MyType.__init__ 
							
			 
"""

类创建的有几种方式？
"""
# 两种方式
class Foo(object):
	a1 = 123
	def func(self):
	return 666

Foo = type("Foo",(object,),{'a1':123,'func':lambda self:666})


foo = Foo()

"""

metaclass 类 是什么 ？ 类的创建的本质是怎么样子的流程 ？
"""
# metaclass 实例 	
class MyType(type):
    def __init__(self,*args,**kwargs):
        super(MyType,self).__init__(*args,**kwargs)

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls)

        cls.__init__(obj,*args, **kwargs)

        return obj

class Foo(object,metaclass=MyType):  # metaclass 指定由谁来创建这个类 
    a1 = 123
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def func(self):
        return 666
	
foo = Foo()
	
	# 创建类的时候会先执行 type 的 __init__  方法 ，由type 的 __init__ 来创建类
	# 当一个类在实例化时候，先执行 type 的 __call__ 方法 ， __call__ 方法 的返回值就是实例化对象 
		# __call__ 内部调用：
			# 类.__new__ 方法 ：创建对象
			# 类.__init__ 方法 ：对象初始化
		
"""


一个类怎么样才可以被 for 循环？
	"""
	变成 可迭代对象 
	要有 __iter__ 方法 且 要返回可迭代对象
	
	class Foo(object):
		
		# def __iter__(self):
		# 	return iter([11,22,33])
		
		def __iter__(self):
		 	yield 1		
		 	yield 2		
		 	yield 3		
		
	obj = F00()
	for item in obj
		print(item)
	"""
	

__new__ 方法的返回值决定对象到底是什么？
	"""
	Bar(object):
		pass

	class Foo(object):

		def __new__(cls, *args, **kwargs):
			# return super(Foo,cls).__new__(cls,*args, **kwargs)
			return Bar()
	obj = Foo()
	print(obj)
	"""

python 中怎么实现面向对象的约束 ？和其他语言有什么区别?
	"""
	jave/c# 中有接口 ，抽象方法，抽象方法来约束 
		接口 ：	（只做约束）
			Interface Xxx：
				def func1(self):
					pass	# 必须是空的
			Interface Aaa(Xxx)：
				def func1(self):	# 基类中的方法，子类必须要有
					print("func1")	
		抽象方法，抽象类：	（约束+继承）
			class abstract IMessage: # 加 abstract 表示抽象类
				def abstract func1(self):	
					pass 
				def abstract func2(self)： # 加 abstract 表示抽象方法
					pass 
				def func3(self):	# 非抽象方法就没有约束
					print('asdfasdf') 
			class Msg(IMessage):
				def func1(self):	# 必须要有同名方法
					print('func1') 
				def func2(self):
					print('func1') 
	
	python 没有接口，但是有抽象方法抽象类
		方法一： ABC 
		方法二：
			# 类继承 + 异常 
			class BaseMessage(object):
				def send(self):
					raise NotImplementedError('必须实现send方法')
			class Msg(BaseMessage):
				def send(self):
					print('发送短信')
			class Wechat(BaseMessage):
				def send(self):
					print('发送微信')
		应用场景：
			在rest_framework 中的 认证的时候必须要求继承 BaseAuthentiction 的时候
			BaseAuthentiction 的 authenticate 就要求子类必须实现 authenticate 方法 
	"""





















	