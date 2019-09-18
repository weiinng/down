"""
restful协议

     ----  一切皆是资源,操作只是请求方式
	 
	 ----book表增删改查
	     /books/                 books
		 /books/add/             addbook
		 /books/(\d+)/change/    changebook
		 /books/(\d+)/delete/    delbook
		 
    ----book表增删改查
	     /books/     -----get            books      -----  返回当前所有数据
		 /books/     -----post           books      -----  返回提交数据 
		 
		 /books/(\d+)-----get            bookdetail -----  返回当前查看的单条数据 
		 /books/(\d+)-----put            bookdetail -----  返回更新数据 
		 /books/(\d+)-----delete         bookdetail -----  返回空

"""



from rest_framework.views import APIView

# 使用 
class PublishView(APIView):
    def get(self,request):
		...
		return ...

# 源码
class APIView(View):	# 继承原生的 View
	...
	def as_view(cls, **initkwargs):	# 重写了 as_view 方法 
	...
		return csrf_exempt(view)	# 返回的是 View 中的 view 方法 
		# view 会返回 dispatch，APIView类中有 dispatch ，因此会执行APIView类中的 
																									def dispatch(self, request, *args, **kwargs):	# 相当于重写了  View 中的 dispatch方法  
																										...
																										request = self.initialize_request(request, *args, **kwargs)	 # 重新定义了 request 
																										...
																										try:
																											self.initial(request, *args, **kwargs)		# 涉及初始化 认证，权限，频率组件 
																											if request.method.lower() in self.http_method_names:	# 根据拿到视图函数的 handler
																												handler = getattr(self, request.method.lower(),
																																  self.http_method_not_allowed)
																											else:
																												handler = self.http_method_not_allowed
																											response = handler(request, *args, **kwargs)	# 执行 handler() 
																										except Exception as exc:
																											response = self.handle_exception(exc)
																										self.response = self.finalize_response(request, response, *args, **kwargs)
																										return self.response	# 返回所有结果 
	def initialize_request(self, request, *args, **kwargs):	# 重新封装 APIView 自己的 request 
		...
		return Request(
			request,	# View 的request 作为参数传过去了
			...
		)	
# APIView 自己的 一个处理函数 
																		class Request(object):
																			...
																		self._request = request		# 将View 的request 封装成 _request
																	
# 版本控制代码 
def determine_version(self, request, *args, **kwargs):
	
	if self.versioning_class is None:
		return (None, None)
	scheme = self.versioning_class()									
	return (scheme.determine_version(request, *args, **kwargs), scheme)
																													def initial(self, request, *args, **kwargs):
																														# 版本控制操作 
																														version, scheme = self.determine_version(request, *args, **kwargs)
																														request.version, request.versioning_scheme = version, scheme
																														
																														# 认证，权限，频率 处理  
																														self.perform_authentication(request)
																														self.check_permissions(request)
																														self.check_throttles(request)

		
		
"""
于原生的 View 对比 
重写了 dispatch 方法 
重构了一个 request 
	原生的 request 可以用 request._request 调出来 
新增了 系列的方法和数据
	新增数据 request.data 用于取 post 数据
		View方式 对于 非urlencoded 的数据是无法解析序列化成字典的
		APIView方式 request.data 可以做到自动序列化并解析成字典
	覆盖原生的 get 数据请求方式 
		request.get  	APIView方式 获取get 数据
		request._request.get  	View方式获取get 数据


		
Django的原生request:
	get 请求必然是 urlencoded 类型 直接可以将后挂参数转换成字典保存在 request.get 中
	post 请求需要判断是否是 urlencoded 类型 urlencoded 类型才会转换成字典
	浏览器   -------------  服务器
	"GET url?a=1&b=2 http/1.1\r\user_agent:Google\r\ncontentType:urlencoded\r\n\r\n"
	"POST url http/1.1\r\user_agent:Google\r\ncontentType:urlencoded\r\n\r\na=1&b=2"
	request.body: a=1&b=2
	request.get:  a=1&b=2----->{"a":1,"b":2}
	request.POST: if contentType:urlencoded: a=1&b=2----->{"a":1,"b":2}



"""


