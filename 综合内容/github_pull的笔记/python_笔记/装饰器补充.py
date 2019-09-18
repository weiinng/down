
# 1. 装饰器
import functools

def auth(func):
    # @functools.wraps(func)
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        return ret
    return inner

@auth
def index():
    print('index')

@auth
def detail():
    print('detail')

print(index.__name__)
print(detail.__name__)

# 2. endpoint默认是函数名


# 3. 装饰器先后顺序















