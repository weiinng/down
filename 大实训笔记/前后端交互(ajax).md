# 前后端交互(ajax)

Axios 是一个基于 promise 的 HTTP 库，可以用在浏览器和 node.js 中。

特性 从浏览器中创建 XMLHttpRequests 从 node.js 创建 http 请求 支持 Promise API 拦截请求和响应 转换请求数据和响应数据 取消请求 自动转换 JSON 数据 客户端支持防御 XSRF

文档地址：<http://www.axios-js.com/zh-cn/docs/>

vue.js 集成axios

```
cnpm install axios --save
```

main.js引入axios 

```
/*引入axios*/
import Axios from 'axios'
Vue.prototype.axios = Axios;

import QS from 'qs'
Vue.prototype.qs = QS;
```

发送get请求 

```
getApiData:function() {
             //设置请求路径
             var url  = "http://localhost:8000";                
             // 发送请求:将数据返回到一个回到函数中
             var _this= this;
             // 并且响应成功以后会执行then方法中的回调函数
             this.axios.get(url,{
    params: {
        id: 123,
        name: 'Henry',
        sex: 1,
        phone: 13333333
    }
}).then(function(result) {

                 console.log(result);
                 //_this.name = result.data.message[0].name;
             });    
             }
```

发送post请求 

```
getApiData_post:function() {
             //设置请求路径
             var url  = "http://localhost:8000";                
             // 发送请求:将数据返回到一个回到函数中
             var _this= this;
             // 并且响应成功以后会执行then方法中的回调函数
             this.axios.post(url,this.qs.stringify({
        id:123
      })).then(function(result) {

                 console.log(result);
                 //_this.name = result.data.message[0].name;
             });    
             }
```

服务端返回json

配置序列化，即数据库结果集对象直接转换json对象

```
def sqlalchemy_json(self):
    obj_dict = self.__dict__
    return dict((key, obj_dict[key]) for key in obj_dict if not key.startswith("_"))

Base.__json__ = sqlalchemy_json
```

```
class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):

        #接收参数
        id = self.get_argument('id','未收到')
        print(id)

        #self.finish({'name':'你好'})

        #写入
        #p = Person(name="你好", age=12)
        #sess.add(p)
        #sess.commit()

        #修改
        p = sess.query(Person).filter(Person.id==1).one()
        #p.name = "shuke"
        #sess.commit()


        #返回json
        self.write(json.dumps({"status":0,"msg":"返回成功","user_info":Person.__json__(p)},ensure_ascii=False,indent=4))



        #self.write("Hello, world123")
        #self.finish()


    def post(self,*args, **kwargs):

        #接收参数
        id = self.get_argument('id','未收到')
        print(id)

        #p = sess.query(Person).filter(Person.id==1).one()
        #返回json
        self.write(json.dumps({"status":0,"msg":"返回成功","user_info":Person.__json__(p)},ensure_ascii=False,indent=4))
```