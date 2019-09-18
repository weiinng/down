再用到这三个的时候你那个div必须放在一个大的div里面！！！！！！！

v-html:

<div id="a">
	<div v-html="m"></div>
</div>
在下面赋值时就给m赋值即是该div里的内容，
<script type="text/javascript">
	window.onload=function(){
	var v=new Vue({
	el:"#a",
	data:{m:"lalala"}
})
}
</script>


v-bind:
<style>
	.a{background-color:red;}
</style>


<div id="#a">
	<div v-bind:class="a">          //这里的class是css类型，当然也可以是id,后面那个a其实就是个形参，可以取任意名字，就跟{{m}}这里面的m一样，要在vue里的data里面给他赋值，然后就可以用css选择器对网页做一些调整啦
		lalalala
	</div>
</div>

<script type="text/javascript">
	window.onload=function(){
	var v=new Vue({
	el:"#a",
	date:{a:"aa"}
})
}
</script>








