求所有电脑产品的平均价格，并且保留两位小数：
select round(avg(price),2) avg_price from goods;

查询每种类型中最贵的信息
select *from goods
inner join
(
select name,max(price) as max_price  from goods group by name
)  as new
on new.name=goods.name and new.max_price=goods.price;

将分组结果写入到cate_goods数据表中
insert into cate_goods(name) select name from goods group by name;

同步表数据：
通过goods_cates数据表来更新goods表
update goods as g inner join goods_cates as c on g.cate_name=c.name set g.cate_name=c.id;

语法：
要更新数据的表：a
根据aa表进行更新a表的数据
他这个应该只改了部分数据，id没改，name改了  则更新数据：
update  a inner join aa on a.id=aa.id set a.name=aa.name;


创建表的同时插入数据：
create table aaa(
id int,
name varchar(10)
)
select id,name from a;
这样就把a表里的id,name的值插入到aaa表里了

