
16 进制转换  hex() 
10 进制转换  int()  
8 进制转换   oct() 
16 进制转换  bin()


v1 = 1 or 3  -- 1
v2 = 1 and 3  -- 3
v3 = 0 and 2 and 1  -- 0
v4 = 0 and 2 or 1  -- 1
v5 = 0 and 2 or 1 or 4  -- 1
v6 = 0 or Flase and 1  -- False
and：前后为真才为真
or：有一为真就为真
优先级：()>not>and>or 
同等优先级下，从左向右


一行代码实现9*9乘法表
print("\n".join(["  ".join(["%s*%s=%s" %(j,i,j*i) for j in range(1,i+1)]) for i in range(1,10)]))
拆解版
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i*j}", end="  ")
    print("")



filter、map、reduce的作用？
	# map:遍历序列，为每一个序列进行操作，获取一个新的序列
		a = ["123", "sb_sdsd", "sb_456"]
		b = map(lambda i: i+("sb"), a)
		print(list(b)) # ['123sb', 'sb_sdsdsb', 'sb_456sb']
	# reduce：对于序列里面的所有元素进行累计操作，可带初始值
		a = [1, 2, 3]
		from functools import reduce
		b = reduce(lambda i, j: i * j, a, 5)
		print(b) # 30
	# filter：对序列里面的元素进行判断筛选，最终获取符合条件的序列。
		a = ["123", "sb_sdsd", "sb_456"]
		b = filter(lambda i: i.startswith("sb"), a)
		print(list(b)) # ["sb_sdsd", "sb_456"]


PEP8 规范
#1、空格使用
a 各种右括号前不要加空格。
b 逗号、冒号、分号前不要加空格。
c 函数的左括号前不要加空格。如Func(1)。
d 序列的左括号前不要加空格。如list[2]。
e 操作符左右各加一个空格，不要为了对齐增加空格。
f 函数默认参数使用的赋值符左右省略空格。
g 不要将多句语句写在同一行，尽管使用‘；’允许。
8 if/for/while语句中，即使执行语句只有一句，也必须另起一行。
#2、代码编排
   a 缩进，4个空格，而不是tab键
   b 每行长度79，换行可使用反斜杠，最好使用圆括号。
   c 类与类之间空两行
   d 方法之间空一行



#Ascii： 1个字节 支持英文
#unicode ：所有字符（无论中文、英文等）1个字符：4个字节
#gbk ： 1个字符，英文1个字节，中文2个字节。
#utf-8 ：英文1个字节，欧洲字符：2个字节， 亚洲： 3个字节。




列举 Python2和Python3的区别
'Print'：
    py2--print; 
    py3--print()函数
'编码'：
    py2默认是ascii码；
    py3默认是utf-8
'字符串'：
    py2中分ascii(8位)、unicode(16位)；
    py3中所有字符串都是unicode字符串
'True和False'：
    py2中是两个全局变量(1和0)可以重新赋值；
    py3中为两个关键字，不可重新赋值
'迭代'：
    py2:xrange；
    py3:range
'Nonlocal'：
    py3专有的（声明为非局部变量）
'经典类&新式类'：
    py2：经典类和新式类并存；
    py3：新式类都默认继承object
'yield'：
    py2：yield
    py3：yield/yield from
'文件操作'：
    py2：readliens（）读取文件的所有行，返回一个列表，包含所有行的结束符
         xreadliens（）返回一个生成器，循环取值　　
    py3: 只有readlines()


用一行代码实现数值交换
	a, b = b, a


