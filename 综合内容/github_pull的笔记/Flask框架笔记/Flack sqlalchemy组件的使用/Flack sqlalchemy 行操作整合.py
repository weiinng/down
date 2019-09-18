from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Users

engine = create_engine(
        "mysql+pymysql://root:123456@127.0.0.1:3306/s9day120?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
SessionFactory = sessionmaker(bind=engine)

# 根据Users类对users表进行增删改查
session = SessionFactory()

# ############################## 基本增删改查 ###############################
# 1. 增加
# obj = Users(name='alex')
# session.add(obj)
# session.commit()

# session.add_all([
#         Users(name='小东北'),  # 	多条增加 
#         Users(name='龙泰')
# ])
# session.commit()

# 2. 查
# result = session.query(Users).all()
# for row in result:
#         print(row.id,row.name)

# result = session.query(Users).filter(Users.id >= 2)
# for row in result:
#         print(row.id,row.name)

# result = session.query(Users).filter(Users.id >= 2).first()
# print(result)

# 3.删
# session.query(Users).filter(Users.id >= 2).delete()
# session.commit()

# 4.改
# session.query(Users).filter(Users.id == 4).update({Users.name:'东北'})
# session.query(Users).filter(Users.id == 4).update({'name':'小东北'})
# session.query(Users).filter(Users.id == 4).update({'name':Users.name+"DSB"},synchronize_session=False)
# session.commit()

# ############################## 其他常用 ###############################
# 1. 指定列
# # select id,name as cname from users;
# result = session.query(Users.id,Users.name.label('cname')).all()
# for item in result:
#         print(item[0],item.id,item.cname)
# query = session.query(Users.id,Users.name.label('cname'))
# print (query) # 打印 实际执行的 SQL 语句

# 2. 默认条件 and
# session.query(Users).filter(Users.id > 1, Users.name == 'eric').all()

# 3. between
# session.query(Users).filter(Users.id.between(1, 3), Users.name == 'eric').all()

# 4. in
# session.query(Users).filter(Users.id.in_([1,3,4])).all()	  # in 
# session.query(Users).filter(~Users.id.in_([1,3,4])).all()   # not in 

# 5. 子查询
# session.query(Users).filter(Users.id.in_(  session.query(Users.id).filter(Users.name=='eric'))  ).all()

# 6. and 和 or
# from sqlalchemy import and_, or_
# session.query(Users).filter(Users.id > 3, Users.name == 'eric').all()	# 默认就是 and 的链接
# session.query(Users).filter(and_(Users.id > 3, Users.name == 'eric')).all() # 且 
# session.query(Users).filter(or_(Users.id < 2, Users.name == 'eric')).all() # 或 
# session.query(Users).filter(
#     or_(
#         Users.id < 2,
#         and_(Users.name == 'eric', Users.id > 3),
#         Users.extra != ""
#     )).all() # 可以嵌套 

# 7. filter_by
# session.query(Users).filter_by(name='alex').all()  # 基于参数，而不是表达式的方式查询 

# 8. 通配符
# ret = session.query(Users).filter(Users.name.like('e%')).all()
# ret = session.query(Users).filter(~Users.name.like('e%')).all()

# 9. 切片
# result = session.query(Users)[1:2]

# 10.排序
# ret = session.query(Users).order_by(Users.name.desc()).all()
# # 先按xxx排序，xxx排序不出来的部分 再用 yyy 来排序 
# ret = session.query(Users).order_by(Users.name.desc(), Users.id.asc()).all()

# 11. group by
from sqlalchemy.sql import func
# ret = session.query(
#         Users.depart_id,
#         func.count(Users.id),
# ).group_by(Users.depart_id).all()
# for item in ret:
#         print(item)
# 
# 对 分组后的数据进行二次筛选 
# ret = session.query(
#         Users.depart_id,
#         func.count(Users.id),
# ).group_by(Users.depart_id).having(func.count(Users.id) >= 2).all()
# for item in ret:
#         print(item)

# 12.union 和 union all 合并表 
"""
select id,name from users
UNION
select id,name from users;
"""
# q1 = session.query(Users.name).filter(Users.id > 2)
# q2 = session.query(Favor.caption).filter(Favor.nid < 2)
# ret = q1.union(q2).all()
#
# q1 = session.query(Users.name).filter(Users.id > 2)
# q2 = session.query(Favor.caption).filter(Favor.nid < 2)
# ret = q1.union_all(q2).all()


session.close()