Django_ORM
	Django项目使用MySQL数据库
		1. 在Django项目的settings.py文件中,配置数据库连接信息：
			DATABASES = {
				"default": {
					"ENGINE": "django.db.backends.mysql",
					"NAME": "你的数据库名称",  # 需要自己手动创建数据库
					"USER": "数据库用户名",
					"PASSWORD": "数据库密码",
					"HOST": "数据库IP",
					"POST": 3306
				}
			}
		2. 在Django项目的__init__.py文件中写如下代码,告诉Django使用pymysql模块连接MySQL数据库:
			import pymysql
			pymysql.install_as_MySQLdb()
	
	Model
		映射关系
			类		--数据表	
			对象	--数据行
			属性	--字段	
		简单示例
			from django.db import models
			class Person(models.Model):
				first_name = models.CharField(max_length=30)
				last_name = models.CharField(max_length=30)
				
	常用字段
		AutoField
			int自增列,必填参 primary_key=True 默认会自动创建一个列名为id的列 
		IntegerField
			一个整数类型,范围在 -2147483648 to 2147483647 
		CharField
			字符类型,必提供max_length参数, max_length表示字符长度 
		DateField
			日期字段,日期格式  YYYY-MM-DD,相当于Python中的datetime.date()实例 
		DateTimeField
			日期时间字段,格式 YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ],相当于Python中的datetime.datetime()实例 
	
	字段合集
		附件 字段合集
	
	字段参数
		null		用于表示某个字段可以为空 
		unique		如果设置为unique=True 则该字段在此表中必须是唯一的  
		db_index	如果db_index=True 则代表着为此字段设置数据库索引 
		default		为该字段设置默认值 
		
	时间字段独有
		DatetimeField、DateField、TimeField这个三个时间字段,都可以设置如下属性 
		auto_now_add		配置auto_now_add=True,创建数据记录的时候会把当前时间添加到数据库 
			可用在生日
		auto_now			配置上auto_now=True,每次更新数据记录的时候会更新该字段 
			可用在最近修改日期
	关系字段
		ForeignKey	外键,一对多
			参数
				1. to				设置要关联的表
				2. to_field			设置要关联的表的字段(不加这个,关联的默认就是 id 字段)
				3. related_name		反向操作使用的字段名,用于代替原反向查询时的'表名_set' 
					栗子:
						class Classes(models.Model):
							name = models.CharField(max_length=32)
						class Student(models.Model):
							name = models.CharField(max_length=32)
							theclass = models.ForeignKey(to="Classes")
						当我们要查询某个班级关联的所有学生（反向查询）时,我们会这么写：
							models.Classes.objects.first().student_set.all()
						
						当我们在ForeignKey字段中添加了参数 related_name 后,
							class Student(models.Model):
								name = models.CharField(max_length=32)
								theclass = models.ForeignKey(to="Classes", related_name="students")
						当我们要查询某个班级关联的所有学生（反向查询）时,我们会这么写：
							models.Classes.objects.first().students.all()
				4. related_query_name	反向查询操作时,双下滑查询的时候可以替换表名
				5. on_delete			当删除关联表中的数据时,当前表与其关联的行的行为
										默认 1.0版本中会设置为on_delete = models.CASCADE
					取值:
						models.CASCADE			删除关联数据,与之关联也删除
							2.0 版本中不会自动添加这个.需要手动添加此参数
						models.DO_NOTHING		删除关联数据,引发错误IntegrityError
						models.PROTECT			删除关联数据,引发错误ProtectedError
						models.SET_NULL			删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空）
						models.SET_DEFAULT		删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值）
						models.SET				删除关联数据,
							a. 与之关联的值设置为指定值,设置：models.SET(值)
							b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象)
							def func():
								return 10

							class MyModel(models.Model):
								user = models.ForeignKey(
									to="User",
									to_field="id",
									on_delete=models.SET(func)
								)
				6. db_constraint			是否在数据库中创建外键约束,默认为True 
											设置成 False 后,将取消约束,即软关联.
											通常我们都是用代码去限制关联,而不是通过数据库
											数据库设置的外键管理太死了,不灵活,后续维护麻烦
											设置成False 后相当于此外键失效的意思 
								
		
		OneToOneField  一对一关联
			参数
				1. to			设置要关联的表 
				2. to_field	设置要关联的字段 
				3. on_delete	同ForeignKey字段 
		
		ManyToManyField	多对多
			参数
				1. to					设置要关联的表
				2. related_name		同ForeignKey字段 
				3. related_query_name	同ForeignKey字段 
				4. symmetrical			仅用于多对多自关联时,指定内部是否创建反向操作的字段 默认为True
					栗子
						class Person(models.Model):
							name = models.CharField(max_length=16)
							friends = models.ManyToManyField("self")
						此时,person对象就没有person_set属性 

						class Person(models.Model):
							name = models.CharField(max_length=16)
							friends = models.ManyToManyField("self", symmetrical=False)
						此时,person对象现在就可以使用person_set属性进行反向查询 
				5. through				使用ManyToManyField字段,Django将自动生成一张表来管理多对多的关联关系 
										手动创建第三张表来管理多对多关系,需要通过through来指定第三张表的表名 
				6. through_fields		设置关联的字段 
				7. db_table				默认创建第三张表时,数据库中表的名称 
	
	多对多关联关系的三种方式 
		方式一：自行创建第三张表
			class Book(models.Model):
				title = models.CharField(max_length=32, verbose_name="书名")
			class Author(models.Model):
				name = models.CharField(max_length=32, verbose_name="作者姓名")
			# 自己创建第三张表,分别通过外键关联书和作者
			class Author2Book(models.Model):
				author = models.ForeignKey(to="Author")
				book = models.ForeignKey(to="Book")
				class Meta:
					unique_together = ("author", "book")
		方式二：通过ManyToManyField自动创建第三张表
			class Book(models.Model):
				title = models.CharField(max_length=32, verbose_name="书名")
			# 通过ORM自带的ManyToManyField自动创建第三张表
			class Author(models.Model):
				name = models.CharField(max_length=32, verbose_name="作者姓名")
				books = models.ManyToManyField(to="Book", related_name="authors")
		方式三：设置ManyTomanyField并指定自行创建的第三张表
			class Book(models.Model):
				title = models.CharField(max_length=32, verbose_name="书名")
			# 自己创建第三张表,并通过ManyToManyField指定关联
			class Author(models.Model):
				name = models.CharField(max_length=32, verbose_name="作者姓名")
				books = models.ManyToManyField(to="Book", through="Author2Book", through_fields=("author", "book"))
				# through_fields接受一个2元组（'field1','field2'）：
				# 其中field1是定义ManyToManyField的模型外键的名（author）,field2是关联目标模型（book）的外键名 
			class Author2Book(models.Model):
				author = models.ForeignKey(to="Author")
				book = models.ForeignKey(to="Book")
				class Meta:
					unique_together = ("author", "book")
		取舍
			当我们需要在第三张关系表中存储额外的字段时,就要使用第三种方式 
			但是当我们使用第三种方式创建多对多关联关系时,
			就无法使用set、add、remove、clear方法来管理多对多的关系了,
			需要通过第三张表的model来管理多对多关系 

		元信息
			ORM对应的类里面包含另一个Meta类,而Meta类封装了一些数据库的信息 主要字段如下:
				db_table			ORM在数据库中的表名默认是 app_类名,可以通过db_table可以重写表名 
				index_together		联合索引 
				unique_together		联合唯一索引 
				ordering			指定默认按什么字段排序 
					只有设置了该属性,我们查询到的结果才可以被reverse()
			栗子:
				class Author2Book(models.Model):
					author = models.ForeignKey(to="Author")
					book = models.ForeignKey(to="Book")
					def __str__(self):
						return self.name
					class Meta:
						db_table = "author2book"
						unique_together = ("author", "book")
		