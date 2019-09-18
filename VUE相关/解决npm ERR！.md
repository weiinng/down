### 解决npm ERR! Unexpected end of JSON input while parsing near的方法汇总

这两天执行 npm install 时会报错误：

```
npm ERR! Unexpected end of JSON input while parsing near
```

这个错误的解决方法有以下几种：

**1.删掉package.lock.json**

**2.清除cache**

```
npm cache clean --force
```

**3.进入下面这个文件夹清除cache**
路径：C:/Users/PC/AppData/Roaming/npm-cache
执行：

```
npm cache clean --force
```

**4.不要用淘宝镜像。**

```
npm set registry https://registry.npmjs.org/
```

其实我也没搞懂到底是什么问题造成的，有大神给解释一下？

参考资料：[https://github.com/vuejs-temp...](https://github.com/vuejs-templates/webpack/issues/990)