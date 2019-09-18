### centos7的网卡重启方法

```html
centos6的网卡重启方法：service network restart
centos7的网卡重启方法：systemctl restart network
```

### 关闭防火墙并设置开机不启动

```javascript
systemctl status firewalld.service  //查看防火墙状态
systemctl stop firewalld    //关闭
systemctl start firewalld   //开启
systemctl disable firewalld  //开机自动关闭
systemctl enable firewalld   //开机自动启动
chkconfig --list|grep network(RHLE6)   //查看开机是否启动
```

### 临时和永久关闭Selinux

```javascript
//临时关闭
_getenforce
Enforcing

_setenforce 0
setenforce:SELinux is disabled

//永久关闭
_vim /etc/selinux/config

```



2、DNS配置文件：

cat /etc/resolv.conf
设置主机和IP绑定信息：cat /etc/hosts
设置主机名：cat /etc/hostname



3、可以使用nmtui文本框方式修改IP

