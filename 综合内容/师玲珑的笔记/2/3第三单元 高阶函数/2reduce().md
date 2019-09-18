reduce()函数：
reduce(function,iterable[,initializer])
功能：
函数将一个数据集合（链表、元祖等）中的所有数据进行下列操作：
用传给reduce中的函数function(有两个参数)先对集合中的第1、2个元素进行操作，得到的结果再与第三个数据用function函数运算，最后得到一个结果
其效果类似：ruduce(f,[x1,x2,x3])=f(f(x1,x2),x3)
参数：
function--函数，有两个参数
iterable--可迭代对象
initializer--可选，初始参数

例如：
from functools import reduce
def add(x,y):
	return x+y
q=[1,2,3,4]
f=reduce(add,q[2::])
print(f)
结果为7
列表也可以切片   要记住切片的范围是左闭右开

reduce里传的函数里只能有两个参数
map里可传一个、两个、三个。。。



