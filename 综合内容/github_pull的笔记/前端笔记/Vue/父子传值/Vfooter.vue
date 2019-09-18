<template>
  <footer class="wrap">
    我是Vfooter，我想测试下给父级组件添加数据: <br>
    <button @click="addCunHandler">给父级组件的数据增加点什么，添加一个村庄</button>
  </footer>
</template>

<script>
  export default {
    name: "Vfooter",
    data() {
      return {}
    },
    methods:{
      addCunHandler(){
      //  触发自定义事件
        this.$emit('addZhuangHandler','破村庄');
      },
    },

  }
</script>

<style scoped>

</style>
