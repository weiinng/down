jQuery
	
	概念:	
		轻量级的多兼容的JavaScript库
	
	优势		
		文件小		核心文件小
		代码少		功能实现所需代码少
		简洁		链式操作间接
		可读性强	相比起来js
		多兼容		多浏览器兼容
		插件多		插件丰富,可以实现更多炫酷的操作	

	基础语法		
		$(selector).action()
	
	查找标签	
		选择器		
			基本选择器:
				
				id选择器：			$("#id")		
				标签选择器：		$("tagName")		
				class选择器：		$(".className")	
					配合使用：		$("div.c1")  // 找到有c1 class类的div标签
				所有元素选择器：	$("*")
				组合选择器：		$("#id, .className, tagName")
			
			层级选择器			
				$("x y");// x的所有后代y（子子孙孙）
				$("x > y");// x的所有儿子y（儿子）
				$("x + y")// 找到所有紧挨在x后面的y
				$("x ~ y")// x之后所有的兄弟y
		
		筛选器		
			基本筛选器:		
				:first // 第一个
				:last // 最后一个
				:eq(index)// 索引等于index的那个元素
				:even // 匹配所有索引值为偶数的元素，从 0 开始计数
				:odd // 匹配所有索引值为奇数的元素，从 0 开始计数
				:gt(index)// 匹配所有大于给定索引值的元素
				:lt(index)// 匹配所有小于给定索引值的元素
				:not(元素选择器)// 移除所有满足not条件的标签
				:has(元素选择器)// 选取所有包含一个或多个标签在其内的标签(指的是从后代元素找)
				
				例子:				
					$("div:has(h1)")// 找到所有后代中有h1标签的div标签
					$("div:has(.c1)")// 找到所有后代中有c1样式类的div标签
					$("li:not(.c1)")// 找到所有不包含c1样式类的li标签
					$("li:not(:has(a))")// 找到所有后代中不含a标签的li标签
			
			属性选择器：			
				[attribute]
				[attribute=value]// 属性等于
				[attribute!=value]// 属性不等于
				
				例子:
					$("input[type='checkbox']");// 取到checkbox类型的input标签
					$("input[type!='text']");// 取到类型不是text的input标签
			
			表单筛选器			
				:text
				:password
				:file
				:radio
				:checkbox

				:submit
				:reset
				:button	
				
			表单对象属性:			
				:enabled
				:disabled
				:checked
				:selected
				
				例子:
					$("input:enabled")  // 找到可用的input标签		
			
		筛选器方法:
		
			下一个元素：				
				$("#id").next()
				$("#id").nextAll()
				$("#id").nextUntil("#i2")
			
			上一个元素：				
				$("#id").prev()
				$("#id").prevAll()
				$("#id").prevUntil("#i2")
			
			父亲元素：				
				$("#id").parent()
				$("#id").parents()  	// 查找当前元素的所有的父辈元素
				$("#id").parentsUntil() // 查找当前元素的所有的父辈元素，直到遇到匹配的那个元素为止。
			
			儿子和兄弟元素：				
				$("#id").children();// 儿子们
				$("#id").siblings();// 兄弟们
			
			查找				
				搜索所有与指定表达式匹配的元素。
				此函数是找出正在处理的元素的后代元素的好方法。
					
					$("div").find("p")
					等价于$("div p")
			
			筛选				
				筛选出与指定表达式匹配的元素集合。
				这个方法用于缩小匹配的范围。用逗号分隔多个表达式。
					
					$("div").filter(".c1")  // 从结果集中过滤出有c1样式类的
					等价于 $("div.c1")
			
			补充：				
				.first() 	// 获取匹配的第一个元素
				.last()	 	// 获取匹配的最后一个元素
				.not() 		// 从匹配元素的集合中删除与指定表达式匹配的元素
				.has() 		// 保留包含特定后代的元素，去掉那些不含有指定后代的元素。
				.eq() 		// 索引值等于指定值的元素
							
	操作标签
		样式操作
			样式类
				addClass();			// 添加指定的CSS类名。
				removeClass();		// 移除指定的CSS类名。
				hasClass();			// 判断样式存不存在
				toggleClass();		// 切换CSS类名，如果有就移除，如果没有就添加。
				
				栗子：
					开关灯(点击标签更换颜色属性)
					模态框

			CSS
				css("color","red")	//DOM操作：tag.style.color="red"
				
				栗子：
					$("p").css("color", "red"); //将所有p标签的字体设置为红色
			
		位置操作
			offset()		// 获取匹配元素在当前窗口的相对偏移或设置元素位置
			position()		// 获取匹配元素相对父元素的偏移
			scrollTop()		// 获取匹配元素相对滚动条顶部的偏移
			scrollLeft()	// 获取匹配元素相对滚动条左侧的偏移
			
			.offset()方法允许我们检索一个元素相对于文档（document）的当前位置。

			和 .position()的差别在于： 
				.position()是相对于相对于父级元素的位移。

			栗子：
				返回顶部栗子
		
		尺寸：
			height()
			width()
			innerHeight()
			innerWidth()
			outerHeight()
			outerWidth()

		文本操作:
			HTML代码：
				html()		// 取得第一个匹配元素的html内容
				html(val)	// 设置所有匹配元素的html内容

			文本值：
				text()		// 取得所有匹配元素的内容
				text(val)	// 设置所有匹配元素的内容

			值：
				val()				// 取得第一个匹配元素的当前值
				val(val)			// 设置所有匹配元素的值
				val([val1, val2])	// 设置多选的checkbox、多选select的值

			栗子:	
				栗子1:
					<input type="checkbox" value="basketball" name="hobby">篮球
					<input type="checkbox" value="football" name="hobby">足球
					<select multiple id="s1">
						<option value="1">1</option>
						<option value="2">2</option>
						<option value="3">3</option>
					</select>
					$("[name='hobby']").val(['basketball', 'football']);
					$("#s1").val(["1", "2"])
				栗子2：
					<label for="c1">女</label>
					<input name="gender" id="c1" type="radio" value="0">
					<label for="c2">男</label>
					<input name="gender" id="c2" type="radio" value="1">
					可以使用：
						$("input[name='gender']:checked").val()
				栗子3:
					自定义登录校验栗子
		
		属性操作:
			用于ID等或自定义属性：
				attr(attrName)				// 返回第一个匹配元素的属性值
				attr(attrName, attrValue)	// 为所有匹配元素设置一个属性值
				attr({k1: v1, k2:v2})		// 为所有匹配元素设置多个属性值
				removeAttr()				// 从每一个匹配的元素中删除一个属性

			用于checkbox和radio
				prop() 			// 获取属性
				removeProp() 	// 移除属性

			注意：
				在1.x及2.x版本的jQuery中使用attr对checkbox进行赋值操作时会出bug，
				在3.x版本的jQuery中则没有这个问题。
				为了兼容性，我们在处理checkbox和radio的时候尽量使用特定的prop()，
				不要使用attr("checked", "checked")。
					
					<input type="checkbox" value="1">
					<input type="radio" value="2">
					<script>
					  $(":checkbox[value='1']").prop("checked", true);
					  $(":radio[value='2']").prop("checked", true);
					</script>

			prop和attr的区别：
				attr全称attribute(属性) 
				prop全称property(属性)
				虽然都是属性，但他们所指的属性并不相同，
					attr所指的属性是HTML标签属性，
					prop所指的是DOM对象属性，
				可以认为
					attr是显式的，
					而prop是隐式的。
			栗子集合:
				举个栗子：
					<input type="checkbox" id="i1" value="1">
					$("#i1").attr("checked")  	// undefined
					$("#i1").prop("checked")  	// false
					可以看到attr获取一个标签内没有的东西会得到undefined，
					而prop获取的是这个DOM对象的属性，因此checked为false。

				换个栗子：
					<input type="checkbox" checked id="i1" value="1">
					$("#i1").attr("checked")    // checked
					$("#i1").prop("checked")  	// true
					可以看出attr的局限性，attr只限于HTML标签内的属性
					而prop获取的是这个DOM对象的属性，选中返回true，没选中返回false。

				再换个栗子：
					<input type="checkbox" checked id="i1" value="1" me="自定义属性">
					$("#i1").attr("me")   // "自定义属性"
					$("#i1").prop("me")  // undefined
					可以看到prop不支持获取标签的自定义属性。

			总结一下：
				对于标签上有的能看到的属性和自定义属性都用attr
				对于返回布尔值的比如checkbox、radio和option的是否被选中都用prop。
			实际操作:
				全选,反选,全部取消

		文档处理
			添加到指定元素内部的后面
				$(A).append(B)		// 把B追加到A
				$(A).appendTo(B)	// 把A追加到B
			
			添加到指定元素内部的前面
				$(A).prepend(B)		// 把B前置到A
				$(A).prependTo(B)	// 把A前置到B
			
			添加到指定元素外部的后面
				$(A).after(B)		// 把B放到A的后面
				$(A).insertAfter(B)	// 把A放到B的后面
			
			添加到指定元素外部的前面
				$(A).before(B)		// 把B放到A的前面
				$(A).insertBefore(B)// 把A放到B的前面
			
			移除和清空元素
				remove()			// 从DOM中删除所有匹配的元素。
				empty()				// 删除匹配的元素集合中所有的子节点。
				
				例子：
					点击按钮在表格添加一行数据。
					点击每一行的删除按钮删除当前行数据。

			替换
				replaceWith()
				replaceAll()
			
			克隆
				clone()// 参数
			
			克隆栗子：
	
	事件
		常用事件
			click(function(){...})
			hover(function(){...})
			blur(function(){...})
			focus(function(){...})
			change(function(){...})
			keyup(function(){...})
			
			栗子集:
				栗子1:
					keydown和keyup事件组合按住shift实现批量操作
				栗子2:
					hover事件
				栗子3:	
					实时监听input输入值变化栗子：
	
		事件绑定
			基本框架:
				.on/off( events [, selector ],function(){})
				
				参数:
					on/off: 绑定/移除事件
					events： 事件
					selector: 选择器（可选的）
					function: 事件处理函数
			
				注意:
					hover 这种jQuery中定义的事件就无法用 .on() 方法绑定
					可用这种方式:
						$('ul').on('mouseenter', 'li', function() {//绑定鼠标进入事件
							$(this).addClass('hover');
						});
						$('ul').on('mouseleave', 'li', function() {//绑定鼠标划出事件
							$(this).removeClass('hover');
						});
						
			阻止后续事件的执行	
				return false; 			// 常见阻止表单提交等
				e.preventDefault();
				
				栗子:	
					<script>
						$("#b1").click(function (e) {
							alert(123);
							//return false;
							e.preventDefault();
						});
					</script>
		
			页面载入
				当DOM载入就绪可以查询及操纵时绑定一个要执行的函数。
				这是事件模块中最重要的一个函数，因为它可以极大地提高web应用程序的响应速度。

				两种写法：
					$(document).ready(function(){
					// 在这里写你的JS代码...
					})
				简写：
					$(function(){
					// 你在这里写你的代码
					})
				
				与window.onload的区别
					window.onload()函数有覆盖现象，必须等待着图片资源加载完成之后才能调用
					jQuery的这个入口函数无函数覆盖现象，文档加载完成之后就可以调用（建议使用此函数）
				
				栗子:
					登录检验
			
			事件委托
				事件委托是通过事件冒泡的原理，利用父标签去捕获子标签的事件。

				栗子：
					表格中每一行的编辑和删除按钮都能触发相应的事件。

					$("table").on("click", ".delete", function () {
					  // 删除按钮绑定的事件
					})
			
			动画效果
				基本
					show([s,[e],[fn]])
					hide([s,[e],[fn]])
					toggle([s],[e],[fn])
				滑动
					slideDown([s],[e],[fn])
					slideUp([s,[e],[fn]])
					slideToggle([s],[e],[fn])
				淡入淡出
					fadeIn([s],[e],[fn])
					fadeOut([s],[e],[fn])
					fadeTo([[s],o,[e],[fn]])
					fadeToggle([s,[e],[fn]])
				自定义（了解即可）
					animate(p,[s],[e],[fn])
			
				栗子:
					自定义动画
			
	补充
		each
			jQuery.each(collection, callback(indexInArray, valueOfElement))：
				描述：
					一个通用的迭代函数，它可以用来无缝迭代对象和数组。
					数组和类似数组的对象通过一个长度属性（如一个函数的参数对象）来迭代数字索引，
					从0到length - 1。其他对象通过其属性名进行迭代。
				
				栗子:
					li =[10,20,30,40]
					$.each(li,function(i, v){
					  console.log(i, v);		//index是索引，ele是每次循环的具体元素。
					})
				输出：
					010
					120
					230
					340
			
			.each(function(index, Element))：
				描述：
					遍历一个jQuery对象，为每个匹配元素执行一个函数。
					.each() 方法用来迭代jQuery对象中的每一个DOM元素。
					每次回调函数执行时，会传递当前循环次数作为参数(从0开始计数)。
					由于回调函数是在当前DOM元素为上下文的语境中触发的，
					所以关键字 this 总是指向这个元素。
				栗子:
					// 为每一个li标签添加foo
					$("li").each(function(){
					  $(this).addClass("c1");
					});
				注意: 
					jQuery的方法返回一个jQuery对象，
					遍历jQuery集合中的元素 - 被称为隐式迭代的过程。
					当这种情况发生时，它通常不需要显式地循环的 .each()方法：
				也就是说，上面的例子没有必要使用each()方法，直接像下面这样写就可以了：
				$("li").addClass("c1");  // 对所有标签做统一操作
				注意：
					在遍历过程中可以使用 return false提前结束each循环。

		.data()
			
			$(selector).data(name)			//从元素返回数据
			$(selector).data(name,value)	//向元素附加数据
			
			栗子:
				$("#btn1").click(function(){
				  $("div").data("greeting", "Hello World");
				});
				$("#btn2").click(function(){
				  alert($("div").data("greeting"));
				});

			.removeData(key):
				移除存放在元素上的数据，不加key参数表示移除所有保存的数据。
			栗子:
			$("div").removeData("k");  //移除元素上存放k对应的数据

			
			
			
			
			
	