### 扩展用户模型

**在中国一般都是使用手机号邮箱等其他方式来登录，一般不适用用户名，所以需要拓展模型。**

Django内置的User模型虽然已经足够强大了。但是有时候还是不能满足我们的需求。比如在验证用户登录的时候，他用的是用户名作为验证，而我们有时候需要通过手机号码或者邮箱来进行验证。还有比如我们想要增加一些新的字段。那么这时候我们就需要扩展用户模型了。扩展用户模型有多种方式。这里我们来一一讨论下。

#### 1.设置Proxy模型：

**第一种方式使用代理，可插拔。**

如果你对Django提供的字段，以及验证的方法都比较满意，没有什么需要改的。但是只是需要在他原有的基础之上增加一些操作的方法。那么建议使用这种方式。示例代码如下：

```python
class Person(User):
    class Meta:
        proxy = True
 
    def get_blacklist(self):
        return self.objects.filter(is_active=False)
```

在以上，我们定义了一个Person类，让他继承自User，并且在Meta中设置proxy=True，说明这个只是User的一个代理模型。他并不会影响原来User模型在数据库中表的结构。以后如果你想方便的获取所有黑名单的人，那么你就可以通过Person.get_blacklist()就可以获取到。并且User.objects.all()和Person.objects.all()其实是等价的。因为他们都是从User这个模型中获取所有的数据。

