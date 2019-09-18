文字属性：
1、color字体颜色
color属性：用于定义文字的颜色

2、font-size字号
font-size属性：设置文字的大小。常用的网页文字大小有：12px(正文),14px（标题）

3、font-family字体
font-family属性：设置文字字体，如宋体，黑体，隶书等

4、font-weight字体加粗
font-weight属性：设置文字的粗细程度，blod设置粗体，normal将粗体改为正常字体

5、font-style字体是否倾斜
italic倾斜
normal正常

段落属性：
1、文字修饰（text-decoration)
underline 下划线
overline 上划线
line-through 删除线
none 无修饰
例如：
<p text-decoration:underline;}

2、水平对齐方式（text-align)
text-align属性：设置文本的水平对齐方式。属性值可以设置为left、center、right等，即如何为文本设置左对齐、居中对齐和右对齐，其他值不要求掌握。
如<h2 text-align:center;>

3、文本缩进（text-indent)
text-indent属性：设置文本块中首行的缩进，属性值可设置为数值加单位或者用em设置缩进几个字，百分比和复制不要求掌握。
如：p{text-indent:24px;} 或 p{text-indent:2em;}

4、文本行高（line-height)
line-height属性：设置行间距，即行高。属性值可设置为数值加单位，百分比和负值，负值不要求掌握
如 p{line-height:25px;}

背景属性 background
背景属性包含背景色、背景图、背景重复、背景位置、背景附件和背景复合属性等
背景颜色：background-color
背景图片：background-img:url(路径);
背景重复：background-repeat:
属性值：repeat/no-repeat/repeat-x/repeat-y
背景位置：background-position:水平 垂直;
可以取得值为关键字，数值，百分比
水平：left,center,right
垂直：top,center,bottom
背景附件：（背景是否滚动 属性值：scroll(默认) 滚动 fixed(固定))

列表案例符号的样式 list-style
list-style-type :定义列表前面的项目符号
disc 实心圆、circle 空心圆、square 方块、none 不使用任何符号

list-style-image定义列表项标志的图像
语法：list-style-image:none\路径

list-style-position列表位置
语法：list-style-position:outside(默认、更靠里面)\inside
去掉列表案例符号的代码是：ul{list-style:none}













