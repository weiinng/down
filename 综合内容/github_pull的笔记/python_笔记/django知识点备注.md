django 知识点


获取model表名字
model_name = obj.queryset.model._meta.model_name

获取app名字
app_label = obj.queryset.model._meta.app_label

from django.utils.safestring import mark_safe
和前端页面 safe 同理 让标签字符串可以正确渲染成标签

valurs 的本质：循环每个字段，生成字典 字段为键，查询的为值，(字典一个键只能有一个值) 因此会有重复数据
	用 .distinctu() 去重


根据字符串取出来每个model字段对象
title_obj = field_obj._meta.get_field("title")
title_max_length = title.max_length  	# 32 	# 可以拿出来字段的属性对应的值
title.rel.to.objects.all() 	# 根据字段对象可取出来映射关联表的所有内容

根据字符串取出来每个forms字段对象
from django.forms.boundfield import BoundField
for bfield in form :
	bfield.field # 每个字段对象
	bfield.field.queryset.model # 每个字段对象关联的表
	bfield.name  # 每个字段名字

return redirect(request.path) 重定向到当前页面

if request.is_ajax()： 判断请求是否是 ajax 

from django.forms.models import mode_to_dict 	将对象转换成字典
dict = mode_to_dict(obj) 

from django.core import serializers
serializers.serializers("json",obj)  	将对象装换成 json 对象


update_or_create 有的话酒更新，没有的话就创建		
UserToken.objects.update_or_create(user=user_obj,defaults={"token":token})	

Django model中数据批量导入bulk_create()
	create 会返回 创建的对象
	同理 form.save 也是返回对象
	update 会返回更新条数   

form字段对象在前端显示的时候特殊点
	limit_choice_to 转换成 forms 的时候进行一次过滤后显示
		gender = models.IntegerField(verbose_name='性别', limit_choice_to = {"depart":[1005,1006]})
		Customer.objects.filter(depart__in[1005,1006]).valurs("pk0","title")
	choices属性 渲染成form的时候前端可以选择显示 (choices属性 在所有字段中都可以使用)
		
		gender = models.IntegerField(verbose_name='性别', choices = [(1,"男"),(2,"女")])
		obj = Customer.objects.create(gender=1)	# 保存在数据库的是 "1" 而不是 "男"
		obj.gender   # 1
		obj.get_gender_dispaly()  # 男










