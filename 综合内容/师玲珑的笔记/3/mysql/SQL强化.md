�����е��Բ�Ʒ��ƽ���۸񣬲��ұ�����λС����
select round(avg(price),2) avg_price from goods;

��ѯÿ��������������Ϣ
select *from goods
inner join
(
select name,max(price) as max_price  from goods group by name
)  as new
on new.name=goods.name and new.max_price=goods.price;

��������д�뵽cate_goods���ݱ���
insert into cate_goods(name) select name from goods group by name;

ͬ�������ݣ�
ͨ��goods_cates���ݱ�������goods��
update goods as g inner join goods_cates as c on g.cate_name=c.name set g.cate_name=c.id;

�﷨��
Ҫ�������ݵı�a
����aa����и���a�������
�����Ӧ��ֻ���˲������ݣ�idû�ģ�name����  ��������ݣ�
update  a inner join aa on a.id=aa.id set a.name=aa.name;


�������ͬʱ�������ݣ�
create table aaa(
id int,
name varchar(10)
)
select id,name from a;
�����Ͱ�a�����id,name��ֵ���뵽aaa������

