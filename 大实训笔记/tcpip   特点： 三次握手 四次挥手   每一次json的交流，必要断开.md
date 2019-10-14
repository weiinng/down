tcp/ip   特点： 三次握手 四次挥手   每一次json的交流，必要断开

websocked  支持持久连接   实时数据（K线图） 轮询  每一次发一次请求。

tornado  自带websocked模块  



from tornado.websocked import webSocketHandler





