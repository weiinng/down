from django.contrib import admin

# Register your models here.

from king_admin import models


class UserInfoAdmin(admin.ModelAdmin):
    filter_horizontal = ('to_group', 'to_control')


admin.site.register(models.User)
admin.site.register(models.Role)
admin.site.register(models.Permission)
admin.site.register(models.PermissionGroup)
