# 利用Docker来搭建分布式文件系统FastDfs

对于文件存储来说，一般情况下简单的处理就是在Django配置文件中配置存储目录，按照规则对文件进行上传或者下载。

​    实际上，当文件较少的时候，Django是可以应付的过来的。但当文件以海量形式出现的时候，Django就并不是那么好用了，于是Fast DFS应运而出。

​        FastDFS是一个开源的分布式文件系统，它对文件进行管理，功能包括：文件存储、文件同步、文件访问（文件上传、文件下载）等，解决了大容量存储和负载均衡的问题。特别适合以文件为载体的在线服务，如相册网站、视频网站等等。可以说它就是为互联网而生，为大数据而生的。

​    FastDFS服务端有两个角色：跟踪器（tracker）和存储节点（storage）。跟踪器主要做调度工作，在访问上起负载均衡的作用。 存储节点存储文件，完成文件管理的所有功能：存储、同步和提供存取接口，FastDFS同时对文件的meta data进行管理。跟踪器和存储节点都可以由多台服务器构成。跟踪器和存储节点中的服务器均可以随时增加或下线而不会影响线上服务。其中跟踪器中的所有服务器都是对等的，可以根据服务器的压力情况随时增加或减少。

 说人话，为啥要用FastDfs:

​    1 解决海量存储，同时存储容量扩展方便。
​    2 解决文件内容重复,如果用户上传的文件重复(文件指纹一样)，那么系统只有存储一份数据，值得一提的是，这项技术目前被广泛应用在网盘中。
​    3 结合Nginx提高网站读取图片的效率。

如果我们从头搭建fastdfs服务器那么就太low了，网上有大把的docker镜像供你选择，所以又到了利用docker优越性的时候了，首先下载fastdfs镜像

> 拉去 docker 镜像

```
docker pull delron/fastdfs
```

> 使用命令查看镜像信息

```
docker images
```

区区四百多兆就承载了nginx和fastdfs服务

> 然后使用docker镜像构建tracker容器（跟踪服务器，起到调度的作用），这里tracker服务将会自动映射到宿主机上

```
docker run -d --network=host --name tracker -v /root:/var/root delron/fastdfs tracker
```

> 使用docker镜像构建storage容器（存储服务器，提供容量和备份服务），这里storage容器需要依赖tracker服务，传入你的tracker服务的ip地址，端口默认是22122，ip地址也就是你宿主机的ip

```bsh
docker run -d --network=host --name storage -e TRACKER_SERVER=192.168.99.100:22122 -v /root:/var/root -e GROUP_NAME=group1 delron/fastdfs storage
```

此时，命令行输入 docker ps 就可以看到两套服务都已经启动

```
docker ps
```

------

$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS           NAMES
b9108588d995       delron/fastdfs   "/usr/bin/start1.sh …"   2 hours ago         Up 2 hours                   storage
ded1b0f84fe1        delron/fastdfs    "/usr/bin/start1.sh …"   2 hours ago         Up 2 hours                        tracker

------

> 这时，进入正在后台运行的storage容器

```
docker exec -it storage /bin/bash
```

> 随便下载一张图片,这个不用担心，因为在容器中如果不提交仓库的话，该图片是不会保存的

```bsh
wget https://v3u.cn/v3u/Public/images/logo.png
```

> 将该图片通过命令上传到分布式系统中

```bsh
/usr/bin/fdfs_upload_file /etc/fdfs/client.conf logo.png
```

> 这时该图片已上传至文件系统，并在执行该语句后返回图片存储的网络地址

[root@default nginx-1.12.2]# /usr/bin/fdfs_upload_file /etc/fdfs/client.conf logo.png
group1/M00/00/00/wKhjZF1U3kqAQzbGAAAS9iNyoDo996.png

> 打开浏览器访问：

```
https://192.168.99.100:8888/group1/M00/00/00/wKhjZF1U3kqAQzbGAAAS9iNyoDo996.png
```

> 可以看到，没有任何问题，同理，如果是视频资源，同样可以上传到fastdfs中，搞定收工。

