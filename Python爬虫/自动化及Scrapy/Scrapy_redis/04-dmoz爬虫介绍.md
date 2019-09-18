# Scrapy_redis之domz

## settings

```python
# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"#指定那个去重方法给request对象去重
SCHEDULER = "scrapy_redis.scheduler.Scheduler"   #指定scheduler队列
SCHEDULER_PERSIST = True   #队列中的内容是否持久保存，为False的时候在关闭redis时候情况redis
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    
    '''scrapy_redis实现items保存到redis的pipeline'''
    'scrapy_redis.pipelines.RedisPipeline': 400,     
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1


#方法一
REDIS_URL = 'redis://127.0.0.1:6379'   #redis数据库地址可以写成如下形式   
#方法二
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = '6379'
```

