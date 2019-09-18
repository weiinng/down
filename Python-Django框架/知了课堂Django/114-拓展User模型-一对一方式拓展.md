#### 2.一对一外键：

如果你对用户验证方法authenticate没有其他要求，就是使用username和password即可完成。但是想要在原来模型的基础之上添加新的字段，那么可以使用一对一外键的方式。示例代码如下：

```python
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
    birthday = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=100)

#监听user的变化，括号内第一个值为接收什么新号 第二个值为接收谁发出的新号
@receiver(post_save, sender=User)
#第三个值为是否是新创建的。
def create_user_extension(sender, instance, created, **kwargs):
    #如果是第一次创建，那就创建一个userex进行绑定。
    if created:
        UserExtension.objects.create(user=instance)
    #如果不是第一次创建，将进行保存
    else:
        instance.extension.save()
```

以上定义一个UserExtension的模型，并且让她和User模型进行一对一的绑定，以后我们新增的字段，就添加到UserExtension上。并且还写了一个接受保存模型的信号处理方法，只要是User调用了save方法，那么就会创建一个UserExtension和User进行绑定。

一对一的关系会更加的安全。

这种方法不会破坏原有的user，进行实际开发的时候建议使用这种方法。

就是比较麻烦一点。





























