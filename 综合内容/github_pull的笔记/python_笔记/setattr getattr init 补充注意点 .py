
class Foo(object):
	def __init__(self):
		self.storage = {}
		
		
	def __getattr__(self,item):   # 查询的时候默认调用 
		print(item)
	
	def __setattr__(self,key,value):  # 设置值的时候默认调用 
		print(key,value)
		
obj = Foo()
obj.xx =  123

"""
obj.xx 默认执行 __setattr__ 方法 
	__init__ 里面也有 .xx 的操作 导致会执行 __setattr__
	但是 python 从上向下执行，
	init 在 setattr 之前，如果自定义了这个 setattr 会导致报错 
	
	
	不自定义 setattr 的时候，会默认执行 object 中的 setattr 从而不会报错
"""

# 解决方式
class Foo(object):
	def __init__(self):
		# self.storage = {}
		object.__setattr__(self,"storage",{})
		
	def __getattr__(self,item):   # 查询的时候默认调用 
		print(item)
	
	def __setattr__(self,key,value):  # 设置值的时候默认调用 
		print(key,value)
		
		
		
		
		
		
		
		
		
		
		
		
		