在 HttpRequest 对象中,属性 GET 和 POST 得到的都是 django.http.QueryDict 所创建的实例。这是一个 django 自定义的类似字典的类，用来处理同一个键带多个值的情况。

　　在 python 原始的字典中，当一个键出现多个值的时候会发生冲突，只保留最后一个值。而在 HTML 表单中，通常会发生一个键有多个值的情况，例如 <select multiple> （多选框）就是一个很常见情况。

　　request.POST 和request.GET 的QueryDict 在一个正常的请求/响应循环中是不可变的。若要获得可变的版本，需要使用.copy()方法。

　　下面我们来看这个类中有什么方法：

1.QueryDict.__init__(query_string=None, mutable=False, encoding=None)

　　这是一个构造函数，其中 query_string 需要一个字符串，例如：

>>> QueryDict('a=1&a=2&c=3')
<QueryDict: {'a': ['1', '2'], 'c': ['3']}>
 

　　如果 query_string 没有传入，则获得一个空的对象。

　　你所遇到的 QueryDict 对象，特别是 request.POST 和 request.GET 得到的。如果你想自己实例化一个对象，可以传递 mutable=True 使你所实例化的对象可变。当然 request.POST 和 request.GET 是django创建的，也就是说除非改 django 源码，否则它们是不可变的。

　　对于设置的键和值，会从 encoding 转码成 Unicode。也就是说，如果传入的字符串 query_string  是 GBK 或者是 utf-8 的编码，将会自动转码成 Unicode，然后用做字典的键和值。如果 encoding = None，也就是没有设定的话，将使用 DEFAULT_CHARSET 的值，默认为：'utf-8'。

2.QueryDict.__getitem__(key)
　　返回给出的 key 的值。如果key 具有多个值，__getitem__() 返回最后（最新）的值。如果 key 不存在，则引发django.utils.datastructures.MultiValueDictKeyError。（它是Python 标准KeyError 的一个子类，所以你仍然可以坚持捕获KeyError。） 

 

3.QueryDict.__setitem__(key, value)

　　设置给出的 key 的值为[value]（一个Python 列表，只有一个元素 value）。注意：只有对象是可以改变的时候才能使用，例如通过 .copy() 方法创建的对象。

 

4.QueryDict.__contains__(key)

　　如果给出的key 已经设置，则返回True。它让你可以做 if "foo" in request.GET  这样的操作。

 

5.QueryDict.get(key, default)

　　使用与上面__getitem__() 相同的逻辑，但是当key 不存在时返回一个默认值。

 

6.QueryDict.setdefault(key, default)

　　类似标准字典的setdefault() 方法，只是它在内部使用的是__setitem__()。也就是说，当key已经存在时，返回其值，key不存在时，返回default，同时添加 key 和 default到对象中。

 

7.QueryDict.update(other_dict)

　　接收一个QueryDict 或标准字典。类似标准字典的update() 方法，但是它附加到当前字典项的后面，而不是替换掉它们。

例如：

复制代码
>>> q = QueryDict('a=1', mutable=True)    # 当然要可变的才能使用
>>> q.update({'a': '2'})
>>> q.getlist('a')
['1', '2']
>>> q['a'] # returns the last
['2']
复制代码
 

 

8.QueryDict.items()

　　类似标准字典的items() 方法，返回一个由键值组成的元祖的列表。但是它使用的是和__getitem__ 一样返回最新的值的逻辑。

例如：

>>> q = QueryDict('a=1&a=2&a=3')
>>> q.items()
[('a', '3')]
 

 

9.QueryDict.iteritems()

　　类似标准字典的iteritems() 方法，返回一个迭代对象。类似 QueryDict.items()，它使用的是和QueryDict.__getitem__() 一样的返回最新的值的逻辑。

 

10.QueryDict.iterlists()

　　类似QueryDict.iteritems()，返回一个包含键值对的元祖(key, value)迭代对象 ，value 是一个包括所有 key 的值的列表。

 

11.QueryDict.values()

　　类似标准字典的values() 方法，但是它使用的是和__getitem__ 一样返回最新的值的逻辑。也就是返回一个所有键对应的最新值的列表。

例如：

>>> q = QueryDict('a=1&a=2&a=3')
>>> q.values()
['3']
 

 

12.QueryDict.itervalues()

　　类似QueryDict.values()，只是它返回的是一个迭代器。

 

13.QueryDict.copy()

　　返回对象的副本，使用Python 标准库中的copy.deepcopy()。此副本是可变的即使原始对象是不可变的。

 

14.QueryDict.getlist(key, default)

　　以Python 列表形式返回所请求的键的数据。如果键不存在并且没有提供默认值，则返回空列表。它保证返回的是某种类型的列表，除非默认值不是列表。

 

15.QueryDict.setlist(key, list_)

　　为给定的键设置list_（与__setitem__() 不同)，可以设置一个多元素的列表。

 

16.QueryDict.appendlist(key, item)

　　将项追加到内部与键相关联的列表中。

 

17.QueryDict.setlistdefault(key, default_list)

　　类似setdefault，除了它接受一个列表而不是单个值。

 

18.QueryDict.lists()

　　类似items，只是它将字典中的每个成员作为列表。也就是说，列表中的每个元素，都是由键和对应的值列表组成的二元元祖。

例如：

>>> q = QueryDict('a=1&a=2&a=3')
>>> q.lists()
[('a', ['1', '2', '3'])]
 

 

19.QueryDict.pop(key)

　　返回给定键的值的列表，并从字典中移除它们。如果键不存在，将引发KeyError。

例如 ︰

>>> q = QueryDict('a=1&a=2&a=3', mutable=True)
>>> q.pop('a')
['1', '2', '3']
 

 

20.QueryDict.popitem()

　　删除字典任意一个成员（因为没有顺序的概念），并返回二值元组，包含键和键的所有值的列表。在一个空的字典上调用时将引发KeyError。

例如 ︰

>>> q = QueryDict('a=1&a=2&a=3', mutable=True)
>>> q.popitem()
('a', ['1', '2', '3'])
 

 

21.QueryDict.dict()

　　返回QueryDict 的dict 表示形式。对于QueryDict 中的每个(key, list)对 ，dict 将有(key, item) 对，其中item 是列表中的一个元素，使用与QueryDict.__getitem__()相同的逻辑，也就是最新的：

>>> q = QueryDict('a=1&a=3&a=5')
>>> q.dict()
{'a': '5'}
 

 

22.QueryDict.urlencode([safe])

　　从数据中返回查询字符串格式。

例如：

>>> q = QueryDict('a=2&b=3&b=5')
>>> q.urlencode()
'a=2&b=3&b=5'
 

　　可选地，urlencode 可以传递不需要编码的字符。（这意味着要进行 url 编码）

例如︰

>>> q = QueryDict(mutable=True)
>>> q['next'] = '/a&b/'
>>> q.urlencode(safe='/')
'next=/a%26b/'