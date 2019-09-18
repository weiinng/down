# from pymysql import connect
# from flask import Flask,request,session
# import json
#
# app=Flask(__name__)
# app.config['PERMANENT_SESSION_LIFETIME']=20
# app.config['SECRET_KEY']='asdadd'
# app.config.from_pyfile('settings.ini')
#
# def open_mysql():
#     conn=connect(host='localhost',port=3306,database='buy',user='root',password='qwq',charset='utf8')
#     cur=conn.cursor()
#     return conn,cur
#
# def find_all(sql):
#     conn,cur=open_mysql()
#     cur.execute(sql)
#     ret=cur.fetchall()
#     return ret
#
# @app.route('/getgoods')
# def a():
#     ret=find_all('select *from goods')
#     list = []
#     for x in ret:
#         dict = {}
#         dict['id'] = x[0]
#         dict['name'] = x[1]
#         dict['price'] = x[2]
#         list.append(dict)
#     mes={}
#     if session.get('username'):
#         mes['code'] = 200
#     else:
#         mes['code']=10010
#     mes['mes']=list
#     return json.dumps(mes,ensure_ascii=False)
#
# @app.route('/login',methods=['POST'])
# def b():
#     data=json.loads(request.data.decode())
#     name=data['name']
#     password=data['password']
#     ret=find_all("select *from user where name=\'%s\' and password=\'%s\'"%(name,password))
#     mes={}
#     if not ret:
#         mes['code']=10010
#     else:
#         mes['code']=200
#         session['username']=name
#         # print(session.get('username'))
#     return json.dumps(mes,ensure_ascii=False)
#
# @app.route('/buy',methods=['POST','GET'])
# def c():
#     data=json.loads(request.data.decode())
#     goodsname=data['name']
#     price=float(data['price'])
#     name=session['username']
#     conn,cur=open_mysql()
#     cur.execute("insert into buy VALUE ('%s','%s',%d,%.2f)"%(name,goodsname,1,price))
#     conn.commit()
#     return 'a'
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
#
#
#

# a=[{'name':1},2,3,4]
# del a[0]
# print(a)


a=[[{'role_id': 1, 'role_name': 'admin', 'id': 1, 'name': '王', 'email': 'wang@', 'password': 'wang'}, {'role_id': 1, 'role_name': 'admin', 'id': 3, 'name': '陈', 'email': 'chen@', 'password': 'chen'}, {'role_id': 1, 'role_name': 'admin', 'id': 5, 'name': '唐', 'email': 'tang@', 'password': 'tang'}, {'role_id': 1, 'role_name': 'admin', 'id': 7, 'name': '钱', 'email': 'qian@', 'password': 'qian'}, {'role_id': 1, 'role_name': 'admin', 'id': 9, 'name': '关', 'email': 'guan@', 'password': 'guan'}], [{'role_id': 2, 'role_name': 'user', 'id': 2, 'name': '张', 'email': 'zhang@', 'password': 'zhang'}, {'role_id': 2, 'role_name': 'user', 'id': 4, 'name': '周', 'email': 'zhou@', 'password': 'zhou'}, {'role_id': 2, 'role_name': 'user', 'id': 6, 'name': '吴', 'email': 'wu@', 'password': 'wu'}, {'role_id': 2, 'role_name': 'user', 'id': 8, 'name': '刘', 'email': 'liu@', 'password': 'liu'}, {'role_id': 2, 'role_name': 'user', 'id': 10, 'name': '马', 'email': 'ma@', 'password': 'ma'}]]
list=[]
for x in a:
    for i in x:
        list.append(i)

list3=sorted(list,key=lambda x:x['id'])
list4=[]
print(len(list3))
for x in range(len(list3)):
    if list3[x]['id']%2==0:
        list4.append(list3[x])

# print(list3)