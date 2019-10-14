# vue和django 跨域

```
# vue跨域配制（第一种方法）
# 在config文件夹下的index.js中配制
#   proxyTable: {
#     '/api': {  //使用"/api"来代替"http://f.apiplus.c"
#     target: 'http://127.0.0.1:8000/', //源地址
#     changeOrigin: true, //改变源
#     pathRewrite: {
#       '^/api': '' //路径重写
#       }
#   }
# }
# 跨域（第二种方法）
# 用Django的第三方包 django-cors-headers 来解决跨域问题
# 操作步骤：
# 1.pip install django-cors-headers
# 2.在settings.py中添加'corsheaders.middleware.CorsMiddleware',在SessionMiddleware和CommonMiddleware的中间
# 3.在settings.py中添加CORS_ORIGIN_ALLOW_ALL = True
# axios
# 安装 axios
# cnpm install --save axios
# 配制axios
# 在src文件下的mian.js中配制
# import axios from 'axios'
# Vue.prototype.axios = axios
# axios使用
# axios完整写法：
#
# this.axios({
#   method: 'post',
#   url: '/user/12345',
#   data: {
#     firstName: 'Fred',
#     lastName: 'Flintstone'
#   }
# }).then((res)=>{
#       console.log(res)
# }).catch((error)=>{
#       console.log(error)
#  });
#
# post请求
#
# this.axios.post('',{}).then((res)=>{}).catch((error)=>{})
#
# get请求
#
# axios.get('/user?ID=12345')
# .then((response)=> {
#   console.log(response);
# })
# .catch((error)=> {
#   console.log(error);
# });
```