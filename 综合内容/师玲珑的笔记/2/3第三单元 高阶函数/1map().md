map()�����÷���
map(function,iterable,...)
���ܣ�����һ������function���������ڲ����ɵ��������е�ÿһ��Ԫ���ϣ����ذ���ÿ��function��������ֵ���µ�����
������
function--�������м������������洫�����ɵ�������
iterable--һ�������ɵ��������磬���У�
����ֵ��
python 3.x

ʵ����
def add(n,q,e):
	return n+q+e
f=map(add,[1,2],{1,2},(1,2))
for x in f:
	print(x)
����ǣ�
3
6


���ʱҲ����print(list(f))
����ǣ�
[3,6]
�ǽ������һ���б����ʽ���


def add(n):
	return n*n
f=map(add,[1,2,3])
for x in f:
	print(x)
����ǣ�
1
4
9









