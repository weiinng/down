<template>
	<div id="a">
		{{m}}
		<button @click='change'>点击反转</button>
		<br>
		{{mm}}
		<div v-bind:id="k">
			设计的萨克大多数		
		</div>
	</div>
</template>
<script type="text/javascript">
	export default{
		name:"a",
		data:function(){
			return{
				m:'我是你爸爸哦',k:"k"
			}
		},
		methods:{
			change:function(){
				this.m=this.m.split("").reverse().join("")
			}
		},
		computed:{
			mm:function(){
				return '我是你爸爸'
			}
		},
		watch:{
			m:function(nvalue,ovalue){
				alert("新的值是"+nvalue+"旧的值是"+ovalue)
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