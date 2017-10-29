# coding=utf-8
# __author__='wujide'
import urllib
import urllib2
import demjson
import json


def initInvest():
    para_path = r"../info/trans_initInvest_para.txt"
    with open(para_path, 'rb') as f:
        values = json.dumps(f.read())
        print (type(values), values)
        d = eval(json.loads(values))
        print (type(d), d)
    # headers = {"logintoken": "c35692bac66148acbf261c17915c4f72", "Content-Type": "application/json;charset=utf-8"}
    # req = urllib2.Request('https://api.gocfae.com/trans/trans/initInvest', headers=headers)
    req = urllib2.Request('https://api.gocfae.com/trans/trans/initInvest', headers=d['headers'])
    # req.add_header('logintoken', 'de38f315a0414195aadca3807ca8c28e')
    # req.add_header('Content-Type', 'application/json;charset=utf-8')
    response = urllib2.urlopen(req, eval(values))
    data = response.read()
    return data

if __name__ == '__main__':
    print initInvest()