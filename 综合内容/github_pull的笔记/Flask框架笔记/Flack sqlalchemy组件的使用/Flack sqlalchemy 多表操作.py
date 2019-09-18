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

# 根据Users类对users表进行增删改查
session = SessionFactory()

# 1. 录入数据
# session.add_all([
#     Student(name='先用'),
#     Student(name='佳俊'),
#     Course(title='生物'),
#     Course(title='体育'),
# ])
# session.commit()

# session.add_all([
#     Student2Course(student_id=2,course_id=1)
# ])
# session.commit()

# 2. 三张表关联
# ret = session.query(Student2Course.id,Student.name,Course.title).join(Student,Student2Course.student_id==Student.id,isouter=True).join(Course,Student2Course.course_id==Course.id,isouter=True).order_by(Student2Course.id.asc())
# for row in ret:	# isouter=True 换成 left join 
#     print(row)
# 3. “羊驼”选的所有课
# ret = session.query(Student2Course.id,Student.name,Course.title).join(Student,Student2Course.student_id==Student.id,isouter=True).join(Course,Student2Course.course_id==Course.id,isouter=True).filter(Student.name=='先用').order_by(Student2Course.id.asc()).all()
# print(ret)

# 用 relationship 会极大的方便 
# obj = session.query(Student).filter(Student.name=='先用').first()
# for item in obj.course_list:
#     print(item.title)

# 4. 选了“生物”的所有人
# obj = session.query(Course).filter(Course.title=='生物').first()
# for item in obj.student_list:
#     print(item.name)

# 5. 创建一个课程，创建2学生，两个学生选新创建的课程。
# obj = Course(title='英语')
# obj.student_list = [Student(name='为名'),Student(name='广宗')]
#
# session.add(obj)
# session.commit()


session.close()