ORM 操作
	必知必会13条
		<1> all():                 查询所有结果
		<2> filter(**kwargs):      它包含了与所给筛选条件相匹配的对象
		<3> get(**kwargs):         返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。
		<4> exclude(**kwargs):     它包含了与所给筛选条件不匹配的对象
		<5> values(*field):        返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列model的实例化对象，而是一个可迭代的字典序列
		<6> values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
		<7> order_by(*field):      对查询结果排序
		<8> reverse():             对查询结果反向排序，请注意reverse()通常只能在具有已定义顺序的QuerySet上调用(在model类的Meta中指定ordering或调用order_by()方法)。
		<9> distinct():            从返回结果中剔除重复纪录(如果你查询跨越多个表，可能在计算QuerySet时得到重复的结果。此时可以使用distinct()，注意只有在PostgreSQL中支持按字段去重。)
		<10> count():              返回数据库中匹配查询(QuerySet)的对象数量。
		<11> first():              返回第一条记录,  .all().first 等效于 .first() 
		<12> last():               返回最后一条记录
		<13> exists():             如果QuerySet包含数据，就返回True，否则返回False
	
		返回QuerySet对象的方法有
			all()
			filter()
			exclude()
			order_by()
			reverse()
			distinct()	
				
		特殊的QuerySet
			values()       返回一个可迭代的字典序列
			values_list() 返回一个可迭代的元祖序列	
				具体的对象是无法使用这两个方法的
					原理上来说models.py 里面的 class类 中就没有 这两个属性
					这两个属性只针对于一个QuerySet序列集进行筛选才可以使用
					比如 .filter(id=1) 虽然只返回了一个QuerySet对象 但是也可以使用
					
		返回具体对象的
			get()
			first()
			last()
				对象可以直接 .属性 的方法去取值
					原理上来说在数据库对象的里面就有属性自然是可以知己调用的
		
		返回布尔值的方法有：
			exists()
		
		返回数字的方法有
			count()
		
		关于返回具体对象和QuerySet对象的区别
			具体对象可以直接 .属性 的方法去取值
				本质上来说具体对象就是 models.py 里面的 class类的实例化,本身就有属性可以自己调用
				具体的对象是无法使用values()和values_list()的因为自己的属性里面就没有
				具体的对象也没有 .update() 方法,在QuerySet对象才可以调用
 			QuerySet对象可以调用values()和values_list()
				这两个属性只针对于一个QuerySet序列集进行筛选才可以使用
				比如 .filter(id=1) 虽然只返回了一个QuerySet对象 但是也可以使用
				
	单表查询之神奇的双下划线	
		models.Tb1.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值
		models.Tb1.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
		models.Tb1.objects.exclude(id__in=[11, 22, 33])  # not in
		models.Tb1.objects.filter(name__contains="ven")  # 获取name字段包含"ven"的
		models.Tb1.objects.filter(name__icontains="ven") # icontains大小写不敏感
		models.Tb1.objects.filter(id__range=[1, 3])      # id范围是1到3的，等价于SQL的bettwen and 左右都包含
		类似的还有：startswith，istartswith, endswith, iendswith　
		date字段还可以单独将年月日拿出来
		models.Class.objects.filter(birtday__year=2017)
		models.Class.objects.filter(birtday__month=7)
		models.Class.objects.filter(birtday__day=17)
	
	ForeignKey操作
		正向查找
			对象查找（跨表）
				语法：
					对象.关联字段.字段
				示例：
					book_obj = models.Book.objects.first()  # 第一本书对象
					print(book_obj.publisher) 				# 得到这本书关联的出版社对象
					print(book_obj.publisher.name)  		# 得到出版社对象的名称
			字段查找（跨表）
				语法：
					关联字段__字段	
						一个双下划綫就代表跨了一张表
				示例：
					# 查询id为1 的书的出版社的名字
					print(models.Book.objects.filter(id=1).values("publisher__name"))
		反向操作
			对象查找
				语法：
					obj.表名_set
				示例：
					publisher_obj = models.Publisher.objects.first()    # 找到第一个出版社对象
					books = publisher_obj.book_set.all()  				# 找到第一个出版社出版的所有书
					books_titles = books.values_list("title")  				# 找到第一个出版社出版的所有书的书名
			字段查找
				语法：
					表名__字段
				示例：
					books_titles = models.Publisher.objects.values_list("book__title")
	
	ManyToManyField	
		利用 关联管理器 进行维护: 
			外键关系的反向查询
			多对多关联关系
		create()
			创建一个新的对象，保存对象，并将它添加到关联对象集之中，返回新创建的对象。
				models.Author.objects.first().book_set.create(title="羊驼之歌", publish_id=2)
		add()
			把指定的model对象添加到关联对象集中。
			添加对象
			>>> author_objs = models.Author.objects.filter(id__lt=3)
			>>> models.Book.objects.first().authors.add(*author_objs)
			添加id
			>>> models.Book.objects.first().authors.add(*[1, 2])
		set()
			更新model对象的关联对象。
				book_obj = models.Book.objects.first()
				book_obj.authors.set([2, 3])
		remove()
			从关联对象集中移除执行的model对象
				book_obj = models.Book.objects.first()
				author_obj.books.remove(book_obj)
				author_obj.books.remove(8)	# 把id = 8 的书删
		clear()
			从关联对象集中移除一切对象。
			book_obj = models.Book.objects.first()
			book_obj.authors.clear()
			注意：
			对于ForeignKey对象，clear()和remove()方法仅在null=True时存在。
			举个例子：
				
					# ForeignKey字段没设置null=True时，
					class Book(models.Model):
						title = models.CharField(max_length=32)
						publisher = models.ForeignKey(to=Publisher)
				
					# 没有clear()和remove()方法：
					>>> models.Publisher.objects.first().book_set.clear()
					Traceback (most recent call last):
					  File "<input>", line 1, in <module>
					AttributeError: 'RelatedManager' object has no attribute 'clear'
				
					# 当ForeignKey字段设置null=True时，
					class Book(models.Model):
						name = models.CharField(max_length=32)
						publisher = models.ForeignKey(to=Class, null=True)
				
					# 此时就有clear()和remove()方法：
					dels.Publisher.objects.first().book_set.clear()
		
		注意：对于所有类型的关联字段，add()、create()、remove()和clear(),set()都会马上更新数据库。换句话说，在关联的任何一端，都不需要再调用save()方法。	
		
	聚合
		导入:
			from django.db.models import Avg, Sum, Max, Min, Count
		
		示例:
			>>> from django.db.models import Avg, Sum, Max, Min, Count
			>>> models.Book.objects.all().aggregate(Avg("price"))
				{'price__avg': 13.233333}
			
			# 指定名称
			>>> models.Book.objects.aggregate(average_price=Avg('price')) 
				{'average_price': 13.233333}
			
			# 多次聚合
			>>> models.Book.objects.all().aggregate(Avg("price"), Max("price"), Min("price"))
			{'price__avg': 13.233333, 'price__max': Decimal('19.90'), 'price__min': Decimal('9.90')}
	
	分组
		命令
			Employee.objects.values("dept").annotate(avg=Avg("salary").values(dept, "avg")
		示例
			统计每一本书的作者个数
				book_list = models.Book.objects.all().annotate(author_num=Count("author"))
			
			统计出每个出版社买的最便宜的书的价格
				publisher_list = models.Publisher.objects.annotate(min_price=Min("book__price"))
				publisher_list = models.Book.objects.values("publisher__name").annotate(min_price=Min("price"))
		
			统计不止一个作者的图书
				book_list = models.Book.objects.annotate(author_num=Count("author")).filter(author_num__gt=1)
			
			根据一本图书作者数量的多少对查询集 QuerySet进行排序
				book_list = models.Book.objects.annotate(author_num=Count("author")).order_by("author_num")
			
			查询各个作者出的书的总价格
				author_list = models.author.annotate(sum_price=Sum("book__price")).values("name", "sum_price"))
	
	F查询
		概念
			对于基础的两个值得比较可以通过上面的方法实现
			但是对于两个字段的比较则需要用到 F 查询
		示例
			查询评论数大于收藏数的书籍
				from django.db.models import F
				models.Book.objects.filter(commnet_num__gt=F('keep_num'))
			
			Django 支持 F() 对象之间以及 F() 对象和常数之间的加减乘除和取模的操作。
				models.Book.objects.filter(commnet_num__lt=F('keep_num')*2)
			
			对整个字段的所有值的操作也可以通过 F 函数实现
			比如将每一本书的价格提高30元
				models.Book.objects.all().update(price=F("price")+30)
			
			关于修改 char 字段的操作
			把所有书名后面加上(第一版)
			>>> from django.db.models.functions import Concat
			>>> from django.db.models import Value
			>>> models.Book.objects.all().update(title=Concat(F("title"), Value("("), Value("第一版"), Value(")")))
	
	Q查询
		概念
			当使用filter 的时候 ,内部多个筛选条件是 and 的关系
			若需求为 or 的关系需要用到 Q 查询
		示例
			查询作者名是羊驼或山羊的
				models.Book.objects.filter(Q(authors__name="羊驼")|Q(authors__name="山羊"))
		复杂示例
			可以组合& 和|  操作符以及使用括号进行分组来编写任意复杂的Q 对象。同时，Q 对象可以使用~ 操作符取反，这允许组合正常的查询和取反(NOT) 查询。
			查询作者名字是羊驼之歌并且不是2018年出版的书的书名。
				models.Book.objects.filter(Q(author__name="羊驼之歌") & ~Q(publish_date__year=2018)).values_list("title")
		注意 
			当 and 和 or 同时一起用的时候 , Q 查询需要放在前面
			示例
				查询出版年份是2017或2018，书名中带羊驼的所有书。
					models.Book.objects.filter(Q(publish_date__year=2018) | Q(publish_date__year=2017), title__icontains="羊驼")
	
	锁
		限制住当前查询结束后才可以其他的操作.保证数据的可靠性
			select_for_update(nowait=False, skip_locked=False)
		示例
			entries = Entry.objects.select_for_update().filter(author=request.user)
		
		
		
		
		
		
		
		
		