<template>
	<div id="a">
		<table border="1" cellspacing="0">
			<tr>
				<td>id</td>
				<td>name</td>
				<td>age</td>
				<td>score</td>
				<td>tid</td>
				<td>tname</td>
			</tr>
			<tr v-for="x in n">
				<td>{{x['id']}}</td>
				<td>{{x['name']}}</td>
				<td>{{x['age']}}</td>
				<td>{{x['score']}}</td>
				<td>{{x['tid']}}</td>
				<td>{{x['tname']}}</td>
				<td v-if="x['score']==100">{{x['name']}}考了满分</td>
				<td v-else-if="x['score']>=60 && x['score']<=99">{{x['name']}}及格了</td>
				<td v-else>{{x['name']}}不及格</td>
			</tr>
		</table>
	</div>
</template>
<script type="text/javascript">
	export default{
		name:"a",
		data:function(){
			return{
				n:[{'id': 1, 'name': '张三', 'age': 18, 'score': 100.0, 'tid': 1, 'tname': '王老师'}, {'id': 2, 'name': '李四', 'age': 19, 'score': 85.0, 'tid': 2, 'tname': '李老师'}, {'id': 3, 'name': '王五', 'age': 20, 'score': 70.0, 'tid': 1, 'tname': '王老师'}, {'id': 4, 'name': '小明', 'age': 16, 'score': 55.0, 'tid': 2, 'tname': '李老师'}, {'id': 5, 'name': '小红', 'age': 27, 'score': 40.0, 'tid': 1, 'tname': '王老师'}]
			}
		}
	}
</script>