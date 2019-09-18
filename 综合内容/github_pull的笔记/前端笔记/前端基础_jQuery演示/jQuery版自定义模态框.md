<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="x-ua-compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>自定义模态框</title>
  <style>
    .cover {
      position: fixed;
      left: 0;
      right: 0;
      top: 0;
      bottom: 0;
      background-color: darkgrey;
      z-index: 999;
    }
    .modal {
      width: 600px;
      height: 400px;
      background-color: white;
      position: fixed;
      left: 50%;
      top: 50%;
      margin-left: -300px;
      margin-top: -200px;
      z-index: 1000;
    }
    .hide {
      display: none;
    }
  </style>
</head>
<body>
<input type="button" value="弹" id="i0">

<div class="cover hide"></div>
<div class="modal hide">
  <label for="i1">姓名</label>
  <input id="i1" type="text">
   <label for="i2">爱好</label>
  <input id="i2" type="text">
  <input type="button" id="i3" value="关闭">
</div>
<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>
<script>
  var tButton = $("#i0")[0];
  tButton.onclick=function () {
    var coverEle = $(".cover")[0];
    var modalEle = $(".modal")[0];

    $(coverEle).removeClass("hide");
    $(modalEle).removeClass("hide");
  };

  var cButton = $("#i3")[0];
  cButton.onclick=function () {
    var coverEle = $(".cover")[0];
    var modalEle = $(".modal")[0];

    $(coverEle).addClass("hide");
    $(modalEle).addClass("hide");
  }
</script>
</body>
</html>

jQuery版自定义模态框