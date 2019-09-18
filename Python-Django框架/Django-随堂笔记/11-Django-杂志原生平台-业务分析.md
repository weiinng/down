## 原生杂志平台需求文档

## 彩虹表

> 123456  -> asjdklajdlakjd
>
> root -> ajdkaldjklasjdjd
>
> admin
>
> test

### 用户模块

#### 抽象基类表:Base

> 将用户、后面其他权限表 角色表的相同属性 作为抽象基类继承

* **create_time** = `Datetime`

  > auto_now_add = True 
  >
  > 这条数据创建时，直接定义成当前时间

* **modify_time** = `Datetime`

  > auto_now = True
  >
  > 当这条数据被修改时，自动同步成当前时间

* **name** = `Char`

  > require=True
  >
  > 数据的名称

#### 用户表:User

> 只存储用户的基本信心，不存储相关权限字段

* **account** = `CharField`

  > max_length=[8,+] ,50
  >
  > unique = True

* **password** = `CharField`

  | md5      | sha256   | sha1     |
  | -------- | -------- | -------- |
  | 速度快   | 速度中等 | 速度慢   |
  | 质量稍低 | 质量中等 | 质量最高 |

  > salt：盐值
  >
  > 123456 -> -> adjkasjlkzxcndajdka
  >
  > 密码的创建要用到 ：make_password check_password
  >
  > 15 
  >
  > max_length=100

* **email** = `Email`

  > 邮箱字段，发邮件
  >
  > 密码找回：回调连接，验证码

* **login_time** = `Decimal`

  > 保存用户在线时间，单位是分钟数
  >
  > default = 0

* **is_active** = `Bool`

  > 表示用户是否处于活跃状态，活跃状态可登陆
  >
  > default = True

* **ip** = `GenericIPAddress`

* avator = `Image`

  > pip3 install pillow 解析文件是否是一个图片
  >
  > 用户头像字段
  >
  > <img href='1.mp3'>
  >
  > null=Ture,blank=True

* **gender** = `Char`

  > 保存性别，最大长度为1
  >
  > 0，1，2，3，4，5，6

* phone = `Char`

  > max_length=11
  >
  > 存储用户手机号
  >
  > null =True,blank=True

* role  = `ForeignKey`

  > 外键关联角色表，代表当前用户的具体权限
  >
  > null = True
  >
  > blank = True
  >
  > models.SET_NULL

##### 用户表属性

* unique_together =  ( (email,  phone, account),)

#### 角色表:Role

> 用来

* role_count = `Int`

  > 保存有多少用户是这个角色
  >
  > default=0

* permission = `ManyToMany`

  > 当前角色多对多关联的权限
  >
  > 代表这个角色有什么样的权限

* is_active = `Bool`

  > 表示当前角色是否有效，可否使用
  >
  > default=True

#### 权限表:Permission

* action = `Char`

  > 表示当前的具体某一个权限

* per_cate = `ForeignKey`

  > 权限的分类，用来在存储同样标识，但是不同业务权限时，进行区分
  >
  > 1 ,2 ,4 ,8  1, 2 ,4 ,8
  >
  > 1.per_cate = 'user'
  >
  > 1.per_cate = 'mag'

##### 权限表属性

* unique_together =  ( (action ,  per_cate ),)

#### 权限分类

* name：
  * 10001：用户
  * 10002：商品
  * 10003：店铺 

* ```python
  if user.role.permission.filter(Q(per_cate__name='10001') & Q(action=1 ))
  ```

  