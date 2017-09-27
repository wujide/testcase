# coding=utf-8
# __author__='wujide'
import urllib
import urllib2
from flask import json


class InterfaceTest:
    def __init__(self, file_path):
        self.file_path = file_path

    def data_get(self):
        with open(self.file_path, 'rb') as f:
            values = json.dumps(f.read())  # type(values): <type 'str'>
            data = eval(json.loads(values))  # type(data): <type 'dict'>
            return data

    @staticmethod
    def data_post(values):
        data = urllib.urlencode(values)
        req = urllib2.Request(values['url'])
        response = urllib2.urlopen(req, data)
        return response

    # write result to a file
    @staticmethod
    def data_save(file_path, data):
        with open(file_path, 'wb+') as f:
            json.dump(eval(data), f)

    @staticmethod
    def pass_or_fail(file_path):
        with open(file_path, 'r') as f:
            values = json.dumps(f.read())
            data = eval(json.loads(values))
            if data['status'] == '0':
                print "%s PASS" % file_path.split("/")[2]
            else:
                print "%s FAIL" % file_path.split("/")[2]

    @staticmethod
    def para_get(**kwargs):
        with open(kwargs['para_path'], 'r') as f:
            values = json.dumps(f.read())
            data = eval(json.loads(values))
        # get the loginToken
        with open(r"../data/login", 'r') as f:
            values = json.dumps(f.read())
            dd = eval(json.loads(values))
            data['loginToken'] = dd['data']['loginToken']
        # get interface url
        with open(r"../info/url", 'r') as f:
            values = json.dumps(f.read())
            d = eval(json.loads(values))
            data['url'] = d[kwargs['iterface_url']]
        with open(kwargs['para_path'], 'wb+') as f:
            json.dump(data, f)
