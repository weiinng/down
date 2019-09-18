from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer,String,Text,Date,DateTime,ForeignKey,UniqueConstraint, Index
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship


Base = declarative_base()

class Depart(Base):
    __tablename__ = 'depart'
    id = Column(Integer, primary_key=True)
    title = Column(String(32), index=True, nullable=False)

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    depart_id = Column(Integer,ForeignKey("depart.id"))	# 外键 表名 不是 类名

    dp = relationship("Depart", backref='pers')

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)

    course_list = relationship('Course', secondary='student2course', backref='student_list')

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    title = Column(String(32), index=True, nullable=False)

class Student2Course(Base): # 多对多关系的 第三张表要自己创建 么有 manytomany 帮你创建了
    __tablename__ = 'student2course'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    course_id = Column(Integer, ForeignKey('course.id'))

    __table_args__ = (
        UniqueConstraint('student_id', 'course_id', name='uix_stu_cou'), # 联合唯一索引
        # Index('ix_id_name', 'name', 'extra'),                          # 联合索引
    )

def create_all():
    engine = create_engine(
        "mysql+pymysql://root:123456@127.0.0.1:3306/s9day120?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.create_all(engine)

def drop_all():
    engine = create_engine(
        "mysql+pymysql://root:123456@127.0.0.1:3306/s9day120?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    Base.metadata.drop_all(engine)

if __name__ == '__main__':
    # drop_all()
    create_all()