
# 对于多线程链接数据库的时候推荐使用此方法 
# 基于 Threading.Local 实现的 

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session # 需要引入这个
from models import Student,Course,Student2Course

engine = create_engine(
        "mysql+pymysql://root:123456@127.0.0.1:3306/s9day120?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
SessionFactory = sessionmaker(bind=engine)

session = scoped_session(SessionFactory)	# 再次封装一下


def task():
    """"""
    # 方式一：
    """
    # 查询
    # cursor = session.execute('select * from users')
    # result = cursor.fetchall()

    # 添加
    cursor = session.execute('INSERT INTO users(name) VALUES(:value)', params={"value": 'wupeiqi'})
    session.commit()
    print(cursor.lastrowid)
    """
    # 方式二：
    """
    # conn = engine.raw_connection()
    # cursor = conn.cursor()
    # cursor.execute(
    #     "select * from t1"
    # )
    # result = cursor.fetchall()
    # cursor.close()
    # conn.close()
    """

    # 将连接交还给连接池
    session.remove() # 方式1 是close 这里要用 remove 


from threading import Thread

for i in range(20):
    t = Thread(target=task)
    t.start()
