---------scrapyd��������---------------
1.��д����
2.���𻷾�
pip install scrapyd	
pip install scrapyd-client 
����scrapyd�ķ���cmd:>scrapyd
�������Ŀ¼ִ�У�scrapyd-deploy,�����ʾ�����ڲ����

3.�������̵�scrapyd
�޸�scrapy.cfg��ȥ��urlǰ��#
���뵽scrapy��Ŀ��Ŀ¼��ִ�У�scrapyd-deploy <target> -p <projectname>��target:spider.cfg��[deploy:NAME]����projectname��spider.cfg��project = XXX��

4.��������
��һ�ַ�����Django��view.py
class StartSpider(View):
    def get(self,request):
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ScrapyAbckg', 'spider': 'abckg'}
        print(requests.post(url=url, data=data))
        return JsonResponse({'result':'OK'})
�ڶ��ַ�����������ʽ�������棺curl http://localhost:6800/schedule.json -d project=default -d spider=somespider��

5.����django
cmd��python manage.py runserver

----------------scrapyd  ��������ӿ�----------------------
1����ȡ״̬

http://127.0.0.1:6800/daemonstatus.json


2����ȡ��Ŀ�б�

http://127.0.0.1:6800/listprojects.json


3����ȡ��Ŀ���ѷ����������б�

http://127.0.0.1:6800/listspiders.json?project=myproject


4����ȡ��Ŀ���ѷ���������汾�б�
http://127.0.0.1:6800/listversions.json?project=myproject


5����ȡ��������״̬

http://127.0.0.1:6800/listjobs.json?project=myproject


6��������������ĳһ���棨�������ѷ�����������������)
http://localhost:6800/schedule.json
(post��ʽ��data={"project":myproject,"spider":myspider}��


7��ɾ��ĳһ�汾����

http://127.0.0.1:6800/delversion.json
(post��ʽ��data={"project":myproject,"version":myversion}��


8��ɾ��ĳһ���̣������ù����µĸ��汾����
(�����������޷�ɾ��)
http://127.0.0.1:6800/delproject.json
(post��ʽ��data={"project":myproject}��

9.ȡ�������е�����
http://127.0.0.1:6800/cancel.json
(post��ʽ��data={"project":myproject,"job":jobid}��


--------------django+scrapy-----------------------------
1.����django��Ŀ������дmodels.py,����django��Ŀ

2.Django��Ŀ��Ŀ¼�´���Scrapy��Ŀ
������scrapy-djangoitem����Ҫ�����ã�
����DjangoǶ�룬��Scrapy��settings.py�м������´��룺
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'django��Ŀ��.settings'
#   �ֶ���ʼ��Django��
import django
django.setup()

3.��д����
4.item.py������Djangoģ����
pip install scrapy-djangoitem
from scrapy_djangoitem import DjangoItem
from app import models
class ScrapyabckgItem(DjangoItem):
    # �˴���������Ϊdjango_model,��������ʹ��item['title']=xxx
    django_model = models.AbckgModel

5.pipelines.py�е���save()
class ScrapyabckgPipeline(object):
    def process_item(self, item, spider):
        # ���뵽���ݿ�
        item.save()
        return  item #��item������һ���ܵ���������

6.�������棺scrapy  crawl  abckg
7.ˢ��django-admin��̨
