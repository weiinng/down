<!-- <template>
	<div id="a">
		{{m1|s}}
		{{m2|s}}
	</div>
</template>
<script type="text/javascript">
	import main from '../../static/main'
	alert(main.person.getname())
	export default{
		name:"a",
		data:function(){
			return{
				m1:10,
				m2:20
			}
		},
		filters:{
			s:function(v){
				return "$"+v+"元"
			}
		}
	}
</script> -->











<!-- <template>
	<div id="a">
		<router-link to="docx2">点击跳转到反转</router-link>
		<router-link to="docx2form">点击跳转到表单</router-link>
	</div>
</template>
<script type="text/javascript">
	export default{
		name:"a",
	}
</script> -->

<!-- <template>
	<div id="helloworld">
		{{mes}}
		{{mes1}}
		<button @click='reverse'>反转</button>
		<div v-html="m"></div>
		<div v-bind:class='n'>去问于i圣诞节说的那句</div>
		<button @click='change'>点击变颜色</button>
		<router-link to="/computed1">计算属性</router-link>
		<router-link to="watch">监听属性</router-link>
		<br>
		<div v-bind:class="{'bgcolor':a,'fontsize':b}">
			请问饿啊收到的那时快
		</div>
		<button @click='w'>点击</button>
	</div>
</template>
<script type="text/javascript">
	export default{
		name:"helloworld",
		data:function(){
			return{
				mes:"这是一个测试",
				mes1:"asdfgh",
				m:"<ul><li>1</li><li>2</li></ul>",
				n:"t1",
				b:true,
				a:false
			}
		},
		methods:{
			reverse:function(){
				this.mes=this.mes.split("").reverse().join("")
			},
			change:function(){
				this.n="t2"
			},
			w:function(){
				this.a=true
			}
		}
	}
</script>
<style type="text/css">
	.t1{
		background-color: yellow;
	}
	.t2{
		background-color: red;
	}
	ul{
		list-style: square;
	}
	.bgcolor{
		background-color: gray;
	}
	.fontsize{
		font-size: 20px;
	}
</style> -->