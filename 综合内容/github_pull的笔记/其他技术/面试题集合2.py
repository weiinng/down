如何用Python输出一个Fibonacci数列？
	# 1 a,b = 0, 1
	# 2 while b<100:
	# 3     print (b),
	# 4     a, b = b, a+b


请写出一段Python代码实现删除一个list里面的重复元素
	#  l = [1,1,2,3,4,5,4]
	#  list(set(l))

Python里面如何拷贝一个对象？
	# copy	拷贝内存地址，源数据变动会受影响
	# deepcopy	完全拷贝，另开内存空间保存 ，完全独立两份数据

如何用Python来进行查询和替换一个文本字符串？
	# sub(replacement, string[, count=0])
	# replacement：被替换成的文本
	# string：需要被替换的文本
	# count：可选参数，指最大被替换的数量

Python里面search()和match()的区别？
	# match()函数只检测RE是不是在string的开始位置匹配，
		# match()只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回none
	# search()会扫描整个string查找匹配 
		
如何在一个function里面设置一个全局的变量？ 
	# global


python代码得到列表list的交集与差集
	# 交集
	# 1 b1=[1,2,3]
	# 2 b2=[2,3,4]
	# 3 b3 = [val for val in b1 if val in b2]
	# 4 print b3
	# 差集
	# 1 b1=[1,2,3]
	# 2 b2=[2,3,4]
	# 3 b3 = [val for val in b1 if val not in b2]
	# 4 print b3 

写一个简单的python socket编程
	"""
	# server 
	import socket
	if __name__ == '__main__':
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind(('localhost', 8001))
		sock.listen(5)

		while True:
			connection,address = sock.accept()
			try:
				connection.settimeout(5)
				msg = connection.recv(1024)
				if msg == '1':
					connection.send('welcome to server!')
				else:
					connection.send('please go out!')
			except socket.timeout:
				print 'time out'

			connection.close()
	
	# client 
	import socket
	import time

	if __name__ == '__main__':
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(('localhost', 8001))
		time.sleep(2)
		sock.send('1')
		print sock.recv(1024)
		sock.close()	
	"""

python递归的最大层数？
	# Python中默认的递归层数约为998左右(会报错)
	# 和计算机性能有关系，我的最大数字在3210 - 3220之间浮动

求结果
	# v = dict.fromkeys(['k1', 'k2'], [])
	# # 内存中k1和k2都指向同一个[](内存地址相同),只要指向的[]发生变化，k1和k2都要改变(保持一致)
	# v['k1'].append(666)
	# print(v)  # {'k1': [666], 'k2': [666]}
	# v['k1'] = 777
	# print(v)  # {'k1': 777, 'k2': [666]}

用python 实现一个 队列 
	"""
	class Stack(object):
		# 初始化栈
		def __init__(self):
		  self.items = []
	
		def push(self, item):
		  self.items.append(item)

		def pop(self):
			return self.items.pop(0)
	"""

用python 实现一个栈
	"""
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
	"""
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  