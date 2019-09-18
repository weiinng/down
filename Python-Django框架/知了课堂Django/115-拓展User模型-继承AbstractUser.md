#### 3.继承自AbstractUser：

对于authenticate不满意，并且不想要修改原来User对象上的一些字段，但是想要增加一些字段，那么这时候可以直接继承自django.contrib.auth.models.AbstractUser，其实这个类也是django.contrib.auth.models.User的父类。比如我们想要在原来User模型的基础之上添加一个telephone和school字段。示例代码如下：

```python
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    telephone = models.CharField(max_length=11,unique=True)
    school = models.CharField(max_length=100)

    # 指定telephone作为USERNAME_FIELD，以后使用authenticate
    # 函数验证的时候，就可以根据telephone来验证
    # 而不是原来的username
    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = []

    # 重新定义Manager对象，在创建user的时候使用telephone和
    # password，而不是使用username和password
    objects = UserManager()


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self,telephone,password,**extra_fields):
        if not telephone:
            raise ValueError("请填入手机号码！")
        user = self.model(telephone=telephone,*extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,telephone,password,**extra_fields):
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(telephone,password)

    def create_superuser(self,telephone,password,**extra_fields):
        extra_fields['is_superuser'] = True
        return self._create_user(telephone,password)
```

然后再在`settings`中配置好`AUTH_USER_MODEL=youapp.User`。

**这种方式因为破坏了原来User模型的表结构，所以必须要在第一次**`migrate`**前就先定义好。**

#### 4.继承自AbstractBaseUser模型：

如果你想修改默认的验证方式，并且对于原来`User`模型上的一些字段不想要，那么可以自定义一个模型，然后继承自`AbstractBaseUser`，再添加你想要的字段。这种方式会比较麻烦，最好是确定自己对`Django`比较了解才推荐使用。步骤如下：

##### **1，创建模型。示例代码如下：**

```python
class User(AbstractBaseUser,PermissionsMixin):
     email = models.EmailField(unique=False)
     username = models.CharField(max_length=150)
     telephone = models.CharField(max_length=11,unique=True)
     is_active = models.BooleanField(default=True)
 
     USERNAME_FIELD = 'telephone'
     REQUIRED_FIELDS = []
 
     objects = UserManager()
 
     def get_full_name(self):
         return self.username
 
     def get_short_name(self):
         return self.username
```

其中`password`和`last_login`是在`AbstractBaseUser`中已经添加好了的，我们直接继承就可以了。然后我们再添加我们想要的字段。比如`email`、`username`、`telephone`等。这样就可以实现自己想要的字段了。但是因为我们重写了`User`，所以应该尽可能的模拟`User`模型：

- `USERNAME_FIELD`：用来描述`User`模型名字字段的字符串，作为唯一的标识。如果没有修改，那么会使用`USERNAME`来作为唯一字段。
- `REQUIRED_FIELDS`：一个字段名列表，用于当通过`createsuperuser`管理命令创建一个用户时的提示。
- `is_active`：一个布尔值，用于标识用户当前是否可用。
- `get_full_name()`：获取完整的名字。
- `get_short_name()`：一个比较简短的用户名。

##### **2，重新定义UserManager：**

我们还需要定义自己的UserManager，因为默认的UserManager在创建用户的时候使用的是username和password，那么我们要替换成telephone。示例代码如下：

```python
 class UserManager(BaseUserManager):
     use_in_migrations = True

     def _create_user(self,telephone,password,**extra_fields):
         if not telephone:
             raise ValueError("请填入手机号码！")
         user = self.model(telephone=telephone,*extra_fields)
         user.set_password(password)
         user.save()
         return user

     def create_user(self,telephone,password,**extra_fields):
         extra_fields.setdefault('is_superuser',False)
         return self._create_user(telephone,password)

     def create_superuser(self,telephone,password,**extra_fields):
         extra_fields['is_superuser'] = True
         return self._create_user(telephone,password)
```
##### 3.设置Setting

在创建了新的`User`模型后，还需要在`settings`中配置好。配置`AUTH_USER_MODEL='appname.User'`。

##### 4.使用自定义模型

如何使用这个自定义的模型：比如以后我们有一个`Article`模型，需要通过外键引用这个`User`模型，那么可以通过以下两种方式引用。
第一种就是直接将`User`导入到当前文件中。示例代码如下：

```python
 from django.db import models
 from myauth.models import User
 class Article(models.Model):
     title = models.CharField(max_length=100)
     content = models.TextField()
     author = models.ForeignKey(User, on_delete=models.CASCADE)
```

这种方式是可以行得通的。但是为了更好的使用性，建议还是将`User`抽象出来，使用`settings.AUTH_USER_MODEL`来表示。示例代码如下：

```python
 from django.db import models
 from django.conf import settings
 class Article(models.Model):
     title = models.CharField(max_length=100)
     content = models.TextField()
     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

****

**这种方式因为破坏了原来User模型的表结构，所以必须要在第一次**`migrate`**前就先定义好。**