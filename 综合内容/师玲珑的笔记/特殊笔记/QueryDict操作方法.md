�� HttpRequest ������,���� GET �� POST �õ��Ķ��� django.http.QueryDict ��������ʵ��������һ�� django �Զ���������ֵ���࣬��������ͬһ���������ֵ�������

������ python ԭʼ���ֵ��У���һ�������ֶ��ֵ��ʱ��ᷢ����ͻ��ֻ�������һ��ֵ������ HTML ���У�ͨ���ᷢ��һ�����ж��ֵ����������� <select multiple> ����ѡ�򣩾���һ���ܳ��������

����request.POST ��request.GET ��QueryDict ��һ������������/��Ӧѭ�����ǲ��ɱ�ġ���Ҫ��ÿɱ�İ汾����Ҫʹ��.copy()������

�������������������������ʲô������

1.QueryDict.__init__(query_string=None, mutable=False, encoding=None)

��������һ�����캯�������� query_string ��Ҫһ���ַ��������磺

>>> QueryDict('a=1&a=2&c=3')
<QueryDict: {'a': ['1', '2'], 'c': ['3']}>
 

������� query_string û�д��룬����һ���յĶ���

�������������� QueryDict �����ر��� request.POST �� request.GET �õ��ġ���������Լ�ʵ����һ�����󣬿��Դ��� mutable=True ʹ����ʵ�����Ķ���ɱ䡣��Ȼ request.POST �� request.GET ��django�����ģ�Ҳ����˵���Ǹ� django Դ�룬���������ǲ��ɱ�ġ�

�����������õļ���ֵ����� encoding ת��� Unicode��Ҳ����˵�����������ַ��� query_string  �� GBK ������ utf-8 �ı��룬�����Զ�ת��� Unicode��Ȼ�������ֵ�ļ���ֵ����� encoding = None��Ҳ����û���趨�Ļ�����ʹ�� DEFAULT_CHARSET ��ֵ��Ĭ��Ϊ��'utf-8'��

2.QueryDict.__getitem__(key)
�������ظ����� key ��ֵ�����key ���ж��ֵ��__getitem__() ����������£���ֵ����� key �����ڣ�������django.utils.datastructures.MultiValueDictKeyError��������Python ��׼KeyError ��һ�����࣬��������Ȼ���Լ�ֲ���KeyError���� 

 

3.QueryDict.__setitem__(key, value)

�������ø����� key ��ֵΪ[value]��һ��Python �б�ֻ��һ��Ԫ�� value����ע�⣺ֻ�ж����ǿ��Ըı��ʱ�����ʹ�ã�����ͨ�� .copy() ���������Ķ���

 

4.QueryDict.__contains__(key)

�������������key �Ѿ����ã��򷵻�True������������� if "foo" in request.GET  �����Ĳ�����

 

5.QueryDict.get(key, default)

����ʹ��������__getitem__() ��ͬ���߼������ǵ�key ������ʱ����һ��Ĭ��ֵ��

 

6.QueryDict.setdefault(key, default)

�������Ʊ�׼�ֵ��setdefault() ������ֻ�������ڲ�ʹ�õ���__setitem__()��Ҳ����˵����key�Ѿ�����ʱ��������ֵ��key������ʱ������default��ͬʱ��� key �� default�������С�

 

7.QueryDict.update(other_dict)

��������һ��QueryDict ���׼�ֵ䡣���Ʊ�׼�ֵ��update() ���������������ӵ���ǰ�ֵ���ĺ��棬�������滻�����ǡ�

���磺

���ƴ���
>>> q = QueryDict('a=1', mutable=True)    # ��ȻҪ�ɱ�Ĳ���ʹ��
>>> q.update({'a': '2'})
>>> q.getlist('a')
['1', '2']
>>> q['a'] # returns the last
['2']
���ƴ���
 

 

8.QueryDict.items()

�������Ʊ�׼�ֵ��items() ����������һ���ɼ�ֵ��ɵ�Ԫ����б�������ʹ�õ��Ǻ�__getitem__ һ���������µ�ֵ���߼���

���磺

>>> q = QueryDict('a=1&a=2&a=3')
>>> q.items()
[('a', '3')]
 

 

9.QueryDict.iteritems()

�������Ʊ�׼�ֵ��iteritems() ����������һ�������������� QueryDict.items()����ʹ�õ��Ǻ�QueryDict.__getitem__() һ���ķ������µ�ֵ���߼���

 

10.QueryDict.iterlists()

��������QueryDict.iteritems()������һ��������ֵ�Ե�Ԫ��(key, value)�������� ��value ��һ���������� key ��ֵ���б�

 

11.QueryDict.values()

�������Ʊ�׼�ֵ��values() ������������ʹ�õ��Ǻ�__getitem__ һ���������µ�ֵ���߼���Ҳ���Ƿ���һ�����м���Ӧ������ֵ���б�

���磺

>>> q = QueryDict('a=1&a=2&a=3')
>>> q.values()
['3']
 

 

12.QueryDict.itervalues()

��������QueryDict.values()��ֻ�������ص���һ����������

 

13.QueryDict.copy()

�������ض���ĸ�����ʹ��Python ��׼���е�copy.deepcopy()���˸����ǿɱ�ļ�ʹԭʼ�����ǲ��ɱ�ġ�

 

14.QueryDict.getlist(key, default)

������Python �б���ʽ����������ļ������ݡ�����������ڲ���û���ṩĬ��ֵ���򷵻ؿ��б�����֤���ص���ĳ�����͵��б�����Ĭ��ֵ�����б�

 

15.QueryDict.setlist(key, list_)

����Ϊ�����ļ�����list_����__setitem__() ��ͬ)����������һ����Ԫ�ص��б�

 

16.QueryDict.appendlist(key, item)

��������׷�ӵ��ڲ������������б��С�

 

17.QueryDict.setlistdefault(key, default_list)

��������setdefault������������һ���б�����ǵ���ֵ��

 

18.QueryDict.lists()

��������items��ֻ�������ֵ��е�ÿ����Ա��Ϊ�б�Ҳ����˵���б��е�ÿ��Ԫ�أ������ɼ��Ͷ�Ӧ��ֵ�б���ɵĶ�ԪԪ�档

���磺

>>> q = QueryDict('a=1&a=2&a=3')
>>> q.lists()
[('a', ['1', '2', '3'])]
 

 

19.QueryDict.pop(key)

�������ظ�������ֵ���б������ֵ����Ƴ����ǡ�����������ڣ�������KeyError��

���� �U

>>> q = QueryDict('a=1&a=2&a=3', mutable=True)
>>> q.pop('a')
['1', '2', '3']
 

 

20.QueryDict.popitem()

����ɾ���ֵ�����һ����Ա����Ϊû��˳��ĸ���������ض�ֵԪ�飬�������ͼ�������ֵ���б���һ���յ��ֵ��ϵ���ʱ������KeyError��

���� �U

>>> q = QueryDict('a=1&a=2&a=3', mutable=True)
>>> q.popitem()
('a', ['1', '2', '3'])
 

 

21.QueryDict.dict()

��������QueryDict ��dict ��ʾ��ʽ������QueryDict �е�ÿ��(key, list)�� ��dict ����(key, item) �ԣ�����item ���б��е�һ��Ԫ�أ�ʹ����QueryDict.__getitem__()��ͬ���߼���Ҳ�������µģ�

>>> q = QueryDict('a=1&a=3&a=5')
>>> q.dict()
{'a': '5'}
 

 

22.QueryDict.urlencode([safe])

�����������з��ز�ѯ�ַ�����ʽ��

���磺

>>> q = QueryDict('a=2&b=3&b=5')
>>> q.urlencode()
'a=2&b=3&b=5'
 

������ѡ�أ�urlencode ���Դ��ݲ���Ҫ������ַ���������ζ��Ҫ���� url ���룩

����U

>>> q = QueryDict(mutable=True)
>>> q['next'] = '/a&b/'
>>> q.urlencode(safe='/')
'next=/a%26b/'