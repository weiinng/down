alter database ���ݿ��� character set utf8;
create database ���ݿ��� charset=utf8;

��һ��������ȫ��ɾ��ʱ��id��������������
truncate table ����;�´�id��1��ʼ  ԭ������ȫ��ɾ��

Ҫ�ǲ���ȫ��ɾ��  �� 
alter table ���� auto_increment 2;
�´�id��2��ʼ

���ȼ�  �ɸߵ��ͣ�
С���ţ�not,�Ƚ���������߼������
and��or�����㣬���ͬʱ���ֲ�ϣ������or����Ҫ��ϣ���ʹ��

���ݱ����뻹ԭ
ע�⣺��Ҫ��ֺţ�����½mysql ֱ����cmd������

1�����ݣ�
mysqldump -uroot -p123 Ҫ���ݵ����ݿ���>���ɵĽű�·��

2���ָ���
source �ű��ļ�·��

�˿ں�Ϊ��3306

Ĭ�ϴ洢���棺innodb

Ĭ���ַ�����utf8

�鿴���б�
show tables;

�鿴�������ݿ�
show databases;

�鿴��ṹ
desc ����;

�л����ݿ�
use ���ݿ���


decimal(m,n)�ǳ���ȷ��С��

������ date
ʱ���� time 
������ʱ���� datetime
�ı����� text  �������������������
unsigned �������ǰ��

�������͵�����
mysql�ؼ���   		����
NULL			�����пɰ���NULLֵ
NOT NULL		�����в��������NULLֵ
DEFAULT			Ĭ��ֵ
PRIMARY KEY		����
AUTO_INCREMENT	�Զ���������������������
UNSIGNED		�޷���
CHARACTER SET name	ָ��һ���ַ���

select IFNULL(age,0) from emp;   ��age��NULL��Ĭ��Ϊ0

�鿴�汾��select version();

��ʾ��ǰʱ�䣺select now();

�鿴��ǰʹ�õ����ݿ�:select database(); 

�޸����룺
set password for root@localhost=password('������');

enum('��','Ů')  ��һ���ֶ��趨����������ֻ�ܲ����л���Ů!!!

ɾ����
drop table ����;

ɾ�����ݿ�
drop database ���ݿ���;

ɾ��һ�����ݣ�
delete from ���� where ����;

�޸ı�����
alter table ���� rename to �±���;

�޸��ֶ�����
alter table ���� change ԭ�ֶ��� ���ֶ��� ��������;

�޸��������ͣ�
alter table ���� modify �ֶ��� ����������;

ɾ��һ���ֶΣ�
alter table ���� drop �ֶ���;

���ֶ�1�����ֶ�2���棺
alter table ���� modify �ֶ���1 �������� after �ֶ���2��


