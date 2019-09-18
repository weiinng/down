### 5.设置为服务

　　上述第3中启动Redis的方法不是很好，因为关闭启动命令窗口后Redis也停止运行，所以可以将Redis的启动设置为Windows的服务运行，这样就不会有这种问题了。

　　在cmd命令窗中进入Redis安装目录，执行命令：

```python
redis-server --service-install redis.windows.conf --loglevel notice --service-name Redis
```

　　然后在Windows的服务中可以找到一个名为Redis的服务，启动此服务就可以启动redis了。

注意：Windows版本的Redis启动时默认配置文件是redis.windows-service.conf，要用其他配置文件启动Redis的话，在启动命令中指定配置文件就行了。

 ps:服务无法启动解决方案：

#### 修改服务用户

属性 --> 登录 --> 修改为本地用户登录 -- > 确定

#### 配置环境变量

找到rides数据库目录将环境变量配置到path里面

通过cmd窗口redis-cil 启动数据库