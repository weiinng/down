mongoDB 命令：


连接-打开mongodb数据库：	monggo



查看当前所在库：显示当前使用的数据库名称	db.getName()  或   db;

删当前使用的数据库	db.dropDatabase() 

修复当前数据库		db.repairDatabase() 

当前数据库版本		db.version()   

查看当前数据库的链接机器地址 		db.getMongo()  

显示当前数据库状态，包含数据库名称，集合个数，当前数据库大小 ...	db.stats()

查看数据库中有那些个集合（表）：	db.getCollectionNames()


查看所有库：		show dbs;

进入数据库（没有的话自动创建）自动创建：	use 库名;

删除当前的数据库：	db.dropDatabase()


创建集合：		db.createCollection("集合名");

查看所有集合：		show collections;

插入数据		db.集合名.insert({"":"","":""});

插入数据小案例：
单条写入数据：
db.posts.insert({"title":"我的第一篇博客","content":"我要开始写博客了"});
db.posts.insert({"title":"我的第二篇博客","content":"写点什么好呢"});
多条写入：加Many方法 或 所有的key不加引号
db.posts.insertMany([{"title":"我的第三篇博客"},{"content":"今天吃什么"}]);
遍历写入数据：(支持css语法，var可加可不加)
for(var i=4;i<=10;i++){db.posts.insert({"title":"我的第"+i+"篇博客"})};


查看集合内所有数据：		db.集合名.find();

条件查找：
格式：db.集合名.find({"字段名":{条件}});
$gte	大于等于
$gt	大于
$lte	小于等于
$lt	小于
$eq	等于
$ne	不等于

正则表达式：/k/,/^k/

按照字段取唯一的值（可去重）：		db.posts.distinct('字段名');

指定提取的字段（投影）(value值为布尔类型true/1,flase/0)：		
语法：		db.字段名.find({},{'字段名':true,'字段名2':1});




案例数据：
db.posts.insert({'title' : '怪物猎人世界评测', 'rank' : 2, 'tag' : 'game' });
db.posts.insert({'title' : '纸片马里奥试玩体验', 'rank' : 1, 'tag' : 'game' });
db.posts.insert({'title' : 'Ubuntu16LTS的安装', 'rank' : 3, 'tag' : 'it' });
db.posts.insert({'title' : '信长之野望大志销量突破10000', 'rank' : 4, 'tag' : 'game' });
db.posts.insert({'title' : 'Ruby的开发效率真的很高吗', 'rank' : 7, 'tag' : 'it' });
db.posts.insert({'title' : '塞尔达传说最近除了DLC', 'rank' : 4, 'tag' : 'game' });
db.posts.insert({'title':'惊！骑士发生重大交易', 'istop':true});



条件查询：
db.posts.find({'rank':{$gte:4}});	查询rank大于等于4的记录
db.posts.find({'rank':{$gt:4}});	查询rank大于4的记录
db.posts.find({'rank':{$lte:4}});	查询rank小于等于4的记录  
db.posts.find({'rank':{$lt:4}});	查询rank小于4的记录
db.posts.find({'rank':{$eq:4}});	查询rank等于4的记录
db.posts.find({'rank':{$ne:4}});	查询rank不等于4的记录

正则查找：
db.posts.find({'title':/u/});		查找title里面含有u的记录
db.posts.find({'title':/U/});		查找title里面开头是U的记录



复杂条件查询文档 -格式： 	
与		db.集合名.find({"":"","":""});
or或		db.集合名.find({$or:[{"":""},{"":""}:{"":""}]});
in在...里	db.集合名.find({'字段名':{$in:[要找到的值]}});
判断该字段是否存在	db.posts.find('字段名'：{$sexists:true});

实战案例：
与	db.posts.find({'title':/u/,'rank':{$gte:5}});
or或	db.posts.find({$or:[{'title':/u/},{'rank':{$gte:5}}]});
in在...里	db.posts.find({'rank':{$in:[1,2,3]}});
按照字段tag取唯一的值	db.posts.distinct('tag');
判断该字段是否存在	db.posts.find('istop'：{$exists:true});


指定提取的字段（投影）(value值为布尔类型true/1,flase/0)		db.posts.find({'title':/u/},{'title':true,'rank':1,'_id':0});



其他方法(管道):
sort()		排序
limit()		限制条数（分页）
skip()		跳过文档
格式：
db.集合名.find({}).sort({'字段':1});	正序
db.集合名.find({}).sort({'字段':1}).limit(3);		正序前三条
db.集合名.find({}).sort({'字段':1});	

