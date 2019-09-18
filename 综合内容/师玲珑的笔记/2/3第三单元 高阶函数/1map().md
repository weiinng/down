map()函数用法：
map(function,iterable,...)
功能：将第一个参数function依次作用在参数可迭代对象中的每一个元素上，返回包含每次function函数返回值的新迭代器
参数：
function--函数，有几个参数，下面传几个可迭代对象
iterable--一个或多个可迭代对象（如，序列）
返回值：
python 3.x

实例：
def add(n,q,e):
	return n+q+e
f=map(add,[1,2],{1,2},(1,2))
for x in f:
	print(x)
结果是：
3
6


输出时也可以print(list(f))
结果是：
[3,6]
是将结果以一个列表的形式输出


def add(n):
	return n*n
f=map(add,[1,2,3])
for x in f:
	print(x)
结果是：
1
4
9









