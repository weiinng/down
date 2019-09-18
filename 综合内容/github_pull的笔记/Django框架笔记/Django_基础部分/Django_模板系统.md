Django模板系统
	常用语法
		{{}} 变量相关
		{%%} 逻辑相关
	变量
		格式
			{{ 变量名 }}
		命名规则
			包括任何字母数字以及下划线 ("_")的组合
			变量名称中不能有空格或标点符号
		示例
			# view中代码
			def template_test(request):
				a = [11, 22, 33]
				d = {"name": "yangtuo"}

				class Person(object):
					def __init__(self, name, age):
						self.name = name
						self.age = age

					def dream(self):
						return "{} is dream...".format(self.name)

				yangtuo = Person(name="yangtuo", age=14)
				yt = Person(name="yt", age=16)
				ytt = Person(name="ytt", age=18)

				person_list = [yangtuo, yt, ytt]
				return render(request, "template_test.html", {"a": l, "d": d, "person_list": person_list})
			
			{#模板中支持的写法#}
			{# 取l中的第一个参数 #}
			{{ l.0 }}
			{# 取字典中key的值 #}
			{{ d.name }}
			{# 取对象的name属性 #}
			{{ person_list.0.name }}
			{# .操作只能调用不带参数的方法 #}
			{{ person_list.0.dream }}
	
	Filters（过滤器）	
		在Django的模板语言中，通过使用 过滤器 来改变变量的显示。

		基本语法： 
			{{ value|filter_name:参数 }}
			使用管道符"|"来应用过滤器。
		注意点:
			过滤器支持“链式”操作。即一个过滤器的输出作为另一个过滤器的输入。
			过滤器可以接受参数，例如：{{ sss|truncatewords:30 }}，这将显示sss的前30个词。
			过滤器参数包含空格的话，必须用引号包裹起来。比如使用逗号和空格去连接一个列表中的元素，如：{{ list|join:', ' }}
			'|'左右没有空格没有空格没有空格						
		常用的过滤器
			default
				如果一个变量是false或者为空，使用给定的默认值。 否则，使用变量的值。
				{{ value|default:"nothing"}}
				如果value没有传值或者值为空的话就显示nothing
			length
				返回值的长度，作用于字符串和列表。
				{{ value|length }}
				返回value的长度，如 value=['a', 'b', 'c', 'd']的话，就显示4.			
			filesizeformat
				将值格式化为一个 “人类可读的” 文件尺寸 （例如 '13 KB', '4.1 MB', '102 bytes', 等等）。例如：
				{{ value|filesizeformat }}
				如果 value 是 123456789，输出将会是 117.7 MB。
			slice
				切片
				{{value|slice:"2:-1"}}
			date
				格式化
				{{ value|date:"Y-m-d H:i:s"}
				可选参数:
					图片1
					图片2
			safe
				为了安全起见,Django的模板中会对HTML标签和JS等语法标签进行自动转义让其无法正确显示为标签
				但是有些HTML元素不希望被转义的时候,可用safe作为标识阻止Django模板的转意
					value = "<a href='#'>点我</a>"
					{{ value|safe}}	 
			truncatechars
				如果字符串字符多于指定的字符数量，那么会被截断。截断的字符串将以可翻译的省略号序列（“...”）结尾。
				参数：截断的字符数
				{{ value|truncatechars:9}}
			cut
				移除value中所有的与给出的变量相同的字符串
				{{ value|cut:' ' }}
				如果value为'i love you'，那么将输出'iloveyou'.
			join
				使用字符串连接列表，例如Python的str.join(list)
			timesince
				表示出设定时间到参数时间的长度
				将日期格式设为自该日期起的时间（例如，“4天，6小时”）。
				采用一个可选参数，它是一个包含用作比较点的日期的变量（不带参数，比较点为现在） 
				例如
				如果blog_date是表示2006年6月1日午夜的日期实例，
				并且comment_date是2006年6月1日08:00的日期实例，则以下将返回“8小时”：
				{{ blog_date|timesince:comment_date }}
				分钟是所使用的最小单位，对于相对于比较点的未来的任何日期，将返回“0分钟”。
			timeuntil
				它测量从现在开始直到给定日期或日期时间的时间。 
				例如，如果今天是2006年6月1日，而conference_date是保留2006年6月29日的日期实例，
				则{{ conference_date | timeuntil }}将返回“4周”。
				使用可选参数，它是一个包含用作比较点的日期（而不是现在）的变量。 
				如果from_date包含2006年6月22日，则以下内容将返回“1周”：
				{{ conference_date|timeuntil:from_date }}
			自定义filter
				自定义过滤器只是带有一个或两个参数的Python函数:
					变量（输入）的值 - -不一定是一个字符串
					参数的值 - 这可以有一个默认值，或完全省略
				例如，在过滤器{{var | foo:'bar'}}中，过滤器foo将传递变量var和参数“bar”。
				自定义filter代码文件摆放位置
					app01/
						__init__.py
						models.py
						templatetags/  # 在app01下面新建一个package package
							__init__.py
							app01_filters.py  # 建一个存放自定义filter的文件
						views.py
				编写自定义filter
					from django import template
					register = template.Library()
					@register.filter(name="cut")
					def cut(value, arg):
						return value.replace(arg, "")
					@register.filter(name="addSB")
					def add_sb(value):
						return "{} SB".format(value)
				使用自定义filter
					{# 先导入我们自定义filter那个文件 #}
					{% load app01_filters %}
					{# 使用我们自定义的filter #}
					{{ somevariable|cut:"0" }}
					{{ d.name|addSB }}
					
	Tags
		for循环		
			普通for循环
				<ul>
				{% for user in user_list %}
					<li>{{ user.name }}</li>
				{% endfor %}
				</ul>
			for循环可用的一些参数：
				Variable	Description
				forloop.counter	当前循环的索引值（从1开始）
				forloop.counter0	当前循环的索引值（从0开始）
				forloop.revcounter	当前循环的倒序索引值（从1开始）
				forloop.revcounter0	当前循环的倒序索引值（从0开始）
				forloop.first	当前循环是不是第一次循环（布尔值）
				forloop.last	当前循环是不是最后一次循环（布尔值）
				forloop.parentloop	本层循环的外层循环
			for ... empty
				如果拿到的数据为空,就用empty的内容代替
				<ul>
				{% for user in user_list %}
					<li>{{ user.name }}</li>
				{% empty %}
					<li>空空如也</li>
				{% endfor %}
				</ul>
		if判断
			if,elif和else
				{% if user_list %}
				  用户人数：{{ user_list|length }}
				{% elif black_list %}
				  黑名单数：{{ black_list|length }}
				{% else %}
				  没有用户
				{% endif %}
			当然也可以只有if和else
				{% if user_list|length > 5 %}
				  七座豪华SUV
				{% else %}
					黄包车
				{% endif %}
				if语句支持 and 、or、==、>、<、!=、<=、>=、in、not in、is、is not判断。	
		with
			定义一个中间变量，多用于给一个复杂的变量起别名。
			注意等号左右不要加空格。
				{% with total=business.employees.count %}
					{{ total }} employee{{ total|pluralize }}
				{% endwith %}
			或
				{% with business.employees.count as total %}
					{{ total }} employee{{ total|pluralize }}
				{% endwith %}					
		csrf_token
			这个标签用于跨站请求伪造保护。
			在页面的form表单里面写上{% csrf_token %}	
		注意事项
			1. Django的模板语言不支持连续判断，即不支持以下写法：
				{% if a > b > c %}
				...
				{% endif %}
			2. Django的模板语言中属性的优先级大于方法
				def xx(request):
					d = {"a": 1, "b": 2, "c": 3, "items": "100"}
					return render(request, "xx.html", {"data": d})
				如上，我们在使用render方法渲染一个页面的时候，传的字典d有一个key是items并且还有默认的 d.items() 方法，此时在模板语言中:
				{{ data.items }}
				默认会取d的items key的值。	
	母版
		会在母板中定义页面专用的CSS块和JS块，方便子页面替换。
		<!DOCTYPE html>
		<html lang="en">
		<head>
		  <meta charset="UTF-8">
		  <meta http-equiv="x-ua-compatible" content="IE=edge">
		  <meta name="viewport" content="width=device-width, initial-scale=1">
		  <title>Title</title>
		  {% block page-css %}
		  {% endblock %}
		</head>
		<body>
		<h1>这是母板的标题</h1>
		{% block page-main %}
		{% endblock %}
		<h1>母板底部内容</h1>
		{% block page-js %}
		{% endblock %}
		</body>
		</html>
	继承母板
		在子页面中在页面最上方使用下面的语法来继承母板。
		{% extends 'layouts.html' %}		
	块（block）
		通过在母板中使用{% block  xxx %}来定义"块"。
		在子页面中通过定义母板中的block名来对应替换母板中相应的内容。
		{% block page-main %}
		  <p>世情薄</p>
		  <p>人情恶</p>
		  <p>雨送黄昏花易落</p>
		{% endblock %}		
	组件
		可以将常用的页面内容如导航条，页尾信息等组件保存在单独的文件中，然后在需要使用的地方按如下语法导入即可。
		{% include 'navbar.html' %}		
	静态文件相关
		{% static %}
		{% load static %}
		<img src="{% static "images/hi.jpg" %}" alt="Hi!" />
		引用JS文件时使用：
			{% load static %}
			<script src="{% static "mytest.js" %}"></script>
		某个文件多处被用到可以存为一个变量
			{% load static %}
			{% static "images/hi.jpg" as myphoto %}
			<img src="{{ myphoto }}"></img>
			{% get_static_prefix %}
			{% load static %}
			<img src="{% get_static_prefix %}images/hi.jpg" alt="Hi!" />
		或者
			{% load static %}
			{% get_static_prefix as STATIC_PREFIX %}
			<img src="{{ STATIC_PREFIX }}images/hi.jpg" alt="Hi!" />
			<img src="{{ STATIC_PREFIX }}images/hi2.jpg" alt="Hello!" />		
	simple_tag
		和自定义filter类似，只不过接收更灵活的参数。
		定义注册simple tag
			@register.simple_tag(name="plus")
			def plus(a, b, c):
				return "{} + {} + {}".format(a, b, c)
		使用自定义simple tag
			{% load app01_demo %}
			{# simple tag #}
			{% plus "1" "2" "abc" %}		
	inclusion_tag
		多用于返回html代码片段
		示例：
			templatetags/my_inclusion.py
				from django import template
				register = template.Library()
				@register.inclusion_tag('result.html')
				def show_results(n):
					n = 1 if n < 1 else int(n)
					data = ["第{}项".format(i) for i in range(1, n+1)]
					return {"data": data}
				templates/snippets/result.html
				<ul>
				  {% for choice in data %}
					<li>{{ choice }}</li>
				  {% endfor %}
				</ul>
			templates/index.html
				<!DOCTYPE html>
				<html lang="en">
				<head>
				  <meta charset="UTF-8">
				  <meta http-equiv="x-ua-compatible" content="IE=edge">
				  <meta name="viewport" content="width=device-width, initial-scale=1">
				  <title>inclusion_tag test</title>
				</head>
				<body>
				{% load inclusion_tag_test %}
				{% show_results 10 %}
				</body>
				</html>
	
						
