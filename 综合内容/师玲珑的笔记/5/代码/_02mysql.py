from flask import Flask,jsonify
from pymysql import connect

app=Flask(__name__)

def open():
    conn=connect(host='localhost',port=3306,database='five',user='root',password='qwq',charset='utf8')
    cur=conn.cursor()
    return conn,cur

def find(sql):
    conn,cur=open()
    cur.execute(sql)
    result=cur.fetchall()
    close(conn,cur)
    return result

def close(conn,cur):
    conn.close()
    cur.close()

@app.route('/')
def export():
    result=find('select *from a')
    print('id\tage')
    # for x in result:
    #     print('\t'.join([str(i) for i in x]))
    return jsonify(result)

app.config.from_pyfile('settings.ini')
if __name__ == '__main__':
    app.run(port=80)






















# from flask import Flask,jsonify
# from pymysql import connect
#
# app=Flask(__name__)
#
# def mysql_conn():
#     conn=connect(host='localhost',port=3306,database='five',user='root',password='qwq',charset='utf8')
#     cur=conn.cursor()
#     return conn,cur
#
# def find_all(sql):
#     conn,cur=mysql_conn()
#     cur.execute(sql)
#     result=cur.fetchall()
#     close_conn(conn,cur)
#     return result
#
#
# def close_conn(conn,cur):
#     conn.close()
#     cur.close()
#
# @app.route('/')
# def users():
#     sql='select *from a'
#     result=find_all(sql)
#     print('id\tage')
#     for x in result:
#         print('\t'.join([str(i) for i in list(x)]))
#     return jsonify(result)
#
# app.config.from_pyfile('settings.ini')
# if __name__ == '__main__':
#     app.run(port=80)
