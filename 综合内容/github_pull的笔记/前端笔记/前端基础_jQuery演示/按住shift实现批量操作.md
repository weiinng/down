<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta http-equiv="content-Type" charset="UTF-8">
    <meta http-equiv="x-ua-compatible" content="IE=edge">
    <title>Title</title>
</head>
<body>


<table border="1">
  <thead>
  <tr>
    <th>#</th>
    <th>姓名</th>
    <th>操作</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td><input type="checkbox"></td>
    <td>Egon</td>
    <td>
      <select>
        <option value="1">上线</option>
        <option value="2">下线</option>
        <option value="3">停职</option>
      </select>
    </td>
  </tr>
  <tr>
    <td><input type="checkbox"></td>
    <td>Alex</td>
    <td>
      <select>
        <option value="1">上线</option>
        <option value="2">下线</option>
        <option value="3">停职</option>
      </select>
    </td>
  </tr>
  <tr>
    <td><input type="checkbox"></td>
    <td>Yuan</td>
    <td>
      <select>
        <option value="1">上线</option>
        <option value="2">下线</option>
        <option value="3">停职</option>
      </select>
    </td>
  </tr>
  <tr>
    <td><input type="checkbox"></td>
    <td>EvaJ</td>
    <td>
      <select>
        <option value="1">上线</option>
        <option value="2">下线</option>
        <option value="3">停职</option>
      </select>
    </td>
  </tr>
  <tr>
    <td><input type="checkbox"></td>
    <td>Gold</td>
    <td>
      <select>
        <option value="1">上线</option>
        <option value="2">下线</option>
        <option value="3">停职</option>
      </select>
    </td>
  </tr>
  </tbody>
</table>

<input type="button" id="b1" value="全选">
<input type="button" id="b2" value="取消">
<input type="button" id="b3" value="反选">


<script src="jquery-3.3.1.js"></script>
<script>

    var flag = false;
    // shift按键被按下的时候
    $(window).keydown(function (event) {
        console.log(event.keyCode);
        if (event.keyCode === 16){
            flag = true;
        }
    });
    // shift按键被抬起的时候
    $(window).keyup(function (event) {
        console.log(event.keyCode);
        if (event.keyCode === 16){
            flag = false;
        }
    });
    // select标签的值发生变化的时候
    $("select").change(function (event) {
        // 如果shift按键被按下，就进入批量编辑模式
        // shift按键对应的code是16
        // 判断当前select这一行是否被选中
        console.log($(this).parent().siblings().first().find(":checkbox"));
        var isChecked = $(this).parent().siblings().first().find(":checkbox").prop("checked");
        console.log(isChecked);
        if (flag && isChecked) {
            // 进入批量编辑模式
            // 1. 取到当前select选中的值
            var value = $(this).val();
            // 2. 给其他被选中行的select设置成和我一样的值
            // 2.1 找到那些被选中行的select
            var $select = $("input:checked").parent().parent().find("select")
            // 2.2 给选中的select赋值
            $select.val(value);
        }
    });
</script>
</body>
</html>

按住shift实现批量操作