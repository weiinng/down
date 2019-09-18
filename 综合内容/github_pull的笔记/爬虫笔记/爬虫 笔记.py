需求： 
	1. 爬取汽车之家新闻咨询
		- 什么都不带
	2. 爬抽屉新热榜
		- 带请求头
		- 带cookie
		- 登录：
			- 获取cookie
			- 登录：携带cookie做授权
			- 带cookie去访问
	3. 爬取GitHub
		- 带请求头
		- 带cookie
		- 请求体中：
			commit:Sign in
			utf8:✓
			authenticity_token:hmGj4oS9ryOrcwoxK83raFqKR4sFG1yC09NxnDJg3B/ycUvCNZFPs4AxTsd8yPbm1F3i38WlPHPcRGQtyR0mmw==
			login:asdfasdfasdf
			password:woshiniba8
	
	4. 登录拉勾网 
		- 密码加密
			- 找js，通过python实现加密方式
			- 找密文，密码<=>密文
		
		- Referer头， 上一次请求地址，可以用于做防盗链。
	
总结：
	请求头：
		user-agent
		referer
		host
		cookie
		特殊请起头，查看上一次请求获取内容。
			'X-Anit-Forge-Code':...
			'X-Anit-Forge-Token':...
	请求体：
		- 原始数据
		- 原始数据 + token
		- 密文
			- 找算法 
			- 使用密文

	套路：
		- post登录获取cookie，以后携带cookie 
		- get获取未授权cookie，post登录携带cookie去授权，以后携带cookie 

基础用法：

	requests
		- url
		- headers
		- cookies 
		- data 
		- json 
		- params 
		- proxy

	bs4 
		- find 		
		- find_all	
		- text 
		- attrs


- scrapy框架 
	介绍：大而全的爬虫组件。
	
	安装：
		- Win:
			下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
			
			pip3 install wheel 
			pip install Twisted‑18.4.0‑cp36‑cp36m‑win_amd64.whl
			
			pip3 install pywin32
			
			pip3 install scrapy 
		- Linux:
			pip3 install scrapy 


	使用：
		Django:
			# 创建project
			django-admin startproject mysite 
			
			cd mysite
			
			# 创建app
			python manage.py startapp app01 
			python manage.py startapp app02 
			
			# 启动项目
			python manage.runserver 
			
		Scrapy：
			# 创建project
			scrapy  startproject xdb 
			
			cd xdb 
			
			# 创建爬虫
			scrapy genspider chouti chouti.com 
			scrapy genspider cnblogs cnblogs.com 
			
			# 启动爬虫
			scrapy crawl chouti


目录结构
	项目名称
	   项目名称/
			- spiders				# 爬虫文件 
				- chouti.py 
				- cnblgos.py 
				....
			- items.py 				# 持久化
			- pipelines				# 持久化
			- middlewares.py		# 中间件
			- settings.py 			# 配置文件（爬虫）
	   scrapy.cfg

scrapy 
	命令：
		scrapy startproject xx 
		cd xx 
		scrapy genspider chouti chouti.com 
		
		scrapy crawl chouti --nolog 
	
	编写：
		def parse(self,response):
			# 1.响应
			# response封装了响应相关的所有数据：
				- response.text 
				- response.encoding
				- response.body 
				- response.request # 当前响应是由那个请求发起；请求中 封装（要访问的url，下载完成之后执行那个函数）
			# 2. 解析器 
			# // 子子孙孙 / 儿子 .// 当前往下找子子孙孙 
			# response.xpath('//div[@href="x1"]/a').extract_first()
			# response.xpath('//div[@href="x1"]/a').extract()
			# response.xpath('//div[@href="x1"]/a/text()').extract()
			# response.xpath('//div[@href="x1"]/a/@href').extract()
			# tag_list = response.xpath('//div[@href="x1"]/a')
			for tag in tag_list:
				tag.xpath('.//p/text()').extract_first()
				
			# 3. 再次发起请求
			# 回调函数 callback 可以在继续执行下一个函数 可以递归
			# from scrapy.http import Request
			# yield Request(url='xxxx',callback=self.parse) 
			
