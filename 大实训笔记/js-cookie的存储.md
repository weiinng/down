

# 登录成功后，将用户名存入cookie

利用vue.js中的js-cookie模块

安装

 npm install js-cookie --save

使用 

```
import Cookies from 'js-cookie'
```

存储 

```
// Create a cookie, valid across the entire site:
Cookies.set('name', 'value');

// Create a cookie that expires 7 days from now, valid across the entire site:
Cookies.set('name', 'value', { expires: 7 });  #过期时间为七天

// Create an expiring cookie, valid to the path of the current page:
Cookies.set('name', 'value', { expires: 7, path: '' }); 
```

取出 

```
// Read cookie:
Cookies.get('name'); // => 'value'
Cookies.get('nothing'); // => undefined

// Read all visible cookies:
Cookies.get(); // => { name: 'value' }
```

删除 

```
// Delete cookie:
Cookies.remove('name');

// Delete a cookie valid to the path of the current page:
Cookies.set('name', 'value', { path: '' });
Cookies.remove('name'); // fail!
Cookies.remove('name', { path: '' }); // removed!
```

```
#参考实例 存入cookie
mounted:function(){

         this.common.get_menu();
         let username = this.$route.query.username
         let user_id = this.$route.query.user_id
         if (username){
             Cookies.set('username',username,{ expires: 7 })
             Cookies.set('user_id',user_id,{ expires: 7 })
         }
         
         this.get_goods() 
         var data = Cookies.get('cart');
if(data){
 data = JSON.parse(data)
 this.datalist = data;
         }
         this.total_price()
         this.count_people()

     },
```

```
#参考实例 取cookie
post_redis:function(){
    let user_id = Cookies.get('user_id')
    if(user_id){
        var add_cart_redis = this.base_url+'/add_cart_redis'
        var _this = this
        var token = localStorage.getItem('token')
        var params = {
            'cartlist':JSON.stringify(this.datalist),
            'user_id':user_id,
            'token':token
        }
        this.axios.post(add_cart_redis,this.qs.stringify(params)).then(function(result) {
        if(result.data['code'] == '200') {
            alert('添加购物车成功')
            console.log(result.data)
            Cookies.set('cart',_this.datalist,{ expires: 7 })
        }
        else {
            _this.msg = result.data.message
            console.log(result.data)
        }
```