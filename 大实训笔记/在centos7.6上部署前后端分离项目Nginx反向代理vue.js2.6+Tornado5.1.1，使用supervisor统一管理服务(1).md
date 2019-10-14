# 在centos7.6上部署前后端分离项目Nginx反向代理vue.js2.6+Tornado5.1.1，使用supervisor统一管理服务

## Vue打包

部署前端，将测试好的vue.js2.6项目打包，值得一提的是，在生产环境并不需要node.js服务，因为利用vue.js的特性可以对前端页面进行打包，使其成为一个纯静态页包，上线后利用nginx对其代理即可，既方便又安全。在项目目录下执行npm run build命令，在执行之前，先把conifg目录下index.js中的bulid配置../dist改成./dist 



* Vue项目根目录下，有一个config文件夹，打开index.js文件。

  tips：dev是开发模式，不要动， 如使用命令 npm run dev就是启动的开发模式

  ​	我们们修改build中的配置（不修改可能会造成白版）

  ​	![](C:\Users\ASUS\Desktop\md用图\build配置.png)



修改为如下：

```python
index: path.resolve(__dirname, './dist/index.html'),

    // Paths
    assetsRoot: path.resolve(__dirname, './dist'),
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',
```

因为项目打包时，找静态页配置文件，css样式等是同级的，所以改为同级。

当我们执行npm run build时，整个vue中所有的服务，所有的组件，所有的网页全部打包转换成静态页面，  这个静态页的位置就是和配置文件同级的  dist文件夹，全部打包到dist文件夹中。这个文件夹可以写进.gitignore中，不需要每次上传代码时上传版本库，随时可能修改。 

![](C:\Users\ASUS\Desktop\md用图\修改gitignore.png)

将dist前面的/去掉！



* ```python
  # 进入vue项目
  cd nvue
  # 执行打包
  npm run build
  ```

  ![](C:\Users\ASUS\Desktop\md用图\打包vue.png)

  ​	![](C:\Users\ASUS\Desktop\md用图\打包vue1.png)



```python
cd config 

dir 

# 可以看到dist文件  说明打包成功
```

![](C:\Users\ASUS\Desktop\md用图\查看是否打包成功.png)

```python
cd dist 

dir 
# 可以看见index.html 打包很方便 便捷

```

![](C:\Users\ASUS\Desktop\md用图\打包查看.png)



执行hs命令，启动测试网页服务

![](C:\Users\ASUS\Desktop\md用图\hs.png)

如果提示hs不是内部或外部命令，下载hs即可。

```python
npm install http-server -g
```

可以看到服务已经启动在8080端口。



**访问页面，如果无法访问就使用命令**

```python
python -m http.server
```

可以看到页面说明，只是打包成功了~~，接下来继续。



tips：

​	如果在vue项目中进行了修改，name就需要重新打包，使用最新的代码。

​	vue项目中所有的a标签和cookie都要修改，a超链接改为router-link ，cookie使用local storage。



## 部署前端

将我们刚刚打包的dist文件夹上传到服务器的root目录下，目前有两种方式：	

* 1、使用MobaXterm工具，在左侧可以看见服务器的目录，直接将dist文件夹直接用鼠标拖入到root目录下即可，但是这个方法存在一个问题就是每次更新代码都需要再次打包，再次上传一次。

* 2、在服务器安装Git，使用Git命令四步即可完成。

  ```python
  git add .
  
  git commit -m ''
  
  git push 
  
  
  git pull
  ```

使用哪种方法都可以，上传完以后，我们使用命令对vue项目文件进行授权

```python
chmod 755 /root/dist
```

然后在服务器安装nginx

```
#设置源
sudo rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm

#安装
yum install -y nginx

#启动服务
systemctl start nginx.service
```

注意：需要在服务器上开放80端口，nginx默认端口为80！

访问服务器的IP，查看是否nginx在欢迎我们！

![](C:\Users\ASUS\Desktop\md用图\nginx欢迎.png)

如果可以看到nginx的欢迎说明没什么问题了。接下来进行配置：

修改nginx配置文件，这里前端服务默认监听80端口 

```python
vim /etc/nginx/conf.d/default.conf 
# vim提示如下
i # 进入编辑模式

# 将配置信息粘贴进去
:wq  # 保存退出
```

题外话：Vim真的很好用，自行百度学习！！！

将内容全部替换为如下配置：

```
server {
    listen       80;
    server_name  localhost;

    access_log      /root/md_vue_access.log;
    error_log       /root/md_vue_error.log;


    client_max_body_size 75M;


    location / {

        root /root/dist;
        index index.html;
        try_files $uri $uri/ /index.html;

    }
    
    error_log    /root/dist/error.log    error;

}
```

```python
# 继续修改配置
vim /etc/nginx/nginx.conf
# 将第一行改为 
user root
```

 ![](C:\Users\ASUS\Desktop\md用图\修改配置.png)

修改完毕重新启动nginx服务

```python
systemctl reload nginx.service
```

**注意：每次更改完配置信息，都需要重新启动才会生效！**

现在我们再访问我们的服务器IP，就可以看见我们打包上线的Vue页面了。

![](C:\Users\ASUS\Desktop\md用图\Vue部署成功.png)