持久化相关：
	pipeline/items
		a. 先写pipeline类
			class XXXPipeline(object):
				def process_item(self, item, spider):
					return item
					
		b. 写Item类
			class XdbItem(scrapy.Item):
				href = scrapy.Field()
				title = scrapy.Field()
						
		c. 配置
			ITEM_PIPELINES = {
			   'xdb.pipelines.XdbPipeline': 300, # 优先级数值 0-1000 越小越优先执行 
			}
		
		d. 爬虫，yield每执行一次，process_item就调用一次。
			
			yield Item对象

	编写pipeline：
		"""
		源码执行顺序 ：
			1. 判断当前XdbPipeline类中是否有from_crawler
				有：
					obj = XdbPipeline.from_crawler(....)
				否：
					obj = XdbPipeline()
			2. obj.open_spider()
			
			3. obj.process_item()/obj.process_item()/obj.process_item()/obj.process_item()/obj.process_item()
			
			4. obj.close_spider()
		
		解析:
			如果不先执行 from_crawler 
			init 里面的 path 就获取不到值了
			先通过 from_crawler 将 path 获取到返回给 init 
			然后 init 才能争取的实例化对象 
		"""
		from scrapy.exceptions import DropItem

		class FilePipeline(object):

			def __init__(self,path):
				self.f = None
				self.path = path	
				# 写入文件的路径参数 ，放在 setting 中了。
				# 通过 from_crawler 来拿到 path 

			@classmethod
			def from_crawler(cls, crawler): 
				"""
				初始化时候，用于创建pipeline对象
				:param crawler:
				:return:
				"""
				print('File.from_crawler')
				path = crawler.settings.get('HREF_FILE_PATH') 
				return cls(path)

			def open_spider(self,spider):
				"""
				爬虫开始执行时，调用 
				用于 文件的打开
				:param spider:
				:return:
				"""
				# if spider.name == "chouti":  # spider参数 用于筛选个性化定制 
				print('File.open_spider')
				self.f = open(self.path,'a+')

			def process_item(self, item, spider):
				# f = open('xx.log','a+')
				# f.write(item['href']+'\n')
				# f.close() 
				# 这样写太low了，每次都要打开关闭文件
				# 因此选择 将 文件操作绕开每次循环。
				print('File',item['href'])
				self.f.write(item['href']+'\n')
				
				# return item  	# 交给下一个pipeline的process_item方法
				raise DropItem()# 后续的 pipeline的process_item方法不再执行

			def close_spider(self,spider):
				"""
				爬虫关闭时，被调用
				用于 文件的关闭 
				:param spider:
				:return:
				"""
				print('File.close_spider')
				self.f.close()


		注意：pipeline是所有爬虫公用，如果想要给某个爬虫定制需要使用spider参数自己进行处理。

去重相关
	系统自动的 去重规则在  scrapy.dupefilter.BaseDupeFilter，如果想自定义重写即可
	自定义去重规则
		from scrapy.dupefilter import BaseDupeFilter
		from scrapy.utils.request import request_fingerprint

		class XdbDupeFilter(BaseDupeFilter):

			def __init__(self):
				self.visited_fd = set()
				# 这里是放在本机内存里面了。也可以放在 redis 里面 

			@classmethod
			def from_settings(cls, settings):
				return cls()

			def request_seen(self, request):
				fd = request_fingerprint(request=request)	# 内置的去重规则在这里再次调用 
				if fd in self.visited_fd:
					return True # 表示已经看过了 
				self.visited_fd.add(fd)	# 未看过的观看后加入到集合中

			def open(self):  # can return deferred
				print('开始')

			def close(self, reason):  # can return a deferred
				print('结束')

			# def log(self, request, spider):  # log that a request has been filtered
			#     print('日志')

	配置 
		# 修改默认的去重规则
		# DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'
		DUPEFILTER_CLASS = 'xdb.dupefilters.XdbDupeFilter'


	爬虫使用：
		# dont_filter 控制是否遵循去重规则 为 False 才可以遵循 ，当然默认是 fales 因此scrapy 是自带去重的
		
		class ChoutiSpider(scrapy.Spider):
			name = 'chouti'
			allowed_domains = ['chouti.com']
			start_urls = ['https://dig.chouti.com/']

			def parse(self, response):
				print(response.request.url)
				
				page_list = response.xpath('//div[@id="dig_lcpage"]//a/@href').extract()
				for page in page_list:
					from scrapy.http import Request
					page = "https://dig.chouti.com" + page
					# yield Request(url=page,callback=self.parse,dont_filter=False) # https://dig.chouti.com/all/hot/recent/2
					yield Request(url=page,callback=self.parse,dont_filter=True) # https://dig.chouti.com/all/hot/recent/2
	
