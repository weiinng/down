# 一.搭建FTP服务器

###思路：

- 一台服务器

- 安装软件

  ```
  yum -y install vsftpd
  cd var/ftp
  ```

- 启动服务

  ```
  rpm -q vsftpd    #查看版本号
  service vsftpd start #启动FTP服务
  ```

- 测试验证

  ​	可以通过 ftp://127.0.0.1

  来访问到你的 FTP服务器

# 二.FTP服务器的客户端工具

### 安装FTP工具

```
cd ftp
yum list|grep ftp  #搜索当前目录下面带有FTP的 所有文件
```

> Linux ：ftp  、lftp (客户端)
>
> windows :FlieZilla  、IE 、Chrome 、Firefox
>
> lftp 和  ftp 工具说明：

- lftp 可以批量并下载目录

  `mirror remote local    下载整个目录到本地`

  `mirror -R local remote rename  上传整个目录到远程同时可以从命名`







  搭建简易的FTP服务器

# 思路

 [关闭防火墙和selinux](Linux操作/Linux如何关闭防火墙.md)

-配置 yum 源



 软件三部曲（安装|确定|软件列表）

- 安装 vsftpd

  ```
  
  ```

- 确定安装成功

  ```
  [root@VM_0_11_centos /]# cd var/ftp
  [root@VM_0_11_centos ftp]# rpm -q vsftpd
  vsftpd-3.0.2-25.el7.x86_64
  ```

  

- 查看软件带来的文件列表

  ```
  /etc/logrotate.d/vsftpd          //日志轮转的文件
  /etc/pam.d/vsftpd               //安全认证相关的文件
  /etc/re.d/init.d/vsftpd           //启动脚本
  /etc/vsftpd                   //配置文件的主目录                
  /etc/vsftpd/ftpusers          //用户列表（黑名单）拒绝访问
  /etc/vsftpd/user_list         //用户列表（默认黑名单，可黑可白）
  /etc/vsftpd/vsftpd.conf        //主配置文件
  
  /usr/sbin/vsftpd             //二进制的命令
  
  /usr/share/doc/vsftpd-3.0.2/EXAMPLE/VIRTUAL_HOSTS
  /usr/share/doc/vsftpd-3.0.2/EXAMPLE/VIRTUAL_HOSTS/README    //虚拟主机
  /usr/share/doc/vsftpd-3.0.2/EXAMPLE/VIRTUAL_USERS           
  /usr/share/doc/vsftpd-3.0.2/EXAMPLE/VIRTUAL_USERS/README   //虚拟用户
  
  /usr/share/man/man5/vsftpd.conf.5.gz    //man文档
  
  /var/ftp     //匿名用户默认数据的跟目录
  /var/ftp/pub    //匿名用户的默认数据目录的拓展目录
  
  ```

  

了解配置文件 ——> (man 5 vsftpd.conf)

```
使用cat 命令查看 vsftpd的配置
[root@VM_0_11_centos /]# cat /etc/vsftpd/vsftpd.conf 

// 配置文件的数量比较大，有#号的是不生效的没#号的是生效的。
//使用下面的命令进行过滤

[root@VM_0_11_centos /]# grep -v ^# /etc/vsftpd/vsftpd.conf
anonymous_enable=YES     //匿名用户访问     
local_enable=YES          //非匿名用户
write_enable=YES          //写的总开关
local_umask=022           //反掩码  file:644     dir:755
dirmessage_enable=YES     //消息功能
xferlog_enable=YES        //开启或者启用xferlog日志
connect_from_port_20=YES    //支持主动模式
xferlog_std_format=YES       //xferlog 日志格式
listen=NO                     //ftp服务独立模式下的监听
listen_ipv6=YES               

pam_service_name=vsftpd        //指定认证文件。安全验证，必须与安全验证保持一致原则上不对其修改。
userlist_enable=YES         //用户列表  
tcp_wrappers=YES             //支持tcp_wrappers 功能


```



根据需求通过修改配置文件来完成服务器的搭建

启动服务器

测试验证



  

