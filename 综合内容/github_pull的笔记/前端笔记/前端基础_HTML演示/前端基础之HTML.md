HTML 笔记整理总结

	概念：
		超文本标记语言，是一种用于创建网页的标记语言。
			ps： 不是编程语言
		利用标签来描述网页
		扩展名：.html .htm
	
	文档结构：
		<!DOCTYPE html>
		<html lang="zh-CN">
		<head>
		  <meta charset="UTF-8">
		  <title>css样式优先级</title>
		</head>
		<body>

		</body>
		</html>
		
		<!DOCTYPE html>	声明为HTML5文档。
		<html></html>	是文档的开始标记和结束的标记。是HTML页面的根元素，在它们之间是文档的头部(head)和主体(body)。
		<head></head>	定义了HTML文档的开头部分。它们之间的内容不会在浏览器的文档窗口显示。包含了文档的元(meta)数据。
		<title></title>	定义了网页标题，在浏览器标题栏显示。
		<body></body>	之间的文本是可见的网页主体内容。
	
	head 内的常用标签
			<title></title>		定义网页标题
			<style></style>		定义内部样式表
			<script></script>	定义JS代码或引入外部JS文件
			<link/>				引入外部样式表文件
			<meta/>				定义网页原信息
	
	body内常用标签		
		
		基本标签(内联标签)
			内联标签不需要另一起一行，以文本大小为定义大小
				<b>加粗</b>
				<i>斜体</i>
				<u>下划线</u>
				<s>删除</s>
				<p>段落标签</p>
				<h1>标题1</h1>
				<h2>标题2</h2>
				<h3>标题3</h3>
				<h4>标题4</h4>
				<h5>标题5</h5>
				<h6>标题6</h6>
				<!--换行--><br>
				<!--水平线--><hr>
		
		基本标签(块级标签)
			块级标签需要另起一行，以一行为定义大小，主要是为了定义css样式用的
				<div></div>
				<span></span>
				<p></p>
			ps：p标签是个特异点，不可以嵌套其他块级标签，嵌套p标签也不行
		
		特殊标签
			
			图片标签
				<img 
				src="图片的路径" 
				alt="图片未加载成功时的提示" 
				title="鼠标悬浮时提示信息" 
				width="宽" 
				height="高">
				ps：宽高两个属性只用一个会自动等比缩放
			
			超链接标签
				<a href="跳转路径" target="跳转后打开方式" >点我</a>
				属性详细:
					href 属性指定目标网页地址。该地址可以有几种类型：
						绝对URL - 指向另一个站点(比如 href="http://www.jd.com)
						相对URL - 指当前站点中确切的路径(href="index.htm")
						锚URL - 指向页面中的锚(href="#top") 
					target：
						_blank表示在新标签页中打开目标网页
						_self表示在当前标签页中打开目标网页(默认为此方式)
			
			列表
				无序:
					<ul type="disc">
					  <li>第一项</li>
					  <li>第二项</li>
					</ul>
					
					type属性：
						disc	实心圆点(默认值)
						circle	空心圆圈
						square	实心方块
						none	无样式
				有序:
					<ol type="1" start="2">
					  <li>第一项</li>
					  <li>第二项</li>
					</ol>
					
					type属性：
						1 	数字列表(默认值)
						A 	大写字母
						a 	小写字母
						Ⅰ	大写罗马
						ⅰ	小写罗马
							
				标题列表:
					<dl>
					  <dt>标题1</dt>
					  <dd>内容1</dd>
					  <dt>标题2</dt>
					  <dd>内容1</dd>
					  <dd>内容2</dd>
					</dl>
				
			表格:
				<table>
				  <thead>
				  <tr>
					<th>序号</th>
					<th>姓名</th>
					<th>爱好</th>
				  </tr>
				  </thead>
				  <tbody>
				  <tr>
					<td>1</td>
					<td>Egon</td>
					<td>杠娘</td>
				  </tr>
				  <tr>
					<td>2</td>
					<td>Yuan</td>
					<td>日天</td>
				  </tr>
				  </tbody>
				</table>
				
				属性:		
					border: 		表格边框.
					cellpadding: 	内边距
					cellspacing: 	外边距.
					width: 			像素 百分比.（最好通过css来设置长宽）
					rowspan: 		单元格竖跨多少行
					colspan: 		单元格横跨多少列（即合并单元格）
					
			form 表单:
				
				表单用于向服务器传输数据，从而实现用户与Web服务器的交互
				
				表单属性:
				
					accept-charset	规定在被提交表单中使用的字符集（默认：页面字符集）。
					action			规定向何处提交表单的地址（URL）（提交页面）。
					autocomplete	规定浏览器应该自动完成表单（默认：开启）。
					enctype			规定被提交数据的编码（默认：url-encoded）。
					method			规定在提交表单时所用的 HTTP 方法（默认：GET）。
					name			规定识别表单的名称（对于 DOM 使用：document.forms.name）。
					novalidate		规定浏览器不验证表单,(L浏览器会自带一个验证功能)
					target			规定 action 属性中地址的目标（默认：_self）。
				
				input系列标签:
				
					text		单行输入文本	<input type=text" />
					password	密码输入框		<input type="password"  />
					date		日期输入框		<input type="date" />
					checkbox	复选框			<input type="checkbox" checked="checked"  />
					radio		单选框			<input type="radio"  />
					submit		提交按钮		<input type="submit" value="提交" />
					reset		重置按钮		<input type="reset" value="重置"  />
					button		普通按钮		<input type="button" value="普通按钮"  />
					hidden		隐藏输入框		<input type="hidden"  />
					file		文本选择框		<input type="file"  />
					
					属性说明:
						name：	表单提交时的“键”,目的为提交后端的数据标识符(注意和id的区别)
						value：	表单提交时对应项的值
							type="button", "reset", "submit"时，为按钮上显示的文本内容
							type="text","password","hidden"时，为输入框的初始值
							type="checkbox", "radio", "file"，为输入相关联的值
						checked：radio和checkbox默认被选中的项
						readonly：text和password设置只读
						disabled：禁用,所有input均适用
					
				select 标签
				
						<form action="" method="post">
							<select name="city" id="city">
								<option value="1">北京</option>
								<option selected="selected" value="2">上海</option>
								<option value="3">广州</option>
								<option value="4">深圳</option>
							</select>
						</form>
						
						属性说明：
							multiple：布尔属性，设置后为多选，否则默认单选
							disabled：禁用
							selected：默认选中该项
							value：定义提交时的选项值
				
				label标签	
					
					label 元素不会向用户呈现任何特殊效果。
					
					<form action="">
						<label for="username">用户名</label>
						<input type="text" id="username" name="username">
					</form>
					
					<label> 标签的 for 属性值应当与相关元素的 id 属性值相同。
					可实现点击label标签的时候自动跳转到 for所指定的的标签.实现相同的点击效果
				
				textarea多行文本
					
					<textarea name="memo" id="memo" cols="30" rows="10">
						默认内容
					</textarea>
					
					属性说明：
					
						name：名称
						rows：行数
						cols：列数
						disabled：禁用
					
					
					
					
					