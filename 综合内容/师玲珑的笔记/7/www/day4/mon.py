from pymongo import MongoClient
from matplotlib  import pyplot as plt 

client=MongoClient(host='localhost',port=27017)
collection=client['test']['py']

ret=collection.find()

three_shot,three_shot_get,two_shot,two_shot_get=[],[],[],[]
for x in ret:
    three_shot.append(float(x['three_shot']))
    three_shot_get.append(float(x['three_shot_get']))
    two_shot.append(float(x['two_shot']))
    two_shot_get.append(float(x['two_shot_get']))

plt.scatter(three_shot,three_shot_get,c='red')
plt.scatter(two_shot,two_shot_get,c='yellow')
plt.show()
# print(three_shot)
# print(three_shot_get)
# print(two_shot)
# print(two_shot_get)
client.close()
