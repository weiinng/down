<template>
	<div id="a">
		<form v-on:submit.prevent="submitmes()" action="http://www.baidu.com" method="post">
			用户名:<input type="text" name="name" v-model="name">
			<br>
			密码:<input type="password" name="userpassword" v-model="userpassword">
			<br>
			性别：<input type="radio" name="sex" v-model="sex" value="男">男
			<input type="radio" name="sex" v-model="sex" value="女">女
			<br>
			爱好:<input type="checkbox" name="joy" v-model="joy" value="唱歌">唱歌
			<input type="checkbox" name="joy" v-model="joy" value="看书">看书
			<input type="checkbox" name="joy" v-model="joy" value="跳舞">跳舞
			<br>
			所属部门:<select name="classid" v-model="classid">
				<option value="1">一年级</option>
				<option value="2">二年级</option>
				<option value="3">三年级</option>
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