实现斐波那契数列
# 0,1,1,2,3,5,8,13,21,34,55
def func(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        for i in range(n):
            return func(n - 1) + func(n - 2)
print(func(10)) # 55

def fab(n):
    pre = 1
    cur = 1
    print(pre,cur,end=" ")
    for i in range(n-2):
        pre, cur = cur, cur+pre
        print(cur,end=" ")

fab(10)


深浅拷贝
	浅拷贝只是增加了一个指针指向一个存在的地址，
	数据半共享（复制其数据独立内存存放，但是只拷贝成功第一层）


	深拷贝是增加一个指针并且开辟了新的内存，这个增加的指针指向这个新的内存
	数据完全不共享（复制其数据完完全全放独立的一个内存，完全拷贝，数据不共享）


	采用浅拷贝的情况，释放内存，会释放同一内存，深拷贝就不会出现释放同一内存的错误
	字典套字典、列表套字典、字典套列表，列表套列表，以及各种复杂数据结构的嵌套中，会出现拷贝后的数据发生变化导致源数据发生变化
	import copy
	 
	# 浅拷贝
	l1 = [1,2,3,[11,22,33]]
	l2 = l1.copy()
	print(l2) #[1,2,3,[11,22,33]]
	l2[3][2]='aaa'
	print(l1) #[1, 2, 3, [11, 22, 'aaa']]
	print(l2) #[1, 2, 3, [11, 22, 'aaa']]
	l1[0]= 0
	print(l1) #[0, 2, 3, [11, 22, 'aaa']]
	print(l2) #[1, 2, 3, [11, 22, 'aaa']]
	print(id(l1)==id(l2)) #False

	# 深拷贝 
	import copy
	l1 = [1, 2, 3, [11, 22, 33]]
	l2 = copy.deepcopy(l1)
	print(l1,'>>>',l2)
	# [1, 2, 3, [11, 22, 33]] >>> [1, 2, 3, [11, 22, 33]]
	l2[3][0] = 1111
	print(l1,">>>",l2)
	# [1, 2, 3, [11, 22, 33]] >>> [1, 2, 3, [1111, 22, 33]]



def num():
   return [lambda x: i * x for i in range(4)] #返回一个列表，里面是四个函数对象 i=3
print([m(2) for m in num()]) 
# [6,6,6,6] 
闭包，延迟绑定， 
lambda x，i=i : i * x # 这时候就会输出 [0,2,4,6]
i 被 引用后被改变了值。最终 i = 3 因此才会输出 4个6 
如果声明一个局部变量 i 即可解决这问题。原因还是在于先执行玩的是循环，
循环的时候是声明，并没有执行，循环完毕最后才运行函数。只是引用的 i 是全局被改变的 i = 3 


[ i % 2 for i in range(10) ] 列表生成式
( i % 2 for i in range(10) ) 生成器表达式


请用代码简单实现stack 。
class Stack(object):
   # 初始化栈
   def __init__(self):
      self.items = []
   # 判断栈是否为空
   def is_empty(self):
      return self.items == []
   # 返回栈顶
   def peek(self):
      return self.items[len(self.items) - 1]
   # 返回栈大小
   def size(self):
      return len(self.items)
   # 压栈
   def push(self, item):
      self.items.append(item)
   # 出栈
   def pop(self):
      return self.items.pop()



闭包的理解
	首先要有函数嵌套，内部函数要调用外部函数的变量


面向对象深度优先和广度优先是什么？
	py3 默认新式类，都是广度优先，即横向查找
	py2 中如果没继承 object 就是经典类，为深度优先，即纵向查找




静态方法和类方法区别？
	Classmethod必须有一个指向类对象的引用作为第一个参数；
@classmethod
def class_func(cls):
		""" 定义类方法，至少有一个cls参数 """
	   print('类方法')
	---------------------------------------------------------
	Staticmethod可以没有任何参数。
	@staticmethod
	def static_func():
		""" 定义静态方法 ，无默认参数"""
	   print('静态方法')




1、2、3、4、5 能组成多少个互不相同且无重复的三位数
方式1：
a = [1,2,3,4,5]
b = 0
for i in a:
    for j in a:
        for x in a:
            if i!=j and i!=x and j!=x:
                b+=1
print(b) # 60
方式2 ：
import itertools
print(len(list(itertools.permutations('12345',3))))



__new__ 做了些什么
__new__ 执行在 __init__ 之前，决定了实例化对象到底是什么
"""
class Bar(object):
    pass

class Foo(object):
    def __new__(cls, *args, **kwargs):
        # return super(Foo,cls).__new__(cls,*args, **kwargs)
        return Bar()
obj = Foo()
print(obj) # <__main__.Bar object at 0x000001A0353A12B0>
"""


__call__ 做了些什么
类中定义了 __call__ 方法，此类的实例化对象就可以加括号执行
执行的时候就执行 __call__ 的内容 
"""
class Bar(object):
    def __call__(self, *args, **kwargs):
        return "123154646"
obj = Bar()
print(obj()) # 123154646
"""


单例模式的实现方式 
# 单例模式
'''单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例类的特殊类。
通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。
如果希望在系统中某个类的对象只能存在一个，单例模式是最好的解决方案。'''
# 1、使用__new__方法
class MyClass(object):
    _instance = False
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(MyClass)
        return cls._instance
# 2、共享属性
# 创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法.
    class Borg(object):
        _state = {}
        def __new__(cls, *args, **kw):
            ob = super(Borg, cls).__new__(cls, *args, **kw)
            ob.__dict__ = cls._state
            return ob
    class MyClass2(Borg):
        a = 1
# 3、装饰器版本
def singleton(cls, *args, **kw):
	instances = {}
	def getinstance():
		if cls not in instances:
			instances[cls] = cls(*args, **kw)
		return instances[cls]
	return getinstance
@singleton
class MyClass:
    ...
# 4、import方法
# 作为python的模块是天然的单例模式
    # mysingleton.py
    class My_Singleton(object):
        def foo(self):
            pass
    my_singleton = My_Singleton()
    # to use
    from mysingleton import my_singleton
    my_singleton.foo()



类装饰器
class Decrator(object):
    def __init__(self, fn):
        print("初始化函数", fn.__name__)
        self._func = fn
    def __call__(self, *args):
        print("打印的内容", *args)
        return self._func(*args)
@Decrator
def ab(x, y):
    print(ab)
    return x + y
print(ab(3, 3))
# 初始化函数 ab
# 打印的内容 3 3
# <__main__.Decrator object at 0x0000013281B7DBE0>
# 6



json序列化时，默认遇到中文会转换成unicode，如果想要保留中文怎么办？
import json
a=json.dumps({"xxx":"你好"},ensure_ascii=False)
print(a) #{"xxx": "你好"}




常用装饰器
@property 	将方法变成变量形式自动调用
@staticmethod  静态方法，类可以不用实例化就可以调用该方法 C.f()，当然也可以实例化后调用 C().f()。
@classmethod	类不需实例化就可以调用内部方法，直接类名.方法即可调用



如何变成迭代器？
	"""
	li = [11,22,33]
		
	iter(li)	
	"""


生成器怎么变成迭代器 ？
	"""
	def func():
		yield 11
		yield 22
		yield 33
	
	li = func()
	
	iter(li)	
	"""


实现二分查找
递归方式
def binary_chop(alist, data):
    n = len(alist)
    if n < 1:
        return False
    mid = n // 2
    if alist[mid] > data:
        return binary_chop(alist[0:mid], data)
    elif alist[mid] < data:
        return binary_chop(alist[mid + 1:], data)
    else:
        return True


lis = [2, 4, 5, 12, 14, 23]
print(binary_chop(lis, 2))
非递归方式
def binary_chop(alist, data):
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (last + first) // 2
        if alist[mid] > data:
            last = mid - 1
        elif alist[mid] < data:
            first = mid + 1
        else:
            return mid
    return False


lis = [2, 4, 5, 12, 14, 23]
print(binary_chop(lis, 23))









