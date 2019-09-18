# 实战vultr搭建SSR+锐速——超速看youtube1080p

[TOC]

今天带大家使用VULTR的服务器实战搭建自己的科学上网服务器来科学上网——ShadowsocksR。文章内有视频教程以及所需资源下载地址，实战视频教程可下载可在线观看。 

## 第一步：购买服务器

**准备：** 

1. **支付宝**（用于支付） 
2. win10 Micsoft Edge浏览器（翻译功能比较好） 

目前vultr已全面**支持支付宝**，比PayPal更便宜。

详细请点击：<https://www.qcgzxw.com/2293.html> 

`请大家不要买2.5$的服务器，2.5$的没有IPV4地址，用不了 `

- 打开链接注册 [充值10美元送25美元](https://www.qcgzxw.cn/go/vultr)（**限时活动**，只有通过本链接注册，才会有**充值$10送$25**的奖励）

- 打开链接注册[点我充值10美元送10美元](https://www.qcgzxw.cn/go/vultr)（长期活动 只有通过本链接注册，才会有**充值$10送$10**的奖励）

- 注册后就充值，由于有活动，通过上面的链接注册充值10美元会送25美元，这样我们的账户就有35美元，足够用大半年了。

  

### 服务器选购

![](img\ssr1.png)

![](img\ssr2.jpg)

![](img\ssr3.png)

![](img\ssr4.png)

--------

## 连接到服务器

```
准备：
1.XShell（for windows）| juiceSSH（for Android）
```

### XShell

 云盘下载  https://freed.ga/Xshell%206/

### juiceSSH

本地下载：http://acj3.pc6.com/pc6_soure/2017-10/com.sonelli.juicessh_116.apk

### 连接到服务器

![](img\ssr5.jpg)



![](img\ssr6.jpg)



![](img\ssr7.jpg)

![](img\ssr8.jpg)



## 安装SSR

执行以下命令

```
wget --no-check-certificate https://freed.ga/github/shadowsocksR.sh; bash shadowsocksR.sh
```

如提示 :

`wget :command not found `

请先执行 

```
yum install wget -y
```

然后按提示操作。 

![](img\ssr9.jpg)

![](img\ssr10.jpg)



## 相关文章

详细步骤请移步<https://www.qcgzxw.com/533.html>
 安装成功后就能通过ssr客户端连接服务器科学上网了
 SSR各平台客户端下载请移步<https://www.qcgzxw.com/301.html>
 SSTap,网游代理工具<https://www.qcgzxw.com/2299.html>

-----------------

`到这里一个能科学上网的服务器就搭建完成了，大家下载SSR客户端连接就能科学上网 可是网速虽然可以，但是youtube只能流畅的看720P 如果你的目标是1080P，请继续往下看 `



在线文档： <https://freed.ga/book/Vultr_SSR.pdf> 下载地址： 

微信关注公众号小文me，回复视频获取完整视频教程，小文手把手教你搭建。 ![img](https://img.qcgzxw.cn/wp-content/uploads/2018/05/5a50d3e7d7360-1.jpg)  







## 破解版锐速安装

### 一键更换内核脚本（Vultr需先执行此脚本）

```
wget -N --no-check-certificate https://freed.ga/kernel/ruisu.sh && bash ruisu.sh
```

脚本执行过程中，请勿进行任何操作。待服务器重启后，重新连接安装锐速即可。

###  锐速安装脚本

```
wget -N --no-check-certificate https://github.com/91yun/serverspeeder/raw/master/serverspeeder.sh && bash serverspeeder.sh
```

若提示：The name of network interface is not eth0, please retry after changing the name.请使用备用脚本

### 备用脚本

```
wget -N --no-check-certificate https://raw.githubusercontent.com/91yun/serverspeeder/master/serverspeeder-all.sh && bash serverspeeder-all.sh
```

成功截图：

![](img\速锐成功截图.png)

--------------

## 成功图

![](img\成功图1.png)

![](img\成功图2.jpg)

------

`如果搭建碰到问题可以留言，博主会处理的！ `

## 服务器推荐（定时更新排名）

### 科学上网服务器性价比排行（高网速）

### 阿里云（香港）

月付24元的阿里云轻量云服务器
月流量1T，30M带宽
IP段（购买前先ping下看看延迟）
149.129.82.*
149.129.88.*

详情地址:<https://www.qcgzxw.com/2945.html>

 

### Vultr（日本 美国）

 

https://www.qcgzxw.cn/go/vultr

优势：`100M大带宽`（实测5-6m/s）  |  超低价2.5$套餐500G流量 |  支持`支付宝`、PayPal、信用卡  |  可联系客服退款 | 按小时计费，随时换IP

缺点：工单最好提交晚上（时差）。日本机房基本没活。强烈建议日本机房5$/月。

小文点评：明显超售了，晚上网络差，电信网络差，移动联通可以考虑。个人建议日本机房5$。
 另外有个无限流量的小彩蛋，移步——》<https://www.qcgzxw.com/2210.html#toc-4>

## 服务器无法连接（被墙）解决方案

若你的服务器表现为：
 1.Xshell无法连接，或者连接超时
 2.ping超时

你可能需要看看下面的文章
 [VULTR服务器被墙解决方案](https://www.qcgzxw.com/2522.html)

## Vultr各机房测速

| 机房位置                                    | 主机名称（做ping测试）   | 各机房数据包下载测试                                         |
| ------------------------------------------- | ------------------------ | ------------------------------------------------------------ |
| (Asia) Tokyo, Japan / Vultr日本机房         | hnd-jp-ping.vultr.com    | [100Mb](http://hnd-jp-ping.vultr.com/vultr.com.100MB.bin)   [1000Mb](http://hnd-jp-ping.vultr.com/vultr.com.1000MB.bin) |
| (AU) Sydney, Australia /  Vultr澳大利亚机房 | syd-au-ping.vultr.com    | [100Mb](http://syd-au-ping.vultr.com/vultr.com.100MB.bin)   [1000Mb](http://syd-au-ping.vultr.com/vultr.com.1000MB.bin) |
| (EU) Frankfurt, DE /  Vultr德国机房         | fra-de-ping.vultr.com    | [100Mb](http://fra-de-ping.vultr.com/vultr.com.100MB.bin)   [1000Mb](http://fra-de-ping.vultr.com/vultr.com.1000MB.bin) |
| (EU) Amsterdam, NL / Vultr荷兰机房          | ams-nl-ping.vultr.com    | [100Mb](http://ams-nl-ping.vultr.com/vultr.com.100MB.bin)   [1000Mb](http://ams-nl-ping.vultr.com/vultr.com.1000MB.bin) |
| Seattle, Washington  / Vultr西雅图机房      | wa-us-ping.vultr.com     | [100Mb](http://wa-us-ping.vultr.com/vultr.com.100MB.bin)   [1000Mb](http://wa-us-ping.vultr.com/vultr.com.1000MB.bin) |
| (EU) London, UK / Vultr伦敦                 | lon-gb-ping.vultr.com    | [100Mb](http://lon-gb-ping.vultr.com/vultr.com.100MB.bin)   [1000Mb](http://lon-gb-ping.vultr.com/vultr.com.1000MB.bin) |
| (EU) Paris, France / Vultr法国巴黎机房      | par-fr-ping.vultr.com    | [100Mb](http://par-fr-ping.vultr.com/vultr.com.100MB.bin)   [1000Mb](http://par-fr-ping.vultr.com/vultr.com.1000MB.bin) |
| Silicon Valley, California / Vultr硅谷机房  | sjo-ca-us-ping.vultr.com | [100Mb](http://sjo-ca-us-ping.vultr.com/vultr.com.100MB.bin)   [1000Mb](http://sjo-ca-us-ping.vultr.com/vultr.com.1000MB.bin) |
| Los Angeles, California / Vultr洛杉矶机房   | lax-ca-us-ping.vultr.com | [100Mb](http://lax-ca-us-ping.vultr.com/vultr.com.100MB.bin)   [1000Mb](http://lax-ca-us-ping.vultr.com/vultr.com.1000MB.bin) |
| Chicago, Illinois / Vultr芝加哥机房         | il-us-ping.vultr.com     | [100Mb](http://il-us-ping.vultr.com/vultr.com.100MB.bin)   [1000Mb](http://il-us-ping.vultr.com/vultr.com.1000MB.bin) |
| Dallas, Texas / Vultr达拉斯机房             | tx-us-ping.vultr.com     | [100Mb](http://tx-us-ping.vultr.com/vultr.com.100MB.bin)   [1000Mb](http://tx-us-ping.vultr.com/vultr.com.1000MB.bin) |
| New York / New Jersey / Vultr纽约机房       | nj-us-ping.vultr.com     | [100Mb](http://nj-us-ping.vultr.com/vultr.com.100MB.bin)   [1000Mb](http://nj-us-ping.vultr.com/vultr.com.1000MB.bin) |
| Atlanta, Georgia / Vultr亚特兰大机房        | ga-us-ping.vultr.com     | [100Mb](http://ga-us-ping.vultr.com/vultr.com.100MB.bin)   [1000Mb](http://ga-us-ping.vultr.com/vultr.com.1000MB.bin) |
| Miami, Florida / Vultr迈阿密机房            | fl-us-ping.vultr.com     | [100Mb](http://fl-us-ping.vultr.com/vultr.com.100MB.bin)   [1000Mb](http://fl-us-ping.vultr.com/vultr.com.1000MB.bin) |

## 进阶脚本命令

### SSR脚本命令合集

启动: /etc/init.d/shadowsocks start
停止: /etc/init.d/shadowsocks stop
重启: /etc/init.d/shadowsocks restart
查看状态: /etc/init.d/shadowsocks status

PS：ssr脚本自己会开机自启，锐速不会开机自启。服务器重启后，锐速需要手动启动

### 锐速脚本命令合集

启动：service serverSpeeder start
停止：service serverSpeeder stop
重启: service serverSpeeder restart
查看状态: service serverSpeeder status