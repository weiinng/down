## 阿里云服务器docker搭建fastDfs

之前写过了在win系统下使用docker搭建fastDfs，这篇讲一下如何在阿里云服务器部署。

* 首先在阿里云服务器上开放端口  

  阿里云首页点击控制台，在最近使用中选择云服务器ECS，跳转新的页面，点击我的资源里的云服务器，跳转实例列表页面，最右边有一个更多，选择网络和安全组里的安全组配置，点击配置规则，上面有一个添加安全组规则，添加要开放的端口。

  端口范围例子：8888/8888

  授权对象列例子：0.0.0.0/0

  * 8000	tornado或者django默认端口
  * 22122     docker fastdfs容器端口
  * 8888        nignx默认端口
  * 80             tornado端口
  * 3306         mysql端口
  * 6379         redis端口
  * 8080         vue端口

* 安装docker

  * ### 升级yum

    sudo yum update

    ### 卸载旧版本docker

    sudo yum remove docker docker-common docker-selinux docker-engine

    ### 安装依赖

    sudo yum install -y yum-utils device-mapper-persistent-data lvm2

    ### 设置源

    sudo yum-config-manager --add-repo <https://download.docker.com/linux/centos/docker-ce.repo>

    ### 安装docker

    sudo yum install docker-ce

    ### 启动服务

    sudo systemctl start docker

    ### 查看docker版本

    docker version



在docker中将fastdfs镜像下载

```python
docker pull delron/fastdfs
```





第一种：在docker容器内下载图片

​	

step1:

  使用docker镜像构建tracker容器（跟踪服务器，起到调度的作用），这里tracker服务将会自动映射到宿主机上 

```python
docker run -d --network=host --name tracker -v /root:/var/root delron/fastdfs tracker
```

step2:

使用docker镜像构建storage容器（存储服务器，提供容量和备份服务），这里storage容器需要依赖tracker服务，传入你的tracker服务的ip地址，端口默认是22122，ip地址也就是你宿主机的ip 

这里的172.16.187.153是服务器centos的ip地址  通过ipconfig即可查看

```python
docker run -d --network=host --name storage -e TRACKER_SERVER=172.16.187.153:22122 -v /root:/var/root -e GROUP_NAME=group1 delron/fastdfs storage
```

此时，命令行输入 docker ps 就可以看到两套服务都已经启动 

step3:

进入正在后台运行的storage容器

 ```python
docker exec -it storage /bin/bash
 ```

随便下载一张图片,这个不用担心，因为在容器中如果不提交仓库的话，该图片是不会保存的 

```
wget https://v3u.cn/v3u/Public/images/logo.png
```

将该图片通过命令上传到分布式系统中 

```
/usr/bin/fdfs_upload_file /etc/fdfs/client.conf logo.png
```

这时该图片已上传至文件系统，并在执行该语句后返回图片存储的网络地址 



最后通过浏览器访问以下存储在Fastdfs的图片，这张图片是通过nginx代理的静态资源，默认nginx监听8888端口，所以需要加上端口号，如果是在阿里云上部署，则需要暴露外部端口8888 



注意：此时查看访问图片的IP地址是自己阿里云服务器提供的  **公**  IP + 8888







第二种：在容器外部上传图片文件



step1：

利用docker的特性，我们知道docker 的 -v 参数，可以自动挂载宿主机的文件件到容器中去，这样宿主和容器就可以进行无障碍的文件共享，我们通过-v参数，把宿主机的root目录自动挂载到docker容器中的/var/root目录中去。



这里的172.16.187.153是服务器centos的ip地址  通过ipconfig即可查看

```python
# 创建tracker
docker run -d --network=host --name tracker -v /root:/var/root delron/fastdfs tracker

# 创建storage
docker run -d --network=host --name storage -e TRACKER_SERVER=172.16.187.153:22122 -v /root:/var/root -e GROUP_NAME=group1 delron/fastdfs storage
```

我们可以利用docker的exec命令不进入容器，直接在宿主机的环境下调用容器内的命令，因为文件夹已经共享，所以我们输入的文件目录虽然是容器中的/var/root目录，但是实际上该上传的文件就在宿主的/root目录中 。



注意：

​	1、上传的图片路径不再是/var/root/文件名  而是/tmp/nginx/nginx-1.12.2/logo.png  这个就要自己进入容器查看一下决定，可能每个人不一样  使用 docker exec -it storage /bin/bash命令进入容器，进入后最左面的路径就是你要写的图片路径。

​	2、这个要上传的文件必须已经存在于你的路径下，也就是说本地要确实存在这个图片或者视频等文件，否则会报错。



```
docker exec -i storage /usr/bin/fdfs_upload_file /etc/fdfs/client.conf /tmp/nginx/nginx-1.12.2/logo.png
```

上传成功后，fastdfs将会网络地址 

然后在服务器访问即可，参照上一种的方法！