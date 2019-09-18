# 常用docker命令

> 显示版本号

```
docker --versions
```

> 显示镜像

```
docker images
```

> 保存镜像    docker save -o 路径+文件名+格式 镜像名

```
docker save -o /home/dyufei/tensorflow.tar tensorflow/tensorflow
或者 
docker save tensorflow/tensorflow > /home/dyufei/tensorflow.tar
```

> 加载镜像   docker load -i '路径+安装包.tar'

```
docker load -i tensorflow.tar
```

> 登录系统 镜像编号

```
docker run -ti 6866
docker run -it centos /bin/bash
```

> 登录系统 容器编号

```
docker run -d --privileged=true mycentos /usr/sbin/init
docker exec –it 容器编号 /bin/bash
```

> 进入虚拟机

```
docker-machine ssh
```

> 挂载共享文件夹

```
docker run -v /www:/mnt/www
```

> 查看所有容器

```
docker ps -a
```

> 删除容器

```
docker rm
```

> 后台启动服务和端口映射

```
docker run -it -d -p 8000:8000 mycentos cmd
```

> 查看宿主ip

```
docker-machine ip default

192.168.99.100
```

> 查看容器编号

```
cat /proc/self/cgroup | head -1
```

> 提交更改

```
docker commit 容器id 镜像名称
```

> 删除镜像

```
docker rmi -f 镜像ID
```

> 检查系统

```
cat /etc/redhat-release
```

> 退出镜像

```
exit
docker run -it ubuntu:rename /bin/echo "Hello World"
```

> 删除镜像缓存

```
docker ps -a | grep "Exited" | awk '{print $1 }'|xargs docker stop

docker ps -a | grep "Exited" | awk '{print $1 }'|xargs docker rm
```



## 删除镜像

**有时候做练习的时候会生成大量的容器，一个一个停用然后删除实在太没有效率了。 **

> 1、停用全部运行中的容器:

```
docker stop $(docker ps -q)
```

> 2、删除全部容器：

```
docker rm $(docker ps -aq)
```

> 3、一条命令实现停用并删除容器：

```
docker stop (docker ps -q) & docker rm (docker ps -aq)
```



​                 

1、安装docker先决条件

①必须是64位CPU架构的计算机，docker目前不支持32位的CPU

②运行Linux3.8或更高版本内核，CentOS的内核版本不能低于3.10；
③内核必须支持一种合适的存储驱动，可以是Device Manager、AUFS、vfs、btrfs、以及默认的驱动Device Mapper中的一个；
④内核必须支持并开启cgroup和命名空间namespace功能。

 

2、centos7安装docker

① Centos7安装docker非常简单，只需要：

yum install docker

systemctl start docker.service     //开启docker服务

systemctl enable docker.service    //设置为开机自动启动docker服务

 

② 不行的话再用下面步骤：

yum update

yum -y remove docker docker-common docker-selinux docker-engine //卸载旧版本

yum install -y yum-utils device-mapper-persistent-data lvm2   //设置yum源

yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo//报错是yum源问题

yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo//不行用阿里源

yum list docker-ce --showduplicates | sort -r  //查看所有仓库docker版本，并选择安装版本（此处是社区版）

yum install docker-ce      //这样写默认安装最新版本

yum install docker-ce-<VERSION_STRING>     //指定安装版本

systemctl start docker     //重启命令 systemctl restart docker

systemctl enable docker    //开机启动

docker version     //查看docker版本号

docker run hello-world   //验证是否安装成功

Docker安装参考链接：https://blog.csdn.net/qq_25838777/article/details/80491923

Docker手册参考链接：http://www.runoob.com/docker/docker-container-usage.html

 

3、docker中使用Centos7镜像

①

systrmctl start docker.service           //启动容器服务

docker pull centos:7.2.1511

docker images                             //如下图



docker run -ti 4cb /bin/bash                //4cb是IMAGE ID前3个字母，能区分是哪个image即可，不必全写

exit            //退出centos系统

docker ps -l   //最近容器查看

 

②

docker pull mysql       //获取一个叫mysql的镜像，默认从docker hub镜像仓库下载

docker images          //显示本地已经有的镜像

docker run -t -i <镜像名,如centos> /bin/bash //以centos镜像为基础创建一个容器并进入   

exit                 //退出容器

docker ps             //查看所有正在运行中的容器

 

4、docker常用命令

yum install docker        //安装服务

systemctl start docker.service   //启动服务

systemctl enable docker.service  //开机启动服务

docker pull centos      //下载映像到本地

docker run -i -t IMAGEID /bin/bash      //以交互式启动容器，其中-t指让docker分配一个伪终端并绑定在容器的标准输入上，-i让容器的标准输入保持打开

docker run --name IMAGEID -itd centos:latest   //利用镜像创建容器，其中-i表示让容器的标准输入打开，-t表示分配一个伪终端，-d表示后台启动，--name指定容器名

docker attach CONTAINERID      //进入一个已经开启的容器

docker exec -it CONTAINERID /bin/sh

