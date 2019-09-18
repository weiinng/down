完整的select语句
select distince *
from 表名
where ...
group by ... having ...
order by ...
limit start,count



视图
1、问题：
对于复杂的查询，往往是有多个数据进行关联查询而得到，如果数据库因为需求等原因发生了改变，为了保证查询出来的数据与之前相同，则需要在多个地方进行修改，维护起来非常麻烦

解决办法：定义视图

2、试图是什么：
通俗的讲，视图就是一条select语句执行后返回的结果集。所以我们在创建视图的时候，主要的工作就落在创建这条SQL查询语句上，视图是对若干张基本表的引用，一张虚表，查询语句执行的结果，不存储具体的数据 （基本表数据发生了改变，视图也会跟着改变）；




事务


索引：
创建索引：
create index 索引名称 on 表名(字段名称（长度））；
如果不是字符串类型就不用加长度

查看索引：
show index from 表名；

删除索引：
drop index 索引名称 on 表名；

使用pycharm给数据库进行增删改查：
首先在黑窗口创建个表：
create database s;
use s;
create table s(
id int,
name varchar(10)
);

打开pycharm
from pymysql import connect
conn=connect(host='localhost',port=3306,database='s',user='root',password='1',charset='utf8')
cursor=conn.cursor()
for x in range(10):
	cursor.execute("insert into s values(%d,'玲珑%d号','%s')"%(x,x,'woshinibaba'))
conn.commit

注意注意
格式化输出是字符串时  %s也要有引号！！！！！！！！！！！！！！！！！！！！！！1

插入或者修改数据的时候必须是双引号！！！

cursor.execute("select *from s")
result=cursor.fetchall()
for x in result:
	print(x)