深度 
	爬取网页的时候会基于访问深度体现。比如基于分页，第二页的时候深度即为2
		
		response.meta.get("depth") 可以看到具体的深度 默认为 0 每次yield时，会根据原来请求中的depth + 1
	配置文件：
		# 限制深度
		DEPTH_LIMIT = 3

		# 优先级 
		# 请求被下载的优先级 -= 深度 * 配置 DEPTH_PRIORITY 
		DEPTH_PRIORITY = 1

cookie 
	方式一：
		- 携带 
			yield Request(
				url='https://dig.chouti.com/login',
				method='POST',
				body="phone=8613121758648&password=woshiniba&oneMonth=1",	# 必须要用 body 格式，如果不适应非要字典那就用 urlencode 转换
				# body=urlencode({})"phone=8615131255555&password=12sdf32sdf&oneMonth=1"
				# urlencode 需要导入 from urllib.parse import urlencode
				# urlencode 可以将字典格式 转换成 body 格式 
				cookies=self.cookie_dict,
				headers={
					'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
				},
				callback=self.check_login # 成功后的回调函数 
			)
			 
			def check_login(self,response):
				print(response.text)
				yield Request(...)
		
		- 解析：
				cookie_dict = {} # 最好写在全局。这样子大家都可以拿
				cookie_jar = CookieJar() # 先实例化 
				cookie_jar.extract_cookies(response, response.request)	# 传入参数，将请求的和响应的 cookie 都拿到 

				# 去对象中将cookie解析到字典
				for k, v in cookie_jar._cookies.items():
					for i, j in v.items():
						for m, n in j.items():
							cookie_dict[m] = n.value
	方式二：meta
	
start_urls
	- 内部原理：
			"""
			scrapy引擎来爬虫中取起始URL：
				1. 调用start_requests并获取返回值
				2. v = iter(返回值)
				3. 
					req1 = 执行 v.__next__()
					req2 = 执行 v.__next__()
					req3 = 执行 v.__next__()
					...
				4. req全部放到调度器中
			"""
	- 编写
		class ChoutiSpider(scrapy.Spider):
			name = 'chouti'
			allowed_domains = ['chouti.com']
			start_urls = ['https://dig.chouti.com/']
			cookie_dict = {}
			
			def start_requests(self):
				# 方式一：
				for url in self.start_urls:
					yield Request(
						url=url,
						callback=self.parse,
						method='POST' 	# 自己写的优先级更高。因此在这里可以指定 post 请求也可以作为起始了
						)	
				# 方式二：
				# req_list = []
				# for url in self.start_urls:
				#     req_list.append(Request(url=url))
				# return req_list
	- 定制：可以去redis中获取


