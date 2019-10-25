在开发时候，我们都是在本地进行代码编译等，使用的都是localhost作为IP地址进行测试访问。但是，如果别人也想访问我们的web，那么就需要修改一下IP地址。

#### 不多说直接代码：

```python
# vue文件根目录 config文件夹 index.js文件
# host 地址改为 0.0.0.0  即所有人可以访问
host: '0.0.0.0', // can be overwritten by process.env.HOST

```

