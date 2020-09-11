## 运行hive

如果用的是华哥的这个虚拟机，在启动hive之前一定要先启动hfds.

```shell
start-all.sh
```

启动hive

```shell
hive
```

做外部连接

```sh
hive --service hiveserver2
```

然后就可以使用编辑器进行连接了