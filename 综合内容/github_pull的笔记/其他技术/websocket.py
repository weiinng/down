websocket其实就是web socket 。
		
		问题：
			a. http是一个协议。
				- 数据格式
				- 一次请求和响应之后断开连接（短连接、无状态）
			
			b. 服务端可以向客户端主动推送消息吗？不可以
			
			c. 服务端只能做出响应。
			
			d. 为了伪造服务端向客户端主动推送消息的效果，我们使用：轮询和长轮询。
	
			
			诞生了一个新的协议：websocket
				- 数据格式 
					- 连接请求
					- 收发数据
				- 不断开连接
		
index.html 
	<!DOCTYPE html>
	<html lang="zh-CN">
	<head>
		<meta charset="UTF-8">
		<title>Title</title>
		<meta name="viewport" content="width=device-width, initial-scale=1">
	</head>
	<body>
		<h1>丑男投票系统</h1>
		<ul>
			{% for k,v in users.items() %}
				<li onclick="vote({{k}})" id="id_{{k}}">{{v.name}}<span>{{v.count}}</span></li>
			{% endfor %}
		</ul>

		<script src="{{ url_for('static',filename='jquery-3.3.1.min.js')}}"></script>
		<script>
			var ws = new WebSocket('ws://192.168.13.253:5000/message')
			ws.onmessage = function (event) {
				/* 服务器端向客户端发送数据时，自动执行 */
				// {'cid':cid,'count':new}
				var response = JSON.parse(event.data);
				$('#id_'+response.cid).find('span').text(response.count);

			};

			function vote(cid) {
				ws.send(cid)
			}
		</script>
	</body>
	</html>
	

app.py 
	from flask import Flask,render_template,request
	from geventwebsocket.handler import WebSocketHandler
	from gevent.pywsgi import WSGIServer
	import json

	app = Flask(__name__)

	USERS = {
		'1':{'name':'钢弹','count':0},
		'2':{'name':'铁锤','count':0},
		'3':{'name':'贝贝','count':100},
	}


	# http://127.0.0.1:5000/index
	@app.route('/index')
	def index():
		return render_template('index.html',users=USERS)

	# http://127.0.0.1:5000/message
	WEBSOCKET_LIST = []
	@app.route('/message')
	def message():
		ws = request.environ.get('wsgi.websocket')
		if not ws:
			print('http')
			return '您使用的是Http协议'
		WEBSOCKET_LIST.append(ws)
		while True:
			cid = ws.receive()
			if not cid:
				WEBSOCKET_LIST.remove(ws)
				ws.close()
				break
			old = USERS[cid]['count']
			new = old + 1
			USERS[cid]['count'] = new
			for client in WEBSOCKET_LIST:
				client.send(json.dumps({'cid':cid,'count':new}))



	if __name__ == '__main__':
		http_server = WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
		http_server.serve_forever()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		