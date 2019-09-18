# Linux下安装npm

```
curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -
yum install -y nodejs
npm install -g cnpm --registry=https://registry.npm.taobao.org
npm install
npm run build
npm -v
```





# docsify的安装

```
npm i docsify-cli -g
```

```
docsify serve ./
```

## 1、安装Nodejs

　　官网地址为http://nodejs.org

　　但国外地址下载太慢了，建议从淘宝下载（https://npm.taobao.org/mirrors/node/）

```
wget https://npm.taobao.org/mirrors/node/latest-v4.x/node-v4.4.7-linux-x64.tar.gz
```

　　解压：

```
tar -zxvf node-v4.4.7-linux-x64.tar.gz
```

　　设置环境变量：

```
export PATH=$PATH:/opt/node-v4.4.7-linux-x64/bin
```

 

 

## 2、安装NMP

　　下载nmp安装包，一般nodejs包中已经包含了，设置过环境变量就可以直接使用nmp命令了，如果没有安装，先下载：

　　官网地址:www.npmjs.com 

　　淘宝地址：https://npm.taobao.org/mirrors/npm/

　　安装使用如下命令：

```
node cli.js install npm -gf  
```

 

## 3、安装CNMP（非必要）

　　由于NMP源都在国外，下载相关资源很慢，所以建议用国内的淘宝NPM镜像（http://npm.taobao.org/）

　　通过cnmp命令安装的包都会从淘宝NMP下载，速度很快。　　

```
$ npm install -g cnpm --registry=https://registry.npm.taobao.org
```

　　安装完之后，安装模块的命令就变为：

```
$ cnpm install [name]
```

　　同步模块命令为：

```
$ cnpm sync connect
```