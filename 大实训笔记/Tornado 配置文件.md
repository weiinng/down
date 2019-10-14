# Tornado 配置文件

config.py 配置文件 

```
import os

BASE_DIRS = os.path.dirname(__file__)


#参数
options = {
    'port':8000,
}

#配置
setting = {
    'static_path':os.path.join(BASE_DIRS,'static'),
    'template_path':os.path.join(BASE_DIRS,'templates'),
    'debug':True,
    # 'autoreload':True
}
```

路由文件 application.py: 

```
import tornado.web
from views import Index
import config


#路由 

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", Index.IndexHandler),
            (r"/tem", Index.MainHandler),
        ]
        super(Application,self).__init__(handlers,**config.setting)
```

程序入口 server.py:

```
import tornado.ioloop
import tornado.httpserver
import config

from application import Application


if __name__ == "__main__":
    print('启动...')
    app = Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    # httpServer.listen(8888)
    #绑定端口
    httpServer.bind(config.options['port'])
    #开启5个子进程（默认1，若为None或者小于0，开启对应硬件的CPU核心数个子进程）
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()
```

views下写视图类 比如

```
class IndexHandler(BaseHandler):
	def get(self, *args, **kwargs):
        self.write("Hello, world123")
        #self.finish({'name':'你好'})
```

upfile文件下放上传的文件，templates下放模板，static下放静态文件/css，/js，/img

这就是一个tornado的一个扁平化项目结构

运行服务

```
python server.py
```