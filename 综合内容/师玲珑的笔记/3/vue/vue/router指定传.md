<template>
	<div id="aa">
		<div v-bind:class="'a'|add">
			һ�������� 
		</div>
		<div v-bind:class="'b'|add">
			<router-link :to="{'name':'f1one',params:{'n':n}}">
			��ɽ���ϻ�
			</router-link>
			<router-link :to="{'name':'AddMes',params:{'m':'�����й���'}}">�����ת˨</router-link>
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

��f1one.vue�
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

Ҫ��index.js ����·��  Ҫ�ڴ���vue��·��д��Ҫ����
����
 {
      path: '/f1one/:n/:m',
      name: 'f1one',
      component: f1one
    }