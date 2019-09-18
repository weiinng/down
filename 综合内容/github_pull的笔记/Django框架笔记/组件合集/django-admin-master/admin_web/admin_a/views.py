from django.shortcuts import render, HttpResponse
import re
# Create your views here.
from king_admin.models import *
from king_admin.permission import initial_session


class Per():
    def __init__(self, actions):
        self.actions = actions

    def add(self):
        return "add" in self.actions

    def delete(self):
        return "del" in self.actions

    def edit(self):
        return "edit" in self.actions

    def cat(self):
        return "cat" in self.actions


def users(request):
    user_list = User.objects.all()
    # permission_dict = request.session["permission_dict"]
    # 查询当前登陆人的名字
    id = request.session.get("user_id")
    user = User.objects.filter(id=id).first()

    per = Per(request.actions)

    return render(request, "rbac/users.html", locals())


def add_user(request):
    permission_list = request.session["permission_list"]
    return HttpResponse("add user.....")


def del_user(request, id):
    return HttpResponse(f"del_user: {id}")


def roles(request):
    role_list = Role.objects.all()

    per = Per(request.actions)

    return render(request, "rbac/roles.html", locals())


def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        # 拿到当前用户对象
        user = User.objects.filter(name=user, pwd=pwd).first()
        if user:
            # 把用户的id 保存在 session 里面
            request.session["user_id"] = user.pk
            # 查询当前用户的所有的权限
            initial_session(user, request)
            return HttpResponse("登录成功！")
    return render(request, "login.html", locals())


def index(request):
    name = User.objects.all()
    request.user_name = "haha"
    return render(request, 'index.html', {'name': name})
