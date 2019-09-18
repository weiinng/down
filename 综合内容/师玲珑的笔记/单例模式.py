import pylab
import PIL
def jpeg2webp(filename):
	if filename:
		im = PIL.Image.open(filename)
		im.save(filename.split('.')[0] + '.webp')

def jpeg2png(filename):
	if filename:
		im = PIL.Image.open(filename)
		im.save(filename.split('.')[0] + '.png')

def jpeg2outline(filename):
	if filename:
		image = PIL.Image.open(filename).convert('L')
		print(image)
		im = pylab.array(image) # 打开图像并存储为灰度图片，保存在数组中
		print(im)
		pylab.figure() # 新建一个图像
		pylab.figure()
		pylab.contour(im, origin='upper')
		print(help(pylab.contour))
		pylab.axis('equal')
		pylab.axis('off') # 关闭x,y坐标
		pylab.show()

#jpeg2outline('1.jpg')

class A:
	var = None
	
	def wai(new):
		def func(cls,*args,**kwargs):
			if not cls.var:
				cls.var = new(cls,*args,**kwargs) 
				return cls.var
			else:
				return cls.var
		return func

	@wai
	def __new__(cls):
		return super().__new__(cls)
	def __init__(self):
		self.a = 1

	@classmethod
	def func(cls):
		cls.var = None

	def __del__(self):
		print('Gaius')
		print('-------------')
		self.func()
		# del self 
		#self.__del__()

a = A() # a= s
print(a)
a.__del__()

# a = open(file, mode, buffering, encoding, errors, newline, closefd, opener)
# a = 1

b = A() # b = s
c = A() # c = b->s
d = A() # d = b
f = A() # 
e = A()


print(b)
print(c)
print(d)
print(e)
print(f)
b.__del__()
# a = 1
# b = a 
# c = a

# del a

# del a
# del b
