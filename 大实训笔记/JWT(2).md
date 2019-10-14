### Json Web Token令牌验证



至于JWT就不细说。tornado项目中如何使用令牌验证，直接上流程代码！

#### 流程：

![](C:\Users\ASUS\Desktop\JWT流程.jpg)

#### 代码：

* 1、func_tool.py

  ```python
  # jwt秘钥
  jwt_code = 'mycode'
  ```

* 2、用户接口文件

  ```python
  from views.func_tool import jwt_code
  
  # 生成token值
  encoded_jwt = jwt.encode({'username': username}, jwt_code, algorithm='HS256')
  # 将token值发给前端，存储
  msg['token'] = json.dumps({'token': str(encoded_jwt, 'utf-8')})
  
  ```

* 3、前端页面

  ```python
  # 获取登录接口返回的数据及token令牌
  _this.token = result.data.token
  # 将token值存入localStorage
  localStorage.setItem('token',_this.token)
  
  # 获取token
  localStorage.getItem('token')
  ```

* 4、在用户访问某些指定API时，进行权限判断,

  写	个小小的装饰器吧(弟弟级别装饰器)

  ```python
  # JWT装饰器
  def is_login(views):
      def warpper(self, *args, **kwargs):
          # 获取前台传来的token值
          token = self.get_argument('token')
          user_name = self.get_argument('name')
          # 验证token值
          if jwt.decode(token, jwt_code, algorithms=['HS256'])['username'] == user_name:
              return views(self, *args, **kwargs)
          else:
              msg = {}
              msg['mes'] = '操作错误'
              msg['code'] = '400'
              self.write(json.dumps(msg, ensure_ascii=False, indent=4))
      return warpper
  ```



需要的地方语法糖一下，前端展示msg信息就可以了！

### 搞定收工~！