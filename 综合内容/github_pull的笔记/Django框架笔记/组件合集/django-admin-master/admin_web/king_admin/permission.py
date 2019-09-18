def initial_session(user, request):
    # 取出来当前用户的权限，每个权限对应的属性
    permissions = user.roles.all().values(
        "permissions__url",
        "permissions__group_id",
        "permissions__action", ).distinct()
    # 对拿到的数据进行数据处理
    permission_dict = {}
    for i in permissions:
        gid = i["permissions__group_id"]
        if gid not in permission_dict:
            permission_dict[gid] = {
                "urls": [i["permissions__url"], ],
                "actions": [i["permissions__action"], ]
            }
        else:
            permission_dict[gid]["urls"].append(i["permissions__url"])
            permission_dict[gid]["actions"].append(i["permissions__action"])
    request.session["permission_dict"] = permission_dict
