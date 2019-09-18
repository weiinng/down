"""
* 了解
*** 重点 
***** 重点中的重点
"""



*** MySQL 引擎有哪些？ 有什么区别？如何指定引擎?
	"""
		mysaim	
			MySQL 数据库 默认引擎  
			不支持事务
			查询速度更快一些 
			只支持 表锁 
		innodb 
			支持事务
			支持行锁 加 表锁 
			
			
		在 表创建的时候  通过 ENGINE=InnoDB 来指定引擎
	"""

*** 锁？有什么用？ 什么时候用？ 怎么用？ 
	"""
		在计数的时候用的最多 ，尽量加行锁
		begin;
		seleck * from tb1 for update; 
		update tb1 set name="yang" where id=2;
		commit;
	"""
	
*** 后端语言中怎么加锁呢？
	"""
	pymysql 
		cursor.execute("seleck * from tb1 for update")
	django
		with trancation.automic():
			model.User.object.all().for_update()
	"""

*** 表结构的设计，比如你帮我设计一个 学校的代码统计 需要什么表？
	"""
		班级表
		用户表
		代码统计表 
		
		
		注意要问 一个用户是否可以报多个班级，这样才考虑是否使用 多对多关系映射 
	"""

***** SQL 语句
	"""
		https://www.cnblogs.com/wupeiqi/articles/5729934.html
	"""

* 视图
	"""
		对一个 SQL 语句起别名保存起来，然后以后对于这个 SQL 语句的使用，直接用过别名
		相当于将 此语句的结果 虚拟成了一个虚拟表 (不真正存在，保存的仅仅是语句本身，且存在数据库中)
		
		create view v1 as select nid.name from table1 where nid>4;
		
		seleck * from v1;
		
		https://www.cnblogs.com/wupeiqi/articles/5713323.html
	"""

* 存储过程
	"""
		和函数类似。但是比函数功能要更强大，再传参数的进行运算的过程还可以再对 SQL 语句进行执行
		主要对结果集和返回结果进行复杂操作 ，保存在 数据库中 
		
		-- 创建存储过程
			delimiter \\
			create procedure p1(
				in i1 int,
				in i2 int,
				inout i3 int,
				out r1 int
			)
			BEGIN
				DECLARE temp1 int;
				DECLARE temp2 int default 0;
				
				set temp1 = 1;

				set r1 = i1 + i2 + temp1 + temp2;
				
				set i3 = i3 + 100;

			end\\
			delimiter ;

		-- 执行存储过程
			set @t1 =4;
			set @t2 = 0;
			CALL p1 (1, 2 ,@t1, @t2);
			SELECT @t1,@t2;

		
		https://www.cnblogs.com/wupeiqi/articles/5713323.html
	"""

* 触发器
	"""
		对某张表进 增加，删除，修改的前后，自定义一系列操作
		保存在 数据库中
		https://www.cnblogs.com/wupeiqi/articles/5713323.html
	"""

* 函数 
	"""
		对数据进行操作的的一个额外途径，只能返回一个数据库能够识别的值
		
		自定义函数 
			delimiter \\
			create function f1(
				i1 int,
				i2 int)
			returns int
			BEGIN
				declare num int;
				set num = i1 + i2;
				return(num);
			END \\
			delimiter ;
		
		使用函数
			# 获取返回值
			declare @i VARCHAR(32);
			select UPPER('alex') into @i;
			SELECT @i;


			# 在查询中使用
			select f1(11,nid) ,name from tb2;
	"""
	
***** 索引 
	"""
	索引作用：加速查找+约束。
	
	索引种类：
		
		- 主键索引：加速查找、唯一、非空
				
		- 唯一索引：加速查找、唯一、
			（可以为空，只是只能有一个为空，第二个为空就和上一个空重复了）
			
		- 普通索引：加速查找
			
		- 联合索引：加速查找
			
		- 联合唯一索引：加速查找、唯一
			（唯一 为两列货多列数据不重复 ）
			
		PS：联合索引遵循最左前缀原则。必须基于最左边的第一个来命中才可以
			id   name   pwd   email 
			# √ 
			select * from tb where name='x' 
			select * from tb where name='x' and pwd='123'
			select * from tb where name='x' and pwd='123' and email='xs'
			# X
			select * from tb where pwd='123'
			select * from tb where pwd='123' and email='xs'
			
		
	名词：
		- 覆盖索引：在索引文件中就可以把想要的数据得到。便无需再在物理表中进行查询 
			select name from tb1;
		- 索引合并：使用多个单列索引去查找数据。
		
	创建索引，但是无法命中索引
		select * from tb1 where name='alex';
	
			- like '%xx'
				select * from tb1 where name like '%cn';
			- 使用函数
				select * from tb1 where reverse(name) = 'wupeiqi';
			- or
				select * from tb1 where nid = 1 or email = 'seven@live.com';
				特别的：当or条件中有未建立索引的列才失效，以下会走索引
						select * from tb1 where nid = 1 or name = 'seven';
						select * from tb1 where nid = 1 or email = 'seven@live.com' and name = 'alex'
			- 类型不一致
				如果列是字符串类型，传入条件是必须用引号引起来，不然...
				select * from tb1 where name = 999;
			- !=
				select * from tb1 where name != 'alex'
				特别的：如果是主键，则还是会走索引
					select * from tb1 where nid != 123
			- >
				select * from tb1 where name > 'alex'
				特别的：如果是主键或索引是整数类型，则还是会走索引
					select * from tb1 where nid > 123
					select * from tb1 where num > 123
			- order by
				select email from tb1 order by name desc;
				当根据索引排序时候，选择的映射如果不是索引，则不走索引
				特别的：如果对主键排序，则还是走索引：
					select * from tb1 order by nid desc;
			 
			- 组合索引最左前缀
				如果组合索引为：(name,email)
				name and email       -- 使用索引
				name                 -- 使用索引
				email                -- 不使用索引
		
	"""
	
 *** 数据库优化方案
	 """
	 - 避免使用select * 
		- 固定长度在前面
		- 内存代替表，如：性别等
		- 读写分离
		- 分库
		- 分表
			- 水平分表
			- 垂直分表
		- 命中索引
		- 组合索引代替索引合并
		- 尽量使用短索引
		- 如果取一条数据时，使用limit 1
			select id,name from tb where name ='alex' limit 1;
		- 使用连接（JOIN）来代替子查询(Sub-Queries)


		注意：char/varchar区别	
			char 不可变长度
			varchar 可变长度
	 """
			


1000w条数据，使用limit offset 分页时，为什么越往后翻越慢？如何解决？
	"""
		# 例如:
		#limit 100000,20; 从第十万条开始往后取二十条,
		#limit 20 offset 100000; limit后面是取20条数据,offset后面是从第10W条数据开始读
		因为当一个数据库表过于庞大，LIMIT offset, length中的offset值过大，则SQL查询语句会非常缓慢
		--------------------------------------------------------------------------
		'优化一'
		先查看主键，再分页：
		select * from tb where id in (select id from tb where limit 10 offset 30)
		--------------------------------------------------------------------------
		'优化二'
		记录当前页，数据、ID、最大值和最小值(用于where查询)
		在翻页时，根据条件进行筛选，筛选完毕后，再根据 limit offset 查询
		select * from(select * from tb where id > 2222) as B limit 10 offset 0;
		\如果用户自己修改页码，也可能导致变慢，此时可以对 url 页码进行加密，例如rest framework
		--------------------------------------------------------------------------
		'优化三'
		可以按照当前业务需求，看是否可以设置只允许看前200页；
		一般情况下，没人会咔咔看个几十上百页的；
	"""



















