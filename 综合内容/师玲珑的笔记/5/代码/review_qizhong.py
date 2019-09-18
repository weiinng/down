from flask import Flask,render_template,request

app=Flask(__name__)
list=[1,3,2,5,4]

@app.route('/')
def c():
    # a=request.args.get('a')
    return 'a'

@app.route('/<a>')
def a(a):
    return render_template('five.html',list=list)

@app.route('/a')
def b():
    headers={
        'content-type':'text/plain',
        'location':'http://www.baidu.com'
    }
    return 's'

if __name__ == '__main__':
    app.run(debug=True)


# print('user:{}'.format('123'))
