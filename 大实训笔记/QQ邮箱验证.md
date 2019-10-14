# QQ邮箱验证

## 将你的qq邮箱开启smtp服务

开启smtp服务攻略:<https://jingyan.baidu.com/article/6079ad0eb14aaa28fe86db5a.html>

1.在QQ客户端登录后,在面板上打开邮件, 

2.在打开的邮箱中心,进入设置 

3.从邮箱设置中心,进入帐户 

4.在这里可以看到POP3/SMTP服务被关闭了,因此客户端会收不到邮件,我们来开启它, 

5.在开启POP3/SMTP服务时,需要进行身份的验证,按要求来发送一条短信后,点击 我已发送, 

6.这时通过验证的话,就会得到授权码了,在客户端中,配置时密码换成这个授权码就可以了.  

7.返回到设置中的POP3/SMTP服务页,查看该服务为已开启时,就可以用客户端来收发邮件了.19:06 2018-01-12 



```
#原代码
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender='3611792766@qq.com'    # 发件人邮箱账号
my_pass = 'ihzsfjvctqdmciff'              # 发件人smtp秘钥(当时申请smtp给的口令)
my_user='3611792766@qq.com'      # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
    try:
        msg=MIMEText('填写邮件内容','plain','utf-8')
        msg['From']=formataddr(["发件人昵称",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["收件人昵称",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="邮件主题-测试"                # 邮件的主题，也可以说是标题

        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)  # smtp秘钥
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()# 关闭连接
    except Exception:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret

ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
```



项目改造后

```
#func_tool.py
# 发件人smtp秘钥(当时申请smtp给的口令)
def mail(my_sender,content):
    ret=True
    try:
        msg=MIMEText(content,'plain','utf-8')
        msg['From']=formataddr(["你好",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["你好",'563173681@qq.com'])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="请您激活用户"                # 邮件的主题，也可以说是标题

        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, 'jrntnoojsilabjcf')  # smtp秘钥
        server.sendmail(my_sender,['563173681@qq.com',],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()# 关闭连接
    except Exception:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
```



```
#user.py
# 发送邮件
class Post_email(BaseHandler):
    def post(self, *args, **kwargs):
        user_id = self.get_argument('user_id')
        user = sess.query(User).filter(User.id == user_id).first()
        if user.email:
            url = 'http://172.16.18.10/activate?id='+user_id
            mail(user.email,url)
        else:
            mes = {}
            mes['code'] = 10002
            mes['message'] = '用户信息不全，请填写邮箱后激活'
            self.write(json.dumps(mes, ensure_ascii=False, indent=4))
```



```
#user.py
# 回调返回首页
class Activate(BaseHandler):
    def get(self, *args, **kwargs):
        user_id = self.get_argument('id')
        user = sess.query(User).filter(User.id == user_id).first()
        user.is_active = 1
        sess.commit()
        self.redirect('http://172.16.18.10:8080/')
```


## 给用户注册增加功能，用户注册成功后，进入用户首页，点击一个按钮激活账号，此时请求后台接口，接口生成一个链接，将该链接作为邮件发给用户邮箱，用户点击邮箱内的链接后跳转到商城首页，此时异步请求后台接口，后台接口根据用户uid将用户状态改为激活