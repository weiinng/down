
 # list=[str(x) for x in range(10)]
# print(list)
# a='a'.join(list)
# print(a)



# for x,y in dicta.items():
#     print(x,y)
#     for q,w in dictb.items():
#         print(q,w,end=' ')
#     print()

# dicta={'a':1,'b':2,'c':3,'d':4,'f':'hello'}
# dictb={'b':3,'d':5,'e':7,'m':9,'f':'world','k':'asd'}
# dictc={}
# for x,y in dicta.items():
#     c=0
#     for q,w in dictb.items():
#         if x==q:
#             c+=1
#             if type(y)==int and type(w)==int:
#                 s=w+y
#                 dictc[q]=s
#                 break
#
#             elif type(y)==str and type(w)==str:
#                 s2=y+w
#                 dictc[q]=s2
#                 break
#         else:
#             if q not in dictc.keys():
#                 dictc[q] = w
#     if c == 0:
#         dictc[x] = y
# print(dictc)

# a='1'
# if type(a)==str:
#     print(a)









# sum=0
# list=[1,2,3,4,5,6,7,8]
# for x,y in enumerate(list):
#     if x%2==1:
#         sum+=y
# print(sum)

# from pymysql import connect
# conn=connect(host='localhost',port=3306,database='work2',user='root',password='qwq',charset='utf8')
# cur=conn.cursor()
# sql1="select distinct depname,depid from shitu order by depid"
# sql2="select group_concat(name) from shitu group by depid order by depid"
# cur.execute(sql1)
# r1=cur.fetchall()
# cur.execute(sql2)
# r2=cur.fetchall()
#
# listr1=[]
#
# for x in r1:
#     listr1.append(x[0])
# cur.close()
# conn.close()
#
# list3=[]
#
# for x in range(len(r1)):
#     dict = {}
#     list4=[]
#     for i in r2[x]:
#         list4.append(i)
#     dict[listr1[x]] = list4
#     list3.append(dict)
#
# print(list3)
# for x in list3:
#     for i in x.values():
#         print(i[0])


# for x in list3[0]['Ë¯¾õ']:
#     print(x)

# for x in range(len(r1)):
#     list1=[]
#     list1.append(r1[x])
#     list2=[]
#     for i in r2[x]:
#         list2.append(i)
#     list1.append(list2)
#     list3.append(list1)
# print(list3)
# list4=[]
# for x in list3:
#     dict={}
#     list5=[]
#     for i in x[1]:
#         list5.append(i)
#     dict['%s'%x[0]]=list5
#     list4.append(dict)
# print(list4)




# dict={}
# for x in range(3):
#
#     dict['%d'%x]=x
# print(dict)





# from pymysql import connect
# conn=connect(host='localhost',port=3306,database='work2',user='root',password='qwq',charset='utf8')
# cur=conn.cursor()
# cur.execute("select *from em inner join dep on em.did=dep.id where em.age>10")
# r=cur.fetchall()
# cur.close()
# conn.close()
# list=[]
# for x in r:
#     dict={}
#     dict['id']=x[0]
#     dict['name']=x[1]
#     dict['age']=x[2]
#     dict['did']=x[3]
#     dict['dname']=x[5]
#     list.append(dict)
# print(list)


# from pymysql import connect
# conn=connect(host='localhost',port=3306,database='cart',user='root',password='qwq',charset='utf8')
# cur=conn.cursor()
# sql="select *from user_cart inner join users on users.id=user_cart.uid where user_cart.num>2"
# cur.execute(sql)
# r=cur.fetchall()
# list=[]
# for x in r:
#     dict={}
#     dict['id']=x[0]
#     dict['name']=x[1]
#     dict['num']=x[2]
#     dict['price']=float(x[3])
#     dict['uid']=x[4]
#     dict['u_id']=x[5]
#     dict['u_name']=x[6]
#     list.append(dict)
# print(list)
# cur.close()
# conn.close()








from pymysql import connect
conn=connect(host='localhost',port=3306,database='vacation',user='root',password='qwq',charset='utf8')
cur=conn.cursor()
cur.execute("insert into content VALUES ('%s',%.2f)"%('wosgunbua',19))
conn.commit()

