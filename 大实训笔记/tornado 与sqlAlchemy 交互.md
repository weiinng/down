## tornado 与sqlAlchemy 交互

sqlAlchemy是python中最著名的ORM(Object Relationship Mapping)框架了。

## 什么是ORM？

一句话解释的话就是，一种可以把model中的模型和数据库中的一条数据相互转换的工具。

安装

```
pip3 install sqlalchemy
```

基本操作 



```
# 导入依赖
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库链接
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)


# 添加
# 创建Session对象
session = DBSession()
# 创建User对象
new_user = User(id='5', name='Bob')
# 添加到session
session.add(new_user)
# 提交
session.commit()
# 关闭session
session.close()


# 查询
# 创建session
session = DBSession()
# 利用session创建查询，query(对象类).filter(条件).one()/all()
user = session.query(User).filter(User.id=='5').one()
print('type:{0}'.format(type(user)))
print('name:{0}'.format(user.name))
# 关闭session
session.close()


# 更新
session = DBSession()
user_result = session.query(User).filter_by(id='1').first()
user_result.name = "jack"
session.commit()
session.close()


# 删除
session = DBSession()
user_willdel = session.query(User).filter_by(id='5').first()
session.delete(user_willdel)
session.commit()
session.close()
```

数据库迁移 

```
Base.metadata.create_all()
```