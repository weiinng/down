---------scrapyd部署爬虫---------------
1.编写爬虫
2.部署环境
pip install scrapyd	
pip install scrapyd-client 
启动scrapyd的服务：cmd:>scrapyd
在爬虫根目录执行：scrapyd-deploy,如果提示不是内部命令，

3.发布工程到scrapyd
修改scrapy.cfg，去掉url前的#
进入到scrapy项目根目录，执行：scrapyd-deploy <target> -p <projectname>（target:spider.cfg中[deploy:NAME]）（projectname：spider.cfg中project = XXX）

4.启动爬虫
第一种方法：Django中view.py
class StartSpider(View):
    def get(self,request):
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyAbckg', 'spider': 'abckg'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result':'OK'})
第二种方法：（命令式启动爬虫：curl http://localhost:6800/schedule.json -d project=default -d spider=somespider）

5.启动django
cmd：python manage.py runserver

----------------scrapyd  管理爬虫接口----------------------
1、获取状态

http://127.0.0.1:6800/daemonstatus.json


2、获取项目列表

http://127.0.0.1:6800/listprojects.json


3、获取项目下已发布的爬虫列表

http://127.0.0.1:6800/listspiders.json?project=myproject


4、获取项目下已发布的爬虫版本列表
http://127.0.0.1:6800/listversions.json?project=myproject


5、获取爬虫运行状态

http://127.0.0.1:6800/listjobs.json?project=myproject


6、启动服务器上某一爬虫（必须是已发布到服务器的爬虫)
http://localhost:6800/schedule.json
(post方式，data={"project":myproject,"spider":myspider}）


7、删除某一版本爬虫

http://127.0.0.1:6800/delversion.json
(post方式，data={"project":myproject,"version":myversion}）


8、删除某一工程，包括该工程下的各版本爬虫
(运行中爬虫无法删除)
http://127.0.0.1:6800/delproject.json
(post方式，data={"project":myproject}）

9.取消运行中的爬虫
http://127.0.0.1:6800/cancel.json
(post方式，data={"project":myproject,"job":jobid}）


--------------django+scrapy-----------------------------
1.创建django项目，并编写models.py,启动django项目

2.Django项目根目录下创建Scrapy项目
（这是scrapy-djangoitem所需要的配置）
配置Django嵌入，在Scrapy的settings.py中加入以下代码：
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'django项目名.settings'
#   手动初始化Django：
import django
django.setup()

3.编写爬虫
4.item.py中引入Django模型类
pip install scrapy-djangoitem
from scrapy_djangoitem import DjangoItem
from app import models
class ScrapyabckgItem(DjangoItem):
    # 此处必须起名为django_model,主爬虫中使用item['title']=xxx
    django_model = models.AbckgModel

5.pipelines.py中调用save()
class ScrapyabckgPipeline(object):
    def process_item(self, item, spider):
        # 插入到数据库
        item.save()
        return  item #将item传给下一个管道继续处理

6.启动爬虫：scrapy  crawl  abckg
7.刷新django-admin后台
