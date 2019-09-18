# twisted 是什么 ？以及 和 requests 的区别？
	"""
		requests 是一个 python 实现的可以伪造浏览器发送Http 请求的 模块
		twisted 是基于事件循环的异步非阻塞网络框架 
		
		scrapy 的安装是基于 twisted 的 
		
		关键词： 
			非阻塞： 不等待
			异步 ： 回调
			事件循环 ： 一直循环检查状态
		
		官方：
			基于事件循环的异步非阻塞模块。
		自己的语言:
			非阻塞的基于一个线程可以发起多次链接请求
			异步的同时还进行回调以及事件循环
			
			一个线程同时可以向多个目标发起Http请求。
	"""
	
scrapy 组件以及执行流程？
	"""
		- 引擎找到要执行的爬虫，并执行爬虫的 start_requests 方法，并的到一个 迭代器。
			- 配置文件中 SPIDER_MODULIES 会找到所有的爬虫文件
			- 然后 scrapy crawl chouti 会根据配置文件的目录里面根据 name 找到 具体的爬虫文件进行执行
			- 找到 文件后就实例化进行执行 start_requests 方法 ，将起始url 封装成 reques 方法 
		
		- 迭代器循环时会获取Request对象，而request对象中封装了要访问的URL和回调函数。
		
		- 将所有的request对象(任务)放到调度器中，用于以后被下载器下载。
		
		- 下载器去调度器中获取要下载任务（就是Request对象），下载完成后执行回调函数。
		
		- 回到spider的回调函数中，
			yield Request() -----> 继续下一轮的 封装 request 放入调度器
			yield Item() ------> 放入 pipeline 中进行执行 
	"""










