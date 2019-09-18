
# Django数据库

## 区分一对一，多对多

**一对一：子表从母表中选出一条数据一一对应，母表中选出来一条就少一条，子表不可以再选择母表中已被选择的那条数据**

**一对多：子表从母表中选出一条数据一一对应，但母表的这条数据还可以被其他子表数据选择**

**共同点是在admin中添加数据的话，都会出现一个select选框，但只能单选，因为不论一对一还是一对多，自己都是“一”**

**多对多总结：**

　　**比如有多个孩子，和多种颜色、**

　　**每个孩子可以喜欢多种颜色，一种颜色可以被多个孩子喜欢，对于双向均是可以有多个选择**

## 应用场景

**一对一：一般用于某张表的补充，比如用户基本信息是一张表，但并非每一个用户都需要有登录的权限，不需要记录用户名和密码，此时，合理的做法就是新建一张记录登录信息的表，与用户信息进行一对一的关联，可以方便的从子表查询母表信息或反向查询**

**外键：有很多的应用场景，比如每个员工归属于一个部门，那么就可以让员工表的部门字段与部门表进行一对多关联，可以查询到一个员工归属于哪个部门，也可反向查出某一部门有哪些员工**

**多对多：如很多公司，一台服务器可能会有多种用途，归属于多个产品线当中，那么服务器与产品线之间就可以做成对多对，多对多在A表添加manytomany字段或者从B表添加，效果一致**



```python
#_*_coding:utf-8_*_
from django.db import models
 
# Create your models here.
 
class Colors(models.Model):
    colors=models.CharField(max_length=10) #蓝色
    def __str__(self):
        return self.colors
 
class Ball(models.Model):
    color=models.OneToOneField("Colors")  #与颜色表为一对一，颜色表为母表
    description=models.CharField(max_length=10) #描述
    def __str__(self):
        return self.description
 
class Clothes(models.Model):
    color=models.ForeignKey("Colors")   #与颜色表为外键，颜色表为母表
    description=models.CharField(max_length=10) #描述
    def __str__(self):
        return self.description   
     
class Child(models.Model):
    name=models.CharField(max_length=10)   #姓名  
    favor=models.ManyToManyField('Colors')    #与颜色表为多对多
```



## 一对一

### 查：

```python
#子表查询母表,找到红球对应的颜色
#写法1：
print(models.Ball.objects.get(description="红球").color.colors)  
#返回红，通过子表查询母表，写法："子表对象.母表表名的小写.母表字段名" ；
#通过Ball表查到description为"红球"，查找到对应colors
#写法2，反向从母表入手：
print(models.Colors.objects.get(ball__description="红球").colors) 
#返回红，通过子表查询母表，但形式上是从母表对象自身直接获取字段，
#写法："母表.objects.get(子表名小写__子表字段="xxx").母表字段名" ；效果和上边完全一致，另一种形式


#母表查询子表，找到红色对应的球的名字
#写法1：
print(models.Colors.objects.get(colors="红").ball.description)  
#返回红球，通过母表查询子表，写法："母表对象.子表表名的小写.子表字段名"；
#找到颜色为红色的Ball的description

#写法2，反向从子表入手：
print(models.Ball.objects.get(color__colors="红").description)  
#返回红球，通过母表查询子表，但形式上是从子表对象自身直接获取字段，
#写法："子表.objects.get(一对一的子表字段__母表字段="xxx").子表字段"；效果和上边完全一致，另一种形式


```

### 增：

```python
#添加一种颜色黑，并添加黑球
color_obj=models.Colors.objects.create(colors="黑")  
#先在母表中创建颜色，并实例化给颜色表对象

models.Ball.objects.create(color=color_obj,description="黑球")  
#更新Ball表，color字段为颜色表对象，添加description字段
```

###备注：增添数据的三种常用方式

```python
#增添数据的三种写法：
#写法1：
color_obj=models.Colors.objects.create(colors="黑")
models.Ball.objects.create(color=color_obj,description="黑球")

#写法1补充：
color_id=models.Colors.objects.create(colors="黑").id
models.Ball.objects.create(color_id=color_id,description="黑球")

#写法2：
color_obj=models.Colors.objects.create(colors="黑")
ball_obj=models.Ball(color=color_obj,description="黑球")
ball_obj.save()

#写法3(字典导入)：
color_obj=models.Colors.objects.create(colors="黑")
ball_dic={'description':"黑球"}
models.Ball.objects.create(color=color_obj,**ball_dic)
```

