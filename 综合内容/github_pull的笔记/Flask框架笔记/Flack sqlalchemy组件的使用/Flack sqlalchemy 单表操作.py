from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Users,Depart

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

# 1. 查询所有用户
# ret = session.query(Users).all()
# for row in ret:
#     print(row.id,row.name,row.depart_id)

# 2. 查询所有用户+所属部门名称
# ret = session.query(Users.id,Users.name,Depart.title).join(Depart,Users.depart_id == Depart.id).all()
# for row in ret:
#     print(row.id,row.name,row.title)

# query = session.query(Users.id,Users.name,Depart.title).join(Depart,Users.depart_id == Depart.id,isouter=True)
# print(query) # inner join

# 3. relation字段:查询所有用户+所属部门名称
# ret = session.query(Users).all()
# for row in ret:
#     print(row.id,row.name,row.depart_id,row.dp.title)

# 4. relation字段:查询销售部所有的人员
# obj = session.query(Depart).filter(Depart.title == '销售').first()
# for row in obj.pers:
#     print(row.id,row.name,obj.title)

# 5. 创建一个名称叫：IT部门，再在该部门中添加一个员工：田硕
# 方式一：
# d1 = Depart(title='IT')
# session.add(d1)
# session.commit()
#
# u1 = Users(name='田硕',depart_id=d1.id)
# session.add(u1)
# session.commit()

# 方式二：
# u1 = Users(name='田硕',dp=Depart(title='IT'))
# session.add(u1)
# session.commit()

# 6. 创建一个名称叫：王者荣耀，再在该部门中添加一个员工：龚林峰/长好梦/王爷们
# d1 = Depart(title='王者荣耀')
# d1.pers = [Users(name='龚林峰'),Users(name='长好梦'),Users(name='王爷们'),]
# session.add(d1)
# session.commit()

session.close()