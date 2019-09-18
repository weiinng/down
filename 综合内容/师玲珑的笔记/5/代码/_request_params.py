from flask import Flask,request,render_template
import json

app=Flask(__name__)
@app.route('/')
def show():
    dict={}
    dict['data']=request.data
    dict['form']=request.form.get('name')
    dict['url']=request.url
    dict['method']=request.method
    print(dict)
    return render_template('1.html')

if __name__ == '__main__':
    app.run(debug=True)