# axios

## 什么是 axios？

Axios 是一个基于 promise 的 HTTP 库，可以用在浏览器和 node.js 中。

## 特性

- 从浏览器中创建 [XMLHttpRequests](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)
- 从 node.js 创建 [http](http://nodejs.org/api/http.html) 请求
- 支持 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) API
- 拦截请求和响应
- 转换请求数据和响应数据
- 取消请求
- 自动转换 JSON 数据
- 客户端支持防御 [XSRF](http://en.wikipedia.org/wiki/Cross-site_request_forgery)

## 安装

使用 npm:

```
$ npm install axios
```

使用 bower:

```
$ bower install axios
```

使用 cdn:

```
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

## 案例

执行 `GET` 请求

```

```

执行 `POST` 请求 

```

```

执行多个并发请求 

```

```

## axios API

可以通过向 `axios` 传递相关配置来创建请求

##### axios(config)

```

```

```
// 获取远端图片
axios({
  method:'get',
  url:'http://bit.ly/2mTM3nY',
  responseType:'stream'
})
  .then(function(response) {
  response.data.pipe(fs.createWriteStream('ada_lovelace.jpg'))
});
```

### 请求方法的别名

为方便起见，为所有支持的请求方法提供了别名

##### axios.request(config)

##### axios.get(url[, config])

##### axios.delete(url[, config])

##### axios.head(url[, config])

##### axios.options(url[, config])

##### axios.post(url[, data[, config]])

##### axios.put(url[, data[, config]])

##### axios.patch(url[, data[, config]])

###### 注意

在使用别名方法时， `url`、`method`、`data` 这些属性都不必在配置中指定。

### 并发

处理并发请求的助手函数

##### axios.all(iterable)

##### axios.spread(callback)

### 创建实例

可以使用自定义配置新建一个 axios 实例

##### axios.create([config])

## 请求配置

这些是创建请求时可以用的配置选项。只有 `url` 是必需的。如果没有指定 `method`，请求将默认使用 `get`方法。

 `{   // `url` 是用于请求的服务器 URL  url: '/user',`

```

```

## 响应结构

某个请求的响应包含以下信息

```
{
// `data` 由服务器提供的响应
  data: {},

  // `status` 来自服务器响应的 HTTP 状态码
  status: 200,

  // `statusText` 来自服务器响应的 HTTP 状态信息
  statusText: 'OK',

  // `headers` 服务器响应的头
  headers: {},

   // `config` 是为请求提供的配置信息
  config: {},
 // 'request'
  // `request` is the request that generated this response
  // It is the last ClientRequest instance in node.js (in redirects)
  // and an XMLHttpRequest instance the browser
  request: {}
}
```

使用 `then` 时，你将接收下面这样的响应 : 

```
axios.get('/user/12345')
  .then(function(response) {
    console.log(response.data);
    console.log(response.status);
    console.log(response.statusText);
    console.log(response.headers);
    console.log(response.config);
  });
```

在使用 `catch` 时，或传递 [rejection callback](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) 作为 `then` 的第二个参数时，响应可以通过 `error` 对象可被使用，正如在[错误处理](https://www.kancloud.cn/yunye/axios/234845#handling-errors)这一节所讲。 

## 配置默认值

你可以指定将被用在各个请求的配置默认值

### 全局的 axios 默认值

```

```

### 自定义实例默认值

```
// Set config defaults when creating the instance
const instance = axios.create({
  baseURL: 'https://api.example.com'
});
// Alter defaults after instance has been created
instance.defaults.headers.common['Authorization'] = AUTH_TOKEN;

```

### 配置的优先顺序

配置会以一个优先顺序进行合并。这个顺序是：在 `lib/defaults.js` 找到的库的默认值，然后是实例的 `defaults` 属性，最后是请求的 `config` 参数。后者将优先于前者。这里是一个例子：

```

```

## 拦截器

在请求或响应被 `then` 或 `catch` 处理前拦截它们。

```

```

如果你想在稍后移除拦截器，可以这样： 

```

```

可以为自定义 axios 实例添加拦截器 

```
const instance = axios.create();
instance.interceptors.request.use(function () {/*...*/});

```

## 错误处理

```
axios.get('/user/12345')
  .catch(function (error) {
    if (error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      console.log(error.response.data);
      console.log(error.response.status);
      console.log(error.response.headers);
    } else if (error.request) {
      // The request was made but no response was received
      // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
      // http.ClientRequest in node.js
      console.log(error.request);
    } else {
      // Something happened in setting up the request that triggered an Error
      console.log('Error', error.message);
    }
    console.log(error.config);
  });
  
```

Y可以使用 `validateStatus` 配置选项定义一个自定义 HTTP 状态码的错误范围。 

```
axios.get('/user/12345', {
  validateStatus: function (status) {
    return status < 500; // Reject only if the status code is greater than or equal to 500
  }
})
```

## 取消

使用 *cancel token* 取消请求

Axios 的 cancel token API 基于[cancelable promises proposal](https://github.com/tc39/proposal-cancelable-promises)，它还处于第一阶段。 

可以使用 `CancelToken.source` 工厂方法创建 cancel token，像这样： 

```
const CancelToken = axios.CancelToken;
const source = CancelToken.source();

axios.get('/user/12345', {
  cancelToken: source.token
}).catch(function(thrown) {
  if (axios.isCancel(thrown)) {
    console.log('Request canceled', thrown.message);
  } else {
     // 处理错误
  }
});

axios.post('/user/12345', {
  name: 'new name'
}, {
  cancelToken: source.token
})

// 取消请求（message 参数是可选的）
source.cancel('Operation canceled by the user.');

```

还可以通过传递一个 executor 函数到 `CancelToken` 的构造函数来创建 cancel token： 

```
const CancelToken = axios.CancelToken;
let cancel;

axios.get('/user/12345', {
  cancelToken: new CancelToken(function executor(c) {
    // executor 函数接收一个 cancel 函数作为参数
    cancel = c;
  })
});

// cancel the request
cancel();
```

注意: 可以使用同一个 cancel token 取消多个请求 

## 使用 application/x-www-form-urlencoded format

默认情况下，axios将JavaScript对象序列化为JSON。 要以application / x-www-form-urlencoded格式发送数据，您可以使用以下选项之一。

### 浏览器

在浏览器中，您可以使用URLSearchParams API，如下所示：

```
const params = new URLSearchParams();
params.append('param1', 'value1');
params.append('param2', 'value2');
axios.post('/foo', params);
请注意，所有浏览器都不支持URLSearchParams（请参阅caniuse.com），但可以使用polyfill（确保填充全局环境）。
```

或者，您可以使用qs库编码数据： 

```

```

或者以另一种方式（ES6） 

```
import qs from 'qs';
const data = { 'bar': 123 };
const options = {
  method: 'POST',
  headers: { 'content-type': 'application/x-www-form-urlencoded' },
  data: qs.stringify(data),
  url,
};
axios(options);
```

 Node.js

在node.js中，您可以使用querystring模块，如下所示：

```

```

您也可以使用qs库。

## Semver

在axios达到1.0版本之前，破坏性更改将以新的次要版本发布。 例如0.5.1和0.5.4将具有相同的API，但0.6.0将具有重大变化。

## Promises

axios 依赖原生的 ES6 Promise 实现而[被支持](http://caniuse.com/promises). 如果你的环境不支持 ES6 Promise，你可以使用 [polyfill](https://github.com/jakearchibald/es6-promise).

## TypeScript

axios包括TypeScript定义。

```

```