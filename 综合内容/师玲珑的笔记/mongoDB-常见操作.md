mongoDB ���


����-��mongodb���ݿ⣺	monggo



�鿴��ǰ���ڿ⣺��ʾ��ǰʹ�õ����ݿ�����	db.getName()  ��   db;

ɾ��ǰʹ�õ����ݿ�	db.dropDatabase() 

�޸���ǰ���ݿ�		db.repairDatabase() 

��ǰ���ݿ�汾		db.version()   

�鿴��ǰ���ݿ�����ӻ�����ַ 		db.getMongo()  

��ʾ��ǰ���ݿ�״̬���������ݿ����ƣ����ϸ�������ǰ���ݿ��С ...	db.stats()

�鿴���ݿ�������Щ�����ϣ�����	db.getCollectionNames()


�鿴���п⣺		show dbs;

�������ݿ⣨û�еĻ��Զ��������Զ�������	use ����;

ɾ����ǰ�����ݿ⣺	db.dropDatabase()


�������ϣ�		db.createCollection("������");

�鿴���м��ϣ�		show collections;

��������		db.������.insert({"":"","":""});

��������С������
����д�����ݣ�
db.posts.insert({"title":"�ҵĵ�һƪ����","content":"��Ҫ��ʼд������"});
db.posts.insert({"title":"�ҵĵڶ�ƪ����","content":"д��ʲô����"});
����д�룺��Many���� �� ���е�key��������
db.posts.insertMany([{"title":"�ҵĵ���ƪ����"},{"content":"�����ʲô"}]);
����д�����ݣ�(֧��css�﷨��var�ɼӿɲ���)
for(var i=4;i<=10;i++){db.posts.insert({"title":"�ҵĵ�"+i+"ƪ����"})};


�鿴�������������ݣ�		db.������.find();

�������ң�
��ʽ��db.������.find({"�ֶ���":{����}});
$gte	���ڵ���
$gt	����
$lte	С�ڵ���
$lt	С��
$eq	����
$ne	������

������ʽ��/k/,/^k/

�����ֶ�ȡΨһ��ֵ����ȥ�أ���		db.posts.distinct('�ֶ���');

ָ����ȡ���ֶΣ�ͶӰ��(valueֵΪ��������true/1,flase/0)��		
�﷨��		db.�ֶ���.find({},{'�ֶ���':true,'�ֶ���2':1});




�������ݣ�
db.posts.insert({'title' : '����������������', 'rank' : 2, 'tag' : 'game' });
db.posts.insert({'title' : 'ֽƬ�������������', 'rank' : 1, 'tag' : 'game' });
db.posts.insert({'title' : 'Ubuntu16LTS�İ�װ', 'rank' : 3, 'tag' : 'it' });
db.posts.insert({'title' : '�ų�֮Ұ����־����ͻ��10000', 'rank' : 4, 'tag' : 'game' });
db.posts.insert({'title' : 'Ruby�Ŀ���Ч����ĺܸ���', 'rank' : 7, 'tag' : 'it' });
db.posts.insert({'title' : '�����ﴫ˵�������DLC', 'rank' : 4, 'tag' : 'game' });
db.posts.insert({'title':'������ʿ�����ش���', 'istop':true});



������ѯ��
db.posts.find({'rank':{$gte:4}});	��ѯrank���ڵ���4�ļ�¼
db.posts.find({'rank':{$gt:4}});	��ѯrank����4�ļ�¼
db.posts.find({'rank':{$lte:4}});	��ѯrankС�ڵ���4�ļ�¼  
db.posts.find({'rank':{$lt:4}});	��ѯrankС��4�ļ�¼
db.posts.find({'rank':{$eq:4}});	��ѯrank����4�ļ�¼
db.posts.find({'rank':{$ne:4}});	��ѯrank������4�ļ�¼

������ң�
db.posts.find({'title':/u/});		����title���溬��u�ļ�¼
db.posts.find({'title':/U/});		����title���濪ͷ��U�ļ�¼



