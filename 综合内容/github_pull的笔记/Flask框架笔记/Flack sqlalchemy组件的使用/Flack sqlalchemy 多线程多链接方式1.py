from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Student,Course,Student2Course

engine = create_engine(
        "mysql+pymysql://root:123456@127.0.0.1:3306/s9day120?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
SessionFactory = sessionmaker(bind=engine)

def task():
    # 去连接池中获取一个连接
    session = SessionFactory()

    ret = session.query(Student).all()

    # 将连接交还给连接池
    session.close()


from threading import Thread

for i in range(20):
    t = Thread(target=task)
    t.start()
