from flask import Flask,render_template,flash,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_,or_

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/book'
app.config['SECRET_KEY']='asd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Author(db.Model):
    __tablename__='author'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(10))

class Book(db.Model):
    __tablename__='book'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(10))
    author_id=db.Column(db.Integer,db.ForeignKey('author.id'))

def first():
    au1=Author(id=1,name='张三')
    au2=Author(id=2,name='李四')
    au3=Author(id=3,name='王五')
    db.session.add_all([au1,au2,au3])
    db.session.commit()
    bo1=Book(id=1,name='one',author_id=au1.id)
    bo2=Book(id=2,name='two',author_id=au1.id)
    bo3=Book(id=3,name='three',author_id=au2.id)
    bo4=Book(id=4,name='four',author_id=au2.id)
    bo5=Book(id=5,name='five',author_id=au3.id)
    bo6=Book(id=6,name='six',author_id=au3.id)
    db.session.add_all([bo1,bo2,bo3,bo4,bo5,bo6])
    db.session.commit()

@app.route('/')
def a():
    authors=Author.query.all()
    books=Book.query.all()
    return render_template('book.html',a=authors,b=books)

@app.route('/add',methods=['GET','POST'])
def b():
    q='1'
    authors = Author.query.all()
    books = Book.query.all()
    author=request.form.get('author')
    book=request.form.get('book')
    if request.method=='POST':
        au=Author.query.filter(Author.name==author).first()
        if au:
            bo = Book.query.filter(and_(Book.author_id == au.id, Book.name == book)).first()
            if bo:
                flash('这本书已经存在')
            else:
                bo=Book(name=book,author_id=au.id)
                db.session.add(bo)
                db.session.commit()
        else:
            au=Author(name=author)
            db.session.add(au)
            db.session.commit()
            bo=Book(name=book,author_id=au.id)
            db.session.add(bo)
            db.session.commit()
    return render_template('book.html',q=q,a=authors,b=books)

@app.route('/delete_book',methods=['GET','POST'])
def c():
    w='q'
    authors = Author.query.all()
    books = Book.query.all()
    author=request.form.get('author')
    book=request.form.get('book')
    if request.method=='POST':
        au = Author.query.filter(Author.name == author).first()
        if au:
            bo=Book.query.filter(and_(Book.name==book,Book.author_id==au.id)).first()
            if bo:
                db.session.delete(bo)
                db.session.commit()
            else:
                flash('没有该作者写的这本书')
        else:
            flash('没有该书')
    return render_template('book.html',a=authors,b=books,w=w)

@app.route('/delete_author',methods=['POST','GET'])
def d():
    e='1'
    authors = Author.query.all()
    books = Book.query.all()
    if request.method=='POST':
        author = request.form.get('author')
        au=Author.query.filter(Author.name==author).first()
        if au:
            bo=Book.query.filter(Book.author_id==au.id).all()
            for x in bo:
                db.session.delete(x)
                db.session.commit()
            db.session.delete(au)
            db.session.commit()
        else:
            flash('没有该作者')
    return render_template('book.html',a=authors,b=books,e=e)

@app.route('/update_book',methods=['GET','POST'])
def e():
    r='1'
    authors = Author.query.all()
    books = Book.query.all()
    if request.method=='POST':
        author=request.form.get('author')
        book=request.form.get('book')
        book2=request.form.get('book2')
        au=Author.query.filter(Author.name==author).first()
        if au:
            bo=Book.query.filter(and_(Book.name==book,Book.author_id==au.id)).first()
            if bo:
                bo.name=book2
                db.session.commit()
            else:
                flash('没有该书')
        else:
            flash('没有该书')
    return render_template('book.html',a=authors,b=books,r=r)

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    first()
    app.run(debug=True)








