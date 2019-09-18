### 4. 继承自`AbstractBaseUser`模型：

如果你想修改默认的验证方式，并且对于原来`User`模型上的一些字段不想要，那么可以自定义一个模型，然后继承自`AbstractBaseUser`，再添加你想要的字段。这种方式会比较麻烦，最好是确定自己对`Django`比较了解才推荐使用。步骤如下：

#### 创建模型。示例代码如下：

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

```python
"""
This module allows importing AbstractBaseUser even when django.contrib.auth is
not in INSTALLED_APPS.
这个模块允许导入AbstractBaseUser，即使在django.contrib中也是如此。身份验证是
INSTALLED_APPS。
"""
import unicodedata

from django.contrib.auth import password_validation
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
from django.db import models
from django.utils.crypto import get_random_string, salted_hmac
from django.utils.translation import gettext_lazy as _


class BaseUserManager(models.Manager):

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the email address by lowercasing the domain part of it.
        将电子邮件地址正常化，将其域部分小写。
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = email_name + '@' + domain_part.lower()
        return email

    def make_random_password(self, length=10,
                             allowed_chars='abcdefghjkmnpqrstuvwxyz'
                                           'ABCDEFGHJKLMNPQRSTUVWXYZ'
                                           '23456789'):
        """
        Generate a random password with the given length and given
        allowed_chars. The default value of allowed_chars does not have "I" or
        "O" or letters and digits that look similar -- just to avoid confusion.
        生成具有给定长度和给定值的随机密码allowed_chars。
        allowed_chars的默认值没有“I”或“O”或看起来相似的字母和数字——只是为了避免混淆。
        """
        return get_random_string(length, allowed_chars)

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})


class AbstractBaseUser(models.Model):
    password = models.CharField(_('password'), max_length=128)
    #Django把password做过特殊的加密处理。
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
		#last_login 记录上次的登录时间
    is_active = True
		#是否是活跃用户 默认为True
    REQUIRED_FIELDS = []
    #一个字段名列表，用于当通过createsuperuser管理命令创建一个用户时的提示。
		
    # Stores the raw password if set_password() is called so that it can
    #如果调用set_password()，则存储原始密码，以便它可以
    # be passed to password_changed() after the model is saved.
    #保存模型后传递给password_changed()。
    _password = None

    class Meta:
        abstract = True

    def get_username(self):
        "Return the identifying username for this User"
        return getattr(self, self.USERNAME_FIELD)

    def __str__(self):
        return self.get_username()

    def clean(self):
        setattr(self, self.USERNAME_FIELD, self.normalize_username(self.get_username()))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None

    def natural_key(self):
        return (self.get_username(),)

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    def set_unusable_password(self):
        # Set a value that will never be a valid hash
        self.password = make_password(None)

    def has_usable_password(self):
        """
        Return False if set_unusable_password() has been called for this user.
        """
        return is_password_usable(self.password)

    def get_session_auth_hash(self):
        """
        Return an HMAC of the password field.
        """
        key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
        return salted_hmac(key_salt, self.password).hexdigest()

    @classmethod
    def get_email_field_name(cls):
        try:
            return cls.EMAIL_FIELD
        except AttributeError:
            return 'email'

    @classmethod
    def normalize_username(cls, username):
        return unicodedata.normalize('NFKC', username) if isinstance(username, str) else username

```



#### 重新定义`UserManager`：

我们还需要定义自己的`UserManager`，因为默认的`UserManager`在创建用户的时候使用的是`username`和`password`，那么我们要替换成`telephone`。

示例代码如下：

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

#### 配置`settings.py`

在创建了新的`User`模型后，还需要在`settings`中配置好。配置`AUTH_USER_MODEL='appname.User'`。

#### 使用自定义模型

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

**这种方式因为破坏了原来User模型的表结构，所以必须要在第一次**`migrate`**前就先定义好。**