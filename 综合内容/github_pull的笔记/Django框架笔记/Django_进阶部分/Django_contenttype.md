django组件：contenttype
	组件的作用：可以通过两个字段让表和N张表创建FK关系
	
	表结构：
		from django.db import models
		from django.contrib.contenttypes.models import ContentType
		from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


		class DegreeCourse(models.Model):
			"""学位课程"""
			name = models.CharField(max_length=128, unique=True)
			course_img = models.CharField(max_length=255, verbose_name="缩略图")
			brief = models.TextField(verbose_name="学位课程简介", )


		class Course(models.Model):
			"""专题课程"""
			name = models.CharField(max_length=128, unique=True)
			course_img = models.CharField(max_length=255)

			# 不会在数据库生成列，只用于帮助你进行查询
			policy_list = GenericRelation("PricePolicy")


		class PricePolicy(models.Model):
			"""价格与有课程效期表"""
			content_type = models.ForeignKey(ContentType) # 图中 表 列 # 关联course or degree_course
			object_id = models.PositiveIntegerField()	# 图中 xid 列

			#不会在数据库生成列，只用于帮助你进行添加和查询
			content_object = GenericForeignKey('content_type', 'object_id')


			valid_period_choices = (
				(1, '1天'),
				(3, '3天'),
				(7, '1周'), (14, '2周'),
				(30, '1个月'),
				(60, '2个月'),
				(90, '3个月'),
				(180, '6个月'), (210, '12个月'),
				(540, '18个月'), (720, '24个月'),
			)
			valid_period = models.SmallIntegerField(choices=valid_period_choices)
			price = models.FloatField()

	使用：
		# 1.在价格策略表中添加一条数据
		# models.PricePolicy.objects.create(
		#     valid_period=7,
		#     price=6.6,
		#     content_type=ContentType.objects.get(model='course'),
		#     object_id=1
		# )

		# models.PricePolicy.objects.create(
		#     valid_period=14,
		#     price=9.9,
		#     content_object=models.Course.objects.get(id=1)
		# )

		# 2. 根据某个价格策略对象，找到他对应的表和数据，如：管理课程名称
		# price = models.PricePolicy.objects.get(id=2)
		# print(price.content_object.name) # 自动帮你找到

		# 3.找到某个课程关联的所有价格策略
		# obj = models.Course.objects.get(id=1)
		# for item in obj.policy_list.all():
		#     print(item.id,item.valid_period,item.price)
		#