实战案例：
db.posts.find({}).sort({'rank':1});

db.posts.find({}).sort({'rank':-1,'title':-1});

db.posts.find({}).sort({'rank':-1}).limit(3);

db.posts.find({}).sort({'rank':-1}).skip(3).limit(3);





更新文档：
update(<filter>,<update>,<options>)	---filter=条件、update=更新内容、options=加{multi:true}更新所有（不加只更新一条） 

db.posts.findOne（{"":""}）		指定查看一条


实战：
db.posts.findOne({'title':'怪物猎人世界评测'})；	指定查看
db.posts.update({'title':'怪物猎人世界评测'},{$set:{'rank':16}});	保留原有字段更新rank字段
db.posts.update({'title':'怪物猎人世界评测'},{'rank':19});	冲掉非_id字段换成rank字段
db.posts.update({"tag":"it"},{$set:{"rank":199}},{multi:true});		多条更新



文档删除：

格式 ： db.集合名.remove(<query>,{justOne:true})
query：		可选，条件
justOne:  	可选，如果设为true或1 表示删除一条  默认False，表示删除多条

实战用法：
移除所有文档		db.集合名.remove({});
移除指定文档		db.集合名.remove({'字段':{条件}},{justOne:true});




统计个数：
.count()   	用于统计集合中的文档条数

实战用法：
db.集合名.find({"":{条件}}).count()
db.集合名.count({"":{条件}})



聚合：
aggregate()	聚合(aggregate)是基于数据处理的聚合管道，每个文档通过一个由多个阶段（stage）组成的管道，
可以对每个阶段进行分组、过滤等功能，然后经过一系列的处理，输出相应的结果
$group		将集合中的文档分组，可用于统计结果
$match		过滤数据，只输出符合条件的文档
$group： 	将集合中的文档分组， 可用于统计结果（$group是所有聚合命令中用的最多的一个命令，用来将集合中的文档分组，可用于统计结果）
$match： 	过滤数据， 只输出符合条件的文档
$project： 	修改输入文档的结构， 如重命名、 增加、 删除字段、 创建计算结果
$sort： 	将输入文档排序后输出
$limit： 	限制聚合管道返回的?档数
$skip：	 	跳过指定数量的?档， 并返回余下的?档

注意点：
db.db_name.aggregate是语法，所有的管道命令都需要写在其中
_id 表示分组的依据，按照哪个字段进行分组，需要使用$gender表示选择这个字段进行分组


在管道中排序，按先排序后显示操作，管道自左而右执行

常用表达式：	表达式：处理输文档并输出 语法：表达式:'$列名' 常用表达式:
$sum： 计算总和， $sum:1 表示以1倍计数

$avg： 计算平均值
$min： 获取最小值
$max： 获取最大值
$push： 在结果文档中插入值到1个数组中




实战语法：
db.集合名.aggregate([ { $group:{ '_id':'$字段分组', 获取的信息变量名:{$push:'$要获取的字段名'} } } ]);
单位数		$sum:1	  每个单位为1



实战案例数据：
db.students.insert({"name" : "郭靖", "hometown" : "蒙古", "age" : 20, "gender" : true });
db.students.insert({"name" : "黄蓉", "hometown" : "桃花岛", "age" : 18, "gender" : false })
db.students.insert({"name" : "华筝", "hometown" : "蒙古", "age" : 18, "gender" : false });
db.students.insert({"name" : "黄药师", "hometown" : "桃花岛", "age" : 40, "gender" : true });
db.students.insert({"name" : "段誉", "hometown" : "大理", "age" : 16, "gender" : true });
db.students.insert({"name" : "段王爷", "hometown" : "大理", "age" : 45, "gender" : true });
db.students.insert({"name" : "洪七公", "hometown" : "华山", "age" : 18, "gender" : true });




实战演习：
db.students.remove({'rank':{$lt:4}},{justOne:true});
db.students.remove({});


db.students.find({'rank':{$lt:4}}).count();
db.students.count({'rank':{$lt:4}});


1 按照某个字段进行分组
$group是所有聚合命令中用的最多的一个命令，用来将集合中的文档分组，可用于统计结果

db.students.aggregate([ { $group:{'_id':'$gender'} } ]);
db.db_name.aggregate是语法，所有的管道命令都需要写在其中
_id 表示分组的依据，按照哪个字段进行分组，需要使用$gender表示选择这个字段进行分组
db.students.aggregate([ { $group:{'_id':'$gender', counter:{$sum:1} } } ]);
$sum:1 表示把每条数据作为1进行统计，统计的是该分组下面数据的条数

