"""
 admin 流程
 
 启动 

 注册
 
 设计url
 
 被使用的形式
""" 

 


"""
admin 启动流程核心
"""
	# setting.py 中会对注册的app自动加载里面的 XadminConfig 模块
INSTALLED_APPS = [
    ...
    'app01.apps.App01Config',
    'app02.apps.App02Config',
]
	# Xadmin下的 apps里面的 XadminConfig 在自动执行的时候可以进行启动操作
from django.apps import AppConfig
class App01Config(AppConfig):
    name = 'app01'
	
	# admin 源码 
import admin
		# 执行每一个app下的admin.py文件
		autodiscover_modules('admin', register_to=site)
		
		

		
"""
admin 注册流程核心
"""
class AdminSite(object):
    def __init__(self,name="admin"):
        # 定义一个空字典用于保存注册
		self._registry={}
		
	# 注册函数
	# 需要有两个参数， 被注册的表 以及 是否有自定义的配置操作
    def register(self, model, admin_class=None, **options):
        
		# 首先对是否存在自定义配置操作进行判断
		if not admin_class:
            # 如果无自定义则用默认的
			admin_class = Modeladmin
		# 有自己的就用自己的
		# 注意这里的键为类名而不是字符串 
        self._registry[model] = admin_class(model, self) 
			# {Book:ModelAdmin(Book),Publi sh:ModelAdmin(Publish)}

# 进行实例化实现单例模式
# 其他所有的程序中的 admin 通过引入，用的都是这个对象 
site=AdminSite()


"""
admin 设计url 核心
"""

# urls.py 中全部写成了一条
# 所有的结果都在调用 urls方法后拿到
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

class AdminSite(object):
	
	# 所有的urls 保存在 urlpatterns列表里面
	def get_urls(self):

		urlpatterns = [
			url(r'^$', wrap(self.index), name='index'),
			url(r'^login/$', self.login, name='login'),
			url(r'^logout/$', wrap(self.logout), name='logout'),
			url(r'^password_change/$', wrap(self.password_change, cacheable=True), name='password_change'),
			url(r'^password_change/done/$', wrap(self.password_change_done, cacheable=True),
				name='password_change_done'),
			url(r'^jsi18n/$', wrap(self.i18n_javascript, cacheable=True), name='jsi18n'),
			url(r'^r/(?P<content_type_id>\d+)/(?P<object_id>.+)/$', wrap(contenttype_views.shortcut),
				name='view_on_site'),
		]
		valid_app_labels = []
        
		# 遍历注册过的表，对每个表生成 相应的 url 进行链接起来 
		for model, model_admin in self._registry.items():
            urlpatterns += [
                url(r'^%s/%s/' % (model._meta.app_label, model._meta.model_name), include(model_admin.urls)),
            ]
            if model._meta.app_label not in valid_app_labels:
                valid_app_labels.append(model._meta.app_label)


        if valid_app_labels:
            regex = r'^(?P<app_label>' + '|'.join(valid_app_labels) + ')/$'
            urlpatterns += [
                url(regex, wrap(self.app_index), name='app_list'),
            ]
		# 返回给urls 得出的 urls列表
        return urlpatterns
	
	# 调用 get_urls 获得全部的结果
    def urls(self):
		# 给urls.py 返回回去
        return self.get_urls(), 'admin', self.name




"""
程序的实际使用。
引入 admin 然后注册就可以了
"""
from django.contrib import admin
from .models import *
admin.site.register(Book,BookConfig)	# 在注册的时候可以对表进行配置操作
admin.site.register(Publish)
admin.site.register(Author)
admin.site.register(AuthorDetail)






