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
    <th>����</th>
    <th>����</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td><input type="checkbox"></td>
    <td>Egon</td>
    <td>
      <select>
        <option value="1">����</option>
        <option value="2">����</option>
        <option value="3">ְͣ</option>
      </select>
    </td>
  </tr>
  <tr>
    <td><input type="checkbox"></td>
    <td>Alex</td>
    <td>
      <select>
        <option value="1">����</option>
        <option value="2">����</option>
        <option value="3">ְͣ</option>
      </select>
    </td>
  </tr>
  <tr>
    <td><input type="checkbox"></td>
    <td>Yuan</td>
    <td>
      <select>
        <option value="1">����</option>
        <option value="2">����</option>
        <option value="3">ְͣ</option>
      </select>
    </td>
  </tr>
  <tr>
    <td><input type="checkbox"></td>
    <td>EvaJ</td>
    <td>
      <select>
        <option value="1">����</option>
        <option value="2">����</option>
        <option value="3">ְͣ</option>
      </select>
    </td>
  </tr>
  <tr>
    <td><input type="checkbox"></td>
    <td>Gold</td>
    <td>
      <select>
        <option value="1">����</option>
        <option value="2">����</option>
        <option value="3">ְͣ</option>
      </select>
    </td>
  </tr>
  </tbody>
</table>

<input type="button" id="b1" value="ȫѡ">
<input type="button" id="b2" value="ȡ��">
<input type="button" id="b3" value="��ѡ">


<script src="jquery-3.3.1.js"></script>
<script>

    var flag = false;
    // shift���������µ�ʱ��
    $(window).keydown(function (event) {
        console.log(event.keyCode);
        if (event.keyCode === 16){
            flag = true;
        }
    });
    // shift������̧���ʱ��
    $(window).keyup(function (event) {
        console.log(event.keyCode);
        if (event.keyCode === 16){
            flag = false;
        }
    });
    // select��ǩ��ֵ�����仯��ʱ��
    $("select").change(function (event) {
        // ���shift���������£��ͽ��������༭ģʽ
        // shift������Ӧ��code��16
        // �жϵ�ǰselect��һ���Ƿ�ѡ��
        console.log($(this).parent().siblings().first().find(":checkbox"));
        var isChecked = $(this).parent().siblings().first().find(":checkbox").prop("checked");
        console.log(isChecked);
        if (flag && isChecked) {
            // ���������༭ģʽ
            // 1. ȡ����ǰselectѡ�е�ֵ
            var value = $(this).val();
            // 2. ��������ѡ���е�select���óɺ���һ����ֵ
            // 2.1 �ҵ���Щ��ѡ���е�select
            var $select = $("input:checked").parent().parent().find("select")
            // 2.2 ��ѡ�е�select��ֵ
            $select.val(value);
        }
    });
</script>
</body>
</html>

��סshiftʵ����������