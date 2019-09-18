<div id="a">
	{{m}}
	<button @click='change'>µã»÷·´×ª</button>
</div>
<script type="text/javascript">
	export default{
	name:"a",
	data:function(){
	return{
		m:"asd"
	},
	methods:{
	change:function(){
	this.m=this.m.split("").reverse().join("")
	}
	}
}
}
</script>