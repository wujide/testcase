# coding=utf-8
# __author__='wujide'

a = dict(one=1, two=2, three=3)
b = {'one': 11, 'two': 22, 'three': 33}
c = dict(zip(['one', 'two', 'three'], [111, 2222, 3333]))
d = dict((['three', 3333], ['one', 1111], ['two', 2222]))
e = dict([('three', 33333), ('one', 11111), ('two', 22222)])


print a
print b
print c
print d
print e

import json
from flask import Flask, jsonify

print json.loads(json.dumps(a))
print json.loads(json.dumps(b))['one']
print json.loads(json.dumps(c))['two']
print json.loads(json.dumps(d))
print json.loads(json.dumps(e))



app = Flask(__name__)


@app.route('/temp/<data>', methods=['get'])
def get_json(data):
    return jsonify({'data': data})
    # return jsonify({'data': json_data})
    # return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)



