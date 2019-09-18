## 创建Scrapy项目

在抓取之前，你需要新建一个Scrapy工程。进入一个你想用来保存代码的目录，然后执行：

```python
scrapy startproject my_scrapy
```

## 定义Item

Items是将要装载抓取的数据的容器，它工作方式像python里面的字典，但它提供更多的保护，比如对未定义的字段填充以防止拼写错误。

```python
from scrapy.item import Item, Field 
class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()
```

## 制作爬虫

```python
scrapy genspider my_gender www.baidu.com
```

## 运行爬虫

```python
scrapy crawl my_gender
```



## scrapy_redis

```python
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"   #指定那个去重方法给request对象去重
SCHEDULER = "scrapy_redis.scheduler.Scheduler"        #指定scheduler队列
SCHEDULER_PERSIST = True                  #队列中的内容是否持久保存，为False的时候在关闭redis时候情况redis
REDIS_URL = 'redis://127.0.0.1:6379'   #redis数据库地址可以写成如下形式
```





## scrapy-请求头

```python
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
```



## scrapy-图片下载路径

```python
IMAGES_STORE = "./image"  # 下载图片路径
```



## 允许中文写入

```python
FEED_EXPORT_ENCODING='utf-8'  # 允需写入中文
```



## 写入文件

```python
scrapy crawl qiche -o qichezhijia.csv   # 写入csv文件
scrapy crawl qiche -o qichezhijia.txt   # 写入txt文件
scrapy crawl qiche -o qichezhijia.json   # 写入json文件
```

