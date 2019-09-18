虚拟环境 
	"""
	命令行创建
	"""
		
		"""
		下载组件
		"""
		pip3 install virtualenv
	
	
		"""
		创建虚拟环境
		"""
		virtualenv env1  --no-site-packages
	
		"""
		激活虚拟环境
		"""
		activate 
		
		"""
		退出虚拟环境
		"""
		deactivate
		
		
	"""
	pychram 创建
	"""
	
		"""
		创建项目的时候选择 虚拟环境 
		
			可以对是否使用当前环境第三方包进行确认
			
			不使用则创建为纯净环境 
		"""