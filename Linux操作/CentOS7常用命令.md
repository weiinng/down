```python
centos常用命令：

查看所有运行的单元：systemctl list-units

查看所有单元：systemctl list-units --all

查看所有启动的服务：systemctl list-units --type=service 对应以前的chkconfig --list

查看是否启用，例如防火墙：systemctl is-enabled firewalld.service

查看是否运行，例如防火墙：systemctl is-active firewalld.service  或者 systemctl status firewalld.service

停止防火墙：systemctl stop firewalld.service

启动防火墙：systemctl start firewalld.service

重启防火墙：systemctl restart firewalld.service

重载防火墙：systemctl reload firewalld.service

注意：当我们使用systemctl的start，restart，stop和reload命令时，
我们不会从终端获取到任何输出内容，只有status命令可以打印输出。


服务开机自启动：systemctl enable httpd

服务不开机自启动：systemctl disable httpd

使用systemctl命令杀死服务：systemctl kill firewalld.service



获取当前某个服务的CPU分配额，例如防火墙：systemctl show -p CPUShares firewalld.service

获取某个服务（httpd）的依赖性列表：systemctl list-dependencies httpd.service



开启防火墙22端口：iptables -I INPUT -p tcp --dport 22 -j ACCEPT

查看主机名： hostnamectl status --static



查看某个服务的名称：

systemctl list-units |grep XXX

```

# CentOS7 常用命令集合

​       这两天一直在对CentOS 7.2进行初体验，各种学习命令肿么用，不过其实大多和DOS是一样的，只是命令的表达上可能有点儿不一样，毕竟这些都不是一家出来的嘛~

​       废话不多说，直接上命令和解析！

## 常用命令

### 文件与目录操作

| 命令                    | 解析                                                         |
| ----------------------- | ------------------------------------------------------------ |
| cd /home                | 进入 ‘/home’ 目录                                            |
| cd ..                   | 返回上一级目录                                               |
| cd ../..                | 返回上两级目录                                               |
| cd -                    | 返回上次所在目录                                             |
| cp file1 file2          | 将file1复制为file2                                           |
| cp -a dir1 dir2         | 复制一个目录                                                 |
| cp -a /tmp/dir1 .       | 复制一个目录到当前工作目录（.代表当前目录）                  |
| ls                      | 查看目录中的文件                                             |
| ls -a                   | 显示隐藏文件                                                 |
| ls -l                   | 显示详细信息                                                 |
| ls -lrt                 | 按时间显示文件（l表示详细列表，r表示反向排序，t表示按时间排序） |
| pwd                     | 显示工作路径                                                 |
| mkdir dir1              | 创建 ‘dir1’ 目录                                             |
| mkdir dir1 dir2         | 同时创建两个目录                                             |
| mkdir -p /tmp/dir1/dir2 | 创建一个目录树                                               |
| mv dir1 dir2            | 移动/重命名一个目录                                          |
| rm -f file1             | 删除 ‘file1’                                                 |
| rm -rf dir1             | 删除 ‘dir1’ 目录及其子目录内容                               |

### 查看文件内容

| 命令          | 解析                                 |
| ------------- | ------------------------------------ |
| cat file1     | 从第一个字节开始正向查看文件的内容   |
| head -2 file1 | 查看一个文件的前两行                 |
| more file1    | 查看一个长文件的内容                 |
| tac file1     | 从最后一行开始反向查看一个文件的内容 |
| tail -3 file1 | 查看一个文件的最后三行               |
| vi file       | 打开并浏览文件                       |

### 文本内容处理

