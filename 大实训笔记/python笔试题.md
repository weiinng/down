* int、float、str、tuple、list、set、dict，前面这些类型哪些可以做dict的key，哪些可以做dict的value？





* 请写出一段python代码实现删除一个list里面的重复元素。



```python
list_element = ['a','c,','z','x','a']      #此列表元素有重复
delete_element = list(set(list_element))     #利用集合的唯一性删除重复元素
print("原始列表为：",list_element)
print("修改后的列表为：",delete_element)

'''运行结果'''
原始列表为： ['a', 'c,', 'z', 'x', 'a']
修改后的列表为： ['c,', 'x', 'z', 'a']

```

但是这样做有缺点，就是去重后，元素的排序改变了，想保持原来的排序，我们需要用下面的方法： 

```python
list_element = ['a','c,','z','x','a']      #此列表元素有重复
delete_element = list( set(list_element))     #利用集合的唯一性删除重复元素
delete_element.sort(key = list_element.index)   #对修改后的列表进行排序
print("原始列表为：",list_element)
print("修改后的列表为：",delete_element)

'''运行结果'''
原始列表为： ['a', 'c,', 'z', 'x', 'a']
修改后的列表为： ['a', 'c,', 'z', 'x']
```





* 写出结果为[1,4,9,16,25....100]的列表推导式

```python
my_list = [x*x for x in range(1, 11)]
print(my_list)

 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```





* 写出结果为{1:1,2:4,3:9,4:16....10:100}的字典推导式

```python
my_dict = {x:x*x for x in range(1,11)}
print(my_dict)

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```





* 下面代码会输出什么？

  ```python
  def f(x,l=[]):
  	for i in range(x):
  		l.append(i*i)
  print(l)
  
  f(2)
  f(3,[3,2,1])
  f(3)
  
  '''结果'''
  [0, 1]
  [3, 2, 1, 0, 1, 4]
  [0, 1, 0, 1, 4]
  ```

  

* a = [1,2,3,4,5], a[::2]=? ,a[-2:]=?

```python
a[::2] = [1,3,5]
a[-2:] = [4,5]
```





* 写出结果

  ```python
  class Person:
      name = []
      
  p1 = Person()
  p2 = Person()
  p1.name.append(1)
  print(p1.name)
  print(p2.name)
  print(Person.name         
  ```





* List = [-2,1,3,-6],如何实现以绝对值大小从小到大将list中内容排序

```python
List = [-2,1,3,-6]
res = sorted(List,key=abs)
print(res)
```





* 写出print输出值

  ```python
  def extendList(val,list=[]):
      list.append(val)
      return list
  list1 = extendList(10)
  list2 = extendList(123,[])
  list3 = extendList('a')
  print('list1=%s'%list1)
  print('list2=%s'%list2)
  print('list3=%s'%list3)
  
  
  '''结果'''
  list1=[10, 'a']
  list2=[123]
  list3=[10, 'a']
  ```

  



* 使用python实现快排







* 广度优先，深度优先，遍历二叉树





* 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。







* 实现一段代码，功能是将这段代码打印出来。





* 写答案

  ```python
  list_a = [1,2,3,4,5,6,7,8]
  list_b = [8,7,6,5,4,3,2,1]
  
  list_a[-4::2] = [5,7]
  list_a.pop() = 8
  
  for i in zip(list_a,list_b):
      print(i)
      
      
  (1, 8)
  (2, 7)
  (3, 6)
  (4, 5)
  (5, 4)
  (6, 3)
  (7, 2)
  ```

  

* 写运行结果

  ```python
  def f(t,lis=[]):
      lis.append(t)
      print(lis)
      
  f(5)    [5]
  f(3) 	[5,3]
  
  ```

  



* 将列表合并，去重，排序，python代码实现

  ```python
  a = [3,6,8]
  b = [8,7,2]
  
  ```

  

* 完成由列表元素组成的全排列的打印函数

  ```python
  Alist = [1,2,3,4]
  ```

  

  















