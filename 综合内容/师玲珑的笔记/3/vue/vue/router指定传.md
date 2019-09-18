<template>
	<div id="aa">
		<div v-bind:class="'a'|add">
			一二三四五 
		</div>
		<div v-bind:class="'b'|add">
			<router-link :to="{'name':'f1one',params:{'n':n}}">
			上山打老虎
			</router-link>
			<router-link :to="{'name':'AddMes',params:{'m':'我是中国人'}}">点击跳转栓</router-link>
			{{n}}
		</div>
	</div>
</template>
<script type="text/javascript">
	export default{
		name:"aa",
		data:function(){
			return{
				n:"asdsad"
			}
		},
		filters:{
			add:function(s){
				return s+' bg'
			}
		}
	}
</script>
<style type="text/css">
	.a{
		color:pink;
	}
	.b{
		color: yellow;
	}
	.bg{
		background-color: blue;
	}
</style>

在f1one.vue里：
<template>
	<div id="a">
		{{$route.params.n}}
		{{$route.params.m}}
	</div>
</template>
<script type="text/javascript">
	export default{
		name:"a"
	}
</script>

要在index.js 内配路径  要在传的vue里路径写你要传的
如下
 {
      path: '/f1one/:n/:m',
      name: 'f1one',
      component: f1one
    }