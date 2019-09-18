<template>
  <div>
    <ul>
      <li>
        <router-link to="/">首页</router-link>
      </li>
      <li>
        <router-link to="/course">课程表</router-link>
      </li>
      <li>
        <router-link to="/mark">编辑器</router-link>
      </li>
    </ul>
    <link href="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    
	<!--路由 出口-->
    <router-view></router-view>
  </div>


</template>

<script>


  export default {
    name: 'app',
    data() {
      return {}
    },
    methods: {},
    computed: {},
    components: {},
  }
</script>

<style>

</style>
