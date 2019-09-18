** 可以将字典拆出来以键值对的方式
* 可以列表打散 
models.UserInfo.objects.create_user(**form_obj.cleaned_data)
book_obj.authors.add(*author_pk_list)

ajax 提交的时候不要用 input type="submit"  用 button 


MySQL内置的时间格式化方法:
	可以将一个时间内容的字段格式化成想要额格式后输出便于分组筛选
	date_format(字段名,"被格式化的格式:如%Y-%m")

HTML 页面的对时间的格式化方法"
	时间数据后面加|date:"Y-m-d H:i"
	{{ comment.create_time|date:"Y-m-d H:i" }}


import datatime
now = datatime.datatime.now()  # 当前时间
datatime.datatime	# 日期加时间
datatime.time		# 时间
datatime.date		# 日期
datatime.timedelta(day=3)		# 时间片 可以取出来所有的时间类型
# 都是对象，没办法直接加减，但是通过 timedelta 可以进行加减操作
now - datatime.timedelta(day=3) # 现在减去3天的时间 

# 随机生成字符串
import uuid
uid = str(uuid.uuid4())  



判断字段类型是否是多对多或者一对多字段
from django.db.models.fields.related import ManyToManyField,ForeignKey
isinstance(bfield.field,ModelChoiceField)




callable(filed) 检查filed 是否是个可执行对象类





def foo(action=None,**kwargs)"
	print(action)
	print(kwargs)
	
foo(**{"a":"1"}) 	# **{} 等同于关键字传参 
# {"a":"1"}
# None
foo({"a":"1"} )		
# None
# {"a":"1"}		
		

		
print(0 and 1)		
# 0	
# 0 and 任何值都是0 没必要看后面的了直接就是0 
print(3 and 0)		
# 0	
# 3 and 后米娜不知道是什么没法判断。必须要读后面的值，后面值是0 因此为0
print(0 or 1)		
# 1	
# 0 or 后面不知道是什么没办法判断，需要读后面的，后面为1 因此为1
print(4 or 0)		
# 4	
# 4 or 后面是啥都无无所谓了没必要判断了。直接就是 4 了
print(4 or 10)		
# 4	
# 4 or 后面是啥都无无所谓了没必要判断了。直接就是 4 了
	总结： 
		and  且  如果有个0了，那就怎么都不会成立了，上来读个0 那就没必要读后面了，肯定是0
		or   或  如果有个1了，那就怎么都成立了，上来来个1，那就没必要读后面了。肯定是个1 

os.work(path) 循环一个文件夹里面的所有文件 会返回三个值 
	（“当前的路径”，“当前路径下的所有文件夹”，“当前路径下的文件”）















