MYSQL�������

���ݱ����뻹ԭ
��ע�⣺��Ҫ��ֺţ�����½mysql ֱ����cmd������

1�����ݣ�
��mysqldump -uroot -p123 Ҫ���ݵ����ݿ���>���ɵĽű�·��

2���ָ���
��source �ű��ļ�·��

���˿ں�Ϊ��3306

��Ĭ�ϴ洢���棺innodb

��Ĭ���ַ�����utf-8


MYSQL�����رռ���ѯʱ��汾ָ�

������MySQL����			net start mysql ��  sudo service mysql start

����������  		      sudo service mysql restart

���鿴���������Ƿ����mysql���� ps ajx|grep mysql

������mysql���ݿ����̨���      mysql -u�û��� -p����

���鿴�汾���	select version();

����ʾ��ǰʱ����� 	select now();

���˳�MySQL���      quit��exit

������MySQL����			net stop mysql ��  sudo service mysql stop

�޸��û������������ָ�
��1���޸������ʽ���		 set password for �û���@localhost = password('������'); 

��2���޸������ʽ���		mysqladmin -u�û��� -p������ password �����룻

���޸��û������
  ����mysql�⣺		use mysql;
  Ȼ�����룺	update user set user ='���û���' where user ='���û���'��


����������ָ�
���������ݿ����     create database ���ݿ��� charset=utf8;

����ʾ���е����ݿ⣺       show databases��

��ɾ�����ݿ���� 	drop database ���ݿ�����

�����루���ӣ����ݿ����        use ���ݿ���

���鿴��ǰʹ�õ����ݿ����	    select database();

����ǰ���ݿ�����ı���Ϣ���	 show tables;

show create table ����;      չʾ��ϸ���� 

�������ָ�
�����������		create table ���� ((�ֶ��� ���� ����)��(�ֶ��� ���� ����));

���޸ı�����	      alter table ���� rename to �±�����

����ȡ��ṹ���	desc ������   ����   show columns from ������

��ɾ�������		drop table ������

���޸��ֶ����	  alter table ���� change ԭ�ֶ��� ���ֶ��� ��������;

���޸������������		alter table ���� modify �ֶ��� ����������;

��ɾ��һ���ֶ����		alter table ���� drop �ֶ���;

�����ֶ�1�����ֶ�2�������		alter table ���� modify �ֶ���1 �������� after �ֶ���2��

��������������
������������� 	   insert into ���� values (��ӵ�����,)    #���б�������������ԣ��ָ�	
			insert into ���� (�ֶ�,�ֶ�) values (��ӵ�����,)
���鿴���������������	select * from ����;

���鿴��������������	   select �ֶ�,�ֶ� from ����;

����ѯָ���ֶ����		select �ֶ� from ����;

����ѯǰ�����������    	�磺�鿴����ǰ������	   select * from ���� limit 0,2;

����������������� 		alter table ���� add �ֶ� ��������;
	

����ձ����������		delete from ����;

����ձ� ����id���´δ�1��ʼ		truncate table ����;

���ڶ���
��ע�⣺�������ͨ��delete from table ֮�� ���õġ���Ȼ�������ã� 

������е����ݻ����ã���ô��Ҫ���ض���ĳһ��ֵ��ʼ�Զ������Ļ����������� 
����������id��2��ʼ�Զ�������sql���� 

alter table jx_pcmx AUTO_INCREMENT 2; 

alter table jx_pcmx AUTO_INCREMENT �˴�д������id�Ӽ���ʼ���������֣�


��ɾ�������������  	 �磺ɾ�����б��Ϊ1�ļ�¼    delete from ���� where id=1;  

���޸ı����������	  update ���� set �ֶ�=��ֵ where���� 	�磺update ���� set name=��Mary��where id=1;

���ڱ��������ֶ���� alter table ���� add�ֶ� ���� ����;
---���磺�ڱ�MyClass�������һ���ֶ�passtest������Ϊint(4)��Ĭ��ֵΪ��
   mysql> alter table MyClass add passtest int(4) default '';

