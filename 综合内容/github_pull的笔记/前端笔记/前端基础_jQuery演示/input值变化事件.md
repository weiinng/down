<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="x-ua-compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ʵʱ����input����ֵ�仯</title>
</head>
<body>
<input type="text" id="i1">

<script src="jquery-3.2.1.min.js"></script>
<script>
  /*
  * oninput��HTML5�ı�׼�¼�
  * �ܹ����textarea,input:text,input:password��input:search�⼸��Ԫ�ص����ݱ仯��
  * �������޸ĺ�����������������onchange�¼���Ҫʧȥ����Ŵ���
  * oninput�¼���IE9���°汾��֧�֣���Ҫʹ��IE���е�onpropertychange�¼����
  * ʹ��jQuery��Ļ�ֱ��ʹ��onͬʱ���������¼����ɡ�
  * */
  $("#i1").on("input propertychange", function () {
    alert($(this).val());
  })
</script>
</body>
</html>

inputֵ�仯�¼