# 使用的时候需要在setting 中注册一下，类似于app 的意思 
INSTALLED_APPS = [
    ...
    "rest_framework",
]


"""
serializers 序列化组件
可以实现很轻松的互相转换 

queryset/对象 -----> 序列化数据 
bs=BookModelSerializers(queryset,many=True)	# 对queryset 对象序列化
bs=BookModelSerializers(obj)				# 对 对象序列化

序列化数据 -----> queryset
bs=BookModelSerializers(data=request.data)	# 将序列化数据 转换成对象 

数据校验
bs.is_valid()

数据提交转换成记录 
 bs.save()
	不指定对象.create() 方法	bs=BookModelSerializers(data=request.data)	
	指定对象.updata() 方法 	bs=BookModelSerializers(book,data=request.data)	
	
"""

# rest_framework 的序列化方式
from rest_framework.response import Response
from rest_framework import serializers
class BookModelSerializers(serializers.ModelSerializer): # 类似于 modelform 一样的操作 
    class Meta:
        model = Book
        fields = "__all__" 
		# fields = ['publist','authors','title',]
		# 默认转换的时候普通字段没啥问题
		# title  = serializers.CharField  # 对于普通字段直接取即可    默认是 取 str(obj.title ) 
		# 对于一对一，一对多字段会有错误的显示
		# publish= serializers.CharField()  # 会显示对象
　　　　# publish_id = serializers.CharField()  # 会显示id 


	# 自定义对一对多字段处理 
    publish = serializers.CharField(source="publish.pk")  # 加 "source=" 取 str(obj.publish.pk )
	# 给字段的赋值一个 url 地址 
	publish=serializers.HyperlinkedIdentityField(
            view_name="detailpublish",	# 反向解析的 别名 
            lookup_field="publish_id",	# 找出来当前的 id 值 
			lookup_url_kwarg="pk"		# 将lookup_field 的值赋值给 url 中
		)
	# authors = serializers.SerializerMethodField(source='authors.all')  # 这样查多对多会查出来 queryset 对象


	# 自定义对多对多字段的处理
    authors = serializers.SerializerMethodField()  
	def get_authors(self,obj):						# 自定义多对多的处理 
	 	temp=[]
	 	for obj in obj.authors.all():
	 		temp.append(obj.name)
	 	return temp 
	# 如果自定义了字段的处理 ，需要重写 create 方法
	def create(self, validated_data):				 
		book=Book.objects.create(title=validated_data["title"],price=validated_data["price"],pub_date=validated_data["pub_date"],publish_id=validated_data["publish"]["pk"])
		book.authors.add(*validated_data["authors"])
		return book


 


class BookView(APIView):
    def get(self,request):		# 对所有数据进行查看
        book_list=Book.objects.all()
        bs=BookModelSerializers(book_list,many=True,context={'request': request})
        return Response(bs.data)
    def post(self,request):		# 对数据进行创建提交 
        # post请求的数据
        bs=BookModelSerializers(data=request.data)
        if bs.is_valid():
            print(bs.validated_data)
            bs.save()	# .create()方法
            return Response(bs.data)
        else:
            return Response(bs.errors)


class BookDetailView(APIView):

    def get(self,request,id):	# 对单条数据进行查看

        book=Book.objects.filter(pk=id).first()
        bs=BookModelSerializers(book,context={'request': request})
        return Response(bs.data)

    def put(self,request,id): # 对单条数据进行更新
        book=Book.objects.filter(pk=id).first()
        bs=BookModelSerializers(book,data=request.data)
        if bs.is_valid():
            bs.save()	 # .updata()
            return Response(bs.data)
        else:
            return Response(bs.errors)
	
	def delete(self,request,id):	# 删除数据 
        Book.objects.filter(pk=id).delete()
        return Response()



 
# 解析器 
# 默认 JSONParser FormParser MultiPartParser 已经足够用了
# 
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser,FileUploadParser
parser_classes = [JSONParser,FormParser]	# 会覆盖原有的解析器 



