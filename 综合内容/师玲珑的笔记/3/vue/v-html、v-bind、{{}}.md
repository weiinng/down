���õ���������ʱ�����Ǹ�div�������һ�����div���棡������������

v-html:

<div id="a">
	<div v-html="m"></div>
</div>
�����渳ֵʱ�͸�m��ֵ���Ǹ�div������ݣ�
<script type="text/javascript">
	window.onload=function(){
	var v=new Vue({
	el:"#a",
	data:{m:"lalala"}
})
}
</script>


v-bind:
<style>
	.a{background-color:red;}
</style>


<div id="#a">
	<div v-bind:class="a">          //�����class��css���ͣ���ȻҲ������id,�����Ǹ�a��ʵ���Ǹ��βΣ�����ȡ�������֣��͸�{{m}}�������mһ����Ҫ��vue���data���������ֵ��Ȼ��Ϳ�����cssѡ��������ҳ��һЩ������
		lalalala
	</div>
</div>

<script type="text/javascript">
	window.onload=function(){
	var v=new Vue({
	el:"#a",
	date:{a:"aa"}
})
}
</script>








