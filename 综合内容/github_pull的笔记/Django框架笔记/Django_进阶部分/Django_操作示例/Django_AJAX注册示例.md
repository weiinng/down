ajax 注册示例

# 注册的视图函数
def register(request):
    if request.method == "POST":
        ret = {"status": 0, "msg": ""}
        form_obj = forms.RegForm(request.POST)
        print(request.POST)
        # 帮我做校验
        if form_obj.is_valid():
            # 校验通过，去数据库创建一个新的用户
            # 传过来的字段里面有个 re_password 字段是无法入库的给去掉
                # 关于这个 cleaned_data 的功能为提取出来字典里面的值
            form_obj.cleaned_data.pop("re_password")
            avatar_img = request.FILES.get("avatar")
            # 因为现在的userinfo
            models.UserInfo.objects.create_user(**form_obj.cleaned_data, avatar=avatar_img)
            ret["msg"] = "/index/"
            return JsonResponse(ret)
        else:
            print(form_obj.errors)
            ret["status"] = 1
            ret["msg"] = form_obj.errors
            print(ret)
            print("=" * 120)
            return JsonResponse(ret)
    # 生成一个form对象
    form_obj = forms.RegForm()
    print(form_obj.fields)
    return render(request, "register.html", {"form_obj": form_obj})


// AJAX提交注册的数据
<script> 
 $("#reg-submit").click(function () {
        // 取到用户填写的注册数据，向后端发送AJAX请求
        var formData = new FormData();
        formData.append("username", $("#id_username").val());
        formData.append("password", $("#id_password").val());
        formData.append("re_password", $("#id_re_password").val());
        formData.append("email", $("#id_email").val());
        // 上传文件的数据需要用 files 拿到
		formData.append("avatar", $("#id_avatar")[0].files[0]);
        formData.append("csrfmiddlewaretoken", $("[name='csrfmiddlewaretoken']").val());

        $.ajax({
            url: "/reg/",
            type: "post",
            // 上传文件的时候需要加这两个 fales
			processData: false,
            contentType: false,
            data: formData,
            success:function (data) {
                if (data.status){
                    // 有错误就展示错误
                    // console.log(data.msg);
                    // 将报错信息填写到页面上
                    $.each(data.msg, function (k,v) {
                        // console.log("id_"+k, v[0]);
                        // console.log($("#id_"+k));
						// 链式操作 先加值然后找父类 加属性
                        $("#id_"+k).next("span").text(v[0]).parent().parent().addClass("has-error");
                    })

                }else {
                    // 没有错误就跳转到指定页面
                    location.href = data.msg;
                }
            }
        })
    });
	
	
		// 将所有的input框绑定获取焦点的事件，将所有的错误信息清空
    $("form input").focus(function () {
        $(this).next().text("").parent().parent().removeClass("has-error");
    })
	
</script> 