| 命令                 | 解析                                                         |
| -------------------- | ------------------------------------------------------------ |
| grep str /tmp/test   | 在文件 ‘/tmp/test’ 中查找 “str”                              |
| grep ^str /tmp/test  | 在文件 ‘/tmp/test’ 中查找以 “str” 开始的行                   |
| grep [0-9] /tmp/test | 查找 ‘/tmp/test’ 文件中所有包含数字的行                      |
| grep str -r /tmp/*   | 在目录 ‘/tmp’ 及其子目录中查找 “str”                         |
| diff file1 file2     | 找出两个文件的不同处                                         |
| sdiff file1 file2    | 以对比的方式显示两个文件的不同                               |
| vi file              | 操作解析i进入编辑文本模式Esc退出编辑文本模式:w保存当前修改:q不保存退出vi:wq保存当前修改并退出vi |

### 查询操作

| 命令                                             | 解析                                             |
| ------------------------------------------------ | ------------------------------------------------ |
| find / -name file1                               | 从 ‘/’ 开始进入根文件系统查找文件和目录          |
| find / -user user1                               | 查找属于用户 ‘user1’ 的文件和目录                |
| find /home/user1 -name *.bin                     | 在目录 ‘/ home/user1’ 中查找以 ‘.bin’ 结尾的文件 |
| find /usr/bin -type f -atime +100                | 查找在过去100天内未被使用过的执行文件            |
| find /usr/bin -type f -mtime -10                 | 查找在10天内被创建或者修改过的文件               |
| locate *.ps                                      | 寻找以 ‘.ps’ 结尾的文件，先运行 ‘updatedb’ 命令  |
| find -name ‘*.[ch]’ \| xargs grep -E ‘expr’      | 在当前目录及其子目录所有.c和.h文件中查找 ‘expr’  |
| find -type f -print0 \| xargs -r0 grep -F ‘expr’ | 在当前目录及其子目录的常规文件中查找 ‘expr’      |
| find -maxdepth 1 -type f \| xargs grep -F ‘expr’ | 在当前目录中查找 ‘expr’                          |

### 压缩、解压

| 命令                            | 解析                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| bzip2 file1                     | 压缩 file1                                                   |
| bunzip2 file1.bz2               | 解压 file1.bz2                                               |
| gzip file1                      | 压缩 file1                                                   |
| gzip -9 file1                   | 最大程度压缩 file1                                           |
| gunzip file1.gz                 | 解压 file1.gz                                                |
| tar -cvf archive.tar file1      | 把file1打包成 archive.tar（-c: 建立压缩档案；-v: 显示所有过程；-f: 使用档案名字，是必须的，是最后一个参数） |
| tar -cvf archive.tar file1 dir1 | 把 file1，dir1 打包成 archive.tar                            |
| tar -tf archive.tar             | 显示一个包中的内容                                           |
| tar -xvf archive.tar            | 释放一个包                                                   |
| tar -xvf archive.tar -C /tmp    | 把压缩包释放到 /tmp目录下                                    |
| zip file1.zip file1             | 创建一个zip格式的压缩包                                      |
| zip -r file1.zip file1 dir1     | 把文件和目录压缩成一个zip格式的压缩包                        |
| unzip file1.zip                 | 解压一个zip格式的压缩包到当前目录                            |
| unzip test.zip -d /tmp/         | 解压一个zip格式的压缩包到 /tmp 目录                          |

### yum安装器

| 命令                           | 解析                                                |
| ------------------------------ | --------------------------------------------------- |
| yum -y install [package]       | 下载并安装一个rpm包                                 |
| yum localinstall [package.rpm] | 安装一个rpm包，使用你自己的软件仓库解决所有依赖关系 |
| yum -y update                  | 更新当前系统中安装的所有rpm包                       |
| yum update [package]           | 更新一个rpm包                                       |
| yum remove [package]           | 删除一个rpm包                                       |
| yum list                       | 列出当前系统中安装的所有包                          |
| yum search [package]           | 在rpm仓库中搜寻软件包                               |
| yum clean [package]            | 清除缓存目录（/var/cache/yum）下的软件包            |
| yum clean headers              | 删除所有头文件                                      |
| yum clean all                  | 删除所有缓存的包和头文件                            |

### 网络相关

| 命令                                            | 解析                   |
| ----------------------------------------------- | ---------------------- |
| ifconfig eth0                                   | 显示一个以太网卡的配置 |
| ifconfig eth0 192.168.1.1 netmask 255.255.255.0 | 配置网卡的IP地址       |
| ifdown eth0                                     | 禁用 ‘eth0’ 网络设备   |
| ifup eth0                                       | 启用 ‘eth0’ 网络设备   |
| iwconfig eth1                                   | 显示一个无线网卡的配置 |
| iwlist scan                                     | 显示无线网络           |
| ip addr show                                    | 显示网卡的IP地址       |

### 系统相关

| 命令                                           | 解析                                         |
| ---------------------------------------------- | -------------------------------------------- |
| su -                                           | 切换到root权限（与su有区别）                 |
| shutdown -h now                                | 关机                                         |
| shutdown -r now                                | 重启                                         |
| top                                            | 罗列使用CPU资源最多的linux任务 （输入q退出） |
| pstree                                         | 以树状图显示程序                             |
| man ping                                       | 查看参考手册（例如ping 命令）                |
| passwd                                         | 修改密码                                     |
| df -h                                          | 显示磁盘的使用情况                           |
| cal -3                                         | 显示前一个月，当前月以及下一个月的月历       |
| cal 10 1988                                    | 显示指定月，年的月历                         |
| date –date ‘1970-01-01 UTC 1427888888 seconds’ | 把一相对于1970-01-01 00:00的秒数转换成时间   |

## XSheel 5相关操作

### 窗体快捷键

| 命令           | 解析                                                         |
| -------------- | ------------------------------------------------------------ |
| Ctrl + u       | 删除光标之前到行首的字符                                     |
| Ctrl + k       | 删除光标之前到行尾的字符                                     |
| Ctrl + c       | 取消当前行输入的命令，相当于Ctrl + Break                     |
| Ctrl + a       | 光标移动到行首（ahead of line），相当于通常的Home键          |
| Ctrl + e       | 光标移动到行尾（end of line）                                |
| Ctrl + f       | 光标向前（forward）移动一个字符位置                          |
| Ctrl + b       | 光标往回（backward）移动一个字符位置                         |
| Ctrl + l       | 清屏，相当于执行clear命令                                    |
| Ctrl + r       | 显示:号提示，根据用户输入查找相关历史命令（reverse-i-search） |
| Ctrl + w       | 删除从光标位置前到当前所处单词（word）的开头                 |
| Ctrl + t       | 交换光标位置前的两个字符                                     |
| Ctrl + y       | 粘贴最后一次被删除的单词                                     |
| Ctrl + Alt + d | 显示桌面                                                     |
| Alt + b        | 光标往回（backward）移动到前一个单词                         |
| Alt + d        | 删除从光标位置到当前所处单词的末尾                           |
| Alt + F2       | 运行                                                         |
| Alt + F4       | 关闭当前窗口                                                 |
| Alt + F9       | 最小化当前窗口                                               |
| Alt + F10      | 最大化当前窗口                                               |
| Alt + Tab      | 切换窗口                                                     |
| Alt + 左键     | 移动窗口（或在最下面的任务栏滚动鼠标滑轮）                   |

### 操作小技巧

​       鼠标中间键：粘贴突出显示的文本。(使用鼠标左键来选择文本。把光标指向想粘贴文本的地方。点击鼠标中间键来粘贴。)

​       Tab：命令行自动补全。使用 shell 提示时可使用这一方式。键入命令或文件名的前几个字符，然后按 [Tab] 键，它会自动补全命令或显示匹配键入字符的所有命令。

​       在滚动条的空白处点击鼠标中键：屏幕即滚动到那个地方。

​       在桌面或文件管理器中直接按 / 就可以输入位置，打开文件管理器。

​       在 vi 或 Firefox 中直接按 / 即可进入快速搜索状态。

​       网站链接和图片可直接拖放到桌面或者目录，可以马上下载。

​       直接将文件管理器中的文件拖到终端中就可以在终端中得到完整的路径名。





#### 1.关机 (系统的关机、重启以及登出 ) 的命令、

| 名称         | 命令1                       | 命令2  | 命令3     |
| ------------ | --------------------------- | ------ | --------- |
| 关闭系统     | shutdown -h now             | init 0 | telinit 0 |
| 定时关机     | shutdown -h hours:minutes & |        |           |
| 取消定时关机 | shutdown -c                 |        |           |
| 重启         | shutdown -r now             | reboot |           |
| 注销         | logout                      |        |           |

#### 2.查看系统信息的命令

| 名称                              | 命令1                | 命令2    | 命令3 | 命令4 |
| --------------------------------- | -------------------- | -------- | ----- | ----- |
| 显示机器的处理器架构              | arch                 | uname -m |       |       |
| 显示正在使用的内核版本            | uname -r             |          |       |       |
| 显示硬件系统部件 - (SMBIOS / DMI) | dmidecode -q         |          |       |       |
| 罗列一个磁盘的架构特性            | hdparm -i /dev/hda   |          |       |       |
| 在磁盘上执行测试性读取操作        | hdparm -tT /dev/sda  |          |       |       |
| 显示CPU info的信息                | cat /proc/cpuinfo    |          |       |       |
| 显示中断                          | cat /proc/interrupts |          |       |       |
| 校验内存使用                      | cat /proc/meminfo    |          |       |       |
| 显示哪些swap被使用                | cat /proc/swaps      |          |       |       |
| 显示内核的版本                    | cat /proc/version    |          |       |       |

cat /proc/net/dev 显示网络适配器及统计

cat /proc/mounts 显示已加载的文件系统

lspci -tv 罗列 PCI 设备

lsusb -tv 显示 USB 设备

date 显示系统日期

cal 2007 显示2007年的日历表

date 041217002007.00 设置日期和时间 - 月日时分年.秒

clock -w 将时间修改保存到 BIOS

#### 3.文件和目录操作命令

cd /home 进入 '/ home' 目录'

cd .. 返回上一级目录

cd ../.. 返回上两级目录

cd 进入个人的主目录

cd ~user1 进入个人的主目录

cd - 返回上次所在的目录

pwd 显示工作路径

ls 查看目录中的文件

ls -F 查看目录中的文件

ls -l 显示文件和目录的详细资料

ls -a 显示隐藏文件

mkdir dir1 创建一个叫做 'dir1' 的目录'

mkdir dir1 dir2 同时创建两个目录

mkdir -p /tmp/dir1/dir2 创建一个目录树

rm -f file1 删除一个叫做 'file1' 的文件'

rmdir dir1 删除一个叫做 'dir1' 的目录'

rm -rf dir1 删除一个叫做 'dir1' 的目录并同时删除其内容

rm -rf dir1 dir2 同时删除两个目录及它们的内容

mv dir1 new_dir 重命名/移动 一个目录

cp file1 file2 复制一个文件

cp dir/* . 复制一个目录下的所有文件到当前工作目录

cp -a /tmp/dir1 . 复制一个目录到当前工作目录

cp -a dir1 dir2 复制一个目录

ln -s file1 lnk1 创建一个指向文件或目录的软链接

ln file1 lnk1 创建一个指向文件或目录的物理链接

touch file1 创建一个文件

#### 4.文件搜索命令

find / -name file1 从 '/' 开始进入根文件系统搜索文件和目录

find / -user user1 搜索属于用户 'user1' 的文件和目录

find /home/user1 -name \*.bin 在目录 '/ home/user1' 中搜索带有'.bin' 结尾的文件

find /usr/bin -type f -atime +100 搜索在过去100天内未被使用过的执行文件

find /usr/bin -type f -mtime -10 搜索在10天内被创建或者修改过的文件

locate \*.ps 寻找以 '.ps' 结尾的文件 - 先运行 'updatedb' 命令

whereis file 显示一个二进制文件、源码或man的位置

which file 显示一个二进制文件或可执行文件的完整路径

#### 5.查看文件内容

cat file1 从第一个字节开始正向查看文件的内容

tac file1 从最后一行开始反向查看一个文件的内容

more file1 查看一个长文件的内容

less file1 类似于 'more' 命令，但是它允许在文件中和正向操作一样的反向操作

head -2 file1 查看一个文件的前两行

tail -2 file1 查看一个文件的最后两行 5.挂载命令

mount /dev/hda2 /mnt/hda2 挂载一个叫做hda2的盘 (注：确定目录 '/ mnt/hda2' 已经存在)

umount /dev/hda2 卸载一个叫做hda2的盘 (先从挂载点 '/ mnt/hda2' 退出)

fuser -km /mnt/hda2 当设备繁忙时强制卸载

umount -n /mnt/hda2 运行卸载操作而不写入 /etc/mtab 文件(当文件为只读或当磁盘写满时非常有用)

mount /dev/fd0 /mnt/floppy 挂载一个软盘

mount /dev/cdrom /mnt/cdrom 挂载一个光盘

mount /dev/hdc /mnt/cdrecorder 挂载一个cdrw或dvdrom

mount /dev/hdb /mnt/cdrecorder 挂载一个cdrw或dvdrom

mount -o loop file.iso /mnt/cdrom 挂载一个文件或ISO镜像文件

mount -t vfat /dev/hda5 /mnt/hda5 挂载一个Windows FAT32文件系统

mount /dev/sda1 /mnt/usbdisk 挂载一个usb 捷盘或闪存设备

mount -t smbfs -o username=user,password=pass //WinClient/share /mnt/share 挂载一个windows网络共享

#### 6.磁盘空间操作的命令

df -h 显示已经挂载的分区列表

ls -lSr |more 以尺寸大小排列文件和目录

du -sh dir1 估算目录 'dir1' 已经使用的磁盘空间'

du -sk * | sort -rn 以容量大小为依据依次显示文件和目录的大小

#### 7.用户和群组相关命令

groupadd group_name 创建一个新用户组

groupdel group_name 删除一个用户组

groupmod -n new_group_name old_group_name 重命名一个用户组

useradd -c "Name Surname " -g admin -d /home/user1 -s /bin/bash user1 创建一个属于 "admin" 用户组的用户

useradd user1 创建一个新用户

userdel -r user1 删除一个用户 ( '-r' 同时删除除主目录)

passwd user1 修改一个用户的口令 (只允许root执行)

chage -E 2005-12-31 user1 设置用户口令的失效期限

ls -lh 显示权限

chmod 777 directory1 设置目录的所有人(u)、群组(g)以及其他人(o)以读(r )、写(w)和执行(x)的权限

chmod 700 directory1 删除群组(g)与其他人(o)对目录的读写执行权限

chown user1 file1 改变一个文件的所有人属性，为use1。

chown -R user1 directory1 改变一个目录的所有人属性并同时改变改目录下所有文件的属性都为use1所有

chgrp group1 file1 改变文件的群组为group1

chown user1:group1 file1 改变一个文件的所有人和群组属性，所属组为group1，用户为use1。

find / -perm -u+s 罗列一个系统中所有使用了SUID控制的文件

chmod u+s /bin/file1 设置一个二进制文件的 SUID 位 - 运行该文件的用户也被赋予和所有者同样的权限

chmod u-s /bin/file1 禁用一个二进制文件的 SUID位

chmod g+s /home/public 设置一个目录的SGID 位 - 类似SUID ，不过这是针对目录的

chmod g-s /home/public 禁用一个目录的 SGID 位

chmod o+t /home/public 设置一个文件的 STIKY 位 - 只允许合法所有人删除文件

chmod o-t /home/public 禁用一个目录的 STIKY 位

#### 8.打包和解压缩文件的命令

bunzip2 file1.bz2 解压一个叫做 'file1.bz2'的文件

bzip2 file1 压缩一个叫做 'file1' 的文件

gunzip file1.gz 解压一个叫做 'file1.gz'的文件

gzip file1 压缩一个叫做 'file1'的文件

gzip -9 file1 最大程度压缩

rar a file1.rar test_file 创建一个叫做 'file1.rar' 的包

rar a file1.rar file1 file2 dir1 打包 'file1', 'file2' 以及目录 'dir1'

rar x file1.rar 解rar包

unrar x file1.rar 解rar包

tar -cvf archive.tar file1 创建一个非压缩的tar包

tar -cvf archive.tar file1 file2 dir1 创建一个包含了 'file1', 'file2' 'dir1'的包

tar -tf archive.tar 显示一个包中的内容

tar -xvf archive.tar 释放一个包

tar -xvf archive.tar -C /tmp 将压缩包释放到 /tmp目录下 (-c是指定目录)

tar -cvfj archive.tar.bz2 dir1 创建一个bzip2格式的压缩包

tar -xvfj archive.tar.bz2 解压一个bzip2格式的压缩包

tar -cvfz archive.tar.gz dir1 创建一个gzip格式的压缩包

tar -xvfz archive.tar.gz 解压一个gzip格式的压缩包

zip file1.zip file1 创建一个zip格式的压缩包

zip -r file1.zip file1 file2 dir1 将几个文件和目录同时压缩成一个zip格式的压缩包

unzip file1.zip 解压一个zip格式压缩包

#### 9.关于RPM 包的命令

rpm -ivh package.rpm 安装一个rpm包

rpm -ivh --nodeeps package.rpm 安装一个rpm包而忽略依赖关系警告

rpm -U package.rpm 更新一个rpm包但不改变其配置文件

rpm -F package.rpm 更新一个确定已经安装的rpm包

rpm -e package_name.rpm 删除一个rpm包

rpm -qa 显示系统中所有已经安装的rpm包

rpm -qa | grep httpd 显示所有名称中包含 "httpd" 字样的rpm包

rpm -qi package_name 获取一个已安装包的特殊信息

rpm -ql package_name 显示一个已经安装的rpm包提供的文件列表

rpm -qc package_name 显示一个已经安装的rpm包提供的配置文件列表

rpm -q package_name --whatrequires 显示与一个rpm包存在依赖关系的列表

rpm -q package_name --whatprovides 显示一个rpm包所占的体积

rpm -q package_name --scripts 显示在安装/删除期间所执行的脚本l

rpm -q package_name --changelog 显示一个rpm包的修改历史

rpm -qf /etc/httpd/conf/httpd.conf 确认所给的文件由哪个rpm包所提供

rpm -qp package.rpm -l 显示由一个尚未安装的rpm包提供的文件列表

rpm --import /media/cdrom/RPM-GPG-KEY 导入公钥数字证书

rpm --checksig package.rpm 确认一个rpm包的完整性

rpm -qa gpg-pubkey 确认已安装的所有rpm包的完整性

rpm -V package_name 检查文件尺寸、 许可、类型、所有者、群组、MD5检查以及最后修改时间

rpm -Va 检查系统中所有已安装的rpm包- 小心使用

rpm -Vp package.rpm 确认一个rpm包还未安装

rpm2cpio package.rpm | cpio --extract --make-directories *bin* 从一个rpm包运行可执行文件

rpm -ivh /usr/src/redhat/RPMS/`arch`/package.rpm 从一个rpm源码安装一个构建好的包

rpmbuild --rebuild package_name.src.rpm 从一个rpm源码构建一个 rpm 包

#### 10.YUM 软件包升级器

yum install package_name 下载并安装一个rpm包

yum localinstall package_name.rpm 将安装一个rpm包，使用你自己的软件仓库为你解决所有依赖关系

yum update package_name.rpm 更新当前系统中所有安装的rpm包

yum update package_name 更新一个rpm包

yum remove package_name 删除一个rpm包

yum list 列出当前系统中安装的所有包

yum search package_name 在rpm仓库中搜寻软件包

yum clean packages 清理rpm缓存删除下载的包

yum clean headers 删除所有头文件

yum clean all 删除所有缓存的包和头文件

