import Vue from 'vue'
import App from './App.vue'


//https://router.vuejs.org/zh/guide/#html 如有疑问。请看官方手册

// 1.引入 vue-router
import VurRouter from "vue-router"

//  3.定义（路由 ）组件
import Vmain from "./components/Vmain"
import Vcourse from "./components/Vcourse"
import Vmark from "./components/Vmark"

// 2.声明使用 vue-router
Vue.use(VurRouter);

// 4.定义路由对象，每个路由对象映射一个组件
const routes = [
  {path:"/",component:Vmain},
  {path:"/course",component:Vcourse},
  {path:"/mark",component:Vmark}
];

// 5.将路由对象的集合加载在 VurRouter 中
const router = new VurRouter({
  mode:"history",
  routes
});


new Vue({
  el: '#app',
  // 6. 挂载在 Vue 中
  router, // 相当于 routes：routes 的简写
  render: h => h(App),

});

// 7. 现在可以启动你的应用了


