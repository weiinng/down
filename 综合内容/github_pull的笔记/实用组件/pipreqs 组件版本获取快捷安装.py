pipreqs  组件 
帮助你查询所有需要用的组件 


"""
安装 
"""
	pip install pipreqs 


"""
切换到项目的路径下 执行查询当前文件下所需要的所有的组件

	会生成一个  requirements.txt 
"""
	pipreqs ./ -encodeing=utf-8


"""
requirements.txt 里面会有所有的组件以及版本信息
"""
	cat requirements.txt


	pip install [-r] requirements.txt 
	# pycharm 打开的时候会提示是否需要安装这些组件提示