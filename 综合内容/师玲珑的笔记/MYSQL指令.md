MYSQL常用命令：

数据备份与还原
·注意：不要打分号，不登陆mysql 直接在cmd下运行

1、备份：
·mysqldump -uroot -p123 要备份的数据库名>生成的脚本路径

2、恢复：
·source 脚本文件路径

·端口号为：3306

·默认存储引擎：innodb

·默认字符集：utf-8


MYSQL开启关闭及查询时间版本指令：

·开启MySQL服务			net start mysql 或  sudo service mysql start

·重启服务  		      sudo service mysql restart

·查看看进程中是否存在mysql服务 ps ajx|grep mysql

·进入mysql数据库控制台命令：      mysql -u用户名 -p密码

·查看版本命令：	select version();

·显示当前时间命令： 	select now();

·退出MySQL命令：      quit或exit

·结束MySQL服务			net stop mysql 或  sudo service mysql stop

修改用户名及密码相关指令：
·1、修改密码格式命令：		 set password for 用户名@localhost = password('新密码'); 

·2、修改密码格式命令：		mysqladmin -u用户名 -p旧密码 password 新密码；

·修改用户名命令：
  进入mysql库：		use mysql;
  然后输入：	update user set user ='新用户名' where user ='旧用户名'；


创建库的相关指令：
·创建数据库命令：     create database 数据库名 charset=utf8;

·显示所有的数据库：       show databases；

·删除数据库命令： 	drop database 数据库名；

·导入（连接）数据库命令：        use 数据库名

·查看当前使用的数据库命令：	    select database();

·当前数据库包含的表信息命令：	 show tables;

show create table 表名;      展示详细属性 

建表相关指令：
·创建表命令：		create table 表名 ((字段名 类型 属性)，(字段名 类型 属性));

·修改表名：	      alter table 表名 rename to 新表名；

·获取表结构命令：	desc 表名；   或者   show columns from 表名；

·删除表命令：		drop table 表名；

·修改字段命令：	  alter table 表名 change 原字段名 新字段名 数据类型;

·修改数据类型命令：		alter table 表名 modify 字段名 新数据类型;

·删除一个字段命令：		alter table 表名 drop 字段名;

·将字段1放在字段2后面命令：		alter table 表名 modify 字段名1 数据类型 after 字段名2；

插入数据相关命令：
·插入数据命令： 	   insert into 表名 values (添加的数据,)    #按列表竖列类型添加以，分隔	
			insert into 表名 (字段,字段) values (添加的数据,)
·查看表中所有数据命令：	select * from 表名;

·查看相关类型数据命令：	   select 字段,字段 from 表名;

·查询指定字段命令：		select 字段 from 表名;

·查询前几行数据命令：    	如：查看表中前行数据	   select * from 表名 limit 0,2;

·插入数据类型命令： 		alter table 表名 add 字段 数据类型;
	

·清空表内数据命令：		delete from 表名;

·清空表 自增id，下次从1开始		truncate table 表名;

·第二种
（注意：这个是你通过delete from table 之后 设置的。不然不起作用） 

如果表中的数据还有用，那么需要从特定的某一个值开始自动增长的话，做法如下 
比如你想让id从2开始自动增长，sql如下 

alter table jx_pcmx AUTO_INCREMENT 2; 

alter table jx_pcmx AUTO_INCREMENT 此处写你想让id从几开始增长的数字；


·删除表中数据命令：  	 如：删除表中编号为1的记录    delete from 表名 where id=1;  

·修改表中数据命令：	  update 表名 set 字段=新值 where条件 	如：update 表名 set name=’Mary’where id=1;

·在表中增加字段命令： alter table 表名 add字段 类型 其他;
---例如：在表MyClass中添加了一个字段passtest，类型为int(4)，默认值为空
   mysql> alter table MyClass add passtest int(4) default '';

