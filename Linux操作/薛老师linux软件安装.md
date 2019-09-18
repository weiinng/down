[TOC]

# 安装anocanda

wget  https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
安装：
bash Anaconda3-4.4.0-Linux-x86_64.sh
（提示错误可执行：yum install -y bzip2）

**添加环境变量**

vim /root/.bashrc

export PATH="/root/anaconda3/bin:$PATH"

export PATH="/root/anaconda3/bin/python:$PATH"

保存后，使用
source /root/.bashrc

------

如果有python2与python3并存问题，可修改软链接来处理：

mv  /usr/bin/python /usr/bin/python.bak
ln -s /usr/local/python3/bin/python3 /usr/bin/python
mv /usr/bin/pip /usr/bin/pip.bak
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip
验证：python，会出python3
验证：pip，会调用pip3

# Linux安装Mysql数据库服务

| 解释       | 命令                               |
| ---------- | ---------------------------------- |
| 安装服务端 | yum install mysql-community-server |
| 启动       | service mysqld start               |
| 停止       | service mysqld stop                |

> CentOS下自带mariadb    可以通过下面命令删除

```
yum remove mariadb-libs.x86_64
```

> 下载Mysql57的源文件

```
cd /
cd tmp
wget https://repo.mysql.com/mysql57-community-release-el7-8.noarch.rpm
```

> 安装Mysql57

```
yum localinstall mysql57-community-release-el7-8.noarch.rpm
```

> 安装数据库服务

```
yum install mysql-community-server
```

> 启动数据库

```
service mysqld start
```

> 停止数据库

```
service mysqld stop
```

# Linux网络连接

ifconfig

ip addr

cd /

cd /etc/sysconfig/newwork-scripts/ifcfg-xxx

```
将最后一行的 no 修改为 yes
i 修改
Esc 退出
：wq 保存退出
```

  

配置完成后关闭客户机

编辑-->虚拟网络编辑器-->还原默认设置

vi /etc/resolv.conf         （添加nameserver114.114.114.114）

service network restart    重启网络服务

yum provides ifconfig      安装ifconfig

yum install net-tools

> ifcfg-xxx     的配置文件内容   提供参考不做修改

```
DEVICE=eth0                              // 装置名称
BOOTPROTO=none                    // 启动引导协议
ONBOOT=yes                             // 启动加载
IPADDR=192.168.1.200              // IP地址                              若无，手动添加
NETMASK=255.255.255.0          // 网络掩码；子网掩码          若无，手动添加
BROADCAST=192.168.1.255      // 
GATEWAY=192.168.1.1              // 网关            若无，手动添加
TYPE=Ethernet
PREFIX=24
DNS1=192.168.1.1          // DNS ，如果桥接配置下，无DNS，无法连接Inernet。 若无，需手动添加。
DEFROUTE=yes           //这个需要打开
IPV4_FAILURE_FATAL=yes
IPV6INIT=no
NAME="System eth0"
UUID=5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03
LAST_CONNECT=1437140517
```

# l-修改密码

```
service mysqld start    //启动数据库服务
第一次启动过程中
ps -ef |frep mysql                  //这条命令查看是否存在Mysql服务  
```

> 查看mysql 密码

```
cat /var/log/mysqld.log |grep "password" 
```

> 修改mysql数据库密码

```
cat /var/log/mysqld.log |grep "password"      //首先查看mysql数据库密码并赋值
mysql -u root -p              //进入数据库
password                         //输入密码
set password = password("123456");          //修改密码为123456
	- 如果显示 OK 证明修改密码成果
	- 如果提示 Your password does not satisfy the current policy requirements
	- 他的意思是告诉你你密码不符合当前策略要求
set global validate_password_policy=0;       //密码安全策略为0
set global validate_password_length=1;        //密码长度为1
alter user 'root'@'localhost' password expire never;  //root密码永不过期
flush privileges;                 //重新加载权限列表
set password = password("123456");          //修改密码为123456
 - 这时候就可以成功了
exit;        //退出
 - 可以尝试使用新的密码重新登陆
```

# Linux系统下使用虚拟环境

> 安装虚拟环境的包

