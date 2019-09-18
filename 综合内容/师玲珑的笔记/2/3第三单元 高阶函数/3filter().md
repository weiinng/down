filter()函数
filter(function,iterable)
功能：
该接受两个函数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回True或False,最后将返回True的元素放到新的迭代器对象中
参数
function--判断函数
iterable--可迭代对象（如 序列）
返回值：
返回一个迭代器对象

实例：
def add(n):
	return n%2==1
f=filter(add,[1,2,3,4])
for x in f:
	print(x)
结果为：
1
3

dict2=[{'name':'小明','age':10},{'name':'小红','age':20},{'name':'校长','age':15}]
print(sorted(dict2,key=lambda x:x['age']))
