����ֵ�����ݲ����б�ǩʱ����������
���б�ǩ��ʱ��{{}}���ܽ�����ǩ
��Ҫ��v-html

<div v-html='m'></div>    �����һ������
<div id="a">{{m}}</div>	�����<p></p>
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