```
pip3 install virtualenv
```

> 创建虚拟环境的软连接

```
ln -s /usr/local/python3/bin/virtualenv /usr/bin/virtualenv
```

> 创建虚拟环境

```
virtualenv -p /usr/bin/python3 xxxxx         
```

> 进入虚拟环境

```
source bin/activate
```

> 退出虚拟环境

```
deactivate
```

# Atom的使用方法

> 汉化
>
> - 打开 packages –setting views–open 
> - 点击install 输入包名simplified-chinese-menu搜索并安装 
> - 汉化成功！

# Linux-Webbench压力测试工具安装

下载            cd 到tmp目录

```
wget http://home.tiscali.cz/~cz210552/distfiles/webbench-1.5.tar.gz
```

解压

```
tar -zxvf ./webbench-1.5.tar.gz
```

安装编译环境

```
yum install -y gcc ctags
```

编译

```
cd ./webbench-1.5
make && make install
make clean
```

如果遇到以下问题：        ps:这是给你参考的要去运行

```
install: cannot create regular file '/usr/local/man/man1': No such file or directory
make: *** [install] Error 1
```

网上解决方法：

```
mkdir /usr/local/man
```

但是我发现`man`目录是存在的，那问题只可能是权限了,修改好权限，问题解决。

```
chmod 777 /usr/local/man
```

### Webbench压力测试工具使语法

```
webbench [option]... URL
  -f|--force               Don't wait for reply from server.
  -r|--reload              Send reload request - Pragma: no-cache.
  -t|--time <sec>          Run benchmark for <sec> seconds. Default 30.
  -p|--proxy <server:port> Use proxy server for request.
  -c|--clients <n>         Run <n> HTTP clients at once. Default one.
  -9|--http09              Use HTTP/0.9 style requests.
  -1|--http10              Use HTTP/1.0 protocol.
  -2|--http11              Use HTTP/1.1 protocol.
  --get                    Use GET request method.
  --head                   Use HEAD request method.
  --options                Use OPTIONS request method.
  --trace                  Use TRACE request method.
  -?|-h|--help             This information.
  -V|--version             Display program version.
```

这里time和clients比较重要，

- time是benchmark持续多久

- clients是指time时间内请求多少次。

  比如我们测试百度, 启动100个客户端同时请求百度首页，持续60S：

```
webbench -t 60 -c 100 http://www.baidu.com/
```

运行结果

```
Webbench - Simple Web Benchmark 1.5
Copyright (c) Radim Kolar 1997-2004, GPL Open Source Software.

Benchmarking: GET http://www.baidu.com/
100 clients, running 60 sec.

Speed=2643 pages/min, 5045450 bytes/sec.
Requests: 2641 susceed, 2 failed.
```

ps:网上荡下来的未亲测，如有问题请找即使联系作者。



# Django Nginx+uWSGI 安装配置

链接：🔗

<https://www.runoob.com/django/django-nginx-uwsgi.html>

>yum  update
>
>yum install gcc 
>
>pip  install  uwsgi

~~~
查看uwsgi动态链接库是否有问题：
which  uwsgi
ldd /root/anaconda3/bin/uwsgi
发现:libicui18n.so.58 => not found
     libicuuc.so.58 => not found
     libicudata.so.58 => not found
通过 LDD 发现 uwsgi 找不到三个包（具体就是 not found 的三个）
于是就把anaconda3/lib 下相应的包软链到/lib64下去（64bit 机器，如果时32bit 机器则软链到/lib下）

[root@localhost ~]# ln -s /root/anaconda3/lib/libicui18n.so.58 /lib64/libicui18n.so.58
[root@localhost ~]# ln -s /root/anaconda3/lib/libicuuc.so.58 /lib64/libicuuc.so.58
[root@localhost ~]# ln -s /root/anaconda3/lib/libicudata.so.58 /lib64/libicudata.so.58
运行uwsgi:发现还有问题
于是：
    把libstdc++.so.6.0.24拷贝到/lib64目录下。
      cp /root/anaconda3/lib/libstdc++.so.6.0.25 /lib64/
    删除原来的libstdc++.so.6符号连接。
      rm -fr /lib64/libstdc++.so.6
    新建新符号连接。
      ln -s /lib64/libstdc++.so.6.0.25 /lib64/libstdc++.so.6
    再次执行uwsgi查看结果符合就哦了。
