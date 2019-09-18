# from flask import Flask,render_template
# from flask_sqlalchemy import SQLAlchemy
#
# app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:qwq@localhost/buy'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# db=SQLAlchemy(app)
#
# class Role(db.Model):
#     __tablename__='roles'
#     id=db.Column(db.Integer,primary_key=True,autoincrement=True)
#     name=db.Column(db.String(10),nullable=False,unique=True)
#
# class User(db.Model):
#     __tablename__='users'
#     id=db.Column(db.Integer,primary_key=True,autoincrement=True)
#     name=db.Column(db.String(10),nullable=False,unique=True)
#     email=db.Column(db.String(50),unique=True)
#     password=db.Column(db.String(20))
#     role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
#
# @app.route('/')
# def a():
#     return render_template('main.html')
#
# if __name__ == '__main__':
#     db.drop_all()
#     db.create_all()
#     r1=Role(id=1,name='管理员')
#     r2=Role(id=2,name='普通用户')
#     db.session.add_all([r1,r2])
#     db.session.commit()
#     u1=User(id=1,name='张三',role_id=r1.id)
#     db.session.add(u1)
#     db.session.commit()
#     # print(Role.query.filter(Role.id==1).first().name)
#     app.run(debug=True)



















from sqlalchemy import or_
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/buy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

#数据库的模型，需要继承db.Model
class Role(db.Model):
    #定义数据库表名
    __tablename__='roles'
    #定义字段，db.Column表示是一个字段
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16),unique=True)
    #表示Role和User模型发生了关联，增加了一个users属性，User模型里增加了一个role属性，但都是隐藏的
    #backref='role' 表示role是User要用的属性
    users=db.relationship('User',backref='role')

    # repr()方法=>当你查询隐藏字段全部内容的时候显示一个可读字符串,   比如要查看ro1下的所有用户 ro1.users
    def __repr__(self):
        return '<Role:%s %s>'%(self.name,self.id)

class User(db.Model):
    #定义表名
    __tablename__='users'
    #定义一个字段，字段名为id,类型为int,为主键
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16),unique=True)
    email=db.Column(db.String(32),unique=True)
    password=db.Column(db.String(32))
    #db.ForeignKey('roles.id') 表示外键， 表名.id
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    #User希望有role属性，但这个属性的定义，需要在另一个模型中定义

    def __repr__(self):
        return '<User: %s %s %s'%(self.id,self.email,self.password)

@app.template_filter('remove')
def new(l):
    a=list(l)
    list2,list4=[],[]
    for x in a:
        for i in x:
            list2.append(i)
    list3=sorted(list2,key=lambda x:x['id'])
    for x in range(len(list3)):
        if list3[x]['id']%2==0:
            list4.append(list3[x])
    return list4


def Get():
    listRole_id = [x.id for x in Role.query.all()]
    listRole_name = [x.name for x in Role.query.all()]
    list2 = []
    for x in range(len(listRole_id)):
        list1 = []
        listAll = User.query.filter(User.role_id == listRole_id[x]).all()
        for i in range(len(listAll)):
            dict = {}
            dict['role_id'] = listRole_id[x]
            dict['role_name'] = listRole_name[x]
            dict['id']=listAll[i].id
            dict['name'] = listAll[i].name
            dict['email'] = listAll[i].email
            dict['password'] = listAll[i].password
            dict['role_id'] = listAll[i].role_id
            list1.append(dict)
        list2.append(list1)
    # print(list2)
    # print(Role.query.filter(id==555).first())
    # print('*'*60)
    return list2

@app.route('/')
def a():
    list2=Get()
    return render_template('main.html',list=list2)

if __name__ == '__main__':
    #删除表
    db.drop_all()
    #创建表
    db.create_all()

    ro1=Role(name='admin')
    ro2=Role(name='user')

    u1=User(id=1,name='王',email='wang@',password='wang',role_id=1)
    u2=User(id=2,name='张',email='zhang@',password='zhang',role_id=2)
    u3=User(id=3,name='陈',email='chen@',password='chen',role_id=1)
    u4=User(id=4,name='周',email='zhou@',password='zhou',role_id=2)
    u5=User(id=5,name='唐',email='tang@',password='tang',role_id=1)
    u6=User(id=6,name='吴',email='wu@',password='wu',role_id=2)
    u7=User(id=7,name='钱',email='qian@',password='qian',role_id=1)
    u8=User(id=8,name='刘',email='liu@',password='liu',role_id=2)
    u9=User(id=9,name='关',email='guan@',password='guan',role_id=1)
    u10=User(id=10,name='马',email='ma@',password='ma',role_id=2)

    db.session.add_all([ro1,ro2,u1,u2,u3,u4,u5,u6,u7,u8,u9,u10])
    db.session.commit()
    # l=Role.query.get(1)    #获取roles表id为1的数据
    # r=User.query.get(l.id)   #获取users表里id为roles表id为1的数据
    # print(r)
    # l=User.query.filter(User.id==4).first().role_id
    # print(Role.query.filter(Role.id==l).first().name)

    # print(u1.role)
    # print([x.name for x in ro1.users])

    # print(User.query.filter(User.name==[x.name for x in ro1.users if x.name=='钱']).first().id)

    # l=User.query.filter(User.name=='钱').first()
    # r=Role.query.filter(Role.id==l.role_id).first()
    # print(r.name)

    # print(u1.role.name)

    # list=User.query.filter(User.password.startswith('z')).all()
    # for x in list:
    #     print(x)



    app.run(debug=True)
