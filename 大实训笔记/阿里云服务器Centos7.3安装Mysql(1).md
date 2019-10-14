## 阿里云服务器Centos7.3安装Mysql数据库

工作中项目会在本地进行开发，在开发完毕后，将项目上线部署，本次使用的是阿里云的服务器，那么就需要在服务器中安装项目用到的程序和服务等。

本文介绍的是：如何安装Mysql数据库并测试运行。

> CentOS下自带mariadb    可以通过下面命令删除

```
yum remove mariadb-libs.x86_64
```

> 下载Mysql57的源文件

```
cd /
cd tmp
wget https://repo.mysql.com/mysql57-community-release-el7-8.noarch.rpm
```

> 安装Mysql57

```
yum localinstall mysql57-community-release-el7-8.noarch.rpm
```

> 安装数据库服务

```
yum install mysql-community-server
```

> 开启数据库

```python
mysql -u root -pexit   
```

开启数据库会需要密码，但是默认密码不知道，接着看下面

# 修改密码    XNT70!N_f:2k  

```
service mysqld start    //启动数据库服务
第一次启动过程中
ps -ef |frep mysql                  //这条命令查看是否存在Mysql服务  
```

> 查看mysql 密码

```python
cat /var/log/mysqld.log |grep "password" 
# 输入上面的命令会出现如下的结果 其中第一行 root@localhost: 后面的就是默认密码  
# cv使用 进入数据库修改密码
[root@iz2zedrblb61bvhoe2yl7qz /]# cat /var/log/mysqld.log |grep "password"
2019-08-16T09:02:23.203191Z 1 [Note] A temporary password is generated for root@localhost: 8m2.(Mmjp3ad
2019-08-16T09:11:32.856910Z 0 [Note] Shutting down plugin 'validate_password'
2019-08-16T09:11:34.068720Z 0 [Note] Shutting down plugin 'sha256_password'
2019-08-16T09:11:34.068722Z 0 [Note] Shutting down plugin 'mysql_native_passwor '

```

> 修改Mysql数据库密码

```
cat /var/log/mysqld.log |grep "password"      //首先查看mysql数据库密码并赋值
mysql -u root -p              //进入数据库
password                         //输入密码
set password = password("123456");          //修改密码为123456
	- 如果显示 OK 证明修改密码成果
	- 如果提示 Your password does not satisfy the current policy requirements
	- 他的意思是告诉你你密码不符合当前策略要求
set global validate_password_policy=0;       //密码安全策略为0
set global validate_password_length=1;        //密码长度为1
alter user 'root'@'localhost' password expire never;  //root密码永不过期
flush privileges;                 //重新加载权限列表
set password = password("123456");          //修改密码为123456
 - 这时候就可以成功了
exit;        //退出
 - 可以尝试使用新的密码重新登陆
```

> 使用Mysql命令进行测试

```python
show databases; 
exit;
```

