

# 替换默认源

替换源：

默认的源是国外的源，国外的源有可能打开比较慢有可能打不开所以要替换源。

国内很多厂商做了镜像我们现在使用163的源。

<http://mirrors.163.com/.help/centos.html>

> 首先备份repo

```
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
```

> 就可以查看到备份的repo

```
cd /etc/yum.repos.d/                //进入指定目录
ll              //查看命令
```

> 安装CentOS 7    下载对应版本的 repo 放入到 /etc/yum.repos.d/CentOS-Base.repo

```
curl http://mirrors.163.com/.help/CentOS7-Base-163.repo -o CentOS7-Base-163.repo
```

> 运行下面命令生成缓存

```
yum clean all             //这条命令如果失败不用管
yum makecache              
```

> 如果提示你看不懂的命令就是因为yum被占用了 我们可以通过下面命令来干掉他

```
rm -f /var/run/yum.pid      //然后在执行 运行下面命令生成缓存 的步骤
```

> 源安装完成后可以安装一个wget   安装过的不用安装

```
yum install wget                //安装wget
```

> 安装vim       机器默认有vi，vim比vi更好用一些
>
> vim 是Linux下面的文件编辑神器

```
yum install vim
```



# 修改yum源为阿里

```python
1. 备份本地yum源

 mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo_bak 

2.获取阿里yum源配置文件

将https://mirrors.tuna.tsinghua.edu.cn/help/centos/  中的内容粘贴到CentOS-Base.repo

3.更新cache

yum  clean   all

yum makecache 

4.查看

yum -y update 

```



