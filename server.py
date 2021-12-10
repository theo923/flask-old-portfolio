from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route('/')
def say_hello():
    return render_template('./index.html')

@app.route('/blog')
def say_hello2():
    return 'This is my blog!'

@app.route('/blog/2020/dogs')
def say_hello3():
    return 'This is my dog!'
