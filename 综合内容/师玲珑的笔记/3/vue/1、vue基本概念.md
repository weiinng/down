Vue.js�������
����ͨ����vue.js��Ϊһ��js����ʹ�ã���ѧϰvue��һЩ�����������������vue.js����Ҫ��ҳ����ͨ��script��ǩ����vue.js�������п���ʹ�ÿ����汾vue.js����Ʒ����Ҫ����vue.min.js��

<script type="text/javascript" src="../static/js/vue.js"></script>
Vueʵ��

ÿ��VueӦ�ö���ͨ��ʵ����һ���µ�Vue����ʼ�ģ�

<div id="app">
	{{message}}
	<button @click='change'>�ı�message��ֵ</button>
</div>

window.onload=function(){
	#vm���������������-���������»��ߣ�����vm-data���У�vm_data����
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
	data:{site:"���ƽ���",url:'www.runoob.com'},
	methods:{
		details:function(){
		return this.site+"-ѧ�Ĳ����Ǽ������������룡"
	}
	}
})
</script>	


