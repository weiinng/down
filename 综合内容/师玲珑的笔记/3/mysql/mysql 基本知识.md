alter database 数据库名 character set utf8;
create database 数据库名 charset=utf8;

当一个表数据全部删除时，id设有主键自增，
truncate table 表名;下次id从1开始  原表数据全部删除

要是不想全部删除  则 
alter table 表名 auto_increment 2;
下次id从2开始

优先级  由高到低：
小括号，not,比较运算符，逻辑运算符
and比or先运算，如果同时出现并希望先算or，需要结合（）使用

数据备份与还原
注意：不要打分号，不登陆mysql 直接在cmd下运行

1、备份：
mysqldump -uroot -p123 要备份的数据库名>生成的脚本路径

2】恢复：
source 脚本文件路径

端口号为：3306

默认存储引擎：innodb

默认字符集：utf8

查看所有表
show tables;

查看所有数据库
show databases;

查看表结构
desc 表名;

切换数据库
use 数据库名


decimal(m,n)非常精确的小数

年月日 date
时分秒 time 
年月日时分秒 datetime
文本类型 text  可以添加任意类型数据
unsigned 必须放在前面

数据类型的属性
mysql关键字   		含义
NULL			数据列可包含NULL值
NOT NULL		数据列不允许包含NULL值
DEFAULT			默认值
PRIMARY KEY		主键
AUTO_INCREMENT	自动递增，适用于整数类型
UNSIGNED		无符号
CHARACTER SET name	指定一个字符集

select IFNULL(age,0) from emp;   当age是NULL是默认为0

查看版本：select version();

显示当前时间：select now();

查看当前使用的数据库:select database(); 

修改密码：
set password for root@localhost=password('新密码');

enum('男','女')  当一个字段设定了这个后插入只能插入男或者女!!!

删除表
drop table 表名;

删除数据库
drop database 数据库名;

删除一行数据：
delete from 表名 where 条件;

修改表名：
alter table 表名 rename to 新表名;

修改字段名：
alter table 表名 change 原字段名 新字段名 数据类型;

修改数据类型：
alter table 表名 modify 字段名 新数据类型;

删除一个字段：
alter table 表名 drop 字段名;

将字段1放在字段2后面：
alter table 表名 modify 字段名1 数据类型 after 字段名2；


插入数据
1、选取字段插入多条记录
insert into 表名(字段名1，字段名2,....） values(值1,值2,...),(值1,值2,...)...; 
2、全部字段插入多条记录
insert into 表名 values(值1，值2,...),(值1，值2,...)...;

修改数据
update 表名 set 要修改的字段名=新的值 where 条件;

使用as 给字段起别名
select id as code from student;  查询出来的结果字段名不是id，变成了code

使用distinct可以消除重复数据
select distinct sex, age from student; 查询出来的性别和年龄没有重复的数据

条件查询：
使用where子句对表中的数据筛选，结果为true的行会出现在结果集中
where后面支持多种运算符，进行条件的处理

select concat('我叫',name,'我的年龄是',age) from stu;


比较运算符 ：>,<,<=.>=,=,!=，is

逻辑运算符：and,or,not,

模糊查询：
like'%_'  %可以匹配任意个字符，
_只可以匹配到一个字符

范围查询：
age between 15 and 20  年龄在15到20之间的   
age in(1,2,4,5) 年龄是1，2，4，5的数据

排序：
select name,age,score from student order by age desc,socre asc;
先按年龄进行降序，如果年龄一样再按成绩升序排序


聚合函数
为了快速得到统计数据，经常会用到如下5个聚合函数
总数：
count（*）表示计算数据为非空的总行数，括号中写*和列名结果是相同的
select count(*) from student;

最大值：
max(列名) 表示求此列的最大值
select max(id) from student;

最小值
min(列名) 表示求此列的最小值
select min(id) from student;

求和：
sum(列名）表示求此列的和
select sum(age) from student;

平均值：
avg(列名）表示求此列的平均值
select avg(id) from student;


分组：
group by
group by的含义：将查询结果按照1个或多个字段进行分组，字段值相同的为一组
group by可用于单个字段分组，也可用于多个字段分组

group by+集合函数
通过group_concat()的启发，我们既然可以统计出每个分组的某字段的值的集合，那么我们也可以通过集合函数来对这个值的集合做一些操作

select gender,group_concat(name,age) from stu group by gender;
结果为：
gender   group_concat(age)
男	玲珑11,玲珑12,玲珑13,玲珑14,玲珑15
女	龙12,龙33,龙45,龙51

分别统计性别为男/女的人年龄平均值
select sex,avg(age) from stu group by sex;

group by + having
having条件表达式：用来分组查询后指定一些条件来输出查询结果
having作用和where一样，但having只能用于group by

select sex,count(*) from stu group by sex having count(*)>2;

group by + with rollup
with rollup的作用是：在最后新增一行，来记录当前列里所有记录的总和
select gender,coount(*) from stu group by gender with rollup;

分页
获取部分行
当数据量过大时，在一页查看数据是一件非常麻烦的事情
语法：
select *from 表名 limit start,count;
从start开始，获取count条数据
例如：查看前三行数据：
select *from stu limit 0,3;

求第n页的数据
select *from stu where limit (n-1)*m,m;

连接查询
当查询结果的列来源于多张表时，需要将多张表连接成一个大的数据集，在选择合适的列返回

内连接：
select *from emp inner join dept on emp.deptno=dept.deptno;

外连接
左外连接：
select *from emp left outer join dept on emp.deptno=dept.deptno;
右外连接：
select *from  emp right outer join dept on emp.deptno=dept.deptno;

创建主键：
create table s(
sid int primary key,
name varchar(10)
);

删除主键：
alter table 表名 drop primary key;

主键自增：
create table stu(
id int primary key auto_increment,
name varchar(10)
);

修改表时主键自增：
alter table stu change sid sid int auto_increment;

修改表时删除主键自增：
alter table stu change sid sid int;

非空约束：not null
唯一约束：unique
create table s(
id int not null unique
);

主键约束是唯一的、非空的、还可以被引用
非空约束是非空的
唯一约束是唯一的
非空约束+唯一约束！=主键约束

删除唯一约束
alter table 表名 drop index 列名;

创建外键：
create table s(
id int,
constraint fk_主表名 foreign key(外键字段名) references 主表名(主键字段名)
);

修改增加外键：
alter table 副表名 add constraint fk_主表名 foreign key(外键字段名) references 主表名（主键字段名）；

删除外键：
alter table 副表名 drop foreign key fk_主表名;

注释：
create table s(
id int comment '作者',
age int
);
跟正常效果一样