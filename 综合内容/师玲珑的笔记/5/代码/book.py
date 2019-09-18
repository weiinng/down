







from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,request,flash
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField
from wtforms.validators import DataRequired
from sqlalchemy import and_

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='asd'

db=SQLAlchemy(app)

class Author(db.Model):
    __tablename__='author'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(32),unique=True)

class Book(db.Model):
    __tablename__='books'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(32))
    author_id=db.Column(db.Integer,db.ForeignKey('author.id'))

class Update(FlaskForm):
    au_name=StringField('作者：',validators=[DataRequired()])
    bo_name=StringField('书名：',validators=[DataRequired()])
    submit=SubmitField('提交')

class Update2(FlaskForm):
    au_name=StringField('请输入你要删除的作者名字：',validators=[DataRequired()])
    submit=SubmitField('提交')

class Find_author(FlaskForm):
    au_name=StringField('请输入你要查找的作者：',validators=[DataRequired()])
    submit=SubmitField('提交')

class Find_book(FlaskForm):
    bo_name=StringField('请输入你要查找的书名：',validators=[DataRequired()])
    submit=SubmitField('提交')

class Update_author(FlaskForm):
    au_name=StringField('请输入你要修改的作者名：',validators=[DataRequired()])
    au_name2=StringField('请输入你改后的作者名：',validators=[DataRequired()])
    submit=SubmitField('提交')

class Update_book(FlaskForm):
    au_name=StringField('请输入你要修改书名的作者名：',validators=[DataRequired()])
    bo_name=StringField('请输入你要修改的书名：',validators=[DataRequired()])
    bo_name2=StringField('请输入你改后的书名：',validators=[DataRequired()])
    submit=SubmitField('提交')

def add():
    au1=Author(id=1,name='老王')
    au2=Author(id=2,name='老尹')
    au3=Author(id=3,name='老刘')
    db.session.add_all([au1,au2,au3])
    db.session.commit()
    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    db.session.commit()

@app.route('/',methods=['GET','POST'])
def index():
    au = Author.query.all()
    bo = Book.query.all()
    form=Update()
    if request.method=='POST':
        if form.validate_on_submit():
            author_name=form.au_name.data
            book_name=form.bo_name.data
            author=Author.query.filter(Author.name==author_name).first()
            if not author:
                author=Author(name=author_name)
                db.session.add(author)
                db.session.commit()
                book=Book(name=book_name,author_id=author.id)
                db.session.add(book)
                db.session.commit()
            else:
                book=Book.query.filter(and_(Book.name==book_name,Book.author_id==author.id)).first()
                if not book:
                    jia=Book(name=book_name,author_id=author.id)
                    db.session.add(jia)
                    db.session.commit()
                else:
                    flash('该书已存在')
    return render_template('index.html',author=au,books=bo,form=form)

@app.route('/delete_book',methods=['GET','POST'])
def delete():
    au = Author.query.all()
    bo = Book.query.all()
    form=Update()
    author_name=form.au_name.data
    book_name=form.bo_name.data
    if request.method=='POST':
        if form.validate_on_submit():
            author = Author.query.filter(Author.name == author_name).first()
            if not author:
                flash('不存在该作者')
            else:
                book = Book.query.filter(Book.name == book_name).first()
                if not book:
                    flash('该作者不存在该书籍')
                else:
                    try:
                        db.session.delete(book)
                        db.session.commit()
                    except Exception as e:
                        flash('删除出错')
                        print(e)
        else:
            flash('输入数据有误')
    return render_template('index.html',form=form,author=au,books=bo)

@app.route('/delete_author',methods=['GET','POST'])
def delete2():
    au=Author.query.all()
    bo=Book.query.all()
    form=Update2()
    author=form.au_name.data
    if request.method=='POST':
        if form.validate_on_submit():
            author = Author.query.filter(Author.name == author).first()
            if not author:
                flash('没有该作者')
            else:
                try:
                    allBook = Book.query.filter(Book.author_id == author.id).all()
                    for x in allBook:
                        book = x
                        db.session.delete(book)
                        db.session.commit()
                    db.session.delete(author)
                    db.session.commit()
                except Exception as e:
                    flash('删除数据出错')
                    print(e)
        else:
            flash('输入数据有误')
    return render_template('index.html',form=form,author=au,books=bo)

@app.route('/find_author',methods=['GET','POST'])
def find():
    au=Author.query.all()
    bo=Book.query.all()
    form=Find_author()
    author=form.au_name.data
    if request.method=='POST':
        author=Author.query.filter(Author.name==author).first()
        if not author:
            flash('不存在该作者')
        else:
            bookName=Book.query.filter(Book.author_id==author.id).all()
            for x in bookName:
                flash(x.name)
    return render_template('index.html',author=au,books=bo,form=form)

@app.route('/find_book',methods=['GET','POST'])
def find2():
    q='1'
    au=Author.query.all()
    bo=Book.query.all()
    form=Find_book()
    book=form.bo_name.data
    if request.method=='POST':
        book=Book.query.filter(Book.name==book).all()
        if not book:
            flash('没有该书')
        else:
            for x in book:
                name=Author.query.filter(Author.id==x.author_id).first().name
                flash('这本书是%s写的' % name)

    return render_template('index.html',author=au,books=bo,form=form,q=q)

@app.route('/update_book',methods=['GET','POST'])
def update1():
    w='2'
    au=Author.query.all()
    bo=Book.query.all()
    form=Update_book()
    author=form.au_name.data
    bo1=form.bo_name.data
    bo2=form.bo_name2.data
    if request.method=='POST':
        bookid=Author.query.filter(Author.name==author).first()

        if not bookid:
            flash('不存在该作者')
        else:
            book = Book.query.filter(and_(Book.name == bo1, Book.author_id == bookid.id)).first()
            if not book:
                flash('不存在该书')
            else:
                book.name = bo2
                db.session.commit()
    return render_template('index.html',author=au,books=bo,form=form,w=w)

@app.route('/update_author',methods=['GET','POST'])
def update2():
    e='3'
    au=Author.query.all()
    bo=Book.query.all()
    form=Update_author()
    if request.method=='POST':
        au1=form.au_name.data
        au2=form.au_name2.data
        name=Author.query.filter(Author.name==au1).first()
        if not name:
            flash('没有该作者')
        else:
            name.name=au2
            db.session.commit()
    return render_template('index.html',author=au,books=bo,form=form,e=e)

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    add()
    app.run(debug=True)





