## vue关于数字的处理（四舍五入，向上取整，向下取整。。）



1、向下取整的函数

#### Math.floor();

例如：Math.floor( 23.2222222); // 23

2、向上取整

#### Math.ceil();

例如： Math.ceil(23.333333）； // 24

3、四舍五入

#### Math.round();

例如：Math.round(23.33333); // 23

4、四舍五入取n位小数，运算后得到的是字符串

#### ().toFixed(n); // 取小数点后n位

例如：(36.36498524).toFixed(3); // 36.365



ps:虽然写的是vue,但是不仅仅vue中可以使用哦
--------------------- 
