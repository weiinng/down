## URL配置全局变量

在VUE中，你想想我们会有很多地方需要后台传输的数据，

那么久需要进行axios交互（说白了就是传输数据用的），

所以每次都拼写路由地址很麻烦，索性写死一个全局的，

在哪都可以用，岂不是很方便，大哥？

* ##### 1、新建一个global.vue，这个是用来写base URL的

  ```python
  # 代码就这么点，直接粘过去就好了，大哥。
  # 如果修改了IP改为了固定IP，写你自己的IP，如果不知道的话，命令行 ipconfig查看一下
  <script>
      const base_url = 'http://127.0.0.1'
      export default{
          base_url
      }
  </script>
  ```

  大哥，直接粘！

* ##### 2、main.js配置一下

```python
# 导入全局变量URL
import base_url from './components/global'
Vue.prototype.base_url = base_url.base_url
```

大哥，直接粘！

* ##### 3、使用示例

```python
# 旧写法，没有设置全局URL
# let url = 'http://127.0.0.1:8000/user_email_active'
# 设置完全局URL的写法，后面直接拼接API接口名称即可
let url = this.base_url +'/user_email_active'
this.axios.get(url)
```



#### 搞定收工！