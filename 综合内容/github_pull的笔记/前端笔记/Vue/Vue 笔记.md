npm init --yes 初始化项目 自动生成一个 package.json 文件
npm rebuild  拿到别人的项目环境不一致导致报错的时候可以先重建一下环境
npm install 下载所有的依赖包 
npm install jquery --save 下载依赖包
npm run build  打包生成静态文件夹
npm run dev  启动项目
npm start  启动项目


npm install -g cnpm --registry=https://registry.npm.taobao.org	更改为淘宝镜像
cnpm install -g vue-cli  安装 vue-cli  vue -V 查看版本 


vue list
	C:\Users\羊驼仙人>vue list

	  Available official templates:

	  ★  browserify - A full-featured Browserify + vueify setup with hot-reload, linting & unit testing.
	  ★  browserify-simple - A simple Browserify + vueify setup for quick prototyping.
	  ★  pwa - PWA template for vue-cli based on the webpack template
	  ★  simple - The simplest possible Vue setup in a single HTML file
	  ★  webpack - A full-featured Webpack + vue-loader setup with hot reload, linting, testing & css extraction.
	  ★  webpack-simple - A simple Webpack + vue-loader setup for quick prototyping.

创建 webpack  项目
F:\yangtuo>vue init webpack

? Generate project in current directory? Yes
'git' �����ڲ����ⲿ���Ҳ���ǿ����еĳ���
���������ļ���
? Project name yangtuo
? Project description A Vue.js project
? Author
? Vue build standalone
? Install vue-router? Yes
? Use ESLint to lint your code? No
? Set up unit tests No
? Setup e2e tests with Nightwatch? No
? Should we run `npm install` for you after the project has been created? (recommended) npm

   vue-cli · Generated "luffy_city".


# Installing project dependencies ...



C:\Users\羊驼仙人\Desktop\study\02>

指令系统
v-if    存在
v-show 	显示
v-bind 	绑定属性
v-on 	绑定事件
v-for 	循环遍历
v-html 	插入标签
v-model 双向绑定数据


设计模式 23种
MVC MVVM MVT


Vue 中 图片也可以被作为变量


npm install bootstrap@3 --save
    下载bootsatrap 的时候要下3版本的。下4版本有问题
    页面使用的时候也会有问题，最好还是用cdn 导入比较方便
<link href="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
import 'bootstrap/dist/css/bootstrap.min.css'   // 引入的时候前面不要加 ./ 会报错的



data(){
       return { }
    }
methods:{ }
computed (){ }
components:{ }
created(){ }






