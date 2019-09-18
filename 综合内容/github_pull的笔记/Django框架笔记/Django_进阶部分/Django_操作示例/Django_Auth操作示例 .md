from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login2(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    # 对用户进行认证
    user = authenticate(username=username,password=password)
    # print(user)
    print(type(user))   # <class 'django.contrib.auth.models.User'>

    if user:
        # 用户对象进行封装
        login(request,user)
        # 检测是否在已登录状态
        ret = request.user.is_authenticated()
        print(ret)      # True
        # 被login 处理后可以从数据库中拿出属性
        print(request.user.username)    # yangtuo
        print(request.user.password)
        # pbkdf2_sha256$36000$upBMqkdpgniF$jOAAWqaOwbTQUW7iceSh9Dj/GwRXqeqoeLdLVvnV7s8=
        return redirect("/index/")
    return render(request, "login.html")


@login_required
def index(request):
    return render(request, "index.html")


def logout_view(request):
    logout(request)
    # 相当于 request.session.flush() 删除session 以及让cookie失效
    return redirect("/login/")


def register(request):
    from django.contrib.auth.models import User
    # 如果用create 确实也可以创建进去.但是因为是明文无加密的缘故无法登录使用
    # User.objects.create(username='yang',password='tuo')

    # 创建普通用户 要用 create_user 方法
    User.objects.create_user(username='yang',password='tuo')

    # 创建超级用户 要用 create_superuser 方法
    # 创建超级用户会有很多的字段限制
    # User.objects.create_superuser(username='tuo',password='yang')

    # 对用户的密码进行核对是否正确
    user_obj = User.objects.create_user(username='yangyang',password='tuo')
    ret = user_obj.check_password("tuo")
    print(ret)

    # 对用户的密码进行修改重置
    user_obj.set_password("tuotuo")
    user_obj.save() # 修改后必须要保存

    return HttpResponse("注册成功~~~")


