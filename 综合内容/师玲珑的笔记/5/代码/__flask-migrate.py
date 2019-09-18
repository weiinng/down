'''
在开发过程中，需要修改数据库模型，而且还要在修改之后更新数据库。最直接的方式就是删除旧表，但这样会丢失数据。
更好的解决办法是使用数据库迁移框架，它可以追踪数据库模式的变化，然后把变动应用到数据库中。
在Flask中可以使用Flask-Migrate扩展，来实现数据迁移。并且集成到Flask-Script中，所有操作通过命令就能完成。
为了导出数据库迁移命令，Flask-Migrate提供了一个MigrateCommand类，可以附加到flask-script的manager对象上
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager

app=Flask(__name__)
manager=Manager(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/flask_test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

#第一个参数是Flask的实例，第二个参数是Sqlalchemy数据库实例
migrate=Migrate(app,db)
#manager是Flask-Script实例，这条语句在flask-Script中添加一个db命令
manager.add_command('db',MigrateCommand)

#定义模型Role
class Role(db.Model):
    #定义表名
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(10),unique=True)
    user=db.relationship('User',backref='role')

    def __repr__(self):
        return 'Role:{}'.format(self.name)

#定义用户
class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(10),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    def __repr__(self):
        return 'User:{}'.format(self.username)

if __name__ == '__main__':
    manager.run()
