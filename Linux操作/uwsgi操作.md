

# linux 安装uwsgi

### 安装并查看版本

- yum groupinstall "Development tools"

- yum install zlib-devel bzip2-devel pcre-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel

- yum install python-devel

- yum install gcc

  - 安装gcc编译器。

- pip3 install uwsgi

  - 安装uwsig可以尝试其他下载源

    ```python
    pip3 install uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider
    ```

  - 在这里我用的是pip3 这看大家用的是那种pip3 根据实际情况使用

- uwsgi --version

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
    
    >配置软连之后可以再任何地方运行 uwsgi
    
    > 再次查看版本号
    
    ```python
    [root@bogon ~]# uwsgi --version
    2.0.18
    ```
  



### uwsig测试

- 普通文件测试

  - **测试uwsgi，创建test.py**

    ```python
    def application(env, start_response):
        start_response('200 OK', [('Content-Type','text/html')])
        return [b"Hello uwsgi!"]
    ```

  - **uwsgi运行该文件**

    ```python
    uwsgi --http-socket :8088 --wsgi-file test.py
    ```

- 设置uwsig.ini 启动

  - **测试uwsgi，创建test.py**

    ```python
    def application(env, start_response):
        start_response('200 OK', [('Content-Type','text/html')])
        return [b"Hello uwsgi!"]
    ```

  - **任意地方创建uwsgi.ini，内容如下：**

    ```python
    [uwsgi]
    http-socket= :8088
    chdir=/home/xlf
    wsgi-file=test.py
    ```

    > 下面是文件内配置文件的内容：

    文件里面的字段意思:
  
    - socket ：指定项目执行的端口号 
      - 用nginx的时候就配socket , 直接运行的时候配 http
    - chadir :指定项目的目录
    - module ：可以这么来理解，对于- myweb_uwsgi.ini文件来说，与它的平级的有一个partner目录，这个目录下有一个wsgi.py文件
    - master :允许主线程存在（true）
    - processes:开启的进程数量（这里是开启4个进程）
    - vacuum :当服务器退出的时候自动清理环境，删除unix socket文件和pid文件
    - 原文：<https://www.jianshu.com/p/f3fd1f831729>
  
  - **到uwsgi.ini目录下**
  
    执行 uwsgi --ini ./uwsgi.ini

