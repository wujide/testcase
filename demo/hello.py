# coding=utf-8
# __author__='wujide'

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!!'


@app.route('/post/<int:num>')
def hello_num(num):
    return 'Hello %d!' % num

if __name__ == '__main__':
    app.run(debug=True)