- scrapy中设置代理 
	- 内置
		在爬虫启动时，提前在os.envrion中设置代理即可。
			class ChoutiSpider(scrapy.Spider):
				name = 'chouti'
				allowed_domains = ['chouti.com']
				start_urls = ['https://dig.chouti.com/']
				cookie_dict = {}

				def start_requests(self):
					import os
					os.environ['HTTPS_PROXY'] = "http://root:woshiniba@192.168.11.11:9999/"
					os.environ['HTTP_PROXY'] = '19.11.2.32',
					for url in self.start_urls:
						yield Request(url=url,callback=self.parse)
		meta:
			class ChoutiSpider(scrapy.Spider):
				name = 'chouti'
				allowed_domains = ['chouti.com']
				start_urls = ['https://dig.chouti.com/']
				cookie_dict = {}

				def start_requests(self):
					for url in self.start_urls:
						yield Request(url=url,callback=self.parse,meta={'proxy':'"http://root:woshiniba@192.168.11.11:9999/"'})

	- 自定义
		import base64
		import random
		from six.moves.urllib.parse import unquote
		try:
			from urllib2 import _parse_proxy
		except ImportError:
			from urllib.request import _parse_proxy
		from six.moves.urllib.parse import urlunparse
		from scrapy.utils.python import to_bytes

		class XdbProxyMiddleware(object):

			def _basic_auth_header(self, username, password):
				user_pass = to_bytes(
					'%s:%s' % (unquote(username), unquote(password)),
					encoding='latin-1')
				return base64.b64encode(user_pass).strip()

			def process_request(self, request, spider):
				PROXIES = [
					"http://root:woshiniba@192.168.11.11:9999/",
					"http://root:woshiniba@192.168.11.12:9999/",
					"http://root:woshiniba@192.168.11.13:9999/",
					"http://root:woshiniba@192.168.11.14:9999/",
					"http://root:woshiniba@192.168.11.15:9999/",
					"http://root:woshiniba@192.168.11.16:9999/",
				]
				url = random.choice(PROXIES)

				orig_type = ""
				proxy_type, user, password, hostport = _parse_proxy(url)
				proxy_url = urlunparse((proxy_type or orig_type, hostport, '', '', '', ''))

				if user:
					creds = self._basic_auth_header(user, password)
				else:
					creds = None
				request.meta['proxy'] = proxy_url
				if creds:
					request.headers['Proxy-Authorization'] = b'Basic ' + creds

