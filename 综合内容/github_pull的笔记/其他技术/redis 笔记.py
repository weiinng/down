# redis
# 	一个软件 帮助开发者对一台机器的内存进行操作，速度更快
# 	可以做持久化 AOF RDB
# 	相当于一个大字典 本身就是单进程单线程
#
# 	关键字
# 		缓存 优先去 redis 中获取
#
# 	数据类型：
# 		redis={
# 					k1:'123',  字符串
# 					k2:[1,2,3,4,4,2,1], 列表
# 					k3:{1,2,3,4}, 集合
# 					k4:{name:123,age:666}, 字典
# 					k5:{('alex',60),('eva-j',80),('rt',70),}，有序集合
# 			}
#
#
# 	安装
# 		服务端
# 		- redis 软件
# 			- 安装 yum -install redis
# 			- 启动 redis-server /etc/redis.conf
# 			- 配置文件
# 				- bind 0.0.0.0
# 				- port 6379
# 				- requirepass：我的密码
# 		客户端
# 		- python 链接 redis 模块
# 			- pip3 install redis
#
# 	链接
#
# 		import redis
#
# 		# 单链接
# 		conn = redis.Redis(host='x.x.x.x',port=6379,password='我的密码' )
# 		conn.set("x1","lalalal",ex=5) # ex 超时时间 秒单位 # px 毫秒单位
# 		val = conn.get("x1")
#
# 		# 链接池
# 		pool = redis.ConnctionPool(host='x.x.x.x',port=6379,password='我的密码',max_connections=1000)
# 		r = redis.Redis(connection_pool=pool)
# 		r.set("foo","Bar")
# 			# 链接需要注意 姿势不对会导致效率降低
# 			# 最好基于模块的单例模式让 链接池唯一，避免链接池的重复创建
#
# 	应用（django）：
# 		1. 自定义使用redis
# 		配置：
# 			创建一个连接好的地址池的单例
# 				import redis
# 				POOL = redis.ConnectionPool(host='10.211.55.4', port=6379,password='luffy1234',max_connections=1000)
#
# 		使用：
# 			import redis
# 			from django.shortcuts import render,HttpResponse
# 			from utils.redis_pool import POOL
# 			def index(request):
# 				conn = redis.Redis(connection_pool=POOL)
# 				conn.hset('kkk','age',18)
#
# 				return HttpResponse('设置成功')
# 			def order(request):
# 				conn = redis.Redis(connection_pool=POOL)
# 				conn.hget('kkk','age')
# 				return HttpResponse('获取成功')
#
# 		2. 使用第三方组件
# 			pip3 install django-redis
#
# 			配置：
# 				settings.py 中设置链接参数以及地址池参数，全局生效
# 				CACHES = {
# 					"default": {
# 						"BACKEND": "django_redis.cache.RedisCache",
# 						"LOCATION": "redis://127.0.0.1:6379",
# 						"OPTIONS": {
# 							"CLIENT_CLASS": "django_redis.client.DefaultClient",
# 							"CONNECTION_POOL_KWARGS": {"max_connections": 100}
# 							# "PASSWORD": "密码",
# 						}
# 					}
# 				}
# 				# 可以使用文件做缓存目录
# 				# CACHES = {
# 				#     'default': {
# 				#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
# 				#         'LOCATION': '/var/tmp/django_cache',
# 				#     }
# 				# }
# 				# 或者其他源
# 				# CACHES = {
# 				#     'default': {
# 				#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
# 				#         'LOCATION': '127.0.0.1:11211',
# 				#     }
# 				# }
#
# 			使用：
# 				import redis
# 				from django.shortcuts import render,HttpResponse
# 				from django_redis import get_redis_connection
# 				def index(request):
# 					conn = get_redis_connection("default")
# 					return HttpResponse('设置成功')
# 				def order(request):
# 					conn = get_redis_connection("back")
# 					return HttpResponse('获取成功')
#
# 	高级应用
# 		1. 全站缓存
# 			设置
# 				setting.py  添加两个中间件  以及 redis 设置
# 					MIDDLEWARE = [
# 						'django.middleware.cache.UpdateCacheMiddleware',
# 						...
# 						'django.middleware.cache.FetchFromCacheMiddleware',
# 					]
#
# 				# redis配置
# 				CACHES = {
# 					"default": {
# 						"BACKEND": "django_redis.cache.RedisCache",
# 						"LOCATION": "redis://127.0.0.1:6379",
# 						"OPTIONS": {
# 							"CLIENT_CLASS": "django_redis.client.DefaultClient",
# 							"CONNECTION_POOL_KWARGS": {"max_connections": 100}
# 							# "PASSWORD": "密码",
# 						}
# 					}
# 				}
#
# 			使用 完全和普通一样无任何操作
# 				from django.shortcuts import render,HttpResponse
# 				import time
#
#
# 				def index(request):
# 					ctime = str(time.time())
# 					return HttpResponse(ctime)
#
# 				def order(request):
# 					ctime = str(time.time())
# 					return HttpResponse(ctime)
#
# 		2. 局部缓存
# 			setting.py 重要配置
# 				# redis配置
# 					CACHES = {
# 						"default": {
# 							"BACKEND": "django_redis.cache.RedisCache",
# 							"LOCATION": "redis://127.0.0.1:6379",
# 							"OPTIONS": {
# 								"CLIENT_CLASS": "django_redis.client.DefaultClient",
# 								"CONNECTION_POOL_KWARGS": {"max_connections": 100}
# 								# "PASSWORD": "密码",
# 							}
# 						}
# 					}
#
# 			应用
# 				{% load cache %}
# 				<!DOCTYPE html>
# 				<html lang="zh-CN">
# 				<head>
# 					<meta charset="UTF-8">
# 					<title>Title</title>
# 					<meta name="viewport" content="width=device-width, initial-scale=1">
# 				</head>
# 				<body>
# 					<h1>asdfasdfasdf</h1>
# 					<div>
# 						asdf
# 					</div>
# 					{% cache 缓存时间(单位毫秒) 缓存的key %}
# 						<div>asdfasdf</div>
# 					{% endcache %}
#
# 				</body>
# 				</html>
#
# 	使用字典：h 开头
# 		- 基本操作
# 			查看
# 				conn.keys() 查看所有的数据
# 				conn.keys("name_1_*")	查看所有name 以name_1_ 开头的键值
# 					对 name 进行取值的时候 用 scan_iter 对key 进行过滤 分批取出
# 					conn.scan_iter("name_1_*",count=10)
# 				conn.hget("name","key") 根据名字自己 key 拿 值
# 				conn.exists("name") 判断是否存在
# 				.conn.expire("name",60*30)  设置超时时间 30分钟
#
#
# 			添加
# 				hset("name","key","value") 一次只能加一对键值
# 				hmset("name",{"k1":"v1","k2":"v2"})  一次可以直接加进去一个字典多个键值对
# 					name 相同的时候表示就是同一个，在赋值会覆盖上次的值。
# 			修改
# 				hset("name","key","value")  重新赋值即可
# 			删除
# 				delet("name")
# 		- 字典的可以有很多层，但是取值的时候只能取出来最外层，没办法用索引继续深处取值
# 		- 慎重使用hgetall, 优先使用 hscan_iter
# 		-
# 		- 计数器
#
# 		注意事项：redis操作时，只有第一层value支持：list,dict ....
#
# 	使用列表： l 开头
# 		lpush 左边添加
# 		rpush 右边添加
# 		lpop  左边取值
# 		rpop  右边取值
# 		blpop 带阻塞的左取值，可设置 timeout=10 超时拿到 none
# 		唯独 列表没有 iter方法。因此可以自己利用 lrange() 和 yield 自己实现一个
#
# 		事务+一次发送多个命令：
# 			conn = redis.Redis(host='47.94.172.250',port=6379,password='Luffy!4321')
#
# 			pipe = conn.pipeline(transaction=True)
# 			pipe.multi()
#
# 			pipe.set('k2','123')
# 			pipe.hset('k3','n1',666)
# 			pipe.lpush('k4','laonanhai')
#
# 			pipe.execute()
#
#
#
#
#