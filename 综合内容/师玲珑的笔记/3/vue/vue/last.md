<template>
	<div id="a">
		<p align="center" id="s"><b><i>Services</i></b></p>
		<br>
		<p align="center"><button type="text" :class="{'q':d1,'g':true}" v-model='z' @click='s1()'><span class="qq">{{z}}</span><span>{{z1}}</span></button></p>
		<p align="center"><button type="text" :class="{'w':d2,'g2':true}" v-model='x' @click='s2()'><span class="qq">{{x}}</span><span>{{x1}}</span></button></p>
		<p align="center"><button type="text" :class="{'e':d3,'g':true}" v-model='c' @click='s3()'><span class="qq">{{c}}</span><span>{{c1}}</span></button></p>
		<p align="center"><button type="text" :class="{'r':d4,'g2':true}" v-model='v' @click='s4()'><span class="qq">{{v}}</span><span>{{v1}}</span></button></p>
		<p align="center"><hr size=1 color=gray width=100%>
		<p align="center"><button type="text" :class="{'t':d5,'g2':true}" v-model='b' ><span class="qq">{{b}}</span><span>${{a5}}.00</span></button></p>
	</div>
</template>
<script type="text/javascript">
	export default{
		name:"a",
		data:function(){
			return{
				a1:300,
				a2:400,
				a3:250,
				a4:220,
				a5:0,
				aa1:0,
				aa2:0,
				aa3:0,
				aa4:0,
				z:"Web Development",
				z1:"$300.00",
				x:"Design",
				x1:"$400.00",
				c:"Integration",
				c1:"$250.00",
				v:"Training",
				v1:'$220.00',
				b:"total",
				b1:'$',
				d1:false,
				d2:false,
				d3:false,
				d4:false
			}
		},
		methods:{
			s1:function(){
				this.d1=!this.d1
				if (this.d1){
					this.aa1=this.a1
				}
				else{
					this.aa1=0
				}
				this.a5=parseInt(this.aa1)+parseInt(this.aa2)+parseInt(this.aa3)+parseInt(this.aa4)
			},
			s2:function(){
				this.d2=!this.d2
				if (this.d2){
					this.aa2=this.a2
				}
				else{
					this.aa2=0
				}
				this.a5=parseInt(this.aa1)+parseInt(this.aa2)+parseInt(this.aa3)+parseInt(this.aa4)
			},
			s3:function(){
				this.d3=!this.d3
				if (this.d3){
					this.aa3=this.a3
				}
				else{
					this.aa3=0
				}
				this.a5=parseInt(this.aa1)+parseInt(this.aa2)+parseInt(this.aa3)+parseInt(this.aa4)
			},
			s4:function(){
				this.d4=!this.d4
				if (this.d4){
					this.aa4=this.a4
				}
				else{
					this.aa4=0
				}
				this.a5=parseInt(this.aa1)+parseInt(this.aa2)+parseInt(this.aa3)+parseInt(this.aa4)
			}
		}
	}
</script>
<style type="text/css">
	#a{
		width: 600px;
		height: 600px;
		border: 1px solid blue;
		border-radius: 15px;
		margin: 0 auto;
	}
	#s{
		font-size: 20px;
	}
	.g{
		display: block;
		width: 400px;
		height: 65px;
		border: 2px solid yellow;
		border-radius: 6px;
		background-color: orange;
		margin-top: 30px; 
		color:gray;
		font-size: 18px;
		font-weight: bold;
	}
	.g2{
		display: block;
		width: 400px;
		height: 65px;
		border: 2px solid yellow;
		border-radius: 6px;
		background-color: pink;
		margin-top: 30px;
		color:gray;
		font-size: 18px;
		font-weight: bold;
	}
	span{
		position: absolute;
		left: 1075px;
	}
	.qq{
		position: absolute;
		left: 800px;
	}
	.q{
		background-color: green;
	}
	.w{
		background-color: green;
	}
	.e{
		background-color: green;
	}
	.r{
		background-color: green;
	}

</style>
