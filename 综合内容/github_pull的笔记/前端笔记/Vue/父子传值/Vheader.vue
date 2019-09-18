<template>
  <header class="wrap">

    我是header，我从父级组件那里拿到了数据很开心：
    <ul v-for="item in cityArray">
      {{item}}
    </ul>
  </header>
</template>

<script>
  export default {
    name: "Vheader",
    data() {
      return {}
    },
    methods: {},
    props: {
      cityArray: Array
      // 如果验证不通过会报错
      //  [Vue warn]: Invalid prop: type check failed for prop "cityArray". Expected String with value "山东,北京,深圳", got Array
    },
  }
</script>

<style scoped>

</style>
