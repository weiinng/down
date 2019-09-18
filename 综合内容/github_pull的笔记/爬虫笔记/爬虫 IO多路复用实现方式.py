高性能相关 如何实现多个任务的同时进行 而且还效率高 



"""
串行实现
"""
import requests

urls = [
    'http://www.baidu.com/',
    'https://www.cnblogs.com/',
    'https://www.cnblogs.com/news/',
    'https://cn.bing.com/',
    'https://stackoverflow.com/',
]

for url in urls:
    response = requests.get(url)
    print(response)


"""
多线程
"""
import requests
import threading


urls = [
    'http://www.baidu.com/',
    'https://www.cnblogs.com/',
    'https://www.cnblogs.com/news/',
    'https://cn.bing.com/',
    'https://stackoverflow.com/',
]

def task(url):
    response = requests.get(url)
    print(response)

for url in urls:
    t = threading.Thread(target=task,args=(url,))
    t.start()


"""
协程+IO切换
pip3 install gevent
gevent内部调用greenlet（实现了协程）。
"""
from gevent import monkey; monkey.patch_all()
import gevent
import requests


def func(url):
    response = requests.get(url)
    print(response)

urls = [
    'http://www.baidu.com/',
    'https://www.cnblogs.com/',
    'https://www.cnblogs.com/news/',
    'https://cn.bing.com/',
    'https://stackoverflow.com/',
]
spawn_list = []	
for url in urls:
    spawn_list.append(gevent.spawn(func, url))	# 创建协程 

gevent.joinall(spawn_list)



"""
基于事件循环的异步非阻塞模块：Twisted
"""
from twisted.web.client import getPage, defer
from twisted.internet import reactor

def stop_loop(arg):
    reactor.stop()


def get_response(contents):
    print(contents)

deferred_list = []

url_list = [
    'http://www.baidu.com/',
    'https://www.cnblogs.com/',
    'https://www.cnblogs.com/news/',
    'https://cn.bing.com/',
    'https://stackoverflow.com/',
]

for url in url_list:
    deferred = getPage(bytes(url, encoding='utf8')) # 拿到了要爬取的任务，并没有真正的执行爬虫
    deferred.addCallback(get_response)	# 要调用的回调函数 
    deferred_list.append(deferred) # 将所有的任务加入带一个列表里面
	


dlist = defer.DeferredList(deferred_list)	# 检测所有的任务是否都被循环
dlist.addBoth(stop_loop)	# 如果列表中的任务都完成了就停止循环，执行停止的函数 

reactor.run()



