- 下载中间件 
		写中间件：
			from scrapy.http import HtmlResponse
			from scrapy.http import Request

			class Md1(object):
				@classmethod
				def from_crawler(cls, crawler):
					# This method is used by Scrapy to create your spiders.
					s = cls()
					return s

				def process_request(self, request, spider):	
					print('md1.process_request',request)
					return None # 返回如果是 空就会继续往下执行下一个中间件的 process_request 方法，如果一旦有返回值就要考虑情况
					"""
					# 1. 返回 Response
					# 返回 Response 之后会往下执行 最后一个中间件的 process_response 方法 
					# import requests
					# result = requests.get(request.url)
					# return HtmlResponse(url=request.url, status=200, headers=None, body=result.content)
					
					# 2. 返回 Request
					# 返回 Request 之后 相当于无视了这次的请求 重新回到 调制器 那边，相当于又产生了新的任务
					# return Request('https://dig.chouti.com/r/tec/hot/1')

					# 3. 抛出异常	
					# 抛出异常 必须要 有 process_exception 方法进行捕捉异常，不然会报错
					# process_exception 方法在进行一系列的操作 在捕捉到异常的时候 
					# from scrapy.exceptions import IgnoreRequest
					# raise IgnoreRequest
					
					# 4. 对请求进行加工(*) 
					# 通常我们都是用于对请求加工，然后再继续下面操作不返回东西 
					# request.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
					# return None
					"""

				def process_response(self, request, response, spider):
					# Called with the response returned from the downloader.

					# Must either;
					# - return a Response object	# 返回一个 Response 来代替当前的 Response
					# - return a Request object		# 返回一个 Request 开启新任务 
					# - or raise IgnoreRequest		# 返回一个 IgnoreRequest 进行异常捕捉 
					print('m1.process_response',request,response)
					return response

				def process_exception(self, request, exception, spider):
					# Called when a download handler or a process_request()
					# (from other downloader middleware) raises an exception.

					# Must either:
					# - return None: continue processing this exception
						# 通常我们都是直接返回 None 就可以了
					# - return a Response object: stops process_exception() chain	# 只要返回了 Response 当前的 process_exception 就不做操作了 
						# 返回 Response 表示交给下一个 中间件的 process_exception 继续处理 
					# - return a Request object: stops process_exception() chain	# 只要返回了 Request 当前的 process_exception 就不做操作了 
						# 返回 Request 放弃本次任务，新建任务 	
					pass

		配置：
			DOWNLOADER_MIDDLEWARES = {	
			   #'xdb.middlewares.XdbDownloaderMiddleware': 543,
				# 'xdb.proxy.XdbProxyMiddleware':751,
				'xdb.md.Md1':666,	# 依旧是 0-1000 越小越优先 
				'xdb.md.Md2':667,
			}
		
		执行顺序 
			调度器给 下载器的时候先走 process_request（从第一个中间件往最后一个走） 然后如果根据返回情况进行判断接下来的方向
				返回 None 继续下一个中间件的 process_request
				返回 Response 进入 最后一个下载中间件的 process_response 流程
				返回 Request 返回 调度器开启新任务 
				返回 异常  进入当前中间件的 process_exception 进行异常处理
			下载器还给 爬虫的时候要走 process_response（从最后一个中间件往第一个走）然后如果根据返回情况进行判断接下来的方向
				返回 None 继续上一个中间件的 process_response
				返回 Response 替换当前Response 进入上一个下载中间件的 process_response 流程
				返回 Request 返回 调度器开启新任务 放弃当前的任务  
				返回 异常  进入当前中间件的 process_exception 进行异常处理
		应用：
			- user-agent # 所有的请求都加 user-agent	
				# 其实不需要做，默认自带一个 可以添加 user-agent 的功能
				# 再 settings 中 USER_AGENT = '' 直接配置就可以实现这个功能 
			- 代理 	# 请求代理操作 
						
	- 爬虫中间件	
		class Sd1(object):
			# Not all methods need to be defined. If a method is not defined,
			# scrapy acts as if the spider middleware does not modify the
			# passed objects.

			@classmethod
			def from_crawler(cls, crawler):
				# This method is used by Scrapy to create your spiders.
				s = cls()
				return s

			def process_spider_input(self, response, spider):
				# Called for each response that goes through the spider
				# middleware and into the spider.

				# Should return None or raise an exception.
				return None

			def process_spider_output(self, response, result, spider):
				# Called with the results returned from the Spider, after
				# it has processed the response.

				# Must return an iterable of Request, dict or Item objects.
				for i in result:
					yield i

			def process_spider_exception(self, response, exception, spider):
				# Called when a spider or process_spider_input() method
				# (from other spider middleware) raises an exception.

				# Should return either None or an iterable of Response, dict
				# or Item objects.
				pass

			# 只在爬虫启动时，执行一次。
			def process_start_requests(self, start_requests, spider):
				# Called with the start requests of the spider, and works
				# similarly to the process_spider_output() method, except
				# that it doesn’t have a response associated.

				# Must return only requests (not items).
				for r in start_requests:
					yield r

		配置：	
			SPIDER_MIDDLEWARES = {
			   # 'xdb.middlewares.XdbSpiderMiddleware': 543,
				'xdb.sd.Sd1': 666,	# 同爬虫中间件一样的判断机制 
				'xdb.sd.Sd2': 667,
			}
		
		执行流程 ：
			第一次启动爬虫文件封装好 request 之后 走 process_start_requests 上传给引擎 
			然后 引擎将封装好的 request 给调度器 
			调度器 继续执行 给下载器
			下载器 下载了内容之后给 引擎 
			引擎再给 爬虫文件的时候要走 process_spider_input 
			爬虫文件处理完之后如果有  yield 就要在走 process_spider_output 给引擎 
		
		应用：
			- 深度
			- 优先级
			
定制命令
	- 单爬虫运行：
		import sys
		from scrapy.cmdline import execute

		if __name__ == '__main__':
			execute(["scrapy","crawl","chouti","--nolog"])
	- 所有爬虫：
		- 在spiders同级创建任意目录，如：commands
		- 在其中创建 crawlall.py 文件 （此处文件名就是自定义的命令）
		- 在settings.py 中添加配置 COMMANDS_MODULE = '项目名称.目录名称'
		- 在项目目录执行命令：scrapy crawlall 
	
	# crawlall.py
	from scrapy.commands import ScrapyCommand
	from scrapy.utils.project import get_project_settings


	class Command(ScrapyCommand):

		requires_project = True

		def syntax(self):
			return '[options]'

		def short_desc(self):
			return 'Runs all of the spiders'

		def run(self, args, opts):
			spider_list = self.crawler_process.spiders.list()
			for name in spider_list:
				self.crawler_process.crawl(name, **opts.__dict__)
			self.crawler_process.start()
	
	# settings.py
	# 自定制命令目录
	COMMANDS_MODULE  = "xdb.commands"


