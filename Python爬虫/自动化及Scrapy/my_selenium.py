from selenium import webdriver
#初始化驱动器
driver  = webdriver.Chrome()

# #请求页面
# driver.get(url='https://www.baidu.com')
# #找到对应标签发送文本
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('我爱你！')
#
# driver.find_element_by_xpath('//*[@id="su"]').click()
#
# #获取页面内容
# content = driver.page_source
# print(content)

driver.get('https://www.autohome.com.cn/all/1/#liststart')


car_lis = driver.find_element_by_xpath('//*[@id="auto-channel-lazyload-article"]/ul[1]/li[1]')
for car_li in car_lis:
    pass












driver.quit()


