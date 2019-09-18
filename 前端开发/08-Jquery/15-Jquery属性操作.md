## Jquery属性操作

### html() 取出或者设置html内容

```python
//取出 html 内容
var $htm = $('#div1').html();

//设置html内容
$('#div1').html('<span>添加文字</span>')；
```

### prop() 取出或设置某个属性的值

```python
//取出图片的地址
var $src = $('#img1').prop('src')

//设置图片的地址和alt属性
$('#img1').prop({
  'src':'1.jpg',
  'alt':'Text Image!'
});
```



