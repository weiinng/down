# 打包vue项目

1.找到vue项目中找到config下面的index.js

2.在index.js下找到第39行 将原来的 “../dist/index.html”     改成下方代码所示  需两处修改。

```
build: {
	// Template for index.html
	index: path.resolve(__dirname, './dist/index.html'),  #此处需要修改
	
	// Paths
        assetsRoot: path.resolve(__dirname, './dist'),   #此处需要修改
        assetsSubDirectory: 'static',
        assetsPublicPath: '/',

        /**
         * Source Maps
         */

        productionSourceMap: true,
        // https://webpack.js.org/configuration/devtool/#production
        devtool: '#source-map',
```

原理：这个理解为 当你运行npm run vue的时候  它会将你所有vue中的服务，所有的组件，所有的网页，打包成静态页， 这个静态页的位置，是跟config同级的dist。

3.将gitignore 第三行 “/dist/”  把前面那个“/”去掉    最后结果成  “dist/”

4.在上述工作完成后到你的vue项目根路径下  运行   npm run build 进行打包

5.执行下面两条命令，可以进到里面看有没有dist  

cd config 

cd dist

6 . 当 cd 进去之后  可以执行hs  自启一个web服务  访问一个纯静态一个网页 





