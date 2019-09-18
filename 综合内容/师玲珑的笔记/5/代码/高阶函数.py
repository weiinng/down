#map()函数用法
#map(function,iterable,..)
#功能：将第一个参数function 一次作用在参数可迭代对象中的每一个元素上，返回包含每次function函数返回值的新迭代器
#参数：
#function--函数，有两个参数
#iterable--一个或多个可迭代对象  （如：序列）
#返回值
#python 3.x 返回迭代器

# def add(x,y):
#     return x+y
#
# s=lambda x,y:x+y
# f=map(s,[1,2],[3,4])
# print(list(f))
#
# ss=lambda x:x**2
# def add2(x):
#     return x**2
# f2=map(ss,[1,2])
# print(list(f2))

# from functools import reduce
# def add(x,y):
#     return x+y
# f=reduce(add,[1,2,3])
# print(f)
# q=lambda x,y:x+y
# w=reduce(q,[1,23,3])
# print(w)

# f=lambda x : x%2==0
# w=filter(f,[4,1,2,3])
# print(list(w))

# def add(n):
#     return n+n
# f=map(add,[1,2,3])
# for x in f:
#     print(x)

# def add(n,q,e):
#     return n+q+e
# f=map(add,[1,2,3],{1,2,3},(1,2,3))
# for x in f:
#     print(x)

# from functools import reduce
# def add(x,y):
#     return x+y
# f=reduce(add,[1,2,3,4,5,6])
# print(f)

# def add(n):
#     return n%2==0
# f=filter(add,[1,2,3,4])
# for x in f:
#     print(x)

#实例：
# def f(x):
#     return x*x
# r=map(f,[1,2,3,4,5])
# print(r)    #打印出来的是地址    r的类型是map  高阶函数
# for x in r:           #遍历迭代器
#     print(x)
# print(list(r))     #将r强制转换为列表类型输出
# print(tuple(r))
# print(type(r))

# def add(x):
#     return x*x
# f=map(add,[1,2,3,4,5])
# print(list(f))

#拓展
# def fan(n):
#         return n%2==0
# r=map(fan,[1,2,3,4,5])
# for x in r:
#     print(x)
# print(list(r))

#结论：就算函数的if条件没满足  返回的值也是None  也放到返回的新的迭代器中  遍历时会有None


#函数返回的是一个迭代器
#当迭代器 迭代完毕后  在迭代出来就是空的  如上  用for遍历出来迭代器后 在print（list(r)）后出来是个空列表
#当先print(list(r)后 for 循环遍历出来什么都没有

#reduce()函数语法
#reduce(function,iterable[,initializer])
#功能：
#函数将一个数据集合（链表，元祖等）中的所有数据进行下列操作：用传给reduce中的函数
#function (有两个参数）先对集合中的第1、2个元素进行操作，得到的结果再与第三个数据
#用function 函数运算，最后得到一个结果
#其效果类似：reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)
#参数
#function--函数，有两个参数
#iterable--可迭代对象
#initializer--可选，初始参数
#返回值
#返回函数计算结果

# from functools import reduce
# def add(x,y):
#     return x+y
# q=[1,2,3,4]
# f=reduce(add,q[1::])
# print(f)

# from functools  import reduce
# def add(x,y):
#     return x+y
# f=reduce(add,[1,2,3,4,5])
# print(f)


#实例：
# from functools import reduce
# def add(x,y):
#     return x+y
# r=reduce(add,[1,2,3,4,5])   #r的值为1+2+3+4+5
# print(r)

#拓展
# from functools import reduce
# def f(x,y):
#         return x+y
# r=reduce(f,[x for x in range(1,101,2)])
# print(r)

#结论  reduce（）函数调用时  上面的函数   不能加判断条件  即 return 不能在if嵌套里 否则报错


# filter()函数
# filter(function,iterable)
# 功能：
# 该接收两个函数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后
# 返回True或False,最后将返回True的元素放到新的迭代器对象中
# 参数
# function--判断函数
# iterable--可迭代对象（如：序列）
# 返回值
# 返回一个迭代器对象
#实例
# def odd(n):
#     return n%2==1
# f=filter(odd,[1,2,3,4,5,6])
# print(list(f))
# for x in f:
#     print(x)
# print(f)
# def pan(n):
#     return n%2==0
# f=filter(pan,[1,2,3,4,5])
# print(list(f))


#拓展
# def fan(n):
#     return n%2==0
# def lie():
#     return [x for x in range(10)]
# f=filter(fan,lie())
# for x in f:
#     print(x)
# print(list(f))


# sorted()函数
#sorted(iterable,key=abs,reverse=False)
#功能：对所有可迭代对象进行排序操作
#参数
#iterable--可迭代对象
#key--key指定的函数将作用于可迭代对象上的每一个元素，并根据key函数返回的结果进行排序
#reverse--排序规则，reverse=True降序，reverse=False升序（默认）
#返回值
#返回重新排序的列表

# list=['I','am','and','student']
# # 按照单词长度进行降序排序：
# print(sorted(list,key=lambda x:len(x),reverse=True))


# list=[1,2,3,4,5]
# print(sorted(list,key=lambda x:x,reverse=True))

# stus=[
# {"name":"zhangsan","age":18},
# {"name":"zhangsan","age":17},
# {"name":"zhangsan","age":19}
# ]
# print(sorted(stus,key=lambda x : x['age']))
# print(sorted(stus,key=lambda x:x['age']))
# print(sorted(stus,key=lambda x:x['age'],reverse=True))
# print(sorted(stus,key=lambda x:x['age']))
# # 按age排序：
# stus.sort(key=lambda x:x['age'],reverse=True)
# print(stus)

#结论：sorted()函数  里 第一个参数是可迭代对象，第二个参数是key=匿名函数（也就是lambda函数）一个变量 ：这个变量
# 这个变量其实就是第一个参数可迭代对象里的元素

# a={1,3,4,5,2,6}
# print(sorted(a,key=lambda x:x,reverse=True))

#偏函数：
# 偏函数由function.partial创建，它的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，
# 调用这个新函数会更简单

#实例：
# import functools as a
# def add(a,b):
#     return a+b
# add10=a.partial(add,b=10)
# r=add10(5)
# print(r)    #这里我们使用function.partial创建出了一个新函数
             # add10,固定住了参数b,其默认值时10，这样相比原来
             # 的函数，新函数add10只需要在接收一个参数就可以
             # 了，整个代码显得简洁、优雅

#拓展：
# def add(a,b=10):
#     return a+b
# print(add(5))


# print(__name__)
# a=0
# if __name__ == '__main__':
#     a=1
# print(a)








