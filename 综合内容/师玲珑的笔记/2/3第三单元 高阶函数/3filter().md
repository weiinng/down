filter()����
filter(function,iterable)
���ܣ�
�ý���������������һ��Ϊ�������ڶ���Ϊ���У����е�ÿ��Ԫ����Ϊ�������ݸ����������жϣ�Ȼ�󷵻�True��False,��󽫷���True��Ԫ�طŵ��µĵ�����������
����
function--�жϺ���
iterable--�ɵ��������� ���У�
����ֵ��
����һ������������

ʵ����
def add(n):
	return n%2==1
f=filter(add,[1,2,3,4])
for x in f:
	print(x)
���Ϊ��
1
3

dict2=[{'name':'С��','age':10},{'name':'С��','age':20},{'name':'У��','age':15}]
print(sorted(dict2,key=lambda x:x['age']))
