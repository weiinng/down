������select���
select distince *
from ����
where ...
group by ... having ...
order by ...
limit start,count



��ͼ
1�����⣺
���ڸ��ӵĲ�ѯ���������ж�����ݽ��й�����ѯ���õ���������ݿ���Ϊ�����ԭ�����˸ı䣬Ϊ�˱�֤��ѯ������������֮ǰ��ͬ������Ҫ�ڶ���ط������޸ģ�ά�������ǳ��鷳

����취��������ͼ

2����ͼ��ʲô��
ͨ�׵Ľ�����ͼ����һ��select���ִ�к󷵻صĽ���������������ڴ�����ͼ��ʱ����Ҫ�Ĺ��������ڴ�������SQL��ѯ����ϣ���ͼ�Ƕ������Ż���������ã�һ�������ѯ���ִ�еĽ�������洢��������� �����������ݷ����˸ı䣬��ͼҲ����Ÿı䣩��




����


������
����������
create index �������� on ����(�ֶ����ƣ����ȣ�����
��������ַ������;Ͳ��üӳ���

�鿴������
show index from ������

ɾ��������
drop index �������� on ������

ʹ��pycharm�����ݿ������ɾ�Ĳ飺
�����ںڴ��ڴ�������
create database s;
use s;
create table s(
id int,
name varchar(10)
);

��pycharm
from pymysql import connect
conn=connect(host='localhost',port=3306,database='s',user='root',password='1',charset='utf8')
cursor=conn.cursor()
for x in range(10):
	cursor.execute("insert into s values(%d,'����%d��','%s')"%(x,x,'woshinibaba'))
conn.commit

ע��ע��
��ʽ��������ַ���ʱ  %sҲҪ�����ţ�������������������������������������������1

��������޸����ݵ�ʱ�������˫���ţ�����

cursor.execute("select *from s")
result=cursor.fetchall()
for x in result:
	print(x)
