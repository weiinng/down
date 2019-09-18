from flask import Flask,jsonify,render_template

app=Flask(__name__)

posts=[{'name':'小明','age':18,'sex':'男'},{'name':'小红','age':28,'sex':'女'},{'name':'小王','age':38,'sex':'男'}]

@app.route('/')
def demo1():
    return render_template('2.html',posts=posts)

app.config.from_pyfile('settings.ini')

if __name__ == '__main__':
    app.run(port=80)