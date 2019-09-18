
"""
class Base(object):

    def func(self):
        print('Base.func')

class Foo(Base):

    def func(self):
        # 方式一：根据mro的顺序执行方法
        # super(Foo,self).func()
        # 方式二：主动执行Base类的方法
        # Base.func(self)

        print('Foo.func')


obj = Foo()
obj.func()
"""
####################################
class Base(object):

    def func(self):
        super(Base, self).func()
        print('Base.func')

class Bar(object):
    def func(self):
        print('Bar.func')

class Foo(Base,Bar):
    pass

# 示例一
# obj = Foo()
# obj.func()
# print(Foo.__mro__)

# 示例二
# obj = Base()
# obj.func()