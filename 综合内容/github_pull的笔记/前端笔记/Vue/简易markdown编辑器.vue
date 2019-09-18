<template>
  <div>
    <textarea cols="30" rows="10" v-model="markValue"></textarea>
    <div v-html="currentValue"></div>
  </div>

</template>

<script>

  import Marked from "marked" // Marked 这个名字随便取  "marked" 这个一定要和你导入的包的名字一致

  export default {
    name: 'app',
    data() {
      return {
        markValue: "",
      }
    },
    methods: {},
    computed: {
      currentValue(){
        return Marked(this.markValue)
      },
    },
    components: {},
  }
</script>

<style>

</style>
