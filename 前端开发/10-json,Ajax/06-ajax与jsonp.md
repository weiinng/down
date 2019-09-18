### ajax与jsonp

ajax技术的目的是让javascript发送http请求，与后台通信，获取数据和信息，ajax技术的原理是实例化xmlhtt对象，使用此对象与后台通信，ajax通信的过程不会受影响后续javascript的执行，从而实现异步。

ajax本身可以发送http请求，就不用通过地址栏，绕过地址栏，直接把数据放在页面上，就可以达到局部刷新和无刷新的效果。

javascript 是不可以操作文件的。python可以操作文件，对文件进行读写，删除。

后台语言可以修改文件，比如java,python,php,因为他们是运行在服务器上面的，不会轻易被访问到，而javascript是运行在客户机上面的。

ajax可以读文件让JavaScript发送后台请求，数据和信息，

#### 同步和异步

现实生活中，同步指的是同时间做几件事情，异步指的是做完一件事后在做另一件事情，程序中的同步和异步就是把现实生活中的概念对调，也就是程序中的异步指的是现实生活中的同步，程序中的同步指的是现实生活中的异步。

- 程序中的同步就是先做一件事情然后在做另一件事情。
- 程序中的异步就是同时做几件事情。程序中的异步比同步好。

#### 局部刷新和无刷新

ajax可以实现局部刷新，也就是无状态刷新，无刷新值的是整个页面不刷新，只是局部刷新，ajax可以自己发送http请求，不通过浏览器的地址栏，所以页面整体不会刷新，ajax获取到后台数据，更新页面显示数据的部分，就做到了页面局部刷新。

- ajax局部刷新可以绕过http请求，

#### 同源策略

ajax请求的页面或资源只能是同一个域下面的资源，不能是其他域的资源，这个在这设计ajax时基于安全考虑。

**特征报错提示：**

```
XMLHttpResponse cannot load https://www.baidu.com/. No
'Access - Control - Allow - Origin'
header is present on the requested resourece.
Origin 'null' is therefore not allowed access.
```



#### $.ajax使用方法

1. url 请求地址
2. type  请求方式默认是是"GET",常用的还有"POST"
3. data Type 设置返回的数据格式，常用的是'json'，也可以设置为'html'
4. data 设置发送给服务器的数据
5. success 设置请求成功后的回调函数
6. error 设置请求失败后的回调函数
7. async 设置是否异步，默认为"true"，表示异步

```javascript
$.ajax({
    url:'js/data.json',         //请求的地址
    type:'GET',                 //请求方式
    dataType:'json',             //返回数据的数据格式
    data:{"a":1}           //传递的数据
    suyccess:function(data){               //回调函数
    	alert(data.name);                   
	}，
    error:function(){
    	alert('服务器超时，请重试！')；	
}
})
```

**新的写法（推荐）：**

```javascript
$.ajax({
				type:"GET",
				url:"js/data.json",
				async:true,    //表示异步
				dataType:'josn',
				data{
					'aa':1,
					
				}
			})
			.done(function(data){   //成功所执行的事情
				alert(data.name);
				
			})
			.fail(function(){      //失败所执行的事情
				alert('服务器超时，请重试！！')
			});
			
			//data.json里面的数据{'name':'tom','age':18}
```







