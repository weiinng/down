路由跳转时：
<router-link to="f">点击跳转</router-link>

传指定内容跳转时:
<router-link :to="{'name':'f',params:{'n':'qweersad'}}">点击跳转</router-link>  多了个: !!!!!!!!!

在f.vue里用下面的代码来接收

<$route.params.n>


在index.js中也要调
   {
      path: '/f/:n',
      name: 'f',
      component: f
    }



指定内容要跳路径   还要指定内容传  接收时也有接收的对象  