·选取字段插入多条记录命令：	insert into 表名(字段名1，字段名2,....） values(值1,值2,...),(值1,值2,...)...; 

·全部字段插入多条记录命令：	insert into 表名 values(值1，值2,...),(值1，值2,...)...;

·使用as 给字段起别名命令：	select 原字段名 as 新字段名 from 表名;  查询出来的结果字段名不是原字段名，变成了新字段名

·使用distinct可以消除重复数据		select distinct 字段名,distince 字段名 from student; 查询出来的性别（字段名）和年龄（字段名）没有重复的数据



 MySQL支持多种类型 大致可以分为三类：数值、日期/时间 和 字符串(字符)类型。


常用字段类型：
·整形：
- tinyint(m)      1个字节 范围（-128···127）

- int(m) 	  4个字节 范围（-2147483648···2147483647）

- bigint(m）	  8个字节 范围 （+-9.22*10的18次方）
 
·浮点型：     # 一般应用于身高体重之类
- float(m,d)	  单精度浮点型 8位精度（4字节） m总个数， d小位数 

- double(m,d)	  双精度浮点型 16位精度（8字节） m总个数， d小位数 

·定点数      # 精确值 一般应用于与钱相关之类的
- decimal(m,d)	  参数 m < 65 是总个数，d<30 且 d<m 是小位数

·字符串：
- chr(n) 	  固定长度 最多255个字符   # 查询速度快，但占固定内存，空间消耗大

- varchar(n)	  不固定长度 最多65535个字符    #占用内存灵活，节省空间，但查询速度慢

- text 		  可变长度，最多65535个字符   # 不确定长度时使用

- 小总结：
 char比varchar查询更快
 varchar比char占用资源少
 char是定长，最多255
 varchar是不定长，最多65535
 char(n)若存入字符数小于n,则以空格补于其后，查询之时再将空格去掉，所以char类型存储的字符串末尾不能有空格，varchar不限于此。
 char(n)固定长度，char(4)不管是存入几个字符，都将占用4个字节，varchar是存入的实际字符数+1个字节（n<=255)或两个字节(n>255),所以varchar(4)存入3个字符都将占用4个字节
 decimal(m,n)非常精确的小数



时间/日期类型：
·date				日期  如：'2018-12-5'

·time				时间 如：'12:33:55'

·datetime			日期时间   如:'2018-12-2 22:06:44'

·timestamp			自动存储记录修改时间


数据类型的属性：
·null 				数据可包含null值

·not null 			数据不可包含null值

·default			默认值

·primary key			主键

·auto_increment		自动递增，适用于整数类型

·unsigned			无符号

·character set 		指定一个字符集
  name

·bit				称为位数据类型 0是假 1是真 作为逻辑变量使用，用来表示真、假或是、否等二值选择

常用权限的解释：
·file			在MySQL服务器上读写文件。

·process		显示或杀死属于其它用户的服务线程。

·reload		重载访问控制表，刷新日志等。

·shutdown		关闭MySQL服务


数据库/数据表/数据列权限：
·alter 		修改已存在的数据表(例如增加/删除列)和索引。

·create		建立新的数据库或数据表。

·delete		删除表的记录。

·drop			删除数据库或数据表

·index			建立或删除索引

·insert		增加表的记录

·select		显示/搜索表的记录

·update		修改表中已存在的记录

·enum			枚举类型

特别的权限：
·all			允许做任何事（和root一样）

·usage			只允许登录–其它什么也不允许做。



条件查询：
 使用where子句对表中的数据筛选，结果为true的行会出现在结果集中
 where后面支持多种运算符，进行条件的处理

·比较运算符：  >    <   <=     >=     =   !=    is
		select * from 表名 where 条件;

·逻辑运算符：and   or   not 
		select * from 表名 where 条件;

·范围查询	between...and...
例：	  （左闭右闭，左右都包含）
    select 字段 from 表名 where 字段 between 开始区间 and 结束区间；

·模糊查询	like 	%表示任意多个任意字符	_表示一个任意字符
 例：		%  和 _ 可以加在任意位置、
	select * from 表名 where 字段 like '字符元素%';
	select * from 表名 where 字段 like '%字符元素';	
	select * from 表名 where 字段 like '字符元素_';
	select * from 表名 where 字段 like '_字符元素';

·判非空	is not null
例：	select * from 表名 where  字段 is not null;


优先级：
优先级由高到低的顺序为：小括号，not，比较运算符，逻辑运算符
and比or先运算，如果同时出现并希望先算or，需要结合()使用


·排序：	默认升序			升序|降序
  语法：	select * from 表名 order by 字段名 asc|desc 

说明：
将行数据按照列1进行排序，如果某些行列1的值相同时，则按照列2排序，以此类推
默认按照列值从小到大排列（asc）
asc从小到大排列，即升序
desc从大到小排序，即降序
多次排序优先执行前面的命令


聚合函数：
·总数：	count(*) 表示计算总行数，括号中写星与列名，结果是相同的
	select count(*) from 表名;

·最大值：	max(字段名) 表示求此列的最大值
	select max(字段名) from 表名;  或 select max(字段名1) from 表名 where 字段名2=定值;

·最小值：	min(字段名) 表示求此列的最小值
	select min(字段名) from 表名;  或 select min(字段名1) from 表名 where 字段名2=定值;

·求和：	sum(字段名)表示求此列的和
	select sum(字段名) from 表名;  或 select sum(字段名1) from 表名 where 字段名2=定值;

·平均值：	avg(字段名)表示求此列的平均值
	select avg(字段名) from 表名;  或 select avg(字段名1) from 表名 where 字段名2=定值 and 字段名3=定值;

·分组：	group by
	select 字段名1 from 表名 group by 字段名1;  或 select avg(字段名1) from 表名 where 字段名2=定值 and 字段名3=定值;
说明：
       group by的含义:将查询结果按照1个或多个字段进行分组，字段值相同的为一组
       group by可用于单个字段分组，也可用于多个字段分组


这些还可以这么用：
· 语法注意：  select @1,字段1 from 表名 group by 字段1 
	或 select 字段1,@1 from 表名 where 条件 group by 字段1;
          @1  ---  位置只能放聚合函数、group_concat和分组的字段

·统计分组：
例：	 select avg(字段名1),字段名2 from 表名 group by 字段名2;
例：	 select count(字段名1),字段名2 from 表名 group by 字段名2;

·嵌套查询：
例：	 select *from 表名 where 字段名1=(select min(字段名1) from 表名);

·group by + group_concat()	
    group_concat(字段名)可以作为一个输出字段来使用，
    表示分组之后，根据分组结果，使用group_concat()来放置每一组的某字段的值的集合
 例：	select 字段名1,group_concat(字段名2) from 表名 group by 字段名1；
     或 select 字段1,group_concat(字段2) from 表名 where 条件 group by 字段1;
	
·group by + 集合函数
     通过group_concat()的启发，我们既然可以统计出每个分组的某字段的值的集合，那么我们也可以通过集合函数来对这个值的集合做一些操作
例：	select 字段名1,group_concat(字段名2) from 表名 group by 字段名1;
	select 字段名1,count(*) from 表名 group by 字段名;

·group by + having
	having 条件表达式：用来分组查询后指定一些条件来输出查询结果
	本质：having作用和where一样，但having只能用于group by
例：	select gender,count(*) from 表名 group by 字段名 having count(*)>数值;

·group by + with rollup
	with rollup的作用是：在最后新增一行，来记录当前列里所有记录的总和
例：	select 字段名1,count(*) from 表名 group by 字段名1 with rollup;
	select 字段名1,group_concat(字段名2) from 表名 group by 字段名1 with rollup;

完整的select语句顺序：
select distince *
from 表名
where ...
group by ... having ...
order by ...
limit start，count


select  获取查看
from    来自
where   后面加条件
group by   分组
having    对分组后的组进一步筛选 
limit（m,n）   分页  m 起始位置  n 每页多少条数据
count（） 总揽条数 括号里可以加条件 总览某种数据
group_concat()  合并多个分组 括号里添加要合并的数据类型  

·where、having之间的区别和用法
作用的对象不同。WHERE 子句作用于表和视图，HAVING 子句作用于组。
聚合函数是比较where、having 的关键。 
where、聚合函数、having 在from后面的执行顺序：where>聚合函数(sum,min,max,avg,count)>having
列出group by来比较二者。（）因where和having 在使用group by时问的最多） 
若须引入聚合函数来对group by 结果进行过滤 则只能用having。
注意事项 ： 

1、where 后不能跟聚合函数，因为where执行顺序大于聚合函数。 

2、where 子句的作用是在对查询结果进行分组前，将不符合where条件的行去掉，
即在分组之前过滤数据，条件中不能包含聚组函数，使用where条件显示特定的行。

3、having 子句的作用是筛选满足条件的组，即在分组之后过滤数据，条件中经常
包含聚组函数，使用having 条件显示特定的组，也可以使用多个分组标准进行分组。



分页：	
分页：select *from 表名 limit 起始位置start,行数计数count;
   或  select *from 表名 where 条件 limit 起始位置start,行数计数count;

分页翻页
已知：每页显示m条数据，当前显示第n页
求总页数：此段逻辑后面会在python中实现
查询总条数p1
使用p1除以m得到p2
如果整除则p2为总数页
如果不整除则p2+1为总页数
求第n页的数据
例：   select *from 表名 limit (n-1)*m,m;



内连接查询：查询的结果为两个表匹配到的数据
语法1： inner join     on
select *from 左表名 inner join 右表名 on 左表名.两表相关联字段 = 右表名.两表相关联字段;
或 select *from 左表名 inner join 右表名 on 左表名.两表相关联字段 = 右表名.两表相关联字段
 where 右表名.条件字段=值 and 左表名.条件字段>值;

例： 如查看不同年级 每个年级都有谁 每个年级都有多少人
select class.name,group_concat(student.name),count(student.id)
 from student inner join class on
 class.id=student.class_id group by class.name;

语法2：
select 左表名.字段1,group_concat(右表名.字段1),count(右表名.两表相关联字段)
 from 右表名 inner join 左表名 on
 左表名.两表相关联字段=右表名.两表相联关字段 group by 左表名.字段一;



右连接查询：  right join     on
查询的结果为两个表匹配到的数据，右表特有的数据，对于左表中不存在的数据使用null填充

语法：
select *from 右表名 right join 左表名 on 右表名.两表相关联字段 = 左表名.两表相关联字段;



左连接查询：   left join     on
查询的结果为两个表匹配到的数据，左表特有的数据，对于右表中不存在的数据使用null填充

语法：
select *from 左表名 left join 右表名 on 左表名.两表相关联字段 = 右表名.两表相关联字段;






查询表中 某字段重复数据的个数和最多的个数
select 字段1,count(*) as count from 表名 group by 字段1 having max(count);

select 字段1,count(*) as count from 表名 as a group by 字段1 having max(count) order by 字段1,count limit 0,1;

视图 
MySql创建视图
(1).第一类：create view 视图名 as select * from 表名;

(2).第二类：create view 视图名 as select 字段,字段,字段 from 表名;

(3).第三类：create view 视图名v[vid,vname,vage] as select 字段,字段,字段 from 表名
删除视图
drop view 视图名；


mysql中去重          distinct

 
explain select 字段1 from 表名 where 字段1=值;     查看查找次数


create index 索引名 on 表名(相关字段);     加索引

drop index 索引名 on 表名;   删除索引


外键   alter table 表名1 add constraint 外键名字 foreign key(列名1) references 表名2(列名2)；



pymysql 交互：

# -*- coding: UTF-8 -*-
# 引入connect
from pymysql import connect
# 建立连接
conn= connect(host='localhost',port=3306,database='库名',user='用户名',password='密码',charset='utf8')
# 获取cursor对象
cur = conn.cursor()
# 执行sql语句
sql ="sql 语句命令"
cur.execute(sql)
# 取出数据 fetchone 取一条数据   fetchall 取多条数据
data=cur.fetchall()
# 定义一个列表
userlist = []
for i in data:
    # 定义一个字典来存放信息
    userdict = {}
    userdict['字段'] = i[-1]       # 索引位置信息
    userdict['字段'] = i[1]
    userdict['字段'] = i[2]
    userdict['带小数字段'] = float(i[3])
    userlist.append(userdict)  # 添加元素
    # print(data)
#  输出
print(userlist)
#关闭连接
cur.close()
conn.close()


# 导入模块
from pymysql import connect
# 建立连接
ck = connect(host='localhost',port=3306,database='库名',user='用户名',password='密码',charset='utf8')
# 获取cursor对象
con = ck.cursor()
# 执行sql语句
con .execute("sql 命令语句")
# 提交
ck.commit()


'''
host             主机           
localhost        本地主机                   
port             端口              
database         数据库              
user             用户         
password         密码       
charset          字符集         
'''


select name from class where name='二年级';

后续待补。。。。。。

















