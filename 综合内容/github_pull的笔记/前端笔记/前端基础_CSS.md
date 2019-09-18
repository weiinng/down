前端基础_CSS

	概念:
		层叠样式表,定义如何显示HTML元素.
		
	引入方式
		
		行内
			<p style="color: red">Hello world.</p>
		
		内部(嵌入式)
			将CSS样式集中写在网页的<head></head>标签对的<style></style>标签对中
				<head>
					<meta charset="UTF-8">
					<title>Title</title>
					<style>
						p{
							background-color: #2b99ff;
						}
					</style>
				</head>
		
		外部(推荐使用此方式.)
			<link href="mystyle.css" rel="stylesheet" type="text/css"/>
			
	CSS 选择器
		基本选择器
			元素选择器	
				p {color: "red";}
			ID选择器	
				#i1 {
					  background-color: red;
				}
			类选择器
				.c1 {
				  font-size: 14px;
				}
				p.c1 {
				  color: red;
				}
			通用选择器
				* {
				  color: white;
				}
		组合选择器
			后代选择器
				/*li内部的a标签设置字体颜色*/
				li a {
				  color: green;
				}
			儿子选择器
				/*选择所有父级是 <div> 元素的 <p> 元素*/
				div>p {
				  font-family: "Arial Black", arial-black, cursive;
				}
			毗邻选择器
				/*选择所有紧接着<div>元素之后的<p>元素*/
				div+p {
				  margin: 5px;
				}
			弟弟选择器
				/*i1后面所有的兄弟p标签*/
				#i1~p {
				  border: 2px solid royalblue;
				}
		属性选择器
			/*用于选取带有指定属性的元素。*/
			p[title] {
			  color: red;
			}
			/*用于选取带有指定属性和值的元素。*/
			p[title="213"] {
			  color: green;
			}
			不怎么常用的属性选择器:
				/*找到所有title属性以hello开头的元素*/
				[title^="hello"] {
				  color: red;
				}

				/*找到所有title属性以hello结尾的元素*/
				[title$="hello"] {
				  color: yellow;
				}

				/*找到所有title属性中包含（字符串包含）hello的元素*/
				[title*="hello"] {
				  color: red;
				}

				/*找到所有title属性(有多个值或值以空格分割)中有一个值为hello的元素：*/
				[title~="hello"] {
				  color: green;
				}

		分组
			当多个元素的样式相同的时候，我们没有必要重复地为每个元素都设置样式，我们可以通过在多个选择器之间使用逗号分隔的分组选择器来统一设置元素样式。 

			例如：div标签和p标签统一设置字体为红色。
				div, p {
				  color: red;
				}

			分两行来写更清晰一些
				div,
				p {
				  color: red;
				}
		嵌套
			多种选择器可以混合起来使用，
			
			.c1类内部所有p标签设置字体颜色为红色。
			.c1 p {
			  color: red;
			}
		伪类选择器
			/* 未访问的链接 */
			a:link {
			  color: #FF0000
			}

			/* 已访问的链接 */
			a:visited {
			  color: #00FF00
			} 

			/* 鼠标移动到链接上 */
			a:hover {
			  color: #FF00FF
			} 

			/* 选定的链接 */ 
			a:active {
			  color: #0000FF
			}

			/*input输入框获取焦点时样式*/
			input:focus {
			  outline: none;
			  background-color: #eee;
			}
		伪元素选择器
			first-letter
				常用的给首字母设置特殊样式：

				p:first-letter {
				  font-size: 48px;
				  color: red;
				}
			before
				/*在每个<p>元素之前插入内容*/
				p:before {
				  content:"*";
				  color:red;
				}
			after
				/*在每个<p>元素之后插入内容*/
				p:after {
				  content:"[?]";
				  color:blue;
				} 
			before和after多用于清除浮动。
		
	选择器的优先级
		CSS继承
			CSS的继承机制得以让一个一个样式可以应予以标签和其后代
			但是某些属性是无法继承的比如:border, margin, padding, background等
		选择器的优先级权重
			内联样式	1000
			id选择器	100
			元素选择器	1
			权重计算永不进位
		特殊方式
			除此之外还可以通过添加 !important 方式来强制让样式生效，但并不推荐使用。
			过多的使用!important 会使样式文件混乱不易维护。
			万不得已可以使用!important
			
			
	CSS 属性
		宽
		高
		字体属性
			文字字体
				按照从第一个开始识别,直到能够识别到为止,识别到后后面的不再继续
					body {
					  font-family: "Microsoft Yahei", "微软雅黑", "Arial", sans-serif
					}
			字体大小
				p {
				  font-size: 14px;
				}
			字重(粗细)
				font-weight用来设置字体的字重（粗细）。
				p {
				  font-weight: bold;
				}
				值	描述
					normal	默认值，标准粗细
					bold	粗体
					bolder	更粗
					lighter	更细
					100~900	设置具体粗细，400等同于normal，而700等同于bold
					inherit	继承父元素字体的粗细值				
			文本颜色
				p {
					  color:RGB(255,0,0);
				}
				十六进制值 - 如: ＃FF0000
				一个RGB值 - 如: RGB(255,0,0)
				颜色的名称 - 如:  red
				rgba(255,0,0,0.3)，第四个值指定了色彩的透明度/不透明度，范围为0.0~1.0
		
		段落属性
			文字对其
				text-align 属性规定元素中的文本的水平对齐方式。
				值	描述
					left	左边对齐 默认值
					right	右对齐
					center	居中对齐
					justify	两端对齐
			文字装饰
				text-decoration 属性用来给文字添加特殊效果。

				值	描述
					none	默认。定义标准的文本。
					underline	定义文本下的一条线。
					overline	定义文本上的一条线。
					line-through	定义穿过文本下的一条线。
					inherit	继承父元素的text-decoration属性的值。
				
				常用的为去掉a标签默认的自划线：

				a {
				  text-decoration: none;
				}
			首行缩进
				将段落的第一行缩进 32像素：

				p {
				  text-indent: 32px;
				}
		背景属性
			/*背景颜色*/
			background-color: red;
			/*背景图片*/
			background-image: url('1.jpg');
			/*
			 背景重复
			 repeat(默认):背景图片平铺排满整个网页
			 repeat-x：背景图片只在水平方向上平铺
			 repeat-y：背景图片只在垂直方向上平铺
			 no-repeat：背景图片不平铺
			*/
			background-repeat: no-repeat; 
			/*背景位置*/
			background-position: right top;
			/*background-position: 200px 200px;*/
		边框
			border-width
			border-style
			border-color
			
			#i1 {
			  border-width: 2px;
			  border-style: solid;
			  border-color: red;
			}
			通常使用简写方式：
			#i1 {
			  border: 2px solid red;
			}
			边框样式
				值	描述
					none	无边框。
					dotted	点状虚线边框。
					dashed	矩形虚线边框。
					solid	实线边框。
		border-radius
			用这个属性能实现圆角边框的效果。
			将border-radius设置为长或高的一半即可得到一个圆形。
		display属性
			用于控制HTML元素的显示效果。
				值	意义
					display:"none"	HTML文档中元素存在，但是在浏览器中不显示。一般用于配合JavaScript代码使用。
					display:"block"	默认占满整个页面宽度，如果设置了指定宽度，则会用margin填充剩下的部分。
					display:"inline"	按行内元素显示，此时再设置元素的width、height、margin-top、margin-bottom和float属性都不会有什么影响。
					display:"inline-block"	使元素同时具有行内元素和块级元素的特点。	 
			display:"none"与visibility:hidden的区别：
				visibility:hidden: 隐藏某个元素，隐藏的元素仍需占用与未隐藏之前一样的空间。会影响布局。
				display:none: 隐藏某个元素，隐藏的元素不会占用任何空间。不影响布局
	CSS盒子
		margin:            用于控制元素与元素之间的距离；margin的最基本用途就是控制元素周围空间的间隔，从视觉角度上达到相互隔开的目的。
		padding:           用于控制内容与边框之间的距离；   
		Border(边框):     围绕在内边距和内容外的边框。
		Content(内容):   盒子的内容，显示文本和图像。
		
		margin外边距
			.margin-test {
			  margin-top:5px;
			  margin-right:10px;
			  margin-bottom:15px;
			  margin-left:20px;
			}
			推荐使用简写：

			.margin-test {
			  margin: 5px 10px 15px 20px;
			}
			顺序：上右下左
			
			常见的居中方式:
			.mycenter {
			  margin: 0 auto;
			}
		
		padding内填充
			.padding-test {
			  padding-top: 5px;
			  padding-right: 10px;
			  padding-bottom: 15px;
			  padding-left: 20px;
			}
			推荐使用简写：

			.padding-test {
			  padding: 5px 10px 15px 20px;
			}
			顺序：上右下左

			补充padding的常用简写方式：

			提供一个，用于四边；
			提供两个，第一个用于上－下，第二个用于左－右；
			如果提供三个，第一个用于上，第二个用于左－右，第三个用于下；
			提供四个参数值，将按上－右－下－左的顺序作用于四边；
			
	float	
		在 CSS 中，任何元素都可以浮动。

		浮动元素会生成一个块级框，而不论它本身是何种元素。

		关于浮动的两个特点：

			浮动的框可以向左或向右移动，直到它的外边缘碰到包含框或另一个浮动框的边框为止。
			由于浮动框不在文档的普通流中，所以文档的普通流中的块框表现得就像浮动框不存在一样。
		
		三种取值
			left：向左浮动
			right：向右浮动
			none：默认值，不浮动
	clear
		清除浮动的副作用（父标签塌陷问题）
			ps:
				父标签塌陷问题: 
					浮动后的元素会脱离文档流,被浮动的元素会跑出父标签,从而破坏页面布局
					最简单的实例
						div设置边框为1,里面包两个p1和p2.p1浮动后.div会变成一条线
						而p1和p2 会被放置在 div 下面而不是div内部 ,即浮动后的元素跑出了父标签
		主要有三种方式：
			固定高度
				固定高度限制死了.如果后期有更多的浮动元素快超出了限定高度就无效了
			伪元素清除法
				只要子孙元素有浮动就给父标签设置这一属性即可,原理是浮动元素的下面添加空内容动态撑起父标签
			overflow:hidden
				将溢出的部分消除,会破坏子标签的显示,不推荐
			
			推荐伪元素清除法（使用较多）：
				.clearfix:after {		# 在元素的最下面插入一个内容
				  content: "";			# 内容为空
				  display: block;		# 展示为整个宽度(变成块级)
				  clear: both;			# 不允许浮动
				}
	overflow溢出属性 
		值	描述
			visible	默认值。内容不会被修剪，会呈现在元素框之外。
			hidden	内容会被修剪，并且其余内容是不可见的。
			scroll	内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
			auto	如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。
			inherit	规定应该从父元素继承 overflow 属性的值。
			 

			overflow（水平和垂直均设置）
			overflow-x（设置水平方向）
			overflow-y（设置垂直方向）
	定位（position）
		static		默认值 不定位
		relative	相对定位 相对于该元素的原始位置
		absolite	绝对定位 相对于父标签的定位,一层一层往上直到 body 
		fixed		固定,以窗口为参考点固定
	z-index
		#i2 {
			  z-index: 999;
			}
		设置对象的层叠顺序。

			z-index 值表示谁压着谁，数值大的压盖住数值小的，
			被定位后的元素，才可使用z-index,不管相对定位，绝对定位，固定定位，都可以使用z-index，而浮动元素不能使用z-index
				ps:position:relative 可以让元素定位而不变换位置.虽然没换位置,但是这个元素已经是被定位过的元素了.
			z-index值没有单位，就是一个正整数，
			默认的z-index值为0如果大家都没有z-index值，
			或者z-index值一样，那么谁写在HTML后面，谁在上面压着别人，
			定位了元素，永远压住没有定位的元素。
	
	opacity
		定义透明效果 0~1 
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			