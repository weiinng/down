# from flask import Flask,request
# import json
# from pymysql import connect
#
# app=Flask(__name__)
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
# @app.route('/mysql',methods=['POST'])
# def show():
#     date=json.loads(request.data.decode())
#     name=date['user']
#     password=date['password']
#     result=find_all("select id,age from a where id=\'%s\' and age=\'%s\'"%(name,password))
#     mes={}
#     if len(result)>0:
#         mes['code']=200
#         list = []
#         for x in result:
#             dict = {}
#             dict['id'] = x[0]
#             dict['age'] = x[1]
#             list.append(dict)
#         mes['mes']=list
#     else:
#         mes['code']=1001
#         mes['mes']='用户名或密码错误'
#     return json.dumps(mes,ensure_ascii=False)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

