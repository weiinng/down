```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 音悦台MV免积分下载
# By Tsing
# Python 2.7.9

import urllib2
import urllib
import re

mv_id = '2278607'   # 这里输入mv的id，即http://v.yinyuetai.com/video/2275893最后的数字

url = "http://www.yinyuetai.com/insite/get-video-info?flex=true&videoId=" + mv_id 
timeout = 30
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

req = urllib2.Request(url, None, headers)
res = urllib2.urlopen(req,None, timeout)
html = res.read()

reg = r"http://\w*?\.yinyuetai\.com/uploads/videos/common/.*?(?=&br)"
pattern=re.compile(reg)
findList = re.findall(pattern,html)     # 找到mv所有版本的下载链接

if len(findList) >= 3:  
    mvurl = findList[2]     # 含有流畅、高清、超清三个版本时下载超清
else:
    mvurl = findList[0]     # 版本少时下载流畅视频

local = 'MV.flv'

try:
    print 'downloading...please wait...'
    urllib.urlretrieve(mvurl,local)
    print "[:)] Great! The mv has been downloaded.\n"
except:
    print "[:(] Sorry! The action is failed.\n"
```

