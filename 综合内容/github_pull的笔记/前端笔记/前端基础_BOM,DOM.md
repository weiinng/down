```
﻿BOM
	浏览器对象模型，它使 JavaScript 有能力与浏览器进行“对话”。
	
DOM
	文档对象模型，通过它，可以访问HTML文档的所有元素。
	
window 对象
	

    window.innerHeight 	 - 浏览器窗口的内部高度
    window.innerWidth	 - 浏览器窗口的内部宽度
    window.open()		 - 打开新窗口
    window.close() 		 - 关闭当前窗口
    
    location.href  			获取URL
    location.href="URL" // 		跳转到指定页面
    location.reload() 		重新加载页面

DOM 对象
 	

    查找节点
    
    	直接查找
    		document.getElementById("")           根据ID获取一个标签
    		document.getElementsByClassName("")   根据class属性获取
    		document.getElementsByTagName("")     根据标签名获取标签合集
    	
    	间接查找(无括号)
    		A.parentElement            找父节点标签元素
    		A.children                 找所有子标签
    		A.firstElementChild        第一个子标签元素
    		A.lastElementChild         最后一个子标签元素
    		A.nextElementSibling       下一个兄弟标签元素
    		A.previousElementSibling   上一个兄弟标签元素
    
    操作节点
    
    	创建节点
    		document.createElement("B"); 	创建一个 B 标签
    	
    	添加节点
    		A.appendChild(B)				在 A 的里面作为 A 的最后一个子节点添加 B
    		A.insertBefore(B,C)				在 A 里面的子标签 C 前面添加 B
    	
    	节点属性操作
    		创建查看属性
    			自带的属性可以直接设置和取值
    				A.B = "C"			为 A 创建 B 属性,值为 C
    			自定义属性只能用
    				A.setAttribute("B", "C"); 	 A 节点添加 B 属性, B 属性值为 C
    				A.getAttribute("B"); 		 获取 A 标签的 B 属性值
    		删除属性(自定义,默认都可)
    			A.removeAttribute("B")			 移除 A 节点的 B 属性
    	
    	为节点添加内容	
    		A.innerText = "B"				给 A 节点设置显示内容为 B 
    			ps:
    			如果 A 有子标签.设置 A 内容后.会清除子标签只剩下一个文本 B
    			取值的时候只能取到子标签的内容
    		A.innerHtml = "<p>p</p>"			给 A 节点设置显示内容为 B 
    			ps:
    			主要用于快速添加简单的标签
    			取值的时候可以取到子标签本身不仅仅是内容
    	
    	删除节点
    		A.document.removeChild(B)	从 A 标签里面移除 B 标签
    	
    	替换阶段
    		A.replaceChild(B, C)		从 A 标签中将 C 标签替换成 B 标签
    		
    	获取值	(只适用于input,select,textarea)
    		A.value		获取A的值
    			
    	class 操作 
    		A.className  				获取所有样式类名(字符串)
    		A.classList.remove("c1")  	删除指定类
    		A.classList.add("c1")  		添加类
    		A.classList.contains("c1")	存在返回true，否则返回false
    		A.classList.toggle("c1")  	存在就删除，否则添加
    	
    	指定的 CSS类操作
    		A.style.backgroundColor="red"	将 A 的背景颜色设置成红色
    		JS操作CSS属性的规律：
    		1.对于没有中横线的CSS属性一般直接使用style.属性名即可。如：
    			obj.style.margin
    			obj.style.width
    			obj.style.left
    			obj.style.position
    		2.对含有中横线的CSS属性，将中横线后面的第一个字母换成大写即可。如：
    			obj.style.marginTop
    			obj.style.borderLeftWidth
    			obj.style.zIndex
    			obj.style.fontFamily
    	事件
    		HTML 事件用于触发浏览器中的动作
    		onclick        当用户点击某个对象时调用的事件句柄。
    		ondblclick     当用户双击某个对象时调用的事件句柄。
    
    		onfocus        元素获得焦点。              
    		onblur         元素失去焦点。               
    			应用场景：用于表单验证,用户离开某个输入框时,代表已经输入完了,我们可以对它进行验证.
    		onchange       域的内容被改变。             
    			应用场景：通常用于表单元素,当元素内容被改变时触发.（select联动）
    	
    		onkeydown      某个键盘按键被按下。          
    			应用场景: 当用户在最后一个输入框按下回车按键时,表单提交.
    		onkeypress     某个键盘按键被按下并松开。
    		onkeyup        某个键盘按键被松开。
    		onload         一张页面或一幅图像完成加载。
    		onmousedown    鼠标按钮被按下。
    		onmousemove    鼠标被移动。
    		onmouseout     鼠标从某元素移开。
    		onmouseover    鼠标移到某元素之上。
    
    		onselect      在文本框中的文本被选中时发生。
    		onsubmit      确认按钮被点击，使用的对象是form。
    		
    		事件绑定方式
    			定义标签内
    				<div id="d1" onclick="changeColor(this);">点我</div>
    				<script>
    				  function changeColor(ths) {
    					ths.style.backgroundColor="green";
    				  }
    				</script>
    			
    			注意：
    				this是实参，表示触发事件的当前元素。
    				函数定义过程中的ths为形参。
    			定义在标签外	
    				<div id="d2">点我</div>
    				<script>
    				  var divEle2 = document.getElementById("d2");
    				  divEle2.onclick=function () {
    					this.innerText="呵呵";
    				  }
    				</script>
    		
    		window.onload
    			绑定事件的时候，要等到文档加载完毕。
    			对于不存在的元素无法绑定事件。
    			window.onload事件在文件加载过程结束时触发。
    			位于DOM中的所有对象都被读取完毕时才会触发
    			注意：.onload()函数存在覆盖现象。

		

```

