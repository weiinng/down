"""
自己实现一个 Xadmin 模块来替换掉 admin

和 admin 一样需要 

	启动

	注册

	url 分发

"""



"""
启动
"""
# setting.py 
INSTALLED_APPS = [
    ...
    'Xadmin.apps.XadminConfig',
    'app01.apps.App01Config',
    'app02.apps.App02Config',
]

# apps.py
from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules

# Xadmin.py
class XadminConfig(AppConfig):
    name = 'Xadmin'
	"""
	启动 
	"""
	def ready(self):
        autodiscover_modules('Xadmin')


class ModelXadmin(object):
    def __init__(self,model,site):

        self.model=model
        self.site=site
	
	"""	
	url 分发
	二级分发和视图函数放在 配置类里面
	不放在 注册类里面的原因：
		因为注册类 单例生成 导致所有的注册表的self里面无法区分出来彼此的 配置类
		如果放在 配置类中 self 就是注册表自己对应的 配置类 根本拿不到想要的数据（比如 表 本身）
		比如 在 配置类 中 self.model 就是那个表，（在init 中注册的都可以随便拿来用了）
	""" 	
	def list_view(self, request):
        print("self.model",self.model)

        data_list=self.model.objects.all()
        print("data_list",data_list)
        return render(request, 'list_view.html',{"data_list":data_list})

    def add_view(self, request):
        return render(request, 'add_view.html')

    def change_view(self, request, id):
        return render(request, 'change_view.html')

    def delete_view(self, request, id):
        return render(request, 'delete_view.html')
	
	
	def get_urls2(self):
        temp = []
        temp.append(url(r"^$", self.list_view))
        temp.append(url(r"^add/$", self.add_view))
        temp.append(url(r"^(\d+)/change/$", self.change_view))
        temp.append(url(r"^(\d+)/delete/$", self.delete_view))
        return temp

    @property
    def urls2(self):
        return self.get_urls2(), None, None


class XadminSite(object):
    def __init__(self,name="admin"):
		self._registry={}
"""
注册 
"""		
    def register(self, model, admin_class=None, **options):
		if not admin_class:
			admin_class = Modeladmin
        self._registry[model] = admin_class(model, self) 

"""
url 分发
"""	


	def get_urls(self):
        temp = []
        for model, admin_class_obj in self._registry.items():
            app_name = model._meta.app_label
            model_name = model._meta.model_name
            temp.append(url(r'^{0}/{1}/'.format(app_name, model_name), admin_class_obj.urls2), )
		return temp
		
	@property
    def urls(self):
        return self.get_urls(),None,None
		
		
site=XadminSite()		

# url.py
from Xadmin.service.Xadmin import site
urlpatterns = [
    url(r'^admin/',  admin.site.urls),
    url(r'^Xadmin/', site.urls),
]


"""
其他的程序使用方式
"""

	"""
	启动
	"""
# setting.py
INSTALLED_APPS = [
    ...
    'app01.apps.App01Config',
    "app02.apps.App02Config"
]

# apps.py
from django.apps import AppConfig
class App01Config(AppConfig):
    name = 'app01'


# Xadmin.py
from Xadmin.service.Xadmin import site, ModelXadmin

	"""
	注册 
	"""	
site.register(Book, BookConfig)







