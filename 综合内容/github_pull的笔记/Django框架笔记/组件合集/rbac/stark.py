from stark.service.stark import site, ModelStark
from rbac import models


class PerConfig(ModelStark):
    list_display = ["title", "url", "action", "group"]


site.register(models.User)
site.register(models.PermissionGroup)
site.register(models.Permission, PerConfig)
site.register(models.Role)
