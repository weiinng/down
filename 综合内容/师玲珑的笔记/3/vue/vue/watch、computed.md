<template>
	<div id="a">
		{{m}}
		<button @click='change'>�����ת</button>
		<br>
		{{mm}}
		<div v-bind:id="k">
			��Ƶ����˴����		
		</div>
	</div>
</template>
<script type="text/javascript">
	export default{
		name:"a",
		data:function(){
			return{
				m:'������ְ�Ŷ',k:"k"
			}
		},
		methods:{
			change:function(){
				this.m=this.m.split("").reverse().join("")
			}
		},
		computed:{
			mm:function(){
				return '������ְ�'
			}
		},
		watch:{
			m:function(nvalue,ovalue){
				alert("�µ�ֵ��"+nvalue+"�ɵ�ֵ��"+ovalue)
			}
		}
	}
</script>
<style type="text/css">
	#k{
		width: 200px;
		height: 200px;
		margin: 0 auto;
	}
</style>