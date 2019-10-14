# JSON(JavaScript Object Notation)

json是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。 JSON采用完全独立于语言的文本格式，但是也使用了类似于C语言家族的习惯（包括C、C++、C#、Java、JavaScript、Perl、Python等）。这些特性使JSON成为理想的数据交换语言。 易于人阅读和编写，同时也易于机器解析和生成(一般用于提升网络传输速率)。



# restful接口

一种软件架构风格、设计风格，而不是标准，只是提供了一组设计原则和约束条件。它主要用于客户端和服务器交互类的软件。基于这个风格设计的软件可以更简洁，更有层次，更易于实现缓存等机制。

如果按照HTTP方法的语义来暴露资源，那么接口将会拥有安全性和幂等性的特性，例如GET和HEAD请求都是安全的， 无论请求多少次，都不会改变服务器状态。而GET、HEAD、PUT和DELETE请求都是幂等的，无论对资源操作多少次， 结果总是一样的，后面的请求并不会产生比第一次更多的影响。



# Tornado 结合 sqlalchemy 来返回json的数据接口

在tornado中增加json支持，需要在model（默认tornado是没有model的，使用sqlalchemy，大家一般会写个models.py文件来做model）里面增加**json**方法：

```
Base = declarative_base()

#给Base添加__json__方法 使输出JSON数据
def sqlalchemy_json(self):
    obj_dict = self.__dict__
    return dict((key, obj_dict[key]) for key in obj_dict if not key.startswith("_"))
Base.__json__ = sqlalchemy_json
```

这样就可以在视图中直接返回json数据 

```
lass users(BaseHandler):
def get(self):
    user_id = self.get_argument("user_id")#获取user_id
    user_info = self.session.query(models.User).filter_by(id=user_id).first()#查询user信息
    self.write(json.dumps({"status":0,"msg":"返回成功","user_info":models.User.__json__(user)},ensure_ascii=False,indent=4))
    #返回自定义数据，models.User.__json__(user)就是使用在Base创建的__json__方法来返回json数据，ensure_ascii=False是不使用ascii为了显示中文，indent=4是缩进，格式化输出json比较美观
```

但是该方法只支持单一元素，如果是元素集就不行了，所以可以写一个扩展类



```
class AlchemyEncoder(json.JSONEncoder):    
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)     # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:    # 添加了对datetime的处理
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (datetime.datetime.min + data).time().isoformat()
                    else:
                        fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
```

视图调用扩展类 

```
self.write(json.dumps({"status":0,"msg":"返回成功","user_info":p},cls=AlchemyEncoder,ensure_ascii=False,indent=4))
```

