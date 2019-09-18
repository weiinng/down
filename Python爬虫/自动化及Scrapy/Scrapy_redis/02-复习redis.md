# redis是什么？

Redis是一个开源的，内存数据库，它可以用作数据库，缓存和消息中间件。它支持多种类型的数据结构，如字符串，哈希，列表，集合，有序集合。

**常用命令**

- redis-server stop                     停止
- redis-server start                    启动
- redis-server restart                重启

- redis-cli -h<hostnname> -p <port>      远程连接redis数据库

**redis中：**

- select 1                    切换到db1 默认为 db0
- keys *                        查看所有的redis键
- type  “键”                   查看对应键的数据类型
- flushdb                      清空当前db
- flushall                      清空所有db

##### 中文文档

http://www.redis.cn/commands.html