����������ѯ�ĵ� -��ʽ�� 	
��		db.������.find({"":"","":""});
or��		db.������.find({$or:[{"":""},{"":""}:{"":""}]});
in��...��	db.������.find({'�ֶ���':{$in:[Ҫ�ҵ���ֵ]}});
�жϸ��ֶ��Ƿ����	db.posts.find('�ֶ���'��{$sexists:true});

ʵս������
��	db.posts.find({'title':/u/,'rank':{$gte:5}});
or��	db.posts.find({$or:[{'title':/u/},{'rank':{$gte:5}}]});
in��...��	db.posts.find({'rank':{$in:[1,2,3]}});
�����ֶ�tagȡΨһ��ֵ	db.posts.distinct('tag');
�жϸ��ֶ��Ƿ����	db.posts.find('istop'��{$exists:true});


ָ����ȡ���ֶΣ�ͶӰ��(valueֵΪ��������true/1,flase/0)		db.posts.find({'title':/u/},{'title':true,'rank':1,'_id':0});



��������(�ܵ�):
sort()		����
limit()		������������ҳ��
skip()		�����ĵ�
��ʽ��
db.������.find({}).sort({'�ֶ�':1});	����
db.������.find({}).sort({'�ֶ�':1}).limit(3);		����ǰ����
db.������.find({}).sort({'�ֶ�':1});	

ʵս������
db.posts.find({}).sort({'rank':1});

db.posts.find({}).sort({'rank':-1,'title':-1});

db.posts.find({}).sort({'rank':-1}).limit(3);

db.posts.find({}).sort({'rank':-1}).skip(3).limit(3);





�����ĵ���
update(<filter>,<update>,<options>)	---filter=������update=�������ݡ�options=��{multi:true}�������У�����ֻ����һ���� 

db.posts.findOne��{"":""}��		ָ���鿴һ��


ʵս��
db.posts.findOne({'title':'����������������'})��	ָ���鿴
db.posts.update({'title':'����������������'},{$set:{'rank':16}});	����ԭ���ֶθ���rank�ֶ�
db.posts.update({'title':'����������������'},{'rank':19});	�����_id�ֶλ���rank�ֶ�
db.posts.update({"tag":"it"},{$set:{"rank":199}},{multi:true});		��������



�ĵ�ɾ����

��ʽ �� db.������.remove(<query>,{justOne:true})
query��		��ѡ������
justOne:  	��ѡ�������Ϊtrue��1 ��ʾɾ��һ��  Ĭ��False����ʾɾ������

ʵս�÷���
�Ƴ������ĵ�		db.������.remove({});
�Ƴ�ָ���ĵ�		db.������.remove({'�ֶ�':{����}},{justOne:true});




ͳ�Ƹ�����
.count()   	����ͳ�Ƽ����е��ĵ�����

ʵս�÷���
db.������.find({"":{����}}).count()
db.������.count({"":{����}})



�ۺϣ�
aggregate()	�ۺ�(aggregate)�ǻ������ݴ���ľۺϹܵ���ÿ���ĵ�ͨ��һ���ɶ���׶Σ�stage����ɵĹܵ���
���Զ�ÿ���׶ν��з��顢���˵ȹ��ܣ�Ȼ�󾭹�һϵ�еĴ��������Ӧ�Ľ��
$group		�������е��ĵ����飬������ͳ�ƽ��
$match		�������ݣ�ֻ��������������ĵ�
$group�� 	�������е��ĵ����飬 ������ͳ�ƽ����$group�����оۺ��������õ�����һ����������������е��ĵ����飬������ͳ�ƽ����
$match�� 	�������ݣ� ֻ��������������ĵ�
$project�� 	�޸������ĵ��Ľṹ�� ���������� ���ӡ� ɾ���ֶΡ� ����������
$sort�� 	�������ĵ���������
$limit�� 	���ƾۺϹܵ����ص�?����
$skip��	 	����ָ��������?���� ���������µ�?��

