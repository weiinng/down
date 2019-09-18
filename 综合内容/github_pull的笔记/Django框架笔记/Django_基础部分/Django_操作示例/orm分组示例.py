import os


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_demo.settings")
    import django
    django.setup()

    from app01 import models

	
	# 查询 "部门表" 的全部内容
	# 查询的时候不带 values或者values_list 默认就是查询 all()
    
	# ret = models.Employee.objects.all()
    # """
    # SELECT `employee`.`id`, `employee`.`name`, `employee`.`age`, `employee`.`salary`, `employee`.`province`, `employee`.`dept` FROM `employee` LIMIT 21; args=()
    # """



	# 查询所有人的 "部门" 和 "年龄"
	#　values 或者 values_list 里面写什么就相当于 select 什么字段
    
	# ret = models.Employee.objects.all().values("dept", "age")
    # """
    # SELECT `employee`.`dept`, `employee`.`age` FROM `employee` LIMIT 21; args=()
    # """

	
	 from django.db.models import Avg
	# 分组
    # 每个 “省” 的 “平均工资”  
	# annotate前面是什么就按照什么来分组，annotate后面的字段是被分组后被计算的新数据列，
	
	ret = models.Employee.objects.values("province").annotate(a=Avg("salary")).values("province", "a")
    # """
    # SELECT `employee`.`province`, AVG(`employee`.`salary`) AS `a` FROM `employee` GROUP BY `employee`.`province` ORDER BY NULL LIMIT 21; args=()
    # """


    # ORM连表分组查询
	# 根据 "部门" 计算出 "平均工资" 结果为显示为 "部门名字 : 平均工资" 的表
    ret = models.Person.objects.values("dept_id").annotate(a=Avg("salary")).values("dept__name", "a")
    # """
    # SELECT `dept`.`name`, AVG(`person`.`salary`) AS `a` FROM `person` INNER JOIN `dept` ON (`person`.`dept_id` = `dept`.`id`) GROUP BY `person`.`dept_id`, `dept`.`name` ORDER BY NULL LIMIT 21; args=()
    # """


# 查询person表，判断每个人的工资是否大于2000
# 利用子查询,可以写入原生的sql语句
ret = models.Person.objects.all().extra(
	select={"gt": "salary > 2000"}
	)

# """
# SELECT (salary > 2000) AS `gt`, `person`.`id`, `person`.`name`, `person`.`salary`, `person`.`dept_id` FROM `person` LIMIT 21; args=()
# """

for i in ret:
	print(i.name, i.gt)


# 执行完全的原生的SQL语句
from django.db import connection
cursor = connection.cursor()  # 获取光标，等待执行SQL语句
cursor.execute("""SELECT * from person where id = %s""", [1])
row = cursor.fetchone()
print(row)


