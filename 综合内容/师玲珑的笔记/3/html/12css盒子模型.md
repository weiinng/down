盒模型：
1、边框属性：
边框颜色：border-color 如border-color:red;
边框样式：border-style 常用边框样式：solid实线、dashed虚线、dotetd 点线、none 取消线
边框宽度：border-width 如：border-width:3px;
border复合属性可同时设置边框的宽度、样式和颜色 如：border:1px red solid;
单独设置一条边框如：
上边框 border-top,右边框 border-right,下边框 border-bottom,左边框 border-left
如：border-bottom:1px red dashed;

2、内填充
padding:内容与边框之间的距离
设置上内填充padding-top属性，右内填充padding-right属性

3、外边距：
margin:元素与元素之间的距离
上外边距 margin-top 属性，右外边距margin-right属性，下外边距 margin-bottom属性。
用长度加单位设置属性值： margin-left:200px 
在div的css选择器里写 margin: 0 auto; 设置居中效果，但是当div被定位后就不好使了

复合属性：
padding复合属性设置所有内填充属性，用法如下：
属性值为一个数值如padding:10px;表示上右下左内填充都是10px
属性值为四个时，padding:10px 20px 30px 40px;表示上10右20下30左40
margin的复合属性与padding用法一样

padding对元素宽高的影响,会增加盒子的大小
盒子的实际宽=width+padding-left+padding-right
盒子的实际高=height+padding-top+padding-bottom

box-shadow 属性盒子阴影
box-shadow:1px 2px 3px red insert
1px表示水平阴影的位置。允许负值，必写
2px表示垂直阴影的位置。允许负值 ，必写
3px表示模糊距离，可选
red 表示阴影的颜色，可选
insert 将外部阴影（outset)改为内部阴影

text-shadow属性文字阴影：
text-shadow:x轴偏移量 y轴偏移量 阴影模糊半径 阴影颜色

border-radius属性：
指定好圆角的半径，就可以绘制圆角边框了，
border-radius:20px;

gradient 渐变
所谓渐变是指从一种颜色慢慢过渡到另外一种颜色。线性渐变和径向渐变
绘制线性渐变：
background:linear-gradient(to bottom,red,yellow);
参数值       渐变方向
to bottom   从上往下
to right      从左往右

第二个参数和第三个参数分别表示渐变的起点色和终点色




















