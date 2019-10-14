## 使用hexo搭建的博客常见问题及方法

* 关于图片展示的问题

  不能使用正常的MD格式图片展示，在网页上并不会展示，资源无法正常加载。我们使用如下方法：

  1.在根目录下的配置文件    **_config.yml **  中的  **post_asset_folder**   改为  true 。

  这样在建立文件时，`Hexo`会自动建立一个与文章同名的文件夹，这样就可以把与该文章相关的所有资源（图片）都放到那个文件夹里方便后面引用。

  2.在根目录打开git bash安装插件  

  ```python
  npm install https://github.com/7ym0n/hexo-asset-image --save
  ```

  （这是个修改过的插件，经测试无问题），使用这个插件来引入图片，而不是用传统md语法相对路径的方法。 

  3.插入图片使用如下格式：

  ```python
  {% asset_img 月.jpg This is an test image %}
  ```

  解读：月.jpg 是你要引用的图片，  后面的This is an test image是对于图片的描述，可以自行更改。

  接下来就进行

  ```python
  hexo clean 
  
  hexo g 
  
  hexo d
  ```

  是不是很神奇，图片能出来了，哈哈哈哈哈哈哈哈！



* 关于文章下面显示的标签问题

  ```python
  title: 123
  date: 2019-09-03 21:13:29
  tags:
      - 随记
  ```

​	创建的文章都会有这样的头部，在tags中写入你想选择的分类即可。



* **所有文章**  功能不可用，不显示。

  1、确保自己的node版本大于9

  2、在博客根目录执行

  ```python
  npm i hexo-generator-json-content --save
  ```

  3、在根目录的配置文件   **_config.yml **  加入以下内容

  ```python
  jsonContent:
      meta: false
      pages: false
      posts:
        title: true
        date: true
        path: true
        text: false
        raw: false
        content: false
        slug: false
        updated: false
        comments: false
        link: false
        permalink: false
        excerpt: false
        categories: false
        tags: true
  ```

  