<template>
    <div>
        <img :src="imgSrc">
    </div>

</template>

<script>
    // webpack file-loader 打包成对象
    import imgSrc from './assets/bili.jpg'

    export default {
        name: "app",
        data() {
            return {
                imgSrc: imgSrc
            }
        }
    }

</script>

<style scoped>

</style>