ע��㣺
db.db_name.aggregate���﷨�����еĹܵ������Ҫд������
_id ��ʾ��������ݣ������ĸ��ֶν��з��飬��Ҫʹ��$gender��ʾѡ������ֶν��з���


�ڹܵ������򣬰����������ʾ�������ܵ��������ִ��

���ñ��ʽ��	���ʽ���������ĵ������ �﷨�����ʽ:'$����' ���ñ��ʽ:
$sum�� �����ܺͣ� $sum:1 ��ʾ��1������

$avg�� ����ƽ��ֵ
$min�� ��ȡ��Сֵ
$max�� ��ȡ���ֵ
$push�� �ڽ���ĵ��в���ֵ��1��������




ʵս�﷨��
db.������.aggregate([ { $group:{ '_id':'$�ֶη���', ��ȡ����Ϣ������:{$push:'$Ҫ��ȡ���ֶ���'} } } ]);
��λ��		$sum:1	  ÿ����λΪ1



ʵս�������ݣ�
db.students.insert({"name" : "����", "hometown" : "�ɹ�", "age" : 20, "gender" : true });
db.students.insert({"name" : "����", "hometown" : "�һ���", "age" : 18, "gender" : false })
db.students.insert({"name" : "����", "hometown" : "�ɹ�", "age" : 18, "gender" : false });
db.students.insert({"name" : "��ҩʦ", "hometown" : "�һ���", "age" : 40, "gender" : true });
db.students.insert({"name" : "����", "hometown" : "����", "age" : 16, "gender" : true });
db.students.insert({"name" : "����ү", "hometown" : "����", "age" : 45, "gender" : true });
db.students.insert({"name" : "���߹�", "hometown" : "��ɽ", "age" : 18, "gender" : true });




ʵս��ϰ��
db.students.remove({'rank':{$lt:4}},{justOne:true});
db.students.remove({});


db.students.find({'rank':{$lt:4}}).count();
db.students.count({'rank':{$lt:4}});


1 ����ĳ���ֶν��з���
$group�����оۺ��������õ�����һ����������������е��ĵ����飬������ͳ�ƽ��

db.students.aggregate([ { $group:{'_id':'$gender'} } ]);
db.db_name.aggregate���﷨�����еĹܵ������Ҫд������
_id ��ʾ��������ݣ������ĸ��ֶν��з��飬��Ҫʹ��$gender��ʾѡ������ֶν��з���
db.students.aggregate([ { $group:{'_id':'$gender', counter:{$sum:1} } } ]);
$sum:1 ��ʾ��ÿ��������Ϊ1����ͳ�ƣ�ͳ�Ƶ��Ǹ÷����������ݵ�����

2 group by null
��������Ҫͳ�������ĵ���ʱ��$group ����һ����;���ǰ������ĵ���Ϊһ�����ͳ��

db.students.aggregate([{$group:{'id':null,counter:{$sum:1}}}]);
_id:null ��ʾ��ָ��������ֶΣ���ͳ�������ĵ�����ʱ��ȡ��counter��ʾ�����ĵ��ĸ���

3  ����͸��
���������ͳ�ƵĲ�ͬ���������ݵ�ʱ����Ҫ֪�����е�name����Ҫ�����۲죬���ͨ��ĳ�ַ�ʽ�����е�name�ŵ�һ����ô��ʱ�Ϳ������Ϊ����͸��
db.students.aggregate([{$group:{'_id':null,'name':{$push:'$name'}}}]);

ʹ��$$ROOT���Խ������ĵ�����������
db.students.aggregate([{$group:{'_id':null,'name':{$push:'$$ROOT'}}}]);






�ۺϵĸ߼�Ӧ�ã�


ʵս���ݣ�
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

ʵս����:

