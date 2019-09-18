from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(verbose_name="用户名", max_length=32)
    pwd = models.CharField(verbose_name="密码", max_length=32)
    roles = models.ManyToManyField(to="Role", verbose_name="角色")

    def __str__(self): return self.name

    class Meta:
        verbose_name_plural = u"用户表"


class Role(models.Model):
    title = models.CharField(verbose_name="角色", max_length=32)
    permissions = models.ManyToManyField(verbose_name="权限", to="Permission")

    def __str__(self): return self.title

    class Meta:
        verbose_name_plural = u"角色表"


class Permission(models.Model):
    title = models.CharField(verbose_name="权限", max_length=32)
    url = models.CharField(max_length=32)
    action = models.CharField(verbose_name="动作", max_length=32, default="1")
    group = models.ForeignKey(to="PermissionGroup", verbose_name="权限组", default=1)

    def __str__(self): return self.title

    class Meta:
        verbose_name_plural = u"权限表"


class PermissionGroup(models.Model):
    title = models.CharField(verbose_name="权限组", max_length=32)

    def __str__(self): return self.title

    class Meta:
        verbose_name_plural = u"权限组表"