# url 控制  
from django.contrib import admin
from django.conf.urls import url,include
from rest_framework import routers
from app01 import views


# 注册前的准备，做一个实例化对象
routers=routers.DefaultRouter()
# 注册需要加两个参数  ("url前缀",视图函数)
routers.register("authors",views.AuthorModelView)
routers.register("books",views.AuthorModelView)
"""
会自动帮你生成 4 条 url 
^authors/$ [name='author-list']
^authors\.(?P<format>[a-z0-9]+)/?$ [name='author-list']
^authors/(?P<pk>[^/.]+)/$ [name='author-detail']	
^authors/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='author-detail']	# 相应器控制
"""

urlpatterns = [
    # url(r'^authors/$', views.AuthorModelView.as_view({"get":"list","post":"create"}),name="author"),
    # url(r'^authors/(?P<pk>\d+)/$', views.AuthorModelView.as_view({"get":"retrieve","put":"update","delete":"destroy"}),name="detailauthor"),

	# 上面的两条被简化成了下面一句话 
    url(r'', include(routers.urls)),
]



# 分页 
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

# 覆盖原有的基础参数，自定义分页参数，需要继承分页器类
	# PageNumberPagination 方式 分页器
class MyPageNumberPagination(PageNumberPagination):
        page_size = 1	# 每页显示数目	
        page_query_param = 'page'	# url 中的指定 关键字 
        page_size_query_param = "size"	# 允许临时添加的参数 
		max_page_size = 5	# 对临时添加数据的限制 

		"""
			关于临时添加参数
				 http://127.0.0.1:8000/?page=1&size=2
				 size 为临时添加数据 由 page_size_query_param 控制
				 max_page_size 控制 size 的限制 
		"""
	# LimitOffsetPagination 方式 分页器
class MyPageNumberPagination(LimitOffsetPagination):	
		default_limit=1	# 每页最多显示多少数目 关键词是 limit 
		"""
			LimitOffsetPagination 的分页器 拥有一个 offset 内置 参数
			http://127.0.0.1:8000/?limit=1&offset=2
			offst 表示向后偏移，偏移块大小为 limit的长度
			当前页1 limit=1 offset=2 表示向下偏移两个长度 显示第三页内容 
		"""

# 分页器的使用一：未封装起来的时候
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    def list(self,request,*args,**kwargs):
        book_list=Book.objects.all()
		# 调用分页器类实例化 （根据分页器类型要做区分）
        pp=LimitOffsetPagination()		
		# 对分页器对象赋值使用 实例化自定义分页类
			# 参数 queryset=被分页的queryset对象，后两个固定即可
        pager_books=pp.MyPageNumberPagination(queryset=book_list,request=request,view=self)
        bs=BookSerializers(pager_books,many=True)
        return pp.get_paginated_response(bs.data)


# 分页器的使用二：封装起来的时候
class AuthorModelView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializers	# 序列化组件
    pagination_class = MyPageNumberPagination	# 分页组件




# 响应器 
from rest_framework.response import  Response



# 渲染器
REST_FRAMEWORK = {
    # 关闭渲染器，只用json 的格式显示在当前页面
    # "DEFAULT_RENDERER_CLASSES": 'rest_framework.renderers.JSONRenderer',
	
	# 打开渲染器，
	"DEFAULT_RENDERER_CLASSES": ['rest_framework.renderers.JSONRenderer',
                                 'rest_framework.renderers.BrowsableAPIRenderer'],
}


# 版本控制
	# 1. 配置文件中加入
REST_FRAMEWORK = {
    # 全局配置版本
    # "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.QueryParameterVersioning",
    #     # 配置默认允许版本
    # "ALLOWED_VERSIONS": ["v1", "v2"],
    #     # 配置默认版本
    # "DEFAULT_VERSION": "v1",
    #     # 配置参数
    # "VERSION_PARAM": "version",

    # 还是推荐用 URLPathVersioning 的方式来控制版本更好用一些
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
}
	# 2. 设置路由 
urlpatterns = [
    url(r'^(?P<version>[v1|v2]+)/api/', include("api.urls")),
]
	# 3 获取版本
		request.version





