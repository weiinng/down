# import re
# from django.utils.deprecation import MiddlewareMixin
# from django.shortcuts import HttpResponse, redirect
#
# """
# 写在中间件里面可以完全避免每次都要重复校验的问题
# 在请求来的时候进行校验，因此要写在 process_request 方法里面
# """
#
#
# class ValidPermission(MiddlewareMixin):
#     def process_request(self, request):
#         # 当前访问路径
#         current_path = request.path_info
#         """
#         检查是否属于白名单
#             admin 的内部流程
#                 不允许一上来就访问首页，必须要跳转到 登陆页面
#                 http://127.0.0.1:8000/admin/login/?next=/admin/
#                 第二次跳转到登录页面的请求如果没有被定义可通过就会被拦截
#                 无法只使用 admin 为过滤选项
#                 不能用 in 单纯的判断，还是要用到正则处理
#                 需要放过所有 admin 开头的 url
#         """
#         valid_url_list = ["/login/", "/reg/", "/admin/.*"]
#         for valid_url in valid_url_list:
#             ret = re.match(valid_url, current_path)
#             if ret:
#                 # 中间件 return None 表示这个中间件已经执行完毕
#                 return None
#
#         """
#         校验是否登录
#             对于没有登陆的用户返回报错应该是让他去登陆
#         """
#         user_id = request.session.get("user_id")
#         if not user_id:
#             return redirect("/login/")
#
#         # """
#         # 校验权限 1 permission_list
#         #     在编辑，以及删除页面的时候 url 不是固定的，
#         #     会有内含的参数，因此权限列表里面不能仅仅是写死的url
#         #     也不能再单纯的用 in 来判断。还是要靠正则来处理
#         #     将权限列表里面的权限信息用 正则表达式来保存
#         #     然后对访问页面进行验证是否可以通过来处理
#         # """
#         # permission_list = request.session.get("permission_list",[])
#         # flag = False
#         # for permission in permission_list:
#         #     permission = "^%s$" % permission
#         #     ret = re.match(permission, current_path)
#         #     if ret:
#         #         flag = True
#         #         break
#         # if not flag:
#         #     return HttpResponse("没有访问权限！")
#         # return None
#
#         """
#         校验权限 2 permission_dict
#         """
#         permission_dict = request.session.get("permission_dict")
#         for i in permission_dict.values():
#             urls = i["urls"]
#             for reg in urls:
#                 reg = f"^{reg}$"
#                 ret = re.match(reg, current_path)
#                 if ret:
#                     # 加一个自定义的 actions 属性在里面
#                     request.actions = i["actions"]
#                     return None
#         return HttpResponse("没有访问权限！")


import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import  HttpResponse,redirect


def reg(request,current_path):
    # 校验权限1(permission_list)
    permission_list = request.session.get("permission_list", [])
    flag = False
    for permission in permission_list:
        permission = "^%s$" % permission
        ret = re.match(permission, current_path)
        if ret:
            flag = True
            break
    return flag

class ValidPermission(MiddlewareMixin):

    def process_request(self,request):


        # 当前访问路径
        current_path = request.path_info

        # 检查是否属于白名单
        valid_url_list=["/login/","/reg/","/admin/.*"]

        for valid_url in valid_url_list:
            ret=re.match(valid_url,current_path)
            if ret:
                return None


        # 校验是否登录

        user_id=request.session.get("user_id")

        if not user_id:
            return redirect("/login/")


        # #校验权限1(permission_list)
        # permission_list = request.session.get("permission_list",[])  # ['/users/', '/users/add', '/users/delete/(\\d+)', 'users/edit/(\\d+)']
        # flag=reg(request,current_path)
        #
        # if not flag:
        #     return HttpResponse("没有访问权限！")
        #
        # return None

        ##校验权限2

        permission_dict=request.session.get("permission_dict")

        for item in permission_dict.values():
              urls=item['urls']
              for reg in urls:
                  reg="^%s$"%reg
                  ret=re.match(reg,current_path)
                  if ret:
                      print("actions",item['actions'])
                      request.actions=item['actions']
                      return None

        return HttpResponse("没有访问权限！")


