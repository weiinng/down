from flask import Flask,render_template,request,flash,session,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo
from sqlalchemy import and_,or_

app=Flask(__name__)
app.config['SECRET_KEY']='123'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/buy2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['PERMANENT_SESSION_LIFETIME']=30

db=SQLAlchemy(app)

class Reg(FlaskForm):
    name=StringField('请输入你的姓名:',validators=[DataRequired()])
    id=StringField('请输入你的账号：',validators=[DataRequired()])
    password=PasswordField('请输入你的密码：',validators=[DataRequired()])
    password2=PasswordField('请确认你的密码：',validators=[DataRequired(),EqualTo('password','两次密码不一致')])
    submit=SubmitField('注册')

class Login(FlaskForm):
    id=StringField('请输入你的账号：',validators=[DataRequired()])
    password=PasswordField('请输入你的密码：',validators=[DataRequired()])
    submit=SubmitField('登录')

class Goods(db.Model):
    __tablename__='goods'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(10))
    price=db.Column(db.FLOAT(5,1))


class User(db.Model):
    __tablename='user'
    name=db.Column(db.String(10))
    id=db.Column(db.Integer,primary_key=True)
    password=db.Column(db.String(10))

class Car(db.Model):
    __tablename__='car'
    userId=db.Column(db.Integer,primary_key=True)
    userName=db.Column(db.String(10))
    goodsName=db.Column(db.String(10))
    goodsPrice=db.Column(db.FLOAT(5,1))

def Insert():
    g1=Goods(id=1,name='可乐',price=4)
    g2=Goods(id=2,name='百岁山',price=5.5)
    g3=Goods(id=3,name='脉动',price=10)
    db.session.add_all([g1,g2,g3])
    db.session.commit()
    u1=User(id=1,name='师玲珑',password='123456')
    u2=User(id=2,name='郭威',password='654321')
    u3=User(id=3,name='马向茹',password='1234567')
    u4=User(id=4,name='师玲珑',password='12345678')
    db.session.add_all([u1,u2,u3,u4])
    db.session.commit()

@app.route('/buy',methods=['GET','POST'])
def buy():
    allGoods=Goods.query.all()
    list=[]
    for x in allGoods:
        dict={}
        dict['id']=x.id
        dict['name']=x.name
        dict['price']='%.2f'%x.price
        list.append(dict)
    if request.method=='POST':
        if session.get('username'):
            goodsName = request.form.get('name')
            goodsPrice = request.form.get('price')
            userid=User.query.filter(User.id==session['username']).first().id
            c=Car(userId=userid,userName=session['username'],goodsName=goodsName,goodsPrice=goodsPrice)
            db.session.add(c)
            db.session.commit()
        else:
            flash('未登录，请先登录')
            q='q'
            return render_template('buy.html', list=list,q=q)

    return render_template('buy.html',list=list)

@app.route('/reg',methods=['GET','POST'])
def reg():
    form=Login()
    form2=Reg()
    if request.method=='POST':
        userName=form2.name.data
        userId=form2.id.data
        password=form2.password.data
        if form2.validate_on_submit():
            ifUserId=User.query.filter(User.id==userId).first()
            if not ifUserId:
                flash('注册成功')
                u = User(id=userId, password=password, name=userName)
                db.session.add(u)
                db.session.commit()
            else:
                flash('该账号已经存在')
        else:
            flash('注册失败')

    return render_template('reg.html', form2=form2, form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    form=Login()
    form2=Reg()
    if request.method=='POST':
        if form.validate_on_submit():
            userId=form.id.data
            password=form.password.data
            ifUserId=User.query.filter(and_(User.id==userId,User.password==password)).first()
            if not ifUserId:
                flash('用户名或者密码错误')
            else:
                flash('登录成功')
                session['username']=userId
                return redirect(url_for('buy'))
        else:
            flash('请填写完整')
    return render_template('login.html', form=form, form2=form)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    Insert()
    app.run(debug=True)

















