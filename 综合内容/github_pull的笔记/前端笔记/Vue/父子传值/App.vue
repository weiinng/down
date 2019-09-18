<template>
  <div>
    <img :src="imgSrc">
    <!-- 父子传值 -->
    <!-- 自定义属性直接 通过属性传值 -->
    <Vheader :cityArray="citys"></Vheader>


    <!-- 自定义事件 -->
    <Vfooter   v-on:addZhuangHandler="addHandler"></Vfooter>
  </div>

</template>

<script>
  import imgSrc from './assets/bili.jpg'
  import Vheader from './components/Vheader'
  import Vfooter from './components/Vfooter'

  export default {
    name: "app",
    data() {
      return {
        imgSrc: imgSrc,
        citys:["山东","北京","深圳"]

      }
    },
    methods:{
      addHandler (str){
        // alert(str)
        this.citys.push(str);
        alert(this.citys);
      }
    },
    components: {
      Vheader,
      Vfooter
    },

  }

</script>

<style scoped>

</style>
