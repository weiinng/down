# [Web性能压力测试之Webbench使用详解](https://www.cnblogs.com/fjping0606/p/5852049.html)

Webbench是知名的网站压力测试工具，它是由Lionbridge公司（http://www.lionbridge.com）开发。
Webbench能测试处在相同硬件上，不同服务的性能以及不同硬件上同一个服务的运行状况。webbench的标准测试可以向我们展示服务器的两项内容：每秒钟相应请求数和每秒钟传输数据量。webbench不但能具有便准静态页面的测试能力，还能对动态页面（ASP,PHP,JAVA,CGI）进 行测试的能力。还有就是他支持对含有SSL的安全网站例如电子商务网站进行静态或动态的性能测试。
Webbench最多可以模拟3万个并发连接去测试网站的负载能力。
官方主页：http://home.tiscali.cz/~cz210552/webbench.html
官方介绍：
Web Bench is very simple tool for benchmarking WWW or proxy servers. Uses fork() for simulating multiple clients and can use HTTP/0.9-HTTP/1.1 requests. This benchmark is not very realistic, but it can test if your HTTPD can realy handle that many clients at once (try to run some CGIs) without taking your machine down. Displays pages/min and bytes/sec. Can be used in more aggressive mode with -f switch.

### 1.WebBench安装

- yum install -y gcc ctags
- wget http://www.ha97.com/code/webbench-1.5.tar.gz
- tar zxvf webbench-1.5.tar.gz
- cd webbench-1.5
- make

- make install

### 2.WebBench使用

webbench -c 1000 -t 60 http://test.domain.com/phpinfo.php
webbench -c 并发数 -t 运行测试时间 URL

### 3.测试结果

当并发300时:
向http://test.domain.com/phpinfo.php发起300个线程请求，持续时间60秒

```
webbench -c 300 -t 60 http://test.domain.com/phpinfo.php
```

Webbench - Simple Web Benchmark 1.5
Copyright (c) Radim Kolar 1997-2004, GPL Open Source Software.

Benchmarking: GET http://test.domain.com/phpinfo.php
300 clients, running 60 sec.

Speed=24525 pages/min, 20794612 bytes/sec. 
Requests: 24525 susceed, 0 failed.	
速度：每秒钟响应请求数：24525 pages/min，每秒钟传输数据量20794612 bytes/sec.
返回数：24525次返回成功，0次返回失败

当并发1000时:

```
webbench -c 1000 -t 60 http://test.domain.com/phpinfo.php
```

Webbench - Simple Web Benchmark 1.5
Copyright (c) Radim Kolar 1997-2004, GPL Open Source Software.

Benchmarking: GET http://test.domain.com/phpinfo.php
1000 clients, running 60 sec.

Speed=24920 pages/min, 21037312 bytes/sec.
Requests: 24833 susceed, 87 failed.

当并发1000时，已经显示有87个连接failed了，说明超负荷了。

备注：
1、压力测试工作应该放到产品上线之前进行
2、测试时尽量跨公网模拟正式环境进行
3、测试时并发应当由小逐渐加大，比如并发100时观察一下网站负载是多少、打开是否流程，并发200时又是多少、网站打开缓慢时并发是多少、网站打不开时并发又是多少