��������
1��ѡȡ�ֶβ��������¼
insert into ����(�ֶ���1���ֶ���2,....�� values(ֵ1,ֵ2,...),(ֵ1,ֵ2,...)...; 
2��ȫ���ֶβ��������¼
insert into ���� values(ֵ1��ֵ2,...),(ֵ1��ֵ2,...)...;

�޸�����
update ���� set Ҫ�޸ĵ��ֶ���=�µ�ֵ where ����;

ʹ��as ���ֶ������
select id as code from student;  ��ѯ�����Ľ���ֶ�������id�������code

ʹ��distinct���������ظ�����
select distinct sex, age from student; ��ѯ�������Ա������û���ظ�������

������ѯ��
ʹ��where�Ӿ�Ա��е�����ɸѡ�����Ϊtrue���л�����ڽ������
where����֧�ֶ�������������������Ĵ���

select concat('�ҽ�',name,'�ҵ�������',age) from stu;


�Ƚ������ ��>,<,<=.>=,=,!=��is

�߼��������and,or,not,

ģ����ѯ��
like'%_'  %����ƥ��������ַ���
_ֻ����ƥ�䵽һ���ַ�

��Χ��ѯ��
age between 15 and 20  ������15��20֮���   
age in(1,2,4,5) ������1��2��4��5������

����
select name,age,score from student order by age desc,socre asc;
�Ȱ�������н����������һ���ٰ��ɼ���������


�ۺϺ���
Ϊ�˿��ٵõ�ͳ�����ݣ��������õ�����5���ۺϺ���
������
count��*����ʾ��������Ϊ�ǿյ���������������д*�������������ͬ��
select count(*) from student;

���ֵ��
max(����) ��ʾ����е����ֵ
select max(id) from student;

��Сֵ
min(����) ��ʾ����е���Сֵ
select min(id) from student;

��ͣ�
sum(��������ʾ����еĺ�
select sum(age) from student;

ƽ��ֵ��
avg(��������ʾ����е�ƽ��ֵ
select avg(id) from student;


���飺
group by
group by�ĺ��壺����ѯ�������1�������ֶν��з��飬�ֶ�ֵ��ͬ��Ϊһ��
group by�����ڵ����ֶη��飬Ҳ�����ڶ���ֶη���

group by+���Ϻ���
ͨ��group_concat()�����������Ǽ�Ȼ����ͳ�Ƴ�ÿ�������ĳ�ֶε�ֵ�ļ��ϣ���ô����Ҳ����ͨ�����Ϻ����������ֵ�ļ�����һЩ����

select gender,group_concat(name,age) from stu group by gender;
���Ϊ��
gender   group_concat(age)
��	����11,����12,����13,����14,����15
Ů	��12,��33,��45,��51

�ֱ�ͳ���Ա�Ϊ��/Ů��������ƽ��ֵ
select sex,avg(age) from stu group by sex;

group by + having
having�������ʽ�����������ѯ��ָ��һЩ�����������ѯ���
having���ú�whereһ������havingֻ������group by

select sex,count(*) from stu group by sex having count(*)>2;

group by + with rollup
with rollup�������ǣ����������һ�У�����¼��ǰ�������м�¼���ܺ�
select gender,coount(*) from stu group by gender with rollup;

��ҳ
��ȡ������
������������ʱ����һҳ�鿴������һ���ǳ��鷳������
�﷨��
select *from ���� limit start,count;
��start��ʼ����ȡcount������
���磺�鿴ǰ�������ݣ�
select *from stu limit 0,3;

���nҳ������
select *from stu where limit (n-1)*m,m;

���Ӳ�ѯ
����ѯ���������Դ�ڶ��ű�ʱ����Ҫ�����ű����ӳ�һ��������ݼ�����ѡ����ʵ��з���

�����ӣ�
select *from emp inner join dept on emp.deptno=dept.deptno;

������
�������ӣ�
select *from emp left outer join dept on emp.deptno=dept.deptno;
�������ӣ�
select *from  emp right outer join dept on emp.deptno=dept.deptno;

����������
create table s(
sid int primary key,
name varchar(10)
);

ɾ��������
alter table ���� drop primary key;

����������
create table stu(
id int primary key auto_increment,
name varchar(10)
);

�޸ı�ʱ����������
alter table stu change sid sid int auto_increment;

�޸ı�ʱɾ������������
alter table stu change sid sid int;

�ǿ�Լ����not null
ΨһԼ����unique
create table s(
id int not null unique
);

����Լ����Ψһ�ġ��ǿյġ������Ա�����
�ǿ�Լ���Ƿǿյ�
ΨһԼ����Ψһ��
�ǿ�Լ��+ΨһԼ����=����Լ��

ɾ��ΨһԼ��
alter table ���� drop index ����;

���������
create table s(
id int,
constraint fk_������ foreign key(����ֶ���) references ������(�����ֶ���)
);

�޸����������
alter table ������ add constraint fk_������ foreign key(����ֶ���) references �������������ֶ�������

ɾ�������
alter table ������ drop foreign key fk_������;

ע�ͣ�
create table s(
id int comment '����',
age int
);
������Ч��һ��