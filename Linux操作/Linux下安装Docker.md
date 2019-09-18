**一、基础环境**
1、操作系统：CentOS 7.3
2、Docker版本：[18.06.1 官方下载地址（打不开可能需要梯子）](https://download.docker.com/linux/static/stable/x86_64/)
3、百度云Docker 18.06.1地址：https://pan.baidu.com/s/1YdN9z72QutPkHBfLq06H1A 密码：dvvh
4、官方参考文档：https://docs.docker.com/install/linux/docker-ce/binaries/#install-static-binaries

**二、Docker安装**

>进入tmp目录下

```
cd /
cd tmp
```

> 下载

```
wget https://download.docker.com/linux/static/stable/x86_64/docker-18.06.1-ce.tgz
```

> 解压

```
tar -xvf docker-18.06.1-ce.tgz
```

>将解压出来的docker文件内容移动到 /usr/bin/ 目录下

```
cp docker/* /usr/bin/
```

> 将docker注册为service

```
vim /etc/systemd/system/docker.service
```

> 进入到文件后 进入插入状态 将下面内容复制进入

```
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target firewalld.service
Wants=network-online.target
  
[Service]
Type=notify
# the default is not to use systemd for cgroups because the delegate issues still
# exists and systemd currently does not support the cgroup feature set required
# for containers run by docker
ExecStart=/usr/bin/dockerd
ExecReload=/bin/kill -s HUP $MAINPID
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
# Uncomment TasksMax if your systemd version supports it.
# Only systemd 226 and above support this version.
#TasksMax=infinity
TimeoutStartSec=0
# set delegate yes so that systemd does not reset the cgroups of docker containers
Delegate=yes
# kill only the docker process, not all processes in the cgroup
KillMode=process
# restart the docker process if it exits prematurely
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s
  
[Install]
WantedBy=multi-user.target
```

> 然后 保存退出

```
Esc
:wq
```

> 启动

```python
chmod +x /etc/systemd/system/docker.service #添加文件权限并启动docker
 
systemctl daemon-reload                 #重新加载配置文件
systemctl start docker          #启动Docker
systemctl enable docker.service         #设置开机自启
```

> 验证

```python
systemctl status docker         #查看Docker状态
docker -v           #查看Docker版本
```

