from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def a():
    return render_template('5.html')
@app.route('/a')
def b():
    return render_template('macro.html')

if __name__ == '__main__':
    app.run(debug=True)