2 group by null
当我们需要统计整个文档的时候，$group 的另一种用途就是把整个文档分为一组进行统计

db.students.aggregate([{$group:{'id':null,counter:{$sum:1}}}]);
_id:null 表示不指定分组的字段，即统计整个文档，此时获取的counter表示整个文档的个数

3  数据透视
正常情况在统计的不同姓名的数据的时候，需要知道所有的name，需要逐条观察，如果通过某种方式把所有的name放到一起，那么此时就可以理解为数据透视
db.students.aggregate([{$group:{'_id':null,'name':{$push:'$name'}}}]);

使用$$ROOT可以将整个文档放入数组中
db.students.aggregate([{$group:{'_id':null,'name':{$push:'$$ROOT'}}}]);






聚合的高级应用：


实战数据：
db.infos.insertMany([
{ "country" : "china", "province" : "sh", "userid" : "a" },
{ "country" : "china", "province" : "sh", "userid" : "b" },
{ "country" : "china", "province" : "sh", "userid" : "c" },
{ "country" : "china", "province" : "sh", "userid" : "d" },
{ "country" : "china", "province" : "tj", "userid" : "a" },
{ "country" : "china", "province" : "tj", "userid" : "b" },
{ "country" : "china", "province" : "tj", "userid" : "c" },
{ "country" : "china", "province" : "bj", "userid" : "a" },
{ "country" : "china", "province" : "bj", "userid" : "b" }
]);

实战案例:

```
db.students.aggregate( [ { group:{'_id':'$gender'} } ] );
==按照country分组==
db.infos.aggregate( [ {group:{'id':'country' } } ] );
==按照country分组后，自定义下标country==
db.infos.aggregate( [ {group:{'id':{'country':'country'} } } ] );
==按照country和province分组后，自定义下标country和province
db.infos.aggregate( [ {group:{'id':{'country':'country', 'province':'province'} } } ] );
==按照country和province和userid分组后，自定义下标country和province和userid==
db.infos.aggregate( [ {$group:{'id':{'country':'country', 'province':'province', 'userid':'userid' } } } ] );
==按照country分组后，并统计出来每个分组下面的数据个数==
db.infos.aggregate( [ {group:{'id':{'country':'country' }, count:{sum:1} } } ] );
==按照country和province分组后，并统计出来每个分组下面的数据个数==
db.infos.aggregate( [ {$group:{'id':{'country':'country', 'province':'province' }, count:{sum:1} } } ] );
==按照country和province和userid分组后，并统计出来每个分组下面的数据个数==
db.infos.aggregate( [ {group:{'id':{'country':'country', 'province':'province', 'userid':'userid' }, count:{sum:1} } } ] );
==按照country和province和userid分组后，并统计出来每个分组下面的数据个数，且不显示当前最顶端country的数据==
db.infos.aggregate( [ {$group:{'id':{'country':'_id.country', 'province':'province', 'userid':'userid' }, count:{sum:1} } } ] );
==按照country和province和userid分组后，并统计出来每个分组下面的数据个数，且不显示当前最顶端province的数据==
db.infos.aggregate( [ {group:{'_id':{'country':'$_id.country', 'province':'$_id.province', 'userid':'$userid' }, count:{$sum:1} } } ] );
==按照country和province和userid分组后，并统计出来每个分组下面的数据个数，且不显示当前最顶端userid的数据==
db.infos.aggregate( [ {group:{'id':{'country':'$id.country', 'province':'_id.province', 'userid':'_id.userid' }, count:{$sum:1} } } ] );
```








 $match:

实战数据：
db.orders.insertMany([
{"cust_id":"A123","amount":500,"status":"A"},
{"cust_id":"A123","amount":250,"status":"A"},
{"cust_id":"B212","amount":200,"status":"A"},
{"cust_id":"A123","amount":300,"status":"D"},
{"cust_id":"A126","amount":360,"status":"U"},
{"cust_id":"A136","amount":360,"status":"W"},
{"cust_id":"A136","amount":360,"status":"A"},
{"cust_id":"A139","amount":660,"status":"A"},
{"cust_id":"A139","amount":960,"status":"A"}]);


实战案例：
==按照cust_id字段进行分组==
> db.orders.aggregate([ { $group:{'_id':'$cust_id'} } ]);
==只取status等于A的数据
> db.orders.aggregate([ { $match:{'status':'A'} } ]);
==只取status等于A的数据，然后再按照cust_id字段进行分组，统计每个分组下的消费总额amount
> db.orders.aggregate([ { $match:{'status':'A'} },{ $group:{'_id':'$cust_id','total':{$sum:'$amount'} } } ]);





