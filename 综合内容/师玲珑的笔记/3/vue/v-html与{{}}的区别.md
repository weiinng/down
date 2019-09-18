当赋值的内容不含有标签时两个无区别
当有标签的时候{{}}不能解析标签
就要用v-html

<div v-html='m'></div>    结果是一个空行
<div id="a">{{m}}</div>	结果是<p></p>
<button @click='c'>ss</button>

<script type="text/javascript">
window.onload=function(){
	var v=new Vue({
	el:"#a",
	data:{m:'<p></p>'}
	methods:{
	c:function(){
	this.m='asd'
}		
}
})

</script>


