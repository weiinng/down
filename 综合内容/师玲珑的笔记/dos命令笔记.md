DOS命令

DOS实际上是Disk Operation System（磁盘操作系统）的简称

*.txt  删除所有的文本文档


1.显示目录dir

例子：dir 显示C盘目录   dir /b 忽略时间日期

例 dir d: 显示d盘目录

2.指定到某个盘符

例 d: 指定到d盘

3.1 新建目录md

例 md liang(目录名称)

3.2 删除目录

例 rd liang(目录名称)  注意：目录里边必须为空

4.1 新建文本文档echo

例 echo >1.txt

4.2 删除文本文档 del

例 del 1.txt

例 del *.txt 删除所有后缀txt的文档

5.显示文本文档内容到dos窗口type

例 type 1.txt

6.改变当前目录cd

例 cd liang 指定到liang目录下

例 cd.. 返回父目录

7.移动文件move 

例 move d:\1.txt 目标路径（盘符路径e:\） 

例 还有重命名作用 move 1.txt 11.txt 或者 rename 1.txt 11.txt

8.复制文件copy

例 copy 1.txt 目标路径（盘符路径e:\）

9. 调试计算机网路 ipconfig

10.测试网络通畅 ping

例 ping 192.168.1.183（ip地址）

例 ping www.baidu.com

注意：

11.查看目录并写入到文件中

dir >目录名称  覆盖

dir >>目录名称 追加

12.命令向文件写入内容

echo 我很好>1.txt

13.返回

cd.. 上级目录（当只有两级目录时，也可说返回根目录）

cd/  根目录


1.复制目录（文件夹） xcopy d:\123  e:\123

注意：文件夹不能为空