###改：

```python
color_obj=models.Colors.objects.get(colors="黑") 
#.get()等同于.filter().first()

color_obj.colors="灰"
color_obj.save()

models.Ball.objects.filter(description="黑球").update(color=color_obj,description="灰球") 
#update(),delete()是QuerySet的方法
```

###*备注：修改数据的常见方式*

```python
#更新一条数据
color_obj=models.Colors.objects.get(colors="黑")
color_obj.colors="灰"
color_obj.save()
#更新多条数据，把满足条件的球的description都变为灰球

#写法1：
models.Ball.objects.filter(color__colors="红").update(description="灰球")

#写法2：
up_dic={"description":"灰球"}
models.Ball.objects.filter(id__gt=0).update(**up_dic)
```

### 删：

```python
models.Ball.objects.get(description="灰球").delete() 
#对象和QuerySet都有方法delete()
models.Colors.objects.filter(colors="灰").delete()

models.Colors.objects.all().delete() #清空一张表
```

##一对多（外键）

### 查：

```python
#外键表联合查询：

#外键子表查询母表,与一对一子表查询母表形式一致
#找到红裤衩所属的颜色表中的颜色--返回:红

#写法1：
print(models.Clothes.objects.get(description="小虎哥").color.colors)  
#返回红，通过子表查询母表，写法："子表对象.母表表名的小写.母表字段名" ；
#通过Clothes表查到description为"小虎哥"，查找到对应colors

#写法2，反向从母表入手：
print(models.Colors.objects.get(clothes__description="小虎哥").colors)  
#返回红，通过子表查询母表，但形式上是从母表对象自身直接获取字段，
#写法："母表.objects.get(子表名小写__子表字段="xxx").母表字段名" ；效果和上边完全一致，另一种形式

#外键母表查询子表,与一对一形式不同，因为母表为"多"，
#不能像一对一一样通过.get().子表.子表字段的方式获取，但与多对多母表查询子表一致
#找到颜色为红的所有服装--返回:[<Clothes: 大美女>, <Clothes: 小虎哥>]

#写法1：
color_obj=models.Colors.objects.get(colors="红")
print(color_obj.clothes_set.all())  
#注意：子表小写_set的写法,它实际上是一个QuerySet,可以用update,delete,all,filter等方法

#写法2：
print(models.Clothes.objects.filter(color=models.Colors.objects.get(colors="红")))

#写法2简便写法（推荐）：
print(models.Clothes.objects.filter(color__colors="红"))  
#写法：filter(子表外键字段__母表字段='过滤条件')

#写法3：
color_id=models.Colors.objects.get(colors="红").id  
#通过母表获取到颜色为红的id
print(models.Clothes.objects.filter(color_id=color_id))  
#filter得到QuerySet,写法：filter(子表外键字段_母表主键=母表主键对象)
```

### 备注：

通过QuerySet的.values()方法，将QuerySet转化为ValuesQuerySet

```python
print(models.Clothes.objects.filter(color=models.Colors.objects.get(colors="红")).values('color__colors','description'))  
#获取子表的description字段，和母表的colors字段，获取母表字段写法: 子表外键字段名__母表字段名--适用于values()或filter()
#简写形式补充：
print(models.Clothes.objects.filter(color__colors="红").values('color__colors','description'))
#返回：
[{'description': u'\u7ea2\u5185\u8863', 'color__colors': u'\u7ea2'}, {'description': u'\u7ea2\u5185\u88e4', 'color__colors': u'\u7ea2'}]
#如果不加values(),返回的是[<Clothes: 大美女>, <Clothes: 小虎哥>]这样一个QuerySet集合，通过values可以形成一个列表，列表中的每一个元素是一个字典，可以通过list()将ValuesQeurySet转化为列表，之后返回给templates


#另外可通过.values_list()将QuerySet转化为ValuesListQuerySet。返回：[(u'\u7ea2', u'\u7ea2\u889c\u5b50'), (u'\u7ea2', u'\u7ea2\u889c\u5b50')]
#得到的是一个列表，列表中是多个元组，每个元组是ValuesQuerySet中字典的value，常用于从models里将数据取出后动态添加到前端模板中的select选项中。
#通过forms.py从models取值传给前端select选项，需重启django后，select选项才能更新，可在定义form时，添加如下关键字保障动态更新select选项
#forms.py
from django import forms
from test1 import models
class ClothesForm(forms.Form):
    color=forms.IntegerField(required=True,widget=forms.Select(),)
    def __init__(self,*args,**kwargs):  #定义这个关键字段，当使用form时，colors表新增了颜色，前端ClothesForm的color字段的选项会自动更新
        super(ClothesForm, self).__init__(*args,**kwargs)
        self.fields['color'].widget.choices=models.Colors.objects.all().order_by('id').values_list('id','colors')
```

