sorted()����
sorted(iterable,key=abs,reverse=False)
���ܣ������пɵ�����������������
����
iterable--�ɵ�������
key--keyָ���Ĺ�ɣũ���������ڿɵ��������ϵ�ÿһ��Ԫ�أ�������key�������صĽ����������
reverse--�������reverse=True����reverse=False����Ĭ�ϣ�
����ֵ��
��������������б�

���磺
list=['I','am','and','student']
���յ��ʳ��Ƚ��н�������
print(sorted(list,key=lambda x:len(x),reverse=True))
���Ϊ��
['student', 'and', 'am', 'I']

stus=[
{"name":"zhangsan","age":18},
{"name":"zhangsan","age":17},
{"name":"zhangsan","age":19}
]
����������������
print(sorted(stus,key=lambda x : x['age']))
���Ϊ��
[{'name': 'zhangsan', 'age': 17}, {'name': 'zhangsan', 'age': 18}, {'name': 'zhangsan', 'age': 19}]

���ۣ�sorted()�������һ�������ǿɵ�������
�ڶ���������key=lambda x: x(�ɵ��������е�Ԫ��)



