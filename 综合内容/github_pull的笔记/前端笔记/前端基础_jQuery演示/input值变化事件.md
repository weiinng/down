<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="x-ua-compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>实时监听input输入值变化</title>
</head>
<body>
<input type="text" id="i1">

<script src="jquery-3.2.1.min.js"></script>
<script>
  /*
  * oninput是HTML5的标准事件
  * 能够检测textarea,input:text,input:password和input:search这几个元素的内容变化，
  * 在内容修改后立即被触发，不像onchange事件需要失去焦点才触发
  * oninput事件在IE9以下版本不支持，需要使用IE特有的onpropertychange事件替代
  * 使用jQuery库的话直接使用on同时绑定这两个事件即可。
  * */
  $("#i1").on("input propertychange", function () {
    alert($(this).val());
  })
</script>
</body>
</html>

input值变化事件