~~~

~~~python
测试：创建index.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]

uwsgi --http :9090 --wsgi-file index.py
浏览器访问9090端口
~~~

###### 添加并发

```python
uwsgi --http :9090 --wsgi-file index.py --processes 4 --threads 2
```

###### 部署 Django

~~~python
#在项目中创建djangospider.ini
[uwsgi]
# 使用Nginx做反向代理时使用socket
#socket=127.0.0.1:8080
# 不通过Nginx反向代理，直接做web服务器时使用http
http = 0.0.0.0:8000
#项目目录
chdir = /usr/www/DjangoSpider/
wsgi-file = DjangoSpider/wsgi.py
processes = 4
threads = 2

#django项目setting中
ALLOWED_HOSTS = [] 改为
ALLOWED_HOSTS = ['*']

启动：uwsji --ini  djangospider.ini
~~~



~~~python

在www中创建uwsgi文件夹，用来存放uwsgi相关文件
#### 启动： 
uwsgi --ini xxx.ini
#### 重启：
uwsgi --reload xxx.pid
#### 停止：
uwsgi --stop xxx.pid
~~~

# 配置Nginx

![img](assets/20181226194100326.png) 

**nginx服务器安装：**

~~~
下载对应当前系统版本的nginx包(package)
# wget  http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm

建立nginx的yum仓库
# rpm -ivh nginx-release-centos-7-0.el7.ngx.noarch.rpm

下载并安装nginx
# yum install -y nginx

启动nginx服务
systemctl restart nginx
验证：直接请求IP，可见nginx

配置
默认的配置文件在 /etc/nginx 路径下，使用该配置已经可以正确地运行nginx；如需要自定义，修改其下的 nginx.conf 等文件即可。


查看是否启动：（如果有master和worker两个进程证明启动成功）
ps -ef | grep nginx

停止(建议用quit，不建议用stop)
nginx -s quit

重新加载配置文件
nginx -s reload

默认配置文件位置：
/etc/nginx/conf.d/default.conf
备份默认配置文件：
cp  /etc/nginx/conf.d/default.conf   /etc/nginx/conf.d/default.conf.bak

welcome所在位置（默认值：/usr/share/nginx/html/）
~~~



**修改nginx配置文件：**

~~~
# 负载均衡
upstream upstream1 {
    server 127.0.0.1:8000;  # 处理相同业务的多个服务器 (负载均衡)
}
server {
    listen       80;
    server_name  localhost;   # 对外部用户提供的统一域名

    # 将动态请求转发给uwsgi服务器
    location / {
        # 包含uwsgi请求的参数
        include uwsgi_params;
        # 转交请求给uwsgi服务器 (uwsgi服务器的ip和端口号)
        #uwsgi_pass 127.0.0.1:8000;  # 单个uwsgi服务器(不需要负载均衡)
        uwsgi_pass upstream1;
    }

    # 如果是静态资源请求就直接响应资源。
    location /static {
        # 指定静态文件存放的目录 (需要修改/usr/...目录的操作权限。 $ chmod 777 /usr)
        alias /usr/www/D_text04/static/;
    }
}
~~~

**验证：**

nginx  -s   reload   (重新加载配置文件)

请求80端口，可能出现permission 问题（办法：先关掉selinux： setenforce 0 ）

**收集Django中的静态资源：**

~~~
项目名/settings.py（项目配置，STATIC_ROOT设置收集静态资源的路径）：
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# 指定收集静态文件的路径 (需要修改/var/...目录的操作权限)
STATIC_ROOT='./static'

$ python manage.py collectstatic
~~~



# 修改yum源为阿里

1. 备份本地yum源

 mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo_bak 

2.获取阿里yum源配置文件

将https://mirrors.tuna.tsinghua.edu.cn/help/centos/  中的内容粘贴到CentOS-Base.repo

3.更新cache

yum  clean   all

 yum makecache 

4.查看

 yum -y update 