��ѡȡ�ֶβ��������¼���	insert into ����(�ֶ���1���ֶ���2,....�� values(ֵ1,ֵ2,...),(ֵ1,ֵ2,...)...; 

��ȫ���ֶβ��������¼���	insert into ���� values(ֵ1��ֵ2,...),(ֵ1��ֵ2,...)...;

��ʹ��as ���ֶ���������	select ԭ�ֶ��� as ���ֶ��� from ����;  ��ѯ�����Ľ���ֶ�������ԭ�ֶ�������������ֶ���

��ʹ��distinct���������ظ�����		select distinct �ֶ���,distince �ֶ��� from student; ��ѯ�������Ա��ֶ����������䣨�ֶ�����û���ظ�������



 MySQL֧�ֶ������� ���¿��Է�Ϊ���ࣺ��ֵ������/ʱ�� �� �ַ���(�ַ�)���͡�


�����ֶ����ͣ�
�����Σ�
- tinyint(m)      1���ֽ� ��Χ��-128������127��

- int(m) 	  4���ֽ� ��Χ��-2147483648������2147483647��

- bigint(m��	  8���ֽ� ��Χ ��+-9.22*10��18�η���
 
�������ͣ�     # һ��Ӧ�����������֮��
- float(m,d)	  �����ȸ����� 8λ���ȣ�4�ֽڣ� m�ܸ����� dСλ�� 

- double(m,d)	  ˫���ȸ����� 16λ���ȣ�8�ֽڣ� m�ܸ����� dСλ�� 

��������      # ��ȷֵ һ��Ӧ������Ǯ���֮���
- decimal(m,d)	  ���� m < 65 ���ܸ�����d<30 �� d<m ��Сλ��

���ַ�����
- chr(n) 	  �̶����� ���255���ַ�   # ��ѯ�ٶȿ죬��ռ�̶��ڴ棬�ռ����Ĵ�

- varchar(n)	  ���̶����� ���65535���ַ�    #ռ���ڴ�����ʡ�ռ䣬����ѯ�ٶ���

- text 		  �ɱ䳤�ȣ����65535���ַ�   # ��ȷ������ʱʹ��

- С�ܽ᣺
 char��varchar��ѯ����
 varchar��charռ����Դ��
 char�Ƕ��������255
 varchar�ǲ����������65535
 char(n)�������ַ���С��n,���Կո�����󣬲�ѯ֮ʱ�ٽ��ո�ȥ��������char���ʹ洢���ַ���ĩβ�����пո�varchar�����ڴˡ�
 char(n)�̶����ȣ�char(4)�����Ǵ��뼸���ַ�������ռ��4���ֽڣ�varchar�Ǵ����ʵ���ַ���+1���ֽڣ�n<=255)�������ֽ�(n>255),����varchar(4)����3���ַ�����ռ��4���ֽ�
 decimal(m,n)�ǳ���ȷ��С��



ʱ��/�������ͣ�
��date				����  �磺'2018-12-5'

��time				ʱ�� �磺'12:33:55'

��datetime			����ʱ��   ��:'2018-12-2 22:06:44'

��timestamp			�Զ��洢��¼�޸�ʱ��


�������͵����ԣ�
��null 				���ݿɰ���nullֵ

��not null 			���ݲ��ɰ���nullֵ

��default			Ĭ��ֵ

��primary key			����

��auto_increment		�Զ���������������������

��unsigned			�޷���

��character set 		ָ��һ���ַ���
  name

��bit				��Ϊλ�������� 0�Ǽ� 1���� ��Ϊ�߼�����ʹ�ã�������ʾ�桢�ٻ��ǡ���ȶ�ֵѡ��

����Ȩ�޵Ľ��ͣ�
��file			��MySQL�������϶�д�ļ���

��process		��ʾ��ɱ�����������û��ķ����̡߳�

��reload		���ط��ʿ��Ʊ�ˢ����־�ȡ�

��shutdown		�ر�MySQL����


���ݿ�/���ݱ�/������Ȩ�ޣ�
��alter 		�޸��Ѵ��ڵ����ݱ�(��������/ɾ����)��������

��create		�����µ����ݿ�����ݱ�

��delete		ɾ����ļ�¼��

��drop			ɾ�����ݿ�����ݱ�

��index			������ɾ������

��insert		���ӱ�ļ�¼

��select		��ʾ/������ļ�¼

��update		�޸ı����Ѵ��ڵļ�¼

��enum			ö������

�ر��Ȩ�ޣ�
��all			�������κ��£���rootһ����

��usage			ֻ�����¼�C����ʲôҲ����������



������ѯ��
 ʹ��where�Ӿ�Ա��е�����ɸѡ�����Ϊtrue���л�����ڽ������
 where����֧�ֶ�������������������Ĵ���

���Ƚ��������  >    <   <=     >=     =   !=    is
		select * from ���� where ����;

���߼��������and   or   not 
		select * from ���� where ����;

����Χ��ѯ	between...and...
����	  ������ұգ����Ҷ�������
    select �ֶ� from ���� where �ֶ� between ��ʼ���� and �������䣻

��ģ����ѯ	like 	%��ʾ�����������ַ�	_��ʾһ�������ַ�
 ����		%  �� _ ���Լ�������λ�á�
	select * from ���� where �ֶ� like '�ַ�Ԫ��%';
	select * from ���� where �ֶ� like '%�ַ�Ԫ��';	
	select * from ���� where �ֶ� like '�ַ�Ԫ��_';
	select * from ���� where �ֶ� like '_�ַ�Ԫ��';

���зǿ�	is not null
����	select * from ���� where  �ֶ� is not null;


���ȼ���
���ȼ��ɸߵ��͵�˳��Ϊ��С���ţ�not���Ƚ���������߼������
and��or�����㣬���ͬʱ���ֲ�ϣ������or����Ҫ���()ʹ��


������	Ĭ������			����|����
  �﷨��	select * from ���� order by �ֶ��� asc|desc 

˵����
�������ݰ�����1�����������ĳЩ����1��ֵ��ͬʱ��������2�����Դ�����
Ĭ�ϰ�����ֵ��С�������У�asc��
asc��С�������У�������
desc�Ӵ�С���򣬼�����
�����������ִ��ǰ�������


�ۺϺ�����
��������	count(*) ��ʾ������������������д�����������������ͬ��
	select count(*) from ����;

�����ֵ��	max(�ֶ���) ��ʾ����е����ֵ
	select max(�ֶ���) from ����;  �� select max(�ֶ���1) from ���� where �ֶ���2=��ֵ;

����Сֵ��	min(�ֶ���) ��ʾ����е���Сֵ
	select min(�ֶ���) from ����;  �� select min(�ֶ���1) from ���� where �ֶ���2=��ֵ;

����ͣ�	sum(�ֶ���)��ʾ����еĺ�
	select sum(�ֶ���) from ����;  �� select sum(�ֶ���1) from ���� where �ֶ���2=��ֵ;

��ƽ��ֵ��	avg(�ֶ���)��ʾ����е�ƽ��ֵ
	select avg(�ֶ���) from ����;  �� select avg(�ֶ���1) from ���� where �ֶ���2=��ֵ and �ֶ���3=��ֵ;

�����飺	group by
	select �ֶ���1 from ���� group by �ֶ���1;  �� select avg(�ֶ���1) from ���� where �ֶ���2=��ֵ and �ֶ���3=��ֵ;
˵����
       group by�ĺ���:����ѯ�������1�������ֶν��з��飬�ֶ�ֵ��ͬ��Ϊһ��
       group by�����ڵ����ֶη��飬Ҳ�����ڶ���ֶη���


��Щ��������ô�ã�
�� �﷨ע�⣺  select @1,�ֶ�1 from ���� group by �ֶ�1 
	�� select �ֶ�1,@1 from ���� where ���� group by �ֶ�1;
          @1  ---  λ��ֻ�ܷžۺϺ�����group_concat�ͷ�����ֶ�

��ͳ�Ʒ��飺
����	 select avg(�ֶ���1),�ֶ���2 from ���� group by �ֶ���2;
����	 select count(�ֶ���1),�ֶ���2 from ���� group by �ֶ���2;

��Ƕ�ײ�ѯ��
����	 select *from ���� where �ֶ���1=(select min(�ֶ���1) from ����);

��group by + group_concat()	
    group_concat(�ֶ���)������Ϊһ������ֶ���ʹ�ã�
    ��ʾ����֮�󣬸��ݷ�������ʹ��group_concat()������ÿһ���ĳ�ֶε�ֵ�ļ���
 ����	select �ֶ���1,group_concat(�ֶ���2) from ���� group by �ֶ���1��
     �� select �ֶ�1,group_concat(�ֶ�2) from ���� where ���� group by �ֶ�1;
	
��group by + ���Ϻ���
     ͨ��group_concat()�����������Ǽ�Ȼ����ͳ�Ƴ�ÿ�������ĳ�ֶε�ֵ�ļ��ϣ���ô����Ҳ����ͨ�����Ϻ����������ֵ�ļ�����һЩ����
����	select �ֶ���1,group_concat(�ֶ���2) from ���� group by �ֶ���1;
	select �ֶ���1,count(*) from ���� group by �ֶ���;

��group by + having
	having �������ʽ�����������ѯ��ָ��һЩ�����������ѯ���
	���ʣ�having���ú�whereһ������havingֻ������group by
����	select gender,count(*) from ���� group by �ֶ��� having count(*)>��ֵ;

��group by + with rollup
	with rollup�������ǣ����������һ�У�����¼��ǰ�������м�¼���ܺ�
����	select �ֶ���1,count(*) from ���� group by �ֶ���1 with rollup;
	select �ֶ���1,group_concat(�ֶ���2) from ���� group by �ֶ���1 with rollup;

������select���˳��
select distince *
from ����
where ...
group by ... having ...
order by ...
limit start��count


select  ��ȡ�鿴
from    ����
where   ���������
group by   ����
having    �Է��������һ��ɸѡ 
limit��m,n��   ��ҳ  m ��ʼλ��  n ÿҳ����������
count���� �������� ��������Լ����� ����ĳ������
group_concat()  �ϲ�������� ���������Ҫ�ϲ�����������  

��where��having֮���������÷�
���õĶ���ͬ��WHERE �Ӿ������ڱ����ͼ��HAVING �Ӿ��������顣
�ۺϺ����ǱȽ�where��having �Ĺؼ��� 
where���ۺϺ�����having ��from�����ִ��˳��where>�ۺϺ���(sum,min,max,avg,count)>having
�г�group by���Ƚ϶��ߡ�������where��having ��ʹ��group byʱ�ʵ���ࣩ 
��������ۺϺ�������group by ������й��� ��ֻ����having��
ע������ �� 

1��where ���ܸ��ۺϺ�������Ϊwhereִ��˳����ھۺϺ����� 

2��where �Ӿ���������ڶԲ�ѯ������з���ǰ����������where��������ȥ����
���ڷ���֮ǰ�������ݣ������в��ܰ������麯����ʹ��where������ʾ�ض����С�

3��having �Ӿ��������ɸѡ�����������飬���ڷ���֮��������ݣ������о���
�������麯����ʹ��having ������ʾ�ض����飬Ҳ����ʹ�ö�������׼���з��顣



��ҳ��	
��ҳ��select *from ���� limit ��ʼλ��start,��������count;
   ��  select *from ���� where ���� limit ��ʼλ��start,��������count;

��ҳ��ҳ
��֪��ÿҳ��ʾm�����ݣ���ǰ��ʾ��nҳ
����ҳ�����˶��߼��������python��ʵ��
��ѯ������p1
ʹ��p1����m�õ�p2
���������p2Ϊ����ҳ
�����������p2+1Ϊ��ҳ��
���nҳ������
����   select *from ���� limit (n-1)*m,m;



�����Ӳ�ѯ����ѯ�Ľ��Ϊ������ƥ�䵽������
�﷨1�� inner join     on
select *from ����� inner join �ұ��� on �����.����������ֶ� = �ұ���.����������ֶ�;
�� select *from ����� inner join �ұ��� on �����.����������ֶ� = �ұ���.����������ֶ�
 where �ұ���.�����ֶ�=ֵ and �����.�����ֶ�>ֵ;

���� ��鿴��ͬ�꼶 ÿ���꼶����˭ ÿ���꼶���ж�����
select class.name,group_concat(student.name),count(student.id)
 from student inner join class on
 class.id=student.class_id group by class.name;

�﷨2��
select �����.�ֶ�1,group_concat(�ұ���.�ֶ�1),count(�ұ���.����������ֶ�)
 from �ұ��� inner join ����� on
 �����.����������ֶ�=�ұ���.�����������ֶ� group by �����.�ֶ�һ;



�����Ӳ�ѯ��  right join     on
��ѯ�Ľ��Ϊ������ƥ�䵽�����ݣ��ұ����е����ݣ���������в����ڵ�����ʹ��null���

�﷨��
select *from �ұ��� right join ����� on �ұ���.����������ֶ� = �����.����������ֶ�;



�����Ӳ�ѯ��   left join     on
��ѯ�Ľ��Ϊ������ƥ�䵽�����ݣ�������е����ݣ������ұ��в����ڵ�����ʹ��null���

�﷨��
select *from ����� left join �ұ��� on �����.����������ֶ� = �ұ���.����������ֶ�;






��ѯ���� ĳ�ֶ��ظ����ݵĸ��������ĸ���
select �ֶ�1,count(*) as count from ���� group by �ֶ�1 having max(count);

select �ֶ�1,count(*) as count from ���� as a group by �ֶ�1 having max(count) order by �ֶ�1,count limit 0,1;

��ͼ 
MySql������ͼ
(1).��һ�ࣺcreate view ��ͼ�� as select * from ����;

(2).�ڶ��ࣺcreate view ��ͼ�� as select �ֶ�,�ֶ�,�ֶ� from ����;

(3).�����ࣺcreate view ��ͼ��v[vid,vname,vage] as select �ֶ�,�ֶ�,�ֶ� from ����
ɾ����ͼ
drop view ��ͼ����


mysql��ȥ��          distinct

 
explain select �ֶ�1 from ���� where �ֶ�1=ֵ;     �鿴���Ҵ���


create index ������ on ����(����ֶ�);     ������

drop index ������ on ����;   ɾ������


���   alter table ����1 add constraint ������� foreign key(����1) references ����2(����2)��



pymysql ������

# -*- coding: UTF-8 -*-
# ����connect
from pymysql import connect
# ��������
conn= connect(host='localhost',port=3306,database='����',user='�û���',password='����',charset='utf8')
# ��ȡcursor����
cur = conn.cursor()
# ִ��sql���
sql ="sql �������"
cur.execute(sql)
# ȡ������ fetchone ȡһ������   fetchall ȡ��������
data=cur.fetchall()
# ����һ���б�
userlist = []
for i in data:
    # ����һ���ֵ��������Ϣ
    userdict = {}
    userdict['�ֶ�'] = i[-1]       # ����λ����Ϣ
    userdict['�ֶ�'] = i[1]
    userdict['�ֶ�'] = i[2]
    userdict['��С���ֶ�'] = float(i[3])
    userlist.append(userdict)  # ���Ԫ��
    # print(data)
#  ���
print(userlist)
#�ر�����
cur.close()
conn.close()


# ����ģ��
from pymysql import connect
# ��������
ck = connect(host='localhost',port=3306,database='����',user='�û���',password='����',charset='utf8')
# ��ȡcursor����
con = ck.cursor()
# ִ��sql���
con .execute("sql �������")
# �ύ
ck.commit()


'''
host             ����           
localhost        ��������                   
port             �˿�              
database         ���ݿ�              
user             �û�         
password         ����       
charset          �ַ���         
'''


select name from class where name='���꼶';

��������������������

















