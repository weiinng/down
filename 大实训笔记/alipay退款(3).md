## Alipay退款接口

* 1、pay.py

  ```python
  from views import goods
  
  # 请求支付宝退款接口
  def api_alipay_trade_refund(refund_amount, out_trade_no=None, trade_no=None, **kwargs):
          biz_content = {
              "refund_amount": refund_amount
          }
          biz_content.update(**kwargs)
          if out_trade_no:
              biz_content["out_trade_no"] = out_trade_no
          if trade_no:
              biz_content["trade_no"] = trade_no
          alipay = goods.get_ali_object()
          data = alipay.build_body("alipay.trade.refund", biz_content)
          url = "https://openapi.alipay.com/gateway.do" + "?" + alipay.sign_data(data)
          r = requests.get(url)
          html = r.content.decode("utf-8")
          return html
      
  # 注意：需要自己实例化 alipay变量， 通过导入接口文件中的函数  from views import goods
  # alipay = goods.get_ali_object()
  # data = alipay.build_body("alipay.trade.refund", biz_content)
  # 此处和接口文件不同，进行了修改
  ```

  

* 2、接口视图文件

  ```python
  # 支付宝退款
  class Refund(BaseHandler):
      def post(self, *args, **kwargs):
          msg = {}
          # 支付宝订单号
          out_trade_no = self.get_argument('out_trade_no')
          # 实付价格
          refund_amount = self.get_argument('refund_amount')
          # 调用退款方法
          order_string = api_alipay_trade_refund(
          # 订单号，一定要注意，这是支付成功后返回的唯一订单号
          out_trade_no = out_trade_no,
          # 退款金额，注意精确到分，不要超过订单支付总金额
          refund_amount = refund_amount,
          # 回调网址
          notify_url='http://localhost:8000/alipayreturn'
          )
          # self.write(order_string)
          
          # 此处以下：是前台判断的逻辑需要，可自己设置返回值。
          
          
          
          # 把数据库的字段修改
          order = sess.query(Orders).filter(Orders.outer_traed_number == out_trade_no).first()
          order.transaction_status = 2
          sess.commit()
          msg['mes'] = '退款完成'
          msg['code'] = '200'
          self.write(json.dumps(msg, cls=AlchemyEncoder, ensure_ascii=False, indent=4))
          
  #  notify_url='http://localhost:8000/alipayreturn' 回调网址为alipay支付时的回调地址，相同
  # 前台调用该这个接口时，需要将付款金额和支付宝订单号out_trade_no 一起传过来，发给alipay接口
  ```

  

* 3、前台逻辑分析：

  * 退款完成后，将数据库中的订单状态修改，改为已退款。
  * 前台页面判断订单状态，展示是否退款，当退款完成后，将退款按钮隐藏。





差不多是这样，完工！