map()������
def f(n):
	if n%2==0:
		return n
r=map(f,[1,2,3])
for x in r:
	print(x)
����ǣ�
None
2
None

def f(n):
	return n%2==0
r=map(f,[1,2,3])
for x in r:
	print(x)
����ǣ�
False
True
False



filter()������
def f(n):
	return n%2==0
r=filter(f,[1,2,3])
for x in r:
	print(x)
����ǣ�
2

����filter()���� ��������return �����ж����ķ��صĶ���True �� False