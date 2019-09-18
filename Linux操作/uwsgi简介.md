# nginx和uwsgi的区别和作用：

Django+uwsgi+nginx

nginx和uwsgi的区别和作用：

1, nginx是对外的服务器，外部浏览器通过url访问nginx, uwsgi是对内的服务器，主要用来处理动态请求。

2, nginx接收到浏览器发送过来的http请求，将包进行解析，分析url， a.如果是静态文件请求就直接访问用户给nginx配置的静态文件目录，直接返回用户请求的静态文件， b.如果不是静态文件，而是一个动态的请求，那么nginx就将请求转发给uwsgi,

```
 uwsgi接收到请求之后将包进行处理，处理成wsgi可以接受的格式，并发给wsgi,
 wsgi根据请求调用应用程序的某个文件，某个文件的某个函数，最后处理完将
 返回值再次交给wsgi,wsgi将返回值进行打包，打包成uwsgi能够接收的格式，
 uwsgi接收wsgi发送的请求，并转发给nginx,nginx最终将返回值返回给浏览器。
```

# uwsgi概念和作用

#### WSGI

WSGI是一种WEB服务器==网关接口==。 是一个Web服务器（如nginx）与应用服务器（如uWSGI）通信的一种规范（协议）。

在生产环境中使用WSGI作为python web的服务器。Python Web服务器网关接口，是Python应用程序或框架和Web服务器之间的一种接口，被广泛接受。WSGI没有官方的实现, 因为WSGI更像一个协议，只要遵照这些协议，WSGI应用(Application)都可以在任何服务器(Server)上运行。

### uWSGI

uWSGI实现了WSGI的所有接口，是一个快速、自我修复、开发人员和系统管理员友好的服务器。uWSGI代码完全用C编写，效率高、性能稳定。

uwsgi是一种线路协议而不是通信协议，在此常用于在uWSGI服务器与其他网络服务器的数据通信。uwsgi协议是一个uWSGI服务器自有的协议，它用于定义传输信息的类型。

##### 作用

Django 是一个 Web 框架，框架的作用在于处理 request 和 reponse，其他的不是框架所关心的内容。所以怎么部署 Django 不是 Django 所需要关心的。

Django 所提供的是一个开发服务器，这个开发服务器，没有经过安全测试，而且使用的是 Python 自带的 simple HTTPServer 创建的，在安全性和效率上都是不行的

而uWSGI 是一个全功能的 HTTP 服务器，他要做的就是把 HTTP 协议转化成语言支持的网络协议。比如把 HTTP 协议转化成 WSGI 协议，让 Python 可以直接使用。 
uwsgi 是一种 uWSGI 的内部协议，使用二进制方式和其他应用程序进行通信。

