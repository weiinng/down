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
				return "$"+v+"Ԫ"
			}
		}
	}
</script> -->











<!-- <template>
	<div id="a">
		<router-link to="docx2">�����ת����ת</router-link>
		<router-link to="docx2form">�����ת����</router-link>
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
		<button @click='reverse'>��ת</button>
		<div v-html="m"></div>
		<div v-bind:class='n'>ȥ����iʥ����˵���Ǿ�</div>
		<button @click='change'>�������ɫ</button>
		<router-link to="/computed1">��������</router-link>
		<router-link to="watch">��������</router-link>
		<br>
		<div v-bind:class="{'bgcolor':a,'fontsize':b}">
			���ʶ����յ�����ʱ��
		</div>
		<button @click='w'>���</button>
	</div>
</template>
<script type="text/javascript">
	export default{
		name:"helloworld",
		data:function(){
			return{
				mes:"����һ������",
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