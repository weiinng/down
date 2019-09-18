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
				<td v-if="x['score']==100">{{x['name']}}��������</td>
				<td v-else-if="x['score']>=60 && x['score']<=99">{{x['name']}}������</td>
				<td v-else>{{x['name']}}������</td>
			</tr>
		</table>
	</div>
</template>
<script type="text/javascript">
	export default{
		name:"a",
		data:function(){
			return{
				n:[{'id': 1, 'name': '����', 'age': 18, 'score': 100.0, 'tid': 1, 'tname': '����ʦ'}, {'id': 2, 'name': '����', 'age': 19, 'score': 85.0, 'tid': 2, 'tname': '����ʦ'}, {'id': 3, 'name': '����', 'age': 20, 'score': 70.0, 'tid': 1, 'tname': '����ʦ'}, {'id': 4, 'name': 'С��', 'age': 16, 'score': 55.0, 'tid': 2, 'tname': '����ʦ'}, {'id': 5, 'name': 'С��', 'age': 27, 'score': 40.0, 'tid': 1, 'tname': '����ʦ'}]
			}
		}
	}
</script>