## tornado项目中实现celery异步队列发送邮件

​	消息中间件可以使用redis，但redis作为消息中间件可谓是差强人意，功能和性能上都不如Rabbitmq，所以本次使用tornado框架结合celery，同时消息中间件使用Rabbitmq来实现异步发邮件，并且使用flower来监控任务队列。 

​	实现celery就需要已经安装了RabbitMQ，安装流程查看 《Win10 下erlang及 RabbitMQ 的 安装 配置》~

​	此时安装tornado和celery，注意指定版本号 

```python
pip3 install tornado==5.1.1
pip3 install celery ==3.1
pip3 install pika ==0.9.14
pip3 install tornado-celery
pip3 install flower
```

tips：此处可以使用pip install  具体pip3和pip的区别自行百度



#### 重点：

​	需要注意一点，由于python3.7中async已经作为关键字存在，但是有的三方库还没有及时修正，导致它们自己声明的变量和系统关键字重名，所以我们要深入三方库的源码，帮他们修改async关键字为async_my，需要修改的文件夹和文件包含但不限于：

​    /site-packages/pika/adapters/libev_connection.py

​    /site-packages/celery下面的文件

​    /site-packages/kombu下面的文件夹



操作方法：将名为  替换  文件夹中的py文件替换python37中的文件即可，已经将async关键字替换为async_my

![](C:\Users\ASUS\Desktop\md用图\async替换文件目录.png)

这个是我的安装目录，根据自己的python37安装目录，找到对应的目录进行改变，将文件中的文件cv进去直接替换即可！



在tornado项目下新建一个任务队列文件task.py： 

```python
import time
from celery import Celery
# from func_tool import send_email  这种导包方法会报错 使用下面导包方式
from views.func_tool import send_email

C_FORCE_ROOT = True

celery = Celery("tasks", broker="amqp://guest:guest@127.0.0.1:5672")
celery.conf.CELERY_RESULT_BACKEND = "amqp"


@celery.task
def sleep(seconds):
    time.sleep(float(seconds))
    return seconds

# 注意：调用func_tool内的发送邮箱功能时，看自己的形参数量，要一致
@celery.task
def sendmail(email, email_content):
    send_email(email, email_content)
    return '发送邮件成功'


if __name__ == "__main__":
    celery.start()
```



然后编写服务端代码: 

注意：这里的逻辑代码，以为是将前端发送邮箱激活的接口改为此接口，不再使用原有接口，所以前端VUE也需要修改，然后API接口获取前端发送的邮箱和内容，对应形参，发送邮件。

```python
from celery import Celery
from tornado import gen
import tcelery
sys.path.append("..")
import task

# 异步任务
class CeleryHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        email = self.get_argument('email')
        u_name = self.get_argument('name')
        user_info = sess.query(User).filter(User.username == u_name).first()
        uid = user_info.id
        url = 'http://localhost:8000/getUserId?uid=' + str(uid)
        yield gen.Task(task.sendmail.apply_async, args=[email, url])
        print('ok')
        self.write('ok')
        self.finish()
```

Application.py   路由代码: 

```python
import tornado.web
from views import Index
import config


#路由 

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/celery", Index.CeleryHandler)
        ]
        super(Application,self).__init__(handlers,**config.setting)
```

程序入口代码server.py: 

（其实和原有项目比较没有改动）

```
import tornado.ioloop
import tornado.httpserver
import config
 
from application import Application
 

if __name__ == "__main__":
    print('请访问 127.0.0.1:8000')
    app = Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    # httpServer.listen(8888)
    # 绑定端口
    httpServer.bind(config.options['port'])
    # 开启5个子进程（默认1，若为None或者小于0，开启对应硬件的CPU核心数个子进程）
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()
```

**进入项目目录**，分别启动tornado服务，celery服务，以及flower服务 ：

应该是需要四个命令行......好多啊

![](C:\Users\ASUS\Desktop\md用图\启动celery服务.png)



![](C:\Users\ASUS\Desktop\md用图\启动flower.png)



正常使用前端VUE发送邮件的页面，触发后端celery接口。



进入flower在线任务监控网址：http://localhost:5555/ 

![](C:\Users\ASUS\Desktop\md用图\flower监控.png)



发现全都是SUCCESS成功，ok！

**搞定下班！**