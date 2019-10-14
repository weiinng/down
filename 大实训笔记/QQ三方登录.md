# QQ三方登录



qq登录官网文档：

<https://wiki.connect.qq.com/%E4%BD%BF%E7%94%A8authorization_code%E8%8E%B7%E5%8F%96access_token>



```
#user.py
#QQ登录获取code码
class Get_authorization_code(BaseHandler):
    def get(self, *args, **kwargs):
        data = {}
        params = {
            'response_type':'code',
            'client_id':'101487535',
            'redirect_uri':'http://login.yskj599.com/user/login/qq_login',
            'state':'111'
        }
        response = requests.get(url='https://graph.qq.com/oauth2.0/authorize',params=params)
        data['code'] = 200
        data['url'] = response.url
        self.write(json.dumps(data))

#QQ登录获取access_token
def QQ_get_access_token(code,app_id):
    app = {
        'grant_type': 'authorization_code',
        'client_id': app_id,
        'client_secret': '9c383c0a358b3382ed52269ccff3691f',
        'code': code,
        'redirect_uri': 'http://login.yskj599.com/user/login'
    }
    access_url = 'https://graph.qq.com/oauth2.0/token'
    response = requests.get(url=access_url, params=app)
    alist = response.text.split('=')
    access_token = alist[1].split('&')[0]
    refresh_token = alist[3]
    return access_token

#QQ登录获取OpenID
def QQ_get_OpenID(access_token):
    OpenID_url = 'https://graph.qq.com/oauth2.0/me'
    response = requests.get(OpenID_url, params={'access_token': access_token})
    print(response.text)
    OpenID = response.text.split('"')[-2]
    return OpenID

#QQ登录接口
class QQ_login(BaseHandler):
    def get(self, *args, **kwargs):
        params = self.request.arguments
        app_id = '101487535'
        try:
            code = params['code'][0].decode()
            access_token = QQ_get_access_token(code,app_id)
            OpenID = QQ_get_OpenID(access_token)
            params2 = {
                'access_token':access_token,
                'oauth_consumer_key':'101487535',
                'openid':OpenID
            }
            # QQ返回登录用户的信息
            get_info_url = 'https://graph.qq.com/user/get_user_info'
            response = requests.get(url = get_info_url,params=params2)
            user_info = response.json()
            nickname = user_info['nickname']
            user = sess.query(User).filter(User.account == nickname).first()
            if not user:
                qq_user = User(account = nickname,password = generate_password_hash('123'),gender=user_info['gender'],
                               address =user_info['province'] + user_info['city'],social_attr = 2,is_active = 1)
                sess.add(qq_user)
                sess.commit()
                user = sess.query(User).filter(User.account == nickname).first()
            self.redirect('http://127.0.0.1:8080?username={}&user_id={}'.format(nickname, user.id))
        except:
            self.write('登录失败')
```



```
# VUE-login.vue
<img src="../assets/images/3T@BS`DNPKQV~UU@CN$EI7A.png" alt="" @click="qq_login()">
```



```
# VUE-login.vue
qq_login:function(){
  var url = this.base_url +'/get_authorization_code'
  var _this = this
  this.axios.get(url).then(function(result) {
   if(result.data.code == 200) {
    window.location.href=result.data.url
}
  else {
      _this.msg = result.data.message
      console.log(result.data)
  }
 }); 
}
```



qq登录
qq登录流程oauth2的认证流程分析
1.用户向美多网站发送qq注册的请求

 2.美多网站向用户返回qq登录的页面 

3.用户在qq登录的界面向qq的服务器发送qq用户名和密码发起登录的请求

 4.qq服务器认证成功之后将用户引导到回调的网址中，并返回给用户qq服务器的token值

 5.用户重定向到美多页面并携带了qq服务器发送的token 

6.后端接收到token后向qq服务器请求access token

 7.qq服务器返回access token 

8.美多服务器通过access token来向qq服务器来获取用户的openid 

9.通过id来查询用户是否已经在美多商城注册 

10.用户已经注册直接返回用户的access token值 

11.用户没有账号，生成注册的access token，（载荷openid）重新注册信息发送给后端 

12.后端接收到数据之后创建对象并将qq用户的openid和账号进行绑定

