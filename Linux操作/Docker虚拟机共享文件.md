点击VirtualBox状态栏上`设备——共享文件夹` 

添加指定文件夹，填写文件夹名称 

FileName  = 文件夹名称

点击进入 docker终端  

```
docker-mechine ssh
```

新建一个文件夹

```
mkdir /var/root
```

设置共享的文件

```
sudo mount -t vboxsf <FileName> /var/root
```

进入到  root 文件内  查看目录下是否与主机共享成功

```
cd /var/root
ls
```



设置自动挂载，可以在/etc/fstab中添加一项 

```
sudo vim /etc/fstab 
c/Users /var/root vboxsf rw,gid=110,uid=1100,auto 0 0 
```

卸载挂载点命令 

```
sudo umount -f /var/root
```