信号 使用框架预留的位置，帮助你自定义一些功能
		from scrapy import signals

		class MyExtend(object):
			def __init__(self):
				pass

			@classmethod
			def from_crawler(cls, crawler):
				self = cls()

				crawler.signals.connect(self.x1, signal=signals.spider_opened)
				crawler.signals.connect(self.x2, signal=signals.spider_closed)

				return self

			def x1(self, spider):
				print('open')

			def x2(self, spider):
				print('close')
	
		"""
		# 信号可选类型  from scrapy import signals 中可以看到 
		engine_started = object()
		engine_stopped = object()
		
		spider_opened = object()
		spider_idle = object()
		spider_closed = object()
		spider_error = object()
		
		request_scheduled = object()
		request_dropped = object()
		response_received = object()
		response_downloaded = object()
		
		item_scraped = object()
		item_dropped = object()
		"""
	配置：
		EXTENSIONS = {
			'xdb.ext.MyExtend':666,
		}


scrapy配置
		- USER_AGENT	# 所有的都加上 USER_AGENT
		- ROBOTSTXT_OBEY	# 君子协定 True 的时候会试探性的发送一次请求 查看是否允许爬取，为 Fales 就暴力爬取无视协议
		
		- CONCURRENT_REQUESTS = 32	# 全部的并发请求数量  存在CONCURRENT_REQUESTS_PER_DOMAIN/IP 的时候此配置不生效
		- CONCURRENT_REQUESTS_PER_DOMAIN = 16	# 对每个域名的并发请求数量
		- CONCURRENT_REQUESTS_PER_IP = 16	# 对每个 IP 的并发请求数量
		
		- DEFAULT_REQUEST_HEADERS = {	# 常见的请求头
			   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			   'Accept-Language': 'en',
			}
		- 下载中间级
		
		- 爬虫中间件
		
		- pipeline
		
		- EXTENSIONS	# 基于信号的扩展
		
		- 缓存机制 
		# HTTPCACHE_ENABLED = True
		# HTTPCACHE_EXPIRATION_SECS = 0
		# HTTPCACHE_DIR = 'httpcache' # 本地会生成一个 httpcache 的目录保存爬取数据
		# HTTPCACHE_IGNORE_HTTP_CODES = []
		# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

		
		
		
		- DOWNLOAD_DELAY = 3	# 下载页面的时候 3s 的延迟 
		
		- 智能限速
			"""
			自动限速算法
			from scrapy.contrib.throttle import AutoThrottle
			自动限速设置
			1. 获取最小延迟 DOWNLOAD_DELAY
			2. 获取最大延迟 AUTOTHROTTLE_MAX_DELAY
			3. 设置初始下载延迟 AUTOTHROTTLE_START_DELAY
			4. 当请求下载完成后，获取其"连接"时间 latency，即：请求连接到接受到响应头之间的时间
			5. 用于计算的... AUTOTHROTTLE_TARGET_CONCURRENCY
			
			target_delay = latency / self.target_concurrency
			new_delay = (slot.delay + target_delay) / 2.0 # 表示上一次的延迟时间
			new_delay = max(target_delay, new_delay)
			new_delay = min(max(self.mindelay, new_delay), self.maxdelay)
			slot.delay = new_delay


			# 智能限速 
			#AUTOTHROTTLE_ENABLED = True
			# The initial download delay
			#AUTOTHROTTLE_START_DELAY = 5
			# The maximum download delay to be set in case of high latencies
			#AUTOTHROTTLE_MAX_DELAY = 60
			# The average number of requests Scrapy should be sending in parallel to
			# each remote server
			#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
			# Enable showing throttling stats for every response received:
			#AUTOTHROTTLE_DEBUG = False
			"""
	
	

	













		