from flask import Flask,session
app=Flask(__name__)
app.config['SECRET_KEY']='asd'
@app.route('/aa')
def a():
    session['name']='qwe'
    return '1'

@app.route('/ba')
def B():
    session.pop('name')
    return '2'


if __name__ == '__main__':
    app.run()










# from flask import Flask,request,Response,jsonify,session
# import json
# app=Flask(__name__)
#
# @app.route('/login',methods=['POST'])
# def login():
#     name=request.form.get('name')   #表单数据通过form获取
#     password=request.form.get('password')
#     return jsonify({'name':name,'password':password})
#
# @app.route('/save_cookie')
# def save_cookie():
#     r=Response('保存cookie')    #实例化Response类
#     r.set_cookie('name1','xiaoming2')   #使用Response类里面的方法set_cookie
#     return r
#
# @app.route('/show_cookie')
# def show_cookie():
#     cookie=request.cookies.get('name1')  #使用request的cookies.get传递key,获取cookie
#     return cookie
#
# @app.route('/delete_cookie')
# def delete_cookie():
#     r=Response('删除cookie')
#     r.delete_cookie('name1')
#     return r
#
# @app.route('/save_session')
# def save_session():
#     session['name2']='xiaohua'
#     return '保存session'
#
# @app.route('/show_session')
# def show_session():
#     return session['name2']
#
# @app.route('/delete_session')
# def delete_session():
#     session.pop('name2')
#     return '删除session'
#

# if __name__ == '__main__':
#     app.run(debug=True)

