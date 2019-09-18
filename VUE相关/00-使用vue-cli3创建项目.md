## <https://github.com/lison16/vue-cource> 

## [Vue\] vue-cli3.0安装

\1. node.js安装
https://nodejs.org/en/download/

2.npm的安装 
由于新版的nodejs已经集成了npm，所以之前npm也一并安装好了。同样可以通过输入 "npm -v" 来测试是否成功安装。命令如下，出现版本提示表示安装成功:

npm -v
5.6.0

\3. 安装vue-cli3.0 
命令 ：npm install -g @vue/cli
若出现错误：Unexpected end of JSON input while parsing near···
解决办法：
npm cache clean --force
npm cache verify
npm i -g @vue/cli
安装后
查看版本（是否安装成功）：vue -V(大写的V)



编码习惯：

创建在node_modules 的同级目录：

内容：

```
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
export default new Vuex.Store({
  state:{
    
  },
  mutations:{
    
  },
  actions:{
    
  },
})
```