进行到了这步，说明我们的前端部署已经没有问题了，全部完成！

（因为后端还没有部署，所以静态图片不会加载显示。）



## 部署后端

首先安装python3，需要注意的是centos自带python2.7，当装软件的时候千万不要影响这个python2.7，因为系统很多东西都依赖python2，所以我们只要python2和python3共存就可以了 。

**也就是说：自带的python2.7不能动！！！不能删！！！**

```python
yum install epel-release

yum install python36

wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py

python3 get-pip.py

pip3 install pymysql

pip3 install pillow

pip3 install pycryptodome

pip3 install tornado==5.1.1

pip3 install sqlalchemy
```

将tornado项目上传到/root/mytornado下 

```python
# 进入root目录
cd /root
# 创建mytornado文件夹
mkdir mytornado
```

然后将tornado项目上传，上面介绍了两种方法，自行选择（Git是真快真方便）

修改项目权限 

```python
chmod -R 755 /root/mytornado 
```

需要将tornado项目的debug模式关闭，并且修改端口为8001，同时阿里云开放8001端口 

```python
# 因为上面已经给了项目权限，所以直接vim进入修改即可
cd /root/mytornado/tornado
# 编辑修改config.py
vim config.py
```



![](C:\Users\ASUS\Desktop\md用图\config修改.png)

进入到tornado项目，执行命令，启动项目，访问服务器IP:8001查看

<http://118.31.19.173:8001/> 

![](C:\Users\ASUS\Desktop\md用图\服务器启动tornado.png)

（运行项目提示错误，根据错误解决就行，一般都是缺少模块，pip install 即可！）



此时：存在一个问题，因为是新部署的项目，所以mysql数据库并没有数据。那么我们使用spl脚本传输，详情看



**《阿里云服务器部署——mysql数据库数据迁移》**



可以看见我们的tornado项目正常运行了，那么下面进行nginx代理的配置。

## nginx代理

修改nginx配置文件，用nginx对tornado进行反向代理，新建一个配置文件 。

```python
vim /etc/nginx/conf.d/tornado.conf
```

```python
# 将这些配置粘贴进去
upstream tornado {
    server 127.0.0.1:8001;
}

server {
    listen   8000;
    root /root/mytornado;
    index server.py index.html;

    server_name server;

        # 静态文件直接由Nginx处理
    location /static/{
        alias /root/mytornado/static/;
        expires 24h;
    }
    location /{
        proxy_pass_header Server;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        # 把请求方向代理传给tornado服务器，负载均衡
        proxy_pass http://tornado;
    }

}
```

解读：该配置的意思就是由nginx监听8000端口，并且将请求反向代理至tornado服务，这里我们只起了一个8001的服务，还可以启动更多，这就是传统意义上的负载均衡 。



重启nginx

```
systemctl restart nginx.service
```

访问服务器的8000端口，阿里云也别忘了开放一下8000 ！

发现项目也正常显示，说明nginx代理成功！



## supervisor 

每次手动在命令行启动应用是比较麻烦的，我们还需要一个能够方便的管理服务进程的工具，包括自动重启进程等，而Supervisor的作用在这里就可以体现了。我们使用它来管理这个Tornado web server相关的进程 。

安装supervisor

```
yum install epel-release
yum install -y supervisor
```



生成配置文件

```
supervisord -c /etc/supervisord.conf 
```



修改配置文件

 ```python
vim /etc/supervisord.conf   
 ```

将下面几行的注释解开

```
[inet_http_server]         ; inet (TCP) server disabled by default
port=*:9001        ; (ip_address:port specifier, *:port for all iface)
username=user              ; (default is no username (open server))
password=123               ; (default is no password (open server))
```

![](C:\Users\ASUS\Desktop\md用图\supervisor配置修改.png)

解读：将web服务页面打开，需要注意ip地址要写*，否则外网访问不了 

​	username和password登录服务页面的用户名和密码 ，自己记号会用到！

​	阿里云开放9001端口。



然后在配置文件末尾加上tornado的配置 

![](C:\Users\ASUS\Desktop\md用图\supervisor中tornado配置.png)

**注意：配置里面server.py文件的位置要根据自己的修改！！！！！！！！！！**

```
[program:mytornado]
command=python3 /root/mytornado/tornado/server.py --port=8001
directory=/root/mytornado
autorestart=true
redirect_stderr=true
```

 

需要注意的是，当修改了supervisor的配置，想要生效就得重启supervisor服务，终止服务命令是： 

```
killall -s INT /usr/bin/python
```

因为supervisor是基于python2的，所以不用担心python3的进程 



启动supervisor服务 

```
supervisord -c /etc/supervisord.conf
```



此时，将刚刚手动启动的tornado服务关闭，然后访问服务器的9001端口，用配置文件中的账号和密码登录 

![](C:\Users\ASUS\Desktop\md用图\supervisor监管服务.png)

 这样就可以在管理页面中控制tornado服务了，同时supervisor还赋予了守护进程模式，方便服务拉起 。





如果只想在命令行中控制tornado也是可以的 

```
#停止tornado服务
supervisorctl stop mytornado

#启动tornado服务
supervisorctl start mytornado
```

至此，我们通过nginx反向代理tornado负载均衡，并且通过supervisor管理就部署好了，简直太简单了 。