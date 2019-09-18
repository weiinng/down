def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        next_url = request.get_full_path()
        if request.get_signed_cookie("login", salt="SSS", default=None) == "yes":
            # 已经登录的用户...
            return func(request, *args, **kwargs)
        else:
            # 没有登录的用户，跳转刚到登录页面
            return redirect("/login/?next={}".format(next_url))
    return inner


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passwd = request.POST.get("password")
        if username == "xxx" and passwd == "dashabi":
            next_url = request.GET.get("next")
            if next_url and next_url != "/logout/":
                response = redirect(next_url)
            else:
                response = redirect("/class_list/")
            response.set_signed_cookie("login", "yes", salt="SSS")
            return response
    return render(request, "login.html")

cookie版登录