### 增：

```python
#增添子表数据，形式与一对一一致
#添加颜色为绿的服装：小帅哥
#方法1：
models.Clothes.objects.create(color=models.Colors.objects.get(colors="绿"),description="小帅哥")
#方法1补充：
models.Clothes.objects.create(color_id=models.Colors.objects.get(colors="绿").id,description="小帅哥")
#方法2：
c_obj=models.Clothes(color=models.Colors.objects.get(colors="绿"),description="小帅哥")
c_obj.save()
#方法3：字典方式录入..参考一对一
```

### 改：

```python
#颜色为红的服装，description都更新为大美女
#写法1：
models.Clothes.objects.filter(color__colors="红").update(description="大美女")
#写法2：
models.Clothes.objects.filter(color_id=models.Colors.objects.get(colors="红").id).update(description="大美女")
#写法3：
colors_obj=models.Colors.objects.get(colors="红")
colors_obj.clothes_set.filter(id__gte=1).update(description="大美女")
#其他写法参照一对一的修改和外键的查询
```

### 删：

```python
models.Clothes.objects.get(description="灰裙子").delete() 
#对象和QuerySet都有方法delete()

models.Colors.objects.filter(colors="灰").delete()
```

## 多对多

###查：

```python
#多对多子表查询母表,查找小明喜欢哪些颜色--返回:[<Colors: 红>, <Colors: 黄>, <Colors: 蓝>]
#与一对多子表查询母表的形式不同，因为一对多，查询的是母表的“一”；多对多，查询的是母表的“多”
#写法1：
child_obj=models.Child.objects.get(name="小明")  

#写法：子表对象.子表多对多字段.过滤条件(all()/filter())
print(child_obj.favor.all())

#写法2，反向从母表入手：
print(models.Colors.objects.filter(child__name="小明")) 
#母表对象.filter(子表表名小写__子表字段名="过滤条件")


#多对多母表查询子表,查找有哪些人喜欢黄色--返回:[<Child: 小明>, <Child: 丫蛋>]
#与一对多母表查询子表的形式完全一致，因为查到的都是QuerySet，一对多和多对多，都是在查询子表的“多”
#写法1：
color_obj=models.Colors.objects.get(colors="黄")
print(color_obj.child_set.all())
#写法2：
print(models.Child.objects.filter(favor=models.Colors.objects.get(colors="黄")))
#写法2简便写法(推荐):
print(models.Child.objects.filter(favor__colors="黄"))  
#写法：filter(子表外键字段__母表字段='过滤条件')
#写法3：
color_id=models.Colors.objects.get(colors="黄").id  
#通过母表获取到颜色为红的id
print(models.Child.objects.filter(favor=color_id))  
#filter得到QuerySet,写法：filter(子表外键字段=母表主键对象),此处和一对多略有不同，是子表外键字段而不是外键字段_母表主键
```

### 增与改

(增添子表或母表数据参照一对一的增，多对多重点在于关系表的对应关系变更)：

