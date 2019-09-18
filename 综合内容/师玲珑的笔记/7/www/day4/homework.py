from selenium import webdriver
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pymongo import MongoClient

client=MongoClient(host='localhost',port=27017)
collection=client['test']['py']

driver=webdriver.Chrome()
driver.get(url='https://www.basketball-reference.com/leagues/NBA_2019.html')
name=driver.find_elements_by_xpath('//*[@id="team-stats-per_game"]//td[@data-stat="team_name"]/a')
three_shot=driver.find_elements_by_xpath('//*[@id="team-stats-per_game"]/tbody//td[@data-stat="fg3"]')
three_shot_get=driver.find_elements_by_xpath('//*[@id="team-stats-per_game"]/tbody//td[@data-stat="fg3a"]')
two_shot=driver.find_elements_by_xpath('//*[@id="team-stats-per_game"]/tbody//td[@data-stat="fg2"]')
two_shot_get=driver.find_elements_by_xpath('//*[@id="team-stats-per_game"]/tbody//td[@data-stat="fg2a"]')
list=[]
for x in range(len(three_shot)):
    dict={}
    dict['name'],name[x]=name[x].text,name[x].text
    dict['three_shot'],three_shot[x]=three_shot[x].text,three_shot[x].text
    dict['three_shot_get'],three_shot_get[x]=three_shot_get[x].text,three_shot_get[x].text
    dict['two_shot'],two_shot[x]=two_shot[x].text,two_shot[x].text
    dict['two_shot_get'],two_shot_get[x]=two_shot_get[x].text,two_shot_get[x].text
    list.append(dict)
for x in list:
    collection.insert_one(x)
# print(three_shot)
client.close()
driver.close()


