"""
ORM补充1：
	- only	只取某些去除其他
	- defer	去除某些取其他
	- selected_related 主动连表查询	一般这个就够用了
	- prefetch_related 进阶版连表查询 最优方案
"""


# 需求: 只取某n列
queryset=[ {},{}]
models.User.objects.all().values( 'id','name')

queryset=[ (),()]
models.User.objects.all().values_list( 'id','name')

queryset=[ obj,obj]
result = models.User.objects.all().only('id','name','age')
# result = models.User.objects.all().defer('id','name','age')
for item in reuslt:
	print(item.id,item.name,item.age)



# 需求: 打印所有用户姓名以及部门名称
	class depart:
		title = ....
	class User:
		name = ...
		dp = FK(depart)
	# select * from user
	# result = models.User.objects.all()
	# for item in result:	# 性能低，会跨表 相当于你查10个人就跨表查了10次+本来1次
	# 但是如果连表太多。那性能也会变差，因为表太多了
	# 	print(item.name,item.dp.title)

	# select * from user left join depart on user.dp_id = depart.id
	# result = models.User.objects.all().selected_related('dp') # 主动创建了关联关系。一次查表就可以拿出来
	# for item in result: # 就不会在发请求查询了，性能更好了
		#print(item.name,item.dp.title )

	# select * from user
	# 通过python 代码获取 dp_id= [1,2]
	# select * from depart where id in dp_id
	result = models.User.objects.all().prefetch_related('dp')
	for item in result: # 相当于查了两次。但是不会因为连表太多影响性能了
		print(item.name,item.dp.title )





"""
orm 补充2：
	- 通过ORM写偏原生SQL：
"""

# - extra
Entry.objects.extra(select={'new_id': "select col from sometable where othercol > %s"}, select_params=(1,))
Entry.objects.extra(where=['headline=%s'], params=['Lennon'])
Entry.objects.extra(where=["foo='a' OR bar = 'a'", "baz = 'a'"])
Entry.objects.extra(select={'new_id': "select id from tb where id > %s"}, select_params=(1,), order_by=['-nid'])


"""----------------------------------- """


# - raw
	# 执行原生SQL
models.UserInfo.objects.raw('select * from userinfo')
	# 如果SQL是其他表时，必须将名字设置为当前UserInfo对象的主键列名
models.UserInfo.objects.raw('select id as nid from 其他表')
	# 为原生SQL设置参数
models.UserInfo.objects.raw('select id as nid from userinfo where nid>%s', params=[12,])
	# 指定捆绑条件后跨表查询
name_map = {'first': 'first_name', 'last': 'last_name', 'bd': 'birth_date', 'pk': 'id'}
Person.objects.raw('SELECT * FROM some_other_table', translations=name_map)


"""----------------------------------- """


# - 完全执行原生SQL
from django.db import connection, connections
cursor = connection.cursor()  # cursor = connections['default'].cursor()
cursor.execute("""SELECT * from auth_user where id = %s""", [1])
row = cursor.fetchone() # fetchall()/fetchmany(..)
	# PS: 选择数据库 using('default') 默认是  default
queryset = models.Course.objects.using('default').all()



































