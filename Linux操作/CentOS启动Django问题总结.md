# Django无法使用Sqlite3问题

**解决Nomodule named _sqlite3**

1. 服务器Centos7.4

2. Python 3.6.5

3. Scrapy 1.5.1


我在本地编写的Scrapy程序放在服务器上跑，但是在启动程序的时候遇到了，没有sqlite3模块，现在的Python版本是3.6.5。


```python
Traceback (most recent call last):
  File "/root/zhongan/.venv/lib/python3.6/site-packages/twisted/internet/defer.py", line 1418, in inlineCallbacks
    result = g.send(result)
  File "/root/zhongan/.venv/lib/python3.6/site-packages/scrapy/crawler.py", line 82, in crawl
    yield self.engine.open_spider(self.spider, start_requests)
ModuleNotFoundError: No module named 'sqlite3'
```

**解决办法**
安装sqlit-devel：yum install sqlite-devel

**还有一种方法就是不适用sqlite3直接使用mysql或者其他数据库！**





# 主机无法连接虚拟机数据库问题

问题解析：

1. 虚拟机防火墙没有关闭。
   - 解决方法
     
     - 查看是否运行
     
       > systemctl is-active firewalld.service
       >
       > ----------------------------------------------------
       >
       > systemctl status firewalld.service
     
     - 停止防火墙
     
       > systemctl stop firewalld.service
     
   - 问题原因：
   
     防火墙拒绝访问了外部连接。
   
2. mysql（mariadb）数据库没有开启允许其他主机连接的设置。

   - 解决方法：

     - 进入数据库使用以下命令。

       >GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
       >
       >flush privileges;

   - 问题原因：

     没有开启外部访问。

3. 检查主机连接的ip以及密码是否正确，可以先使用虚拟机上面的数据库是否能进去。

4. 直接关闭防火墙的方式比较粗暴，我们可以开启指定端口来控制mysql的链接。

   - 解决方法。

     - 进入虚拟机操作窗口。

       

# 启动python3的软连接问题

mv  /usr/bin/python /usr/bin/python.bak
ln -s /usr/local/python3/bin/python3 /usr/bin/python
mv /usr/bin/pip /usr/bin/pip.bak
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip
验证：python，会出python3
验证：pip，会调用pip3



# 安装uwsgi后无法使用问题

- 报错：

  ```python
  [root@bogon /]# uwsgi --version
  -bash: uwsgi: command not found
  ```

- 解决：

  > 查看位置： find / -name uwsgi

  ```python
  [root@bogon /]# find / -name uwsgi
  /usr/local/python3/bin/uwsgi
  ```

  > 配置软连接：   ps:软连接在这只作为解决方法 可能大家的python路径都不同酌情安装

  ```python
  ln -s /usr/local/python3/bin/uwsgi /usr/bin/uwsgi
  ```

  > 配置软连之后可以再任何地方运行 uwsgi

	> 再次查看版本号
  
	```python
[root@bogon ~]# uwsgi --version
2.0.18
	```

# 无法安装scrapy问题

**报错**

```python
Collecting Twisted>=10.0.0 (from scrapy)
  Could not find a version that satisfies the requirement Twisted>=10.0.0 (from scrapy) (from versions: )
No matching distribution found for Twisted>=10.0.0 (from scrapy)
```

**还有一个错误是提示版本太低的因为这是因为pip insatall twisted 安装的版本低 不能支持python3.6以上的版本 **

由于使用python3.6，因此需要下载最新的17.9.0版本，此版本已经支持python3.6

>下载对应python3.6的版本 这里直接给个链接:执行

```python
wget https://twistedmatrix.com/Releases/Twisted/17.9/Twisted-17.9.0.tar.bz2
```

>解压下载下来的Twisted-17.9.0.tar.bz2

```python
tar -xvf Twisted-17.9.0.tar.bz2
```

> 进入目录

```python
cd Twisted-17.9.0.tar.bz2
```

> 执行：

```python
python setup.py install
```

> 验证

```
pip list
```

**安装scrapy，scrapyd**

> 安装scrapy

```python
pip install scrapy
```

> 相同的道理安装scrapyd







# 报错

```python
django.core.exceptions.ImproperlyConfigured: 
Error loading MySQLdb module. Did you install mysqlclient?
```

这是错误的意思是你要不要使用mysql数据库。

- 检查是否安装了pymysql
  - 查看：pip3 pymysql
  - 安装：pip3 install pymysql

- 打开项目与setting.py同级目录的 `__init__.py`文件配置：

  ```python
  import pymysql
  pymysql.install_as_MySQLdb()
  ```



# 报错

```python
Command "python setup.py egg_info" failed with error code 1
```

报出错误为下载工具文件缺失问题：

- 解决方法：

  - 故通过https://pypi.org/simple/setuptools-scm/下载补丁setuptools_scm-3.0.6-py2.py3-noneany.whl进行解决。

  - 通过**pip install setuptools_scm-3.0.6-py2.py3-none-any.whl** 

  - 后进行**sudo pip install drf-haystack**解决

    

# 报错

```python
Error loading MySQLdb module:No module named MySQLdb
```

原因没有安装 pymysql模块

解决方法：

>pip install pymysql


