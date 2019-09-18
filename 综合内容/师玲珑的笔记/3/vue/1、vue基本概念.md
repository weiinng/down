Vue.js基本概念：
首先通过将vue.js作为一个js库来使用，来学习vue的一些基本概念，我们下载了vue.js后，需要在页面上通过script标签引入vue.js。开发中可以使用开发版本vue.js。产品上线要换成vue.min.js。

<script type="text/javascript" src="../static/js/vue.js"></script>
Vue实例

每个Vue应用都是通过实例化一个新的Vue对象开始的：

<div id="app">
	{{message}}
	<button @click='change'>改变message的值</button>
</div>

window.onload=function(){
	#vm这个变量名不能用-，可以用下划线，比如vm-data不行，vm_data可以
	var vm= new Vue({
	el:"#app",
	data:{message:'hello world!'},
	methods:{
		change:function(){
			this.message='hello python'
		}	
	}
	})
}
...


<div id="vue_det">
	<h1>site:{{site}}</h1>
	<h1>url:{{url}}</h1>
	<h1>{{details()}}</h1>
</div>
<script type="text/javascript">
	var vm=new Vue({
	el:"#vue_det",
	data:{site:"积云教育",url:'www.runoob.com'},
	methods:{
		details:function(){
		return this.site+"-学的不仅是技术，更是梦想！"
	}
	}
})
</script>	


