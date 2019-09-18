from flask import Flask,render_template,request,flash

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def html():
    if request.method=='POST':
        name=request.form.get('name')
        password=request.form.get('password')
        password2=request.form.get('password2')
        print(name,password,password2)
        if not all([name,password,password2]):
            flash(u'参数不完整')
        elif password2!=password:
            flash(u'密码不一致')
        else:
            flash(u'登录成功')
    return render_template('1.html')

app.secret_key='itheima'
app.config.from_pyfile('settings.ini')

if __name__ == '__main__':
    app.run(port=80)