```
db.students.aggregate( [ { group:{'_id':'$gender'} } ] );
==����country����==
db.infos.aggregate( [ {group:{'id':'country' } } ] );
==����country������Զ����±�country==
db.infos.aggregate( [ {group:{'id':{'country':'country'} } } ] );
==����country��province������Զ����±�country��province
db.infos.aggregate( [ {group:{'id':{'country':'country', 'province':'province'} } } ] );
==����country��province��userid������Զ����±�country��province��userid==
db.infos.aggregate( [ {$group:{'id':{'country':'country', 'province':'province', 'userid':'userid' } } } ] );
==����country����󣬲�ͳ�Ƴ���ÿ��������������ݸ���==
db.infos.aggregate( [ {group:{'id':{'country':'country' }, count:{sum:1} } } ] );
==����country��province����󣬲�ͳ�Ƴ���ÿ��������������ݸ���==
db.infos.aggregate( [ {$group:{'id':{'country':'country', 'province':'province' }, count:{sum:1} } } ] );
==����country��province��userid����󣬲�ͳ�Ƴ���ÿ��������������ݸ���==
db.infos.aggregate( [ {group:{'id':{'country':'country', 'province':'province', 'userid':'userid' }, count:{sum:1} } } ] );
==����country��province��userid����󣬲�ͳ�Ƴ���ÿ��������������ݸ������Ҳ���ʾ��ǰ���country������==
db.infos.aggregate( [ {$group:{'id':{'country':'_id.country', 'province':'province', 'userid':'userid' }, count:{sum:1} } } ] );
==����country��province��userid����󣬲�ͳ�Ƴ���ÿ��������������ݸ������Ҳ���ʾ��ǰ���province������==
db.infos.aggregate( [ {group:{'_id':{'country':'$_id.country', 'province':'$_id.province', 'userid':'$userid' }, count:{$sum:1} } } ] );
==����country��province��userid����󣬲�ͳ�Ƴ���ÿ��������������ݸ������Ҳ���ʾ��ǰ���userid������==
db.infos.aggregate( [ {group:{'id':{'country':'$id.country', 'province':'_id.province', 'userid':'_id.userid' }, count:{$sum:1} } } ] );
```








 $match:

ʵս���ݣ�
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


ʵս������
==����cust_id�ֶν��з���==
> db.orders.aggregate([ { $group:{'_id':'$cust_id'} } ]);
==ֻȡstatus����A������
> db.orders.aggregate([ { $match:{'status':'A'} } ]);
==ֻȡstatus����A�����ݣ�Ȼ���ٰ���cust_id�ֶν��з��飬ͳ��ÿ�������µ������ܶ�amount
> db.orders.aggregate([ { $match:{'status':'A'} },{ $group:{'_id':'$cust_id','total':{$sum:'$amount'} } } ]);





$project:

ʵս������
==ֻչʾname��age�ֶ�����==
> db.students.aggregate( { $project:{'_id':0,'name':1,'age':1} } );
==����age�ֶ���==
> db.students.aggregate( { $project:{'_id':0,'name':1,'age1':'$age'} } );
==�����ݰ��Ա���з��飬��ͳ��ÿ�����ݵĸ�����ֻ��ʾcounter�ֶ�==
> db.students.aggregate( [ { $group:{'_id':'$gender',counter:{$sum:1} } }, { $project:{'_id':0, counter:1} } ] );
==�ٻ���һ��֮ǰ��infos����==
> db.infos.aggregate( [ {$group:{'_id':{'country':'$country', 'province':'$province', 'userid':'$userid' }, count:{$sum:1} } } ] );
==���������ݻ���֮�Ͻ��ж���չʾ����==
> db.infos.aggregate( [ {$group:{'_id':{'country':'$country', 'province':'$province', 'userid':'$userid' }, count:{$sum:1} } },{$project:{'_id':0,'country':'$_id.country','province':'$_id.province','counter':'$count'}}] );
> ��ѯ��Ů����������������������
> db.students.aggregate([ {$group:{'_id':'$gender','counter':{$sum:1} }},{$sort:{'counter':1}} ]);
> db.students.aggregate({$skip:3});






