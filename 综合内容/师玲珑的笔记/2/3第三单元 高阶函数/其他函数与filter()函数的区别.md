map()函数：
def f(n):
	if n%2==0:
		return n
r=map(f,[1,2,3])
for x in r:
	print(x)
结果是：
None
2
None

def f(n):
	return n%2==0
r=map(f,[1,2,3])
for x in r:
	print(x)
结果是：
False
True
False



filter()函数：
def f(n):
	return n%2==0
r=filter(f,[1,2,3])
for x in r:
	print(x)
结果是：
2

除了filter()函数 其他函数return 里有判断语句的返回的都是True 或 False