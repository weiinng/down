## 用户模块视图

* 头像：

  * 头像文件为了避免重名，要用时间或者md5去处理
    * 1.png -> 1238198asjkhdhkas.png
    * 1.png -> 1asdjkhkjczxhckjasd.png

  * 用户一旦修改头像，之前的头像直接覆盖即可
    * 10.png

* 注册

  * 必须在用户没有登陆的情况下进行注册功能
  * get
    * 返回表单页面
  * post
    * 获取表单数据
      * 为空
      * 昵称长度 <= 4
      * 密码长度 >=8 
      * from_data['name'] = {'error':'昵称不能为空'}
    * 判断数据库重复
      * from_data['error'] = '账号重复'
    * 存入数据库
      * 密码使用make_password

* 登陆

  * 在未登陆情况下才能登陆

  * get

  * post

    * 账号是否存在
      * user = User.get()
    * 校验密码
      * check_password(password,user.password())
    * session设置
      * key:user value:user.id

    * 