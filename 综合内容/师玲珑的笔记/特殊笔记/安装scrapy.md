python3.6 pip安装twisted 出现报错：error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-buil

d-tools



解决方法：






1，下载相应版本的whl文件:http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted

Twisted-18.4.0-cp36-cp36m-win_amd64.whl     

(我认为：cp36表示python36)






2、安装whl


pip install Twisted-18.4.0-cp36-cp36m-win_amd64.whl
至此Twisted已经安装成功



之后再pip install Scrapy


在pip install pypiwin32