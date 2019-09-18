http 是什么？
	"""
	超文本传输协议 是一种规定了传输数据格式的协议
	短链接无状态
	请求首行 请求头 请求体
	响应首行 响应头 响应体 
	"""

为什么会有跨域？
	"""
	浏览器具有同源策略所有才出现跨域。
	同源策略：
		- 开放：src
		- 禁止：ajax
	解决跨域：
		- jsonp，在客户端动态创建一个script标签
			1.客户端：创建一个
				<script src='http://www.jxntv.cn/data/jmd-jxtv2.html'></script>
				<script>
					function func(arg){
						alert(arg);
					}
				</script>
			2.服务端：接收到请求并处理并返回值 "func('success')"
				相当于：
					<script>
						func('success')
					</script>

			弊端： jsonp只能进行 GET请求，而且需要两端协定函数名

		- cors，设置响应头
			- 简单请求
			- 复杂请求
				- options请求做预检
				- PUT/POST....

	在django中解决方案：
		- 中间件中设置响应头
		- django中的一个第三方组件：cors

	补充：
		jQuery Ajax：
			$.ajax({
				...
			})
		原生Ajax：XMLHttpRequest对象：
			var xhr = new XMLHttpRequest()

			xhr.onreadystatechange = function(){
				if(xhr.readyState == 4){
					// 已经接收到全部响应数据，执行以下操作
					var data = xhr.responseText;
					console.log(data);
				}
			};

			xhr.open('POST', "/test/", true);

			// 设置请求头
			xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset-UTF-8');

			// 发送请求
			xhr.send('n1=1;n2=2;');
	"""

常见请求头
	"""
		- Content-Type
		- User-Agent
		- referer，可以做图片防盗链。
		- Host
		- cookies
	"""
	
常见的请求体？
		Form表单提交：
			POST /index http1.1\r\nhost:www.luffycity.com...\r\n\r\nusername=alex&password=123&...
		Ajax请求：
			POST /index http1.1\r\nhost:www.luffycity.com...\r\n\r\nusername=alex&password=123&...
			POST /index http1.1\r\nhost:www.luffycity.com...\r\n\r\n{“username”:"alex","password":123}

		补充：django中获取请求体
			- request.POST 	username=alex&password=123&...	只能取到这种格式的
			- request.body 	{“username”:"alex","password":123}	可以取到所有格式的

常见的请求方法：
	- GET/POST/DELETE/PUT/PATCH/OPTIONS

常见的状态码：
	- 200	正常
	- 301/302	临时/永久重定向
	- 403/404
	- 500	服务器错误

路飞表结构：
	- 课程（13表）
		- 课程大类
		- 课程子类
		- 学位课
			- 讲师
			- 奖学金
		- 专题课（学位课模块表）
		- 价格策略(contenttype)
		- 课程详细(o2o -> 水平分表)
		- 常见问题
		- 课程大纲
		- 章节
		- 课时
		- 作业 
	- 深科技（4+2）
		- 用户表
		- 用户token
		- 文章来源
		- 文章表
		- 通用评论表
		- 通用收藏表

支付宝
	- rsa 加密
	- 商户私钥 和 支付宝公钥
	- 精度 小数点后两位
	- 支付宝收不到 succes 会一直发生 24小时的请求。才会结束

什么是响应式布局？
	根据浏览器的窗口大小的不同显示不同的效果
	@meida 属性 就可以实现 ,比如下面 长度超过 888 变红 
	@meida(min-width:888px) {  
		.div {
			background-color:red 
		}
	}

MySQL 数据库的引擎？有什么区别？
	innodb 支持事务 能做的事情更多功能更全
	mysaim 不支持事务 查询速度更快 是默认的引擎 



















