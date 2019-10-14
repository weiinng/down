# Fastdfs

 fastdfs :  分布式文件存储系统，只要大于一台 机器就是分布式， 

 业务逻辑：两个服务 ， 一个是tracker ， 一个是storage （仓库）

 storage ：负责存储系统文件，存图片， 

 tracker ：负责调度， 把图片交给tracker ， tracker  自己自主分发，tracker把图片网址返回给上传的人，返回给tornado， 把唯一的网址存到数据库， 多一步。

这么做的好处就是server端动静分离，把静态文件剔除，分布式fastdfs 帮我处理静态文件，上传图片加一个fastdfs上传方式。背景就是随着server端，随着量越来越多，server端逐渐扛不住压力，不仅要抗json数据接口的压力，只要用户访问详情页，图片也访问server端， 所以要解耦， 动静分离 。 

VUE本身要做内部处理， 钩子方法，内部逻辑，在开发环境里会很慢，到生产环境会很快，最终生成静态页。

一个JPg就是一个HTTP请求， 大部分都是静态文件的请求， 这种请求和我们接口请求混在一起，都在访问server端， 造成巨大压力，server还得承担静态文件的压力， 其实server只处理逻辑就ok了，接口的压力只传json数据就ok了，为了解耦，用fastdfs  



fastdfs：分布式文件存储系统。有两个服务，一个是tracker ()另外一个是storage(仓库)，storage负责存图片，视频， 文件 ，tracker调度分发，tracker自己自主分发，tracker会把这个图片的网址返回给给上传的人，传统意义把图片名放到mysql数据库里，使用fastdfs会多了一步，fastdfs会把在tracker存储的url返回给tornado，tornado把完整的唯一的网址存入mysql数据库，这么做的好处是server端动静分离，把静态文件剔除，fastdfs 分布式多台服务器。



什么是分布式： 就是大于一台机器， 就是分布式



为什么要使用FASTDFS。(跟传统请求做对比)

传统文件上传步骤： client发送二进制流的请求 ， 把文件传到  server端，图片保存在server端， 保存在tornado项目里， 如果client端 vue展示的时候，需要继续向 server端发请求，server端以接口形式把图片地址返回给前端，地址还是tornado文件服务器的地址。在负载量高的情况下，会造成，图片的请求会越来越多，一张图片就是一个HTTP请求。







