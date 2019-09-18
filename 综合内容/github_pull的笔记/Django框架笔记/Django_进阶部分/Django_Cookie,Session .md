Cookie
	Cookie的由来
		HTTP协议是无状态的,每次请求都是独立的,对服务器来说，每次的请求都是全新的,上一次的访问是数据是无法保留到下一次的
		某些场景需要状态数据或者中间数据等相关对下一次会话请求有需求的数据,因此需要一种可以传递的手段
	Cookie的本质
		Cookie具体为一段小信息，由 服务器 发出存储在 浏览器 上的一组组 键值对
		下次访问服务器时浏览器会自动携带这些键值对，以便服务器提取有用信息
	Cookie的原理
		由服务器产生内容，浏览器收到请求后保存在本地；
		当浏览器再次访问时，浏览器会自动带上Cookie，这样服务器就能通过Cookie的内容来判断这个是“谁”了
	查看Cookie
		谷歌浏览器--右键检查--Network--all--具体项目--cookie
	Django中操作Cookie	
		获取Cookie
			request.COOKIES['key']
			request.get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)
			参数：
				default: 默认值
				salt: 加密盐
				max_age: 后台控制过期时间 如果没有设置的话默认cookie 关闭浏览器就失效
		设置Cookie
			rep = HttpResponse(...)
			rep ＝ render(request, ...)

			rep.set_cookie(key,value,...)
			rep.set_signed_cookie(key,value,salt='加密盐', max_age=None, ...)
			参数：
				key, 键
				value='', 值
				max_age=None, 超时时间
				expires=None, 超时时间(IE requires expires, so set it if hasn't been already.)
				path='/', Cookie生效的路径，/ 表示根路径，特殊的：根路径的cookie可以被任何url的页面访问
				domain=None, Cookie生效的域名
				secure=False, https传输
				httponly=False 只能http协议传输，无法被JavaScript获取（不是绝对，底层抓包可以获取到也可以被覆盖）
		删除Cookie
			def logout(request):
				rep = redirect("/login/")
				rep.delete_cookie("user")  # 删除用户浏览器上之前设置的usercookie值
				return rep

Session		
	Session的由来
		cookie最大支持4096字节,以及保存在客户端本地不安全
		session 将私密信息能以超过4096的限制保存在服务器,
	Session的工作原理
		因为html的无状态性,为了辨识访问者,还是需要基于cookie
		服务器为每个cookie分配一个唯一id,然后在服务器端可以为此id保存信息
	Django 中的 Session的相关方法	
		# 获取、设置、删除Session中数据
		request.session['k1']
		request.session.get('k1',None)
		request.session['k1'] = 123
		request.session.setdefault('k1',123) # 存在则不设置
		del request.session['k1']

		# 所有 键、值、键值对
		request.session.keys()
		request.session.values()
		request.session.items()
		request.session.iterkeys()
		request.session.itervalues()
		request.session.iteritems()

		# 会话session的key
		request.session.session_key

		# 将所有Session失效日期小于当前日期的数据删除
		request.session.clear_expired()

		# 检查会话session的key在数据库中是否存在
		request.session.exists("session_key")

		# 删除当前会话的所有Session数据
		request.session.delete()
		　　
		# 删除当前的会话数据并删除会话的Cookie。
		request.session.flush() 
			这用于确保前面的会话数据不可以再次被用户的浏览器访问
			例如，django.contrib.auth.logout() 函数中就会调用它。

		# 设置会话Session和Cookie的超时时间
		request.session.set_expiry(value)
			* 如果value是个整数，session会在些秒数后失效。
			* 如果value是个datatime或timedelta，session就会在这个时间后失效。
			* 如果value是0,用户关闭浏览器session就会失效。
			* 如果value是None,session会依赖全局session失效策略。
		
		
		