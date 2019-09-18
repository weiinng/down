## GitBook安装

安装`GitBook`其实很简单，前提是你的机器已经有了`Node.js`环境。
全局安装：

```
npm install gitbook-cli -g
```

这个执行完毕之后

```
gitbook -v
```

可以查看到gitbook版本，就表示安装成功。



## GitBook常用命令

```javascript
gitbook init  //初始化目录文件
gitbook help  //列出gitbook所有的命令
gitbook --help  //输出gitbook-cli的帮助信息
gitbook build  //生成静态网页
gitbook serve //生成静态网页并运行服务器
gitbook build --gitbook=2.0.1 //生成时指定gitbook的版本, 本地没有会先下载
gitbook ls //列出本地所有的gitbook版本
gitbook ls-remote //列出远程可用的gitbook版本
gitbook fetch 标签/版本号 //安装对应的gitbook版本
gitbook update //更新到gitbook的最新版本
gitbook uninstall 2.0.1 //卸载对应的gitbook版本
gitbook build --log=debug //指定log的级别
gitbook builid --debug //输出错误信息
```

> 基本也就是上线的操作命令，常用的就是前面的6个了。 

在执行完gitbook init后，会给自动生成一个模板，剩下的就是修改模板为你自己的文章了。 

gitbook serve这个可以在本地生成预览。本地启动http://localhost:4000即可预览。 
当然写文章不只是为了自己看，需要分享出去，这里就需要gitbook build了，执行完gitbook build之后，目录下面会生成一个_book这里就是生成的静态网页资源，里面有个index.html，这个是网站的入口。

## 阿里云服务器部署GitBook

想在阿里云服务器上面部署GitBook，前提是你的阿里云服务器已经安装了GitBook。

其他服务器也是同样情况。 
上面说了gitbook build之后，目录下面会生成一个_book这里就是生成的静态网页资源，里面有个index.html，这个是网站的入口。在这个之前先看看《Nginx部署静态网页》。我用GitBook生成的书也是用Nginx部署的。 
在/etc/nginx/sites-enabled的目录下面，新建一个.conf格式的文件api_gitbook.conf。文件里面的代码如下：

```javascript
server {
      listen 4000;
      server_name localhost;
      location / {
           root /home/apibook/_book;
           index index.html;
           try_files $uri $uri/ =404;
      }
}
```

- listen  后面是指定的端口号
- root 后面指向的是你_book 的路径位置
- index  指的是启动页

先 ps -ef | grep nginx ,会出现5个关于nginx的进程，如果5个进程的id分别为 100、101、102、103、104

杀掉所有nginx进程 kill -9 101 102 103 104

进入目录 cd /usr/sbin

重启 nginx -c /etc/nginx/nginx.conf



这样我们就可以远程访问使用`GitBook`制作的书了,前提是你的服务器的安全组开放了4000端口。 
比如：`http://云服务器IP地址:4000`

拓展：

>启动nginx的时候也可以 cd /usr/sbin,然后直接 nginx , 
>(-c 配置文件，表示根据指定文件启动，如果该配置文件和安装的nginx命令不是一个版本，会报错) 
>启动后，nginx -t 可以查看是根据那个配置文件启动的，所以建议linux系统里只保留一个nginx.conf文件， 
>以免出现冲突，一般nginx.conf在两个位置，分别是/usr/local/nginx/conf/nginx.conf和/etc/nginx/nginx.conf



## 如何将win文件上传到云服务

### 方法一：使用工具

使用`FileZilleClient`工具。

打卡工具填写：

- 主机 == 云服务公网IP
- 用户名 == 用户名比如ROOT
- 密码 == 云服务器的密码
- 端口 == 22

将需要上传的文件拖拽到指定目录



