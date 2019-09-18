# 对每个线程单独创建内存空间来保存数据，实现数据的空间分离

# 在 DBUtils 中可以用到 ，为每个线程创建一个数据库连接的时候


"""
import threading
from threading import local
import time

def task(i):
	global v
    time.sleep(1)
    print(v)

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()
#  9 9 9 9 9 9 9 9 9 
"""

"""
import threading
from threading import local
import time

obj = local()  # 为每个线程创建一个独立的空间。数据空间隔离


def task(i):
    obj.xxxxx = i
    time.sleep(2)
    print(obj.xxxxx,i)

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()
# 0-9 打乱顺序 
"""

"""
import threading
from threading import local

def task(i):
    print(threading.get_ident(),i)  # 获取线程的唯一标记 

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()
"""

"""
# threading local 的内部实现原理 
import time
import threading
import greenlet

DIC = {}	# 用线程的唯一标识作为 key 来创建一个大字典分别保存每个线程的数据

def task(i):

    # ident = threading.get_ident()  # 获取进程的 唯一id
    ident = greenlet.getcurrent()	# 获取协程的 唯一id
    if ident in DIC:
        DIC[ident]['xxxxx'] = i
    else:
        DIC[ident] = {'xxxxx':i }
    time.sleep(2)

    print(DIC[ident]['xxxxx'],i)

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()

"""
# 完整版。封装更方便使用 

import time
import threading
try:
    import greenlet
    get_ident =  greenlet.getcurrent
except Exception as e:
    get_ident = threading.get_ident

class Local(object):
    DIC = {}

    def __getattr__(self, item):
        ident = get_ident()
        if ident in self.DIC:
            return self.DIC[ident].get(item)
        return None

    def __setattr__(self, key, value):
        ident = get_ident()
        if ident in self.DIC:
            self.DIC[ident][key] = value
        else:
            self.DIC[ident] = {key:value}


obj = Local()

def task(i):
    obj.xxxxx = i
    time.sleep(2)
    print(obj.xxxxx,i)

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()
