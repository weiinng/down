Django接受上传文件代码

from django.conf.urls import url
from django.shortcuts import HttpResponse


def upload(request):
    print("request.GET:", request.GET)
    print("request.POST:", request.POST)

    if request.FILES:
        filename = request.FILES["file"].name
        with open(filename, 'wb') as f:
            for chunk in request.FILES['file'].chunks():
                f.write(chunk)
            return HttpResponse('上传成功')
    return HttpResponse("收到了！")

urlpatterns = [
    url(r'^upload/', upload),
]