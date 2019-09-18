// HTML部分代码
!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="x-ua-compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AJAX局部刷新实例</title>
</head>
<body>

<input type="text" id="i1">+
<input type="text" id="i2">=
<input type="text" id="i3">
<input type="button" value="AJAX提交" id="b1">

<script src="/static/jquery-3.2.1.min.js"></script>
<script>
  $("#b1").on("click", function () {
    $.ajax({
      url:"/ajax_add/",
      type:"GET",
      data:{
	  "i1":$("#i1").val(),
	  "i2":$("#i2").val()
	  },
      success:function (data) {
        $("#i3").val(data);
      }
    })
  })
</script>
</body>
</html>


# views.py
def ajax_demo1(request):
    return render(request, "ajax_demo1.html")


def ajax_add(request):
    i1 = int(request.GET.get("i1"))
    i2 = int(request.GET.get("i2"))
    ret = i1 + i2
    return JsonResponse(ret, safe=False)


urls.py
urlpatterns = [
    ...
    url(r'^ajax_add/', views.ajax_add),
    url(r'^ajax_demo1/', views.ajax_demo1),
    ...   
]