<template>
	<div id="a">
		<form v-on:submit.prevent="submitmes()" action="http://www.baidu.com" method="post">
			�û���:<input type="text" name="name" v-model="name">
			<br>
			����:<input type="password" name="userpassword" v-model="userpassword">
			<br>
			�Ա�<input type="radio" name="sex" v-model="sex" value="��">��
			<input type="radio" name="sex" v-model="sex" value="Ů">Ů
			<br>
			����:<input type="checkbox" name="joy" v-model="joy" value="����">����
			<input type="checkbox" name="joy" v-model="joy" value="����">����
			<input type="checkbox" name="joy" v-model="joy" value="����">����
			<br>
			��������:<select name="classid" v-model="classid">
				<option value="1">һ�꼶</option>
				<option value="2">���꼶</option>
				<option value="3">���꼶</option>
			</select>
			<button type="submit">submit</button>
		</form>
	</div>
</template>
<script type="text/javascript">
	export default{
		name:"a",
		data:function(){
			return{
				name:'',
				userpassword:'',
				sex:'',
				joy:[],
				classid:''
			}
		},
		methods:{
			submitmes:function(){
				console.log(this.name)
				console.log(this.userpassword)
				console.log(this.sex)
				console.log(this.classid)
				var list=[]
				this.joy.forEach(function(i){
					list.push(i)
				})
				console.log(list)
			}
		}
	}
</script>