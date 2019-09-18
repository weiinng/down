""""""

# ################################### 示例一：爬取数据（携带请起头） ###################################
"""
import requests
from bs4 import BeautifulSoup

r1 = requests.get(
    url='https://dig.chouti.com/',
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
)

soup = BeautifulSoup(r1.text,'html.parser')

# 标签对象
# content_list = soup.find(name='div',id='content-list')
# find 取到第一个  find_all 取到所有 
content_list = soup.find(name='div',attrs={"id":"content-list"})

# [标签对象,标签对象]
item_list = content_list.find_all(name='div',attrs={'class':'item'})
for item in item_list:
    a = item.find(name='a',attrs={'class':'show-content color-chag'})
    print(a.text.strip())

"""
# ################################### 示例二：登陆点赞 ###################################
"""
import requests
# 1. 查看首页
r1 = requests.get(
    url='https://dig.chouti.com/',
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
)

# 2. 提交用户名和密码
r2 = requests.post(
    url='https://dig.chouti.com/login',
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    },
    data={
        'phone':'8613121758648',
        'password':'woshiniba',
        'oneMonth':1
    },
    cookies=r1.cookies.get_dict() 
	# 套路 正常用户必然会先访问首页然后再登陆
	# 如果你直接登陆必然是爬虫，因此设计在第一次访问首页的时候先创建cookie 并且返回了回去
	# 并且要求你第二次访问的时候要带着这个 cookie 
)

# 3. 点赞
r3 = requests.post(
    url='https://dig.chouti.com/link/vote?linksId=20435396',
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    },
    cookies=r1.cookies.get_dict()
)
print(r3.text)
"""

# ############## 方式二 session 方式 ##############
"""
# 用 session 自动封装好 cookie 不用在以后自己携带
import requests

session = requests.Session()
i1 = session.get(url="http://dig.chouti.com/help/service")
i2 = session.post(
    url="http://dig.chouti.com/login",
    data={
        'phone': "8615131255089",
        'password': "xxooxxoo",
        'oneMonth': ""
    }
)
i3 = session.post(
    url="http://dig.chouti.com/link/vote?linksId=8589523"
)
print(i3.text)
"""