```python
#添加子表关联关系
#添加小虎并让他喜欢所有颜色

#写法1：
child_obj=models.Child.objects.create(name="小虎")  
#如果是已有用户，使用.get()
colors_obj=models.Colors.objects.all()  
#创建颜色表的所有颜色QuerySet对象
child_obj.favor.add(*colors_obj)  
#添加对应关系,将小虎和所有颜色进行关联，写法：子表对象.子表多对多字段.add(*QuerySet对象)

#写法2：
child_obj=models.Child.objects.get(name="小虎")
colors_obj=models.Colors.objects.all()
child_obj.favor=colors_obj
child_obj.save()
#让小虎喜欢黄色和蓝色(2种写法和上边一致，只展示一种写法)
child_obj=models.Child.objects.get(name="小虎")
colors_obj=models.Colors.objects.filter(colors__in=["蓝","黄"])  
#models默认只能用这种方式得到并集，如需更复杂的过滤逻辑，需使用模块Q
child_obj.favor.clear()  
#清空小虎已经喜欢的颜色
child_obj.favor.add(*colors_obj)  
#add是追加模式，如果当前小虎已经喜欢绿色，那么执行后，小虎会额外喜欢蓝，黄
#让小虎喜欢绿色(2种写法和上边一致，只展示一种写法)
child_obj=models.Child.objects.get(name="小虎")
colors_obj=models.Colors.objects.get(colors="绿")
child_obj.favor.clear()
child_obj.favor.add(colors_obj)  #此处没有*


#添加母表关联关系
#让喜欢蓝色的人里添加小虎,可以用上边的方法，一个效果，让小虎喜欢蓝色，下边介绍反向插入(从母表入手)的写法
child_obj=models.Child.objects.get(name="小虎")
colors_obj=models.Colors.objects.get(colors="蓝")
colors_obj.child_set.add(child_obj)  #从colors表插入小虎，写法：母表对象.子表名小写_set.add(子表对象)。 让喜欢蓝色的child_set集合添加name="小虎"
#让所有人都喜欢蓝色
children_obj=models.Child.objects.all()
colors_obj=models.Colors.objects.get(colors="蓝")
colors_obj.child_set.add(*children_obj)
#关于_set写法，是否已经有些晕了，究竟什么时候使用_set,简单记忆，只有子表才有"子表名小写_set"的写法，得到的是一个QuerySet集合，后边可以接.add(),.remove(),.update(),.delete(),.clear()
#另外备注一下，colors_obj.child_set.clear()是让所有人喜欢的颜色里去掉蓝色，colors_obj.child_set.all().delete()是删除.child_set的所有人
```

### 删：删除多对多关系:

```python
#删除子表与母表关联关系
#让小虎不喜欢任何颜色
#写法1：
child_obj=models.Child.objects.get(name="小虎")
colors_obj=models.Colors.objects.all()
child_obj.favor=''
child_obj.save()
#写法2：
child_obj=models.Child.objects.get(name="小虎")
colors_obj=models.Colors.objects.all()
child_obj.favor.remove(*colors_obj)
#写法3：
child_obj=models.Child.objects.get(name="小虎")
child_obj.favor.clear()
#其他例子参照多对多的增与改案例，这里不做举例

#删除母表与子表关联关系
#让所有人不再喜欢蓝色
#写法1：
children_obj=models.Child.objects.all()
colors_obj=models.Colors.objects.get(colors="蓝")
colors_obj.child_set.remove(*children_obj)
#写法2：
colors_obj=models.Colors.objects.get(colors="蓝")
colors_obj.child_set.clear()
```

### 删多对多表数据：

```python
#删除子表数据
#喜欢蓝色的所有人都删掉
colors_obj=models.Colors.objects.get(colors="蓝")
colors_obj.child_set.all().delete()  #注意有.all()
#删除所有child
models.Child.objects.all().delete()
```

### 删除母表数据：

默认情况下，比如列中，删除’红‘色，那么子表与颜色表是一对一或者外键关系的数据会自动删除，比如红球，小虎哥，

与颜色表是多对多关系的话，不会自动删除喜欢红色的人，热水去掉红色已选

如果想让与母表外键关联的子表在删除外键之后依旧可以保留子表的数据，需要子表建表时加入以下字段：

```python
class Clothes(models.Model):
    color=models.ForeignKey("Colors",null=True,on_delete=models.SET_NULL))  
    #可为空，如果外键被删后，子表数据此字段置空而不是直接删除这条数据，同理也可以SET_DEFAULT,需要此字段有默认值
    description=models.CharField(max_length=10)  
    #描述 
```

### choice

```python
#choices相当于实现一个简化版的外键，外键的选项不能动态更新，如可选项目较少，可以采用
#先在models添加choices字段
class Child(models.Model):
    sex_choice=((0,"男"),(1,"女"))
    name=models.CharField(max_length=10)  #姓名
    favor=models.ManyToManyField('Colors')    #与颜色表为多对多
    sex=models.IntegerField(choices=sex_choice,default=0)
    def __unicode__(self):
        return self.name

#在views.py中调用
child_obj=models.Child.objects.get(name="小虎")
print(child_obj.sex)  #返回0或1
print(child_obj.get_sex_display())  #返回男或女
```

