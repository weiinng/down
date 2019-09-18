import re
import requests


"""
密码加密了的时候
	找js 通过 python 实现加密方式
	直接把加密后的密文拿来用
"""

r1 = requests.get(
    url='https://passport.lagou.com/login/login.html',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
)

"""
	有两个奇怪的东西，是网站的防御机制
		这两个数据必然是对方发给我们的
		要不在响应头里面，要不在响应体里面
			响应头看不到。那就去响应体里面找。
"""

# 因为不是写在标签里面的。只能用正则来拿了
X_Anti_Forge_Token = re.findall("X_Anti_Forge_Token = '(.*?)'", r1.text, re.S)[0]
X_Anti_Forge_Code = re.findall("X_Anti_Forge_Code = '(.*?)'", r1.text, re.S)[0]
# print(X_Anti_Forge_Token, X_Anti_Forge_Code)

r2 = requests.post(
    url='https://passport.lagou.com/login/login.json',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'X-Anit-Forge-Code':X_Anti_Forge_Code,
        'X-Anit-Forge-Token':X_Anti_Forge_Token,
        'Referer': 'https://passport.lagou.com/login/login.html', # 上一次请求地址是什么？很多网站会要求带着个才可以继续
    },
    data={
        "isValidate": True,
        'username': '15131255089',
        'password': 'ab18d270d7126ea65915c50288c22c0d',	# 直接发密文了
        'request_form_verifyCode': '',
        'submit': ''
    },
    cookies=r1.cookies.get_dict()
)
print(r2.text)