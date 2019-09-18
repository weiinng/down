# """
# 为了解耦，将处理权限的代码保存在组件里面
# """
#
#
# def initial_session(user, request):
#
#     """
#     方案1
#         不好用，只用一个权限字段实在功能有限
#     """
#
#     # # 查看当前用户的所有的权限
#     # # 因为会有values 的原理会导致有重复需要去重
#     # ret = user.roles.all().values("permissions__url").distinct()
#     # permission_list = []
#     # # 将所有的权限保存在一个列表里面，稍微处理下数据便于操作
#     # for i in ret:
#     #     permission_list.append(i["permissions__url"])
#     # # 把用户的用户权限保存在 session 里面
#     # request.session["permission_list"] = permission_list
#
#     """
#     方案2
#
#     """
#     # permission__group_id permission表 的group 字段 因为外键会后面加个 ”_id“ 别忘了啊
#     # 取出来当前用户的权限，每个权限对应的属性
#     print(user)
#     permissions = user.roles.all().values(
#         "permissions__url",
#         "permissions__group_id",
#         "permissions__action",).distinct()
#     # 对拿到的数据进行数据处理
#     permission_dict = {}
#     for i in permissions:
#         gid = i["permissions__group_id"]
#         if gid not in permission_dict:
#             permission_dict[gid] = {
#                 "urls": [i["permissions__url"], ],
#                 "actions": [i["permissions__action"], ]
#             }
#         else:
#             permission_dict[gid]["urls"].append(i["permissions__url"])
#             permission_dict[gid]["actions"].append(i["permissions__action"])
#     request.session["permission_dict"] = permission_dict
#
#     # 左侧菜单的显示文本处理，可以在这里进行数据处理，也可以在 是视图函数里面直接用 orm 操作都可
#     # 注册菜单权限
#     permissions = user.roles.all().values("permissions__url", "permissions__action",
#                                           "permissions__group__title").distinct()
#     print("permissions", permissions)
#
#     menu_permission_list = []
#     for item in permissions:
#         if item["permissions__action"] == "list":
#             menu_permission_list.append((item["permissions__url"], item["permissions__group__title"]))
#
#     print(menu_permission_list)
#     request.session["menu_permission_list"] = menu_permission_list
#




def initial_session(user,request):
    # #方案1
    # permissions = user.roles.all().values("permissions__url").distinct()
    # # 【{}，{}】
    # permission_list = []
    #
    # for item in permissions:
    #     permission_list.append(item["permissions__url"])
    # print(permission_list)
    #
    # request.session["permission_list"] = permission_list

    ##方案2

    permissions = user.roles.all().values("permissions__url","permissions__group_id","permissions__action").distinct()
    print("permissions",permissions)


    permission_dict={}
    for item in permissions:
        gid=item.get('permissions__group_id')

        if not gid in permission_dict:

            permission_dict[gid]={
                "urls":[item["permissions__url"],],
                "actions":[item["permissions__action"],]
            }
        else:
            permission_dict[gid]["urls"].append(item["permissions__url"])
            permission_dict[gid]["actions"].append(item["permissions__action"])



    request.session['permission_dict']=permission_dict


    # 注册菜单权限
    permissions = user.roles.all().values("permissions__url","permissions__action","permissions__title").distinct()

    menu_permission_list=[]
    for item in permissions:
        if item["permissions__action"]=="list":
            menu_permission_list.append((item["permissions__url"],item["permissions__title"]))

    request.session["menu_permission_list"]=menu_permission_list











