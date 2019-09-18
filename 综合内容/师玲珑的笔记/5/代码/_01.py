# from flask import Flask,render_template,jsonify,request,redirect,url_for
# import json
#
# app = Flask(__name__)
#
# content_dict=str({'a':'b'})
# _str='123456789'
# @app.route('/')
# def hello_world():
#     return render_template('1.html',url_str=_str,content_dict=content_dict )   #return只能返回字符串 json  render_template
#     # return json.dumps({'a':'b'})             #json.dumps将python转为json，发送到网页是文本类型
#     # return str({'a':'b'})  #如果强转为字符串 就破坏了数据结构，无法通过键值对找值
#     # return jsonify({'a':'啊啊啊saaaaaaa'})   #发送到网页是json类型
#     # return json.dumps({'a':'b'}),200,{'content-type':'application/json'}   #跟上面那个一样了
#
# @app.route('/<int:id>/<name>')
# def id(id,name):
#     gender=request.args.get('gender')
#     return "{'name':%s,'id':%d,'gender':%s}"%(name,id,gender)
#
# @app.route('/param')
# def params():
#     name=request.args.get('name')
#     id=request.args.get('id')
#     return jsonify({'name':name,'id':id})
#
# @app.route('/five')
# def five():
#     return redirect(url_for('hello_world'))     #重定向url_for里的参数是给你要跳转页面的视图函数名
#
# @app.route('/chuan')
# def chuan():
#     return redirect(url_for('tiao',content='啦啦啦'))
#
# @app.route('/<content>')
# def tiao(content):
#     return content
#
# # app.config['JSON_AS_ASCII']=False   #将返回的汉字不要以ASCII码形式返回
#
# app.config.from_pyfile('settings.ini')   #从文件中导入配置,在文件里写的配置 配置名都要大写
#
# if __name__ == '__main__':
#     app.run(port=80)


# a=(1,2)
# print('\t'.join([str(x) for x in list(a)]))

# from flask import Flask,jsonify
# from pymysql import connect
# import json
#
# def open_mysql():
#     conn=connect(host='localhost',port=3306,database='five',user='root',password='qwq',charset='utf8')
#     cur=conn.cursor()
#     return conn,cur
#
# def find_all(sql):
#     conn,cur=open_mysql()
#     cur.execute(sql)
#     result=cur.fetchall()
#     close_mysql(conn,cur)
#     return result
#
# def close_mysql(conn,cur):
#     cur.close()
#     conn.close()
#
# app=Flask(__name__)
# @app.route('/')
# def a():
#     result=find_all('select *from a')
#     list=[]
#     for x in result:
#         dict={}
#         dict['id']=x[0]
#         dict['age']=x[1]
#         list.append(dict)
#     return json.dumps(list)
#
# app.config.from_pyfile('settings.ini')
# if __name__ == '__main__':
#     app.run(debug=True)


