reduce()������
reduce(function,iterable[,initializer])
���ܣ�
������һ�����ݼ��ϣ�����Ԫ��ȣ��е��������ݽ������в�����
�ô���reduce�еĺ���function(����������)�ȶԼ����еĵ�1��2��Ԫ�ؽ��в������õ��Ľ�����������������function�������㣬���õ�һ�����
��Ч�����ƣ�ruduce(f,[x1,x2,x3])=f(f(x1,x2),x3)
������
function--����������������
iterable--�ɵ�������
initializer--��ѡ����ʼ����

���磺
from functools import reduce
def add(x,y):
	return x+y
q=[1,2,3,4]
f=reduce(add,q[2::])
print(f)
���Ϊ7
�б�Ҳ������Ƭ   Ҫ��ס��Ƭ�ķ�Χ������ҿ�

reduce�ﴫ�ĺ�����ֻ������������
map��ɴ�һ��������������������



