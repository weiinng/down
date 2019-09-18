
```
select联动
```

```
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="x-ua-compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>select联动</title>
</head>
<body>
<select id="province">
  <option>请选择省:</option>
</select>
​```
<select id="city">
  <option>请选择市:</option>
</select>

<script>
  data = {"河北省": ["廊坊", "邯郸"], "北京": ["朝阳区", "海淀区"], "山东": ["威海市", "烟台市"]};

  var p = document.getElementById("province");
  var c = document.getElementById("city");

  for (var i in data) {
    var optionP = document.createElement("option");
    optionP.innerHTML = i;
    p.appendChild(optionP);
  }
  p.onchange = function () {
    var pro = (this.options[this.selectedIndex]).innerHTML;
    var citys = data[pro];
    // 清空option
    c.innerHTML = "";

    for (var i=0;i<citys.length;i++) {
      var option_city = document.createElement("option");
      option_city.innerHTML = citys[i];
      c.appendChild(option_city);
    }
  }
</script>
</body>
</html>

```

