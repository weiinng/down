import functools


def index(a1,a2):
    return a1 + a2

# 原来的调用方式
# ret = index(1,23)
# print(ret)

# 偏函数，帮助开发者自动传递参数
new_func = functools.partial(index,666)
ret = new_func(1)
print(ret)


