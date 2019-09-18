# 使用Hexo建立一个轻量、简易、高逼格的博客

    在之前的一篇文章中，介绍了如何使用Hugo在[三分钟之内建立一个简单的个人博客系统](https://v3u.cn/a_id_81)，它是基于go lang的，其实，市面上还有一款类似的静态页生成器，就是Hexo 读音/hækso/ ，它是基于node.js的，和Hugo一样，Hexo 正常来说，不需要部署到我们的服务器上，我们的服务器上保存的，其实是基于在hexo通过markdown编写的文章，然后hexo帮我们生成静态的html页面，然后，将生成的html上传到我们的服务器。简而言之：hexo是个静态页面生成、上传的工具。 

首先安装Hugo，在此之前，请确保电脑里已经安装好新版的node.js 

```
npm install -g hexo-cli
```

 如果感觉安装速度比较慢，可以为npm指定国内的源 

```
npm config set registry https://registry.npm.taobao.org
```

安装完成后，创建博客项目

```
hexo init blog
```



# 安装 NexT 主题

## NexT 入门

- 官方文档 [NexT 入门](http://theme-next.iissnan.com/getting-started.html)
- 下载 NexT 主题

将主题克隆到 themes 目录下，以下截图就是 clone 之后的结果。

```
$ cd <博客存放的目录>
$ git clone https://github.com/iissnan/hexo-theme-next themes/next
ps : git clone <博客主题的链接> themes/next
```

 

 

 

 

 

