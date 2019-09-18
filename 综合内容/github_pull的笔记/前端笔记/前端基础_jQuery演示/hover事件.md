<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="x-ua-compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>hover示例</title>
  <style>
    * {
      margin: 0;
      padding: 0;
    }
    .nav {
      height: 40px;
      width: 100%;
      background-color: #3d3d3d;
      position: fixed;
      top: 0;
    }

    .nav ul {
      list-style-type: none;
      line-height: 40px;
    }

    .nav li {
      float: left;
      padding: 0 10px;
      color: #999999;
      position: relative;
    }
    .nav li:hover {
      background-color: #0f0f0f;
      color: white;
    }

    .clearfix:after {
      content: "";
      display: block;
      clear: both;
    }

    .son {
      position: absolute;
      top: 40px;
      right: 0;
      height: 50px;
      width: 100px;
      background-color: #00a9ff;
      display: none;
    }

    .hover .son {
      display: block;
    }
  </style>
</head>
<body>
<div class="nav">
  <ul class="clearfix">
    <li>登录</li>
    <li>注册</li>
    <li>购物车
      <p class="son hide">
        空空如也...
      </p>
    </li>
  </ul>
</div>
<script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
<script>
$(".nav li").hover(
  function () {
    $(this).addClass("hover");
  },
  function () {
    $(this).removeClass("hover");
  }
);
</script>
</body>
</html>

hover事件