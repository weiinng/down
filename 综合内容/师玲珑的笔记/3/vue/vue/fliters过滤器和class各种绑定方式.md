<template>
	<div id="a">
		{{mes|add}}
		{{mess|add}}
		<div :class="'bg'|addcolor">
			������ְ�
		</div>
		<div :class="'ag'|addcolor">
			������ְ�2
		</div>
		<div :class="as">
			������ְ�3
		</div>
		<div :class="{'q':aa,'w':aaa}">
			������ְ�22
		</div>
		
	</div>
</template>
<script type="text/javascript">
	export default{
		name:"a",
		data:function(){
			return{
				mes:'asdsa',
				mess:'zxc',
				as:"as",
				aa:true,
				aaa:false
			}
		},
		filters:{
			add:function(v){
				return v+"$"
			},
			addcolor:function(s){
				return s+" hh"
			}
		}
	}
</script>
<style type="text/css">
	.hh{
		background-color: pink;
	}
	.bg{
		color: orange
	}
	.ag{
		color: red;
	}
	.as{
		font-size: 20px;
	}
	.q{
		background-color: orange
	}
	.w{
		font-size: 20px;
	}
</style>