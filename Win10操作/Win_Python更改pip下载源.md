# Win系统下更改pip下载源：

## 解决方法一：

pip install <包名> -i http://pypi.douban.com/simple --trusted-host pypi.douban.com



## 解决方法二：

- 在当前用户目录下新建pip文件
- 在pip文件夹内 建立---> pip.ini

- 打开pip.ini  -->编辑

  ```
  [global]
  index-url = http://pypi.douban.com/simple
  trusted-host = pypi.douban.com
  ```

- 保存退出

接下来就可以正常使用pip命令了。