$project:

实战案例：
==只展示name和age字段数据==
> db.students.aggregate( { $project:{'_id':0,'name':1,'age':1} } );
==更改age字段名==
> db.students.aggregate( { $project:{'_id':0,'name':1,'age1':'$age'} } );
==将数据按性别进行分组，且统计每组数据的个数后，只显示counter字段==
> db.students.aggregate( [ { $group:{'_id':'$gender',counter:{$sum:1} } }, { $project:{'_id':0, counter:1} } ] );
==再回忆一下之前的infos数据==
> db.infos.aggregate( [ {$group:{'_id':{'country':'$country', 'province':'$province', 'userid':'$userid' }, count:{$sum:1} } } ] );
==在上面数据基础之上进行定制展示数据==
> db.infos.aggregate( [ {$group:{'_id':{'country':'$country', 'province':'$province', 'userid':'$userid' }, count:{$sum:1} } },{$project:{'_id':0,'country':'$_id.country','province':'$_id.province','counter':'$count'}}] );
> 查询男女人数，按照人数升序排列
> db.students.aggregate([ {$group:{'_id':'$gender','counter':{$sum:1} }},{$sort:{'counter':1}} ]);
> db.students.aggregate({$skip:3});






索引:		
作用：加快查询速度,进行数据的去重

默认情况下_id是集合的索引


创建索引方法：
语法：	db.集合名.createIndex({'字段':1/-1})
注意：从 mongoDB 3.0 开始，ensureIndex 被废弃，今后都仅仅是 createIndex 的一个别名。
db.集合.createIndex({属性:1})1表示升序， -1表示降序


索引查看方法：
语法：		db.集合名.getIndexes()


添加唯一索引：
语法：	db.集合名.ensureIndex({字段:1},{unique:true});
	db.集合名.createIndex({字段:1},{unique:true});

删除索引方法：
语法：		db.集合名.dropIndex({'索引名称':1/-1})









备份的相关操作：
作用：保证数据库安全，主要用于灾难处理
mongo端口号：27017


备份:		保证数据库安全，主要用于灾难处理
备份的语法：
mongodump -h dbhost -d dbname -o dbdirectory
mongodump -h 服务器地址也可以指定端口号 -d 要备份的库名 -o 要备份的地址路径

示例：mongodump -h 192.168.196.128:27017 -d test1 -o ~/Desktop/test1bak




恢复:语法：	
mongorestore -h 服务器地址也可以指定端口号 -d 要恢复数据库名(要和备份之前不一样) --dir 备份数据所在位置
mongorestore -h dbhost -d dbname --dir dbdirectory

示例：mongorestore -h 192.168.196.128:27017 -d test2 --dir ~/Desktop/test1bak/test1




导出：
导出：用于和其他平台进行交互对接，将数据导出成指定格式文件进行使用，
比如数据分析常用的csv文件 用于给非计算机行业的用户查看数据，对于他们来说csv文件(打开之后是电子表格)更方便
导出语法: 	
mongoexport -h 服务器地址，也可以指定端口号 -d 数据库名 -c 集合名 -o 导出地址/文件名 --type 文件类型(默认json) -f 指定导出哪些字段，默认全部，导出成csv文件是必须指定

mongoexport -h dbhost -d dbname -c colname -o filename --type json/csv -f field

示例：mongoexport -h 192.168.196.128:27017 -d test2 -c col1 -o test1_col1 [--type csv -f name,age,number]



导入：语法: 
mongoimport -h 服务器地址，也可以指定端口号 -d 数据库名 -c 集合名 --file 导入文件路径 --type 文件类型 -f 要导入的字段

mongoimport -h dbhost -d dbname -c colname --file filename --type json/csv -f field

示例：mongoimport -h 127.0.0.1:27017 -d abcde -c infos --file c:\Users\wzh\aa\abc_csv --type csv -f title,description


关键词释义：
-c: 集合名
-h： 服务器地址， 也可以指定端口号
-d： 需要备份的数据库名称
-o： 备份的数据存放位置， 此目录中存放着备份出来的数据
--type: 文件类型，默认json格式，可选数据类型json，csv
-f: 需要导出的字段,导出为json格式的数据时可以不指定导出哪些字段，默认全部，导出成csv文件是必须指定
--type: 文件类型，默认json格式，可选数据类型json，csv
--dir： 备份数据所在位置