docker run centos echo ‘Hello World’  

docker ps            //查看正在运行的容器  

docker ps -l   //查询最后一次创建的容器

docker ps -a   //查看所有容器

docker port <ID或者名字>  //容器信息可通过docker ps查看

docker logs -f <ID或者名字> //查看对应容器log，输出形式和tail -f一样

docker top <ID或者名字>    //查看容器内部运行进程

docker stop <ID或者名字>   //停止容器

docker start <ID或者名字>  //启动容器

docker info

docker search

docker tag      //修改标签

docker push     //上传image

docker save       //保存image

docker commit    //提交image

docker build       //编译Dockerfile文件

docker import       //将tar.gz格式的镜像文件导入docker

docker load --input image.tar.gz    //也是导入，用于删除后的恢复

docker load < image.tar.gz      //docker load命令另一种写法

docker start/stop/restart CONTAINERNAME       //启动、停止、重启容器

docker attach CONTAINERID     //进入刚刚启动的容器

docker logs <imageID>   //查看对应容器日志

docker exec -ti <containname> /bin/bash    //进入后台运行的容器

docker stop $(docker ps -a -q)    //停止所有容器

docker -rm CONTAINERID    //删除容器

docker -rm -f CONTAINERID   //强制删除容器

docker rm $(docker ps -a -q)    //删除所有容器

docker container prune    //删除所有停止的容器

docker rmi <imageID>       //删除本地镜像，删除镜像前记得停止所有该镜像的容器

docker rmi -f IMAGEID      //强制删除本地镜像

docker rmi $(docker images -q)   //删除全部image

docker image prune --force --all    //删除所有不使用的镜像

docker rename old_CONTAINERNAME new_CONTAINERNAME     //重命名一个容器

docker inspect -f '{{.Name}} - {{.NetworkSettings.IPAddress }}' $(docker ps -aq)   //获取所有容器名称及其IP地址

cat /etc/hosts     //进入容器内部后获取目前容器IP

在docker容器和宿主机之间复制文件（需要root权限）：

docker cp host_path containerID:container_path   //从宿主机复制文件到容器

docker cp containerID:container_path host_path   //从容器复制文件到宿主机

怎样退出容器但是不关闭容器：按键ctrl+p+q

5、docker常见使用场景

5.1、创建镜像

5.1.1、修改已有镜像并重新打包

docker pull training/sinatra                //下载镜像

docker images          //显示本地已经有的镜像

docker run -t -i training/sinatra /bin/bash  //打开并进入容器

gem install json      //尝试安装一些东西，下面好准备打包新的容器

exit                  //退出容器

docker commit -m ‘add json gem’ -a ‘Docker Container’ 7b789b19757d my/sinatra:v2     //这是提交命令，其中-m代表提交注释，-a代表维护者的信息，7b789b19757d代表镜像仓库的ID（容器ID，进入容器后会显示）,my/sinatra:v2代表给这个镜像命名为另外一个名字，my指所属者，sinatra指镜像名字，v2是个tag标签，注意my/sinatra代表仓库名，必须都是小写字母。

 

5.1.2、用Dockerfile创建镜像

mkdir centos         //比如先创建一个名为centos的文件夹

touch Dockerfile     //创建Dockerfile文件，注意首字母为大写

Dockerfile内容如下：

注解

FROM centos

MAINTAINER REGAN 1206274923@qq.com

RUN yum -qqy install python

其中：

FROM告诉Docker使用哪个镜像作为基础（也可以是docker images产生的对应的image ID）。

MAINTAINER是维护者信息。

RUN开头的指令会在创建中运行，例如安装一些软件包，这里使用python安装python，注意使用yum需要定制参数-qqy，不然可能会报错。注意每个命令代表镜像一层，一共不能操作127层。

 

docker build -t=’arvin/python:v1.0.2’ .   //-t参数表示添加tag，指定新的镜像的用户信息，”.”点参数很重要，代表Dockerfile在当前路径，这个参数也可以替换为具体Dockerfile的路径。

docker tag 5725c0d57443 mysql/centos:v1.0.1  //docker tag命令可以用来修改images名字和标签

 

5.2、本地导入镜像

比如本地有一个ubuntu_eml.tar.gz的镜像文件需要导入，用docker import命令：

cat ubuntu_eml.tar.gz | docker import - my/ubuntu_eml:v1.1.0

注意：这里被导入镜像的名字必须是.tar.gz或者.tar格式结尾。

docker push my/ubuntu_eml    //上传镜像，默认上传到公有仓库docker hub，其中my/ubuntu_eml用docker tag命令改为提前在docker hub创建的用户，否则上传失败。

 

5.3、保存、载入、删除镜像

docker save -o mysql.tar.gz arvin/mysql  //将名为arvin/mysql的镜像保存在当前目录，命名为mysql.tar.gz

docker rmi <imageID>       //删除本地镜像docker rmi -f 为强制删除

docker load --input image.tar.gz    //导入以tar.gz结尾的本地镜像，用于删除后的恢复

 

5.4、docker容器的创建、启动、和停止

docker run -t -i <imageID> /bin/bash   //这是一种与容器的交互方式，其中-t指让docker分配一个伪终端并绑定在容器的标准输入上，-i让容器的标准输入保持打开

docker run <imageID> cal      //查看image日历,这是另一种与容器交互方式

当执行docker run命令来启动容器，docker在后台运行的标准操作包括：

①检查本地是否存在指定的镜像，不存在则从私有仓库下载

②使用镜像创建并启动容器

③分配一个文件系统，并在只读的镜像层外面挂载一层可读可写层

④从宿主机配置的网桥接口中桥接一个虚拟接口到容器中去

⑤从地址池分配一个IP地址给容器

⑥执行用户指定的应用程序

⑦执行完毕之后容器被终止

docker stop <imageID>   //停止容器

docker ps                  //查看正再启动的容器有哪些

docker start <imageID>   //启动容器

 

守护状态运行：很多时候我们希望容器在后台以守护状态运行，此时可以添加-d参数来实现（d是daemon的首字母），例如我们启动centos后台容器，每隔一秒打印当天日历：

docker run -d centos /bin/sh -c “while true;do echo hello docker;sellp 1;done”

docker ps    //检查效果

docker logs <imageID>   //查看对应容器日志

 

5.5、docker私有仓库

5.5.1、创建私有仓库

安装并启动docker

docker run -d -p 5000:5000 --name registry registry:2

docker pull centos

docker image tag centos localhost:5000/myfirstimage

docker push localhost:5000/myfirstimage

docker pull localhost:5000/myfirstimage

docker container stop registry && docker container rm -v registry //停止registry并删除所有数据

 

docker push 172.16.1.118:5000/myfirstimage  //在另一台主机下载118主机仓库里的镜像

注意：客户机上报错：(此处举例：118为仓库服务器，117为客户机)

Get https://172.16.1.118:5000/v2/_ping: http: server gave HTTP response to HTTPS client

解决方案：打开客户机cd /etc/docker目录

vi daemon.json，写入：

{“insecure-registries”:[“172.16.1.118:5000”]}    //写完保存退出

systemctl restart docker.service    //重启docker服务生效

docker run -d -p 5000:5000 -v /opt/ata/registry:/tmp/registry registry

再push镜像成功

 

curl http://172.16.1.118:5000/v2/_catalog   //查看118主机仓库的所有镜像

 

Docker官方手册：https://docs.docker.com/registry/#requirements

 

5.6、docker共享目录

docker run -it -v /test:/soft centos /bin/bash  //启动一个centos容器，宿主机的/test目录挂载到容器的/soft目录，注意目录必须为绝对路径

 

5.7、制作docker镜像

参考链接：https://www.jb51.net/article/114023.htm

```
              https://www.cnblogs.com/zhengah/p/4935459.html
```

 

此处以制作centos6为例：

需要找一个centos6.5的系统，因为centos7已不再提供febootstrap相关包的下载了

但是centos6.5上安装docker不能直接yum install docker，具体步骤如下：

①先在centos6.5上安装docker

rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm

rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6

yum -y install yum -priorities

yum -y install docker-io

service docker start

chkconfig docker on

 

②安装febootstrap

yum -y install febootstrap

 

③设置Docker镜像源

yum install -y yum-priorities && rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm && rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6

 

④制作centos镜像文件centos6-image目录

febootstrap -i bash -i wget -i yum -i iputils -i iproute -i man -i vim -i openssh-server -i openssh-clients -i tar -i gzip centos6 centos6-image http://mirrors.aliyun.com/centos/6/os/x86_64/  

注意：

制作centos6.5镜像命令（在上面的步骤中替换以下对应命令）：

febootstrap -i bash -i wget -i yum -i iputils -i iproute centos65 centos65-image http://archive.kernel.org/centos-vault/6.5/os/x86_64/

制作centos7.5命令：

febootstrap -i bash -i wget -i yum -i iputils -i iproute centos75 centos75-image http://mirrors.aliyun.com/centos/7.5.1804/os/x86_64/

 

⑤此时会生成一个centos6-image文件目录，上面命令中参数 -i 后面的都是基础镜像中安装的一些服务。如果你不想要这么多服务（因为把所有服务安装后镜像会变的非常大）可以只安装一些基本的，必不可少的服务。centos6是指版本，centos6-image是生成的目录名称。

 

⑥

cd centos6-image

cp etc/skel/.bash* root/

tar -c .|docker import - centos6-base

docker images       //查看有无刚刚创建的名为centos6-base的镜像

docker run -ti centos6-base /bin/bash

docker tag IMAGEID localhost:5000/myfirstimage

docker save -o image.tar.gz arvin/mysql    //导出镜像

docker load --input image.tar.gz   //导入镜像（换一台机器）

 

5.8、docker容器运行监测

docker ps -a     //查看所有容器，包括不在运行的容器,找到CONTAINERID

ps -ef | grep CONTAINERID    //查看对应容器的进程号

 

top -p CONTAINERPID        //查看内存占用情况

