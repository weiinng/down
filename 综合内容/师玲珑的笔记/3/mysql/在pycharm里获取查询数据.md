cur.execute("select *from em inner join dep on em.did=dep.id where em.age>10")
r=cur.fetchall()
r就是你查询到的数据

