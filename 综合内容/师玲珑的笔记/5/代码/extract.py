from pymysql import connect
def extract():
    conn=connect(host='localhost',port=3306,database='five',user='root',password='qwq',charset='utf8')
    cur=conn.cursor()
    cur.execute('select *from a')
    result=cur.fetchall()
    list=[]
    for x in result:
        dict={}
        dict['id']=x[0]
        dict['age']=x[1]
        list.append(dict)
    return list