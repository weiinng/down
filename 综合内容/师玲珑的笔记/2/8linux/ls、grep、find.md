ls 是查看当前路径的内容
ls *.txt  
查看所有的txt文件 不用加引号


find 是查看当前路径下的所有路径的内容
find -name '*.txt'  
查看所有的txt文件，必须加引号！！！！！！！！！！！！！！！！


grep 是查看文件里指定的内容
grep '^w' 1.txt 
查看1.txt里哪些行以小写w开头  后面加个-n 显示行数 加个-i 不区分大小写 也就是大写的W也可以  加个-v是查找的反结果

cat 是查看文件里的所有内容
cat 1.txt 
cat 1.txt 2.txt >> 3.txt 将1.txt 和 2.txt 里的内容添加到3.txt 后面
cat 1.txt 2.txt > 3.txt 将1.txt 和 2.txt 里的内容添加到3.txt 里  3.txt里原先的内容没有了



