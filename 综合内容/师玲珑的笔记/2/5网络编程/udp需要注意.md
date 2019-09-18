udp=socket(AF_INET,SOCK_DGRAM)
接收数据是recvfrom 
需要两个参数接收，第一个是内容，第二个是ip地址和端口号
例如
r,ip=udp.recvfrom(1024)
1024代表最大接收字节数


encode('gbk')编码
decode('gbk')转码

发送sendto