����:		
���ã��ӿ��ѯ�ٶ�,�������ݵ�ȥ��

Ĭ�������_id�Ǽ��ϵ�����


��������������
�﷨��	db.������.createIndex({'�ֶ�':1/-1})
ע�⣺�� mongoDB 3.0 ��ʼ��ensureIndex ����������󶼽����� createIndex ��һ��������
db.����.createIndex({����:1})1��ʾ���� -1��ʾ����


�����鿴������
�﷨��		db.������.getIndexes()


���Ψһ������
�﷨��	db.������.ensureIndex({�ֶ�:1},{unique:true});
	db.������.createIndex({�ֶ�:1},{unique:true});

ɾ������������
�﷨��		db.������.dropIndex({'��������':1/-1})









���ݵ���ز�����
���ã���֤���ݿⰲȫ����Ҫ�������Ѵ���
mongo�˿ںţ�27017


����:		��֤���ݿⰲȫ����Ҫ�������Ѵ���
���ݵ��﷨��
mongodump -h dbhost -d dbname -o dbdirectory
mongodump -h ��������ַҲ����ָ���˿ں� -d Ҫ���ݵĿ��� -o Ҫ���ݵĵ�ַ·��

ʾ����mongodump -h 192.168.196.128:27017 -d test1 -o ~/Desktop/test1bak




�ָ�:�﷨��	
mongorestore -h ��������ַҲ����ָ���˿ں� -d Ҫ�ָ����ݿ���(Ҫ�ͱ���֮ǰ��һ��) --dir ������������λ��
mongorestore -h dbhost -d dbname --dir dbdirectory

ʾ����mongorestore -h 192.168.196.128:27017 -d test2 --dir ~/Desktop/test1bak/test1




������
���������ں�����ƽ̨���н����Խӣ������ݵ�����ָ����ʽ�ļ�����ʹ�ã�
�������ݷ������õ�csv�ļ� ���ڸ��Ǽ������ҵ���û��鿴���ݣ�����������˵csv�ļ�(��֮���ǵ��ӱ��)������
�����﷨: 	
mongoexport -h ��������ַ��Ҳ����ָ���˿ں� -d ���ݿ��� -c ������ -o ������ַ/�ļ��� --type �ļ�����(Ĭ��json) -f ָ��������Щ�ֶΣ�Ĭ��ȫ����������csv�ļ��Ǳ���ָ��

mongoexport -h dbhost -d dbname -c colname -o filename --type json/csv -f field

ʾ����mongoexport -h 192.168.196.128:27017 -d test2 -c col1 -o test1_col1 [--type csv -f name,age,number]



���룺�﷨: 
mongoimport -h ��������ַ��Ҳ����ָ���˿ں� -d ���ݿ��� -c ������ --file �����ļ�·�� --type �ļ����� -f Ҫ������ֶ�

mongoimport -h dbhost -d dbname -c colname --file filename --type json/csv -f field

ʾ����mongoimport -h 127.0.0.1:27017 -d abcde -c infos --file c:\Users\wzh\aa\abc_csv --type csv -f title,description


�ؼ������壺
-c: ������
-h�� ��������ַ�� Ҳ����ָ���˿ں�
-d�� ��Ҫ���ݵ����ݿ�����
-o�� ���ݵ����ݴ��λ�ã� ��Ŀ¼�д���ű��ݳ���������
--type: �ļ����ͣ�Ĭ��json��ʽ����ѡ��������json��csv
-f: ��Ҫ�������ֶ�,����Ϊjson��ʽ������ʱ���Բ�ָ��������Щ�ֶΣ�Ĭ��ȫ����������csv�ļ��Ǳ���ָ��
--type: �ļ����ͣ�Ĭ��json��ʽ����ѡ��������json��csv
--dir�� ������������λ��





