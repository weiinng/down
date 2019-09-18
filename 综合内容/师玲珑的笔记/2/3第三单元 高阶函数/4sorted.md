sorted()函数
sorted(iterable,key=abs,reverse=False)
功能：对所有可迭代对象进行排序操作
参数
iterable--可迭代对象
key--key指定的哈桑农户将作用于可迭代对象上的每一个元素，并根据key函数返回的结果进行排序
reverse--排序规则，reverse=True降序，reverse=False升序（默认）
返回值：
返回重新排序的列表

例如：
list=['I','am','and','student']
按照单词长度进行降序排序：
print(sorted(list,key=lambda x:len(x),reverse=True))
结果为：
['student', 'and', 'am', 'I']

stus=[
{"name":"zhangsan","age":18},
{"name":"zhangsan","age":17},
{"name":"zhangsan","age":19}
]
按照年龄升序排序
print(sorted(stus,key=lambda x : x['age']))
结果为：
[{'name': 'zhangsan', 'age': 17}, {'name': 'zhangsan', 'age': 18}, {'name': 'zhangsan', 'age': 19}]

结论：sorted()函数里第一个参数是可迭代对象
第二个参数是key=lambda x: x(可迭代对象中的元素)



