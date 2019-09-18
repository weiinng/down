```
gitbook init  //初始化目录文件
gitbook help  //列出gitbook所有的命令
gitbook --help  //输出gitbook-cli的帮助信息
gitbook build  //生成静态网页
gitbook serve //生成静态网页并运行服务器
gitbook build --gitbook=2.0.1 //生成时指定gitbook的版本, 本地没有会先下载
gitbook ls //列出本地所有的gitbook版本
gitbook ls-remote //列出远程可用的gitbook版本
gitbook fetch 标签/版本号 //安装对应的gitbook版本
gitbook update //更新到gitbook的最新版本
gitbook uninstall 2.0.1 //卸载对应的gitbook版本
gitbook build --log=debug //指定log的级别
gitbook builid --debug //输出错误信息
```

## GitBook 的使用笔记

因为近期想翻译一些英文技术文档和英文技术书籍，需要左右带有目录栏的电子书籍格式，所以找到了 GitBook。

GitBook 是目前最流行的开源书籍写作方案，下面记录一下初次集成使用过程。

本文介绍的是命令行工具使用 GitBook.

### 本地通过 NPM 安装 GitBook 命令行工具

运行下面的命令进行安装

```
$ npm install gitbook-cli -g
```

其中 gitbook-cli 是 gitbook 的一个命令行工具, 通过它可以在电脑上安装和管理 gitbook 的多个版本.

BUT 执行上述命令，我的终端报错：

```
npm WARN  checkPermissions Missing write access to /usr/local/lib/node_modules
npm ERR! path /usr/local/lib/node_modules
npm ERR! code EACCES
npm ERR! errno -13
npm ERR! syscall access
npm ERR! Error: EACCES: permission denied, access '/usr/local/lib/node_modules'
npm ERR!  { Error: EACCES: permission denied, access '/usr/local/lib/node_modules'
npm ERR!   stack: 'Error: EACCES: permission denied, access \'/usr/local/lib/node_modules\'',
npm ERR!   errno: -13,
npm ERR!   code: 'EACCES',
npm ERR!   syscall: 'access',
npm ERR!   path: '/usr/local/lib/node_modules' }
npm ERR! 
npm ERR! Please try running this command again as root/Administrator.
```

报错原因是：Mac 安装 npm 的全局包，报错没有权限。

解决方法：在安装命令前加上sudo,输入用户的登陆密码，提升权限进行安装。

```
$ sudo npm install gitbook-cli -g
```

安装成功后，执行`gitbook -V`查看版本信息。此命令会默认同时安装 GitBook。

至此，安装成功。

### GitBook 创建以及预览

#### 1.初始化

1. 打开一个文件夹 MyGitBook，使用 `gitbook init` 初始化文件夹，会自动生成两个必要的文件 README.md 和 SUMMARY.md。

```
$ gitbook init
```

-  **README.md**:  书的介绍文字，如前言、简介，在章节中也可做为章节的简介。
-  **SUMMARY.md**: 定制书籍的章节结构和顺序。

README.md 和 SUMMARY.md 是 GitBook 制作电子书的必要文件，可用 gitbook init 命令自动生成。

1. 在 MyGitBook 文件夹下面增加其他章节下的文件，文件目录如下：



![img](https:////upload-images.jianshu.io/upload_images/2423912-b5d71c6b3f56a937.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/528/format/webp)

文件目录

1. GitBook 使用 SUMMARY.md 文件作为书籍的目录结构，可以用来制作书籍目录。

```
// SUMMARY.md

# Summary
* [Introduction](README.md)
* Part I
    * [从命令行进行测试](Chapter1/CommandLine.md)
    * [Monkey](Chapter1/Monkey.md)
    * [monkeyrunner 参考](Chapter1/MonkeyrunnerReference.md)
        * [概览](Chapter1/MonkeyrunnerSummary.md)
        * [MonkeyDevice](Chapter1/MonkeyDevice.md)
        * [MonkeyImage](Chapter1/MonkeyImage.md)
        * [MonkeyRunner](Chapter1/MonkeyRunner.md)
* Part II
    * [Introduction](Chapter2/c1.md)
    * [Introduction](Chapter2/c2.md)
    * [Introduction](Chapter2/c3.md)
    * [Introduction](Chapter2/c4.md)
```

#### 2.预览

1. 执行命令 gitbook serve ，gitbook 会启动一个 4000 端口用于预览。

```
$ gitbook serve
```

你可以你的浏览器中打开这个网址： [http://localhost:4000](http://localhost:4000/)  预览电子书效果。



![img](https:////upload-images.jianshu.io/upload_images/2423912-6eb524fef2ea83e6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

预览效果

1. 第二种预览方式，运行 gitbook build 命令后会在书籍的文件夹中生成一个 _book 文件夹, 里面的内容即为生成的 html 文件. 我们可以使用下面命令来生成网页而不开启服务器。

```
$ gitbook build
```

另外，如果想发布在 [GitBook.com](http://GitBook.com) ,可以参考：https://segmentfault.com/a/1190000015012209

> 注意⚠️
>  当出现执行 gitbook serve 后报错找不到 fontsettings.js ，谷歌了一下，有 [issue](https://github.com/GitbookIO/gitbook-cli/issues/55) 在反应这个问题。
>  其他人的解决办法是降低版本，比如我的版本是`GitBook version: 3.2.3` 切换至 2.6.7~2.6.4 即可解决。我不倾向降版本。
>
> > 我个人的解决办法是：如果执行 gitbook serve 后报上述错，那么先执行一次 `gitbook build` ,成功后再执行 gitbook serve 就不会报错找不到 fontsettings.js 了。

### GitBook 插件

当遇到「左侧的目录折叠」这种需求的时候，就用到 GitBook 插件了。

官方获取插件地址： https://plugins.gitbook.com/

#### 安装插件

安装插件只需要在书籍目录下增加 `book.json` 文件，例如增加[ 折叠目录 ](https://plugins.gitbook.com/plugin/expandable-chapters-small)的插件，需要在 book.json 内增加下面代码:

```
{
    "plugins": ["expandable-chapters-small"],
    "pluginsConfig": {
        "expandable-chapters-small":{}
    }
}
```

然后终端执行 install 来安装插件即可：

```
$ gitbook install
```

## 其他链接

1. 去官网注册 GitBook。[官网链接>>](https://www.gitbook.com)
2. 本地安装 GitBook 客户端。 [客户端下载链接>>](http://www.pc6.com/mac/238113.html)

参考：

- [gitbook新版本 build命令导出的html不能跳转?](https://blog.csdn.net/qi_ruihua/article/details/80026160)