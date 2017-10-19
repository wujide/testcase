# coding=utf-8
# __author__='wujide'
import urllib

import mock
import unittest
import client


# mock.Mock 用法
class Client_demo(unittest.TestCase):

    def test_success_request(self):
        success_send = mock.Mock(return_value='200', name='test_success_request')
        print success_send
        client.send_request = success_send
        self.assertEqual(client.visit_baidu(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        client.send_request = fail_send
        self.assertEqual(client.visit_baidu(), '404')


    def test_call_send_request_with_right_arguments(self):
        client.send_request = mock.Mock()
        client.visit_baidu()
        self.assertEqual(client.send_request.called, True)
        call_args = client.send_request.call_args
        self.assertIsInstance(call_args[0][0], str)
        print call_args[0][0]

    def runTest(self):
        pass


# mock.patch 用法
class TestClient_2(unittest.TestCase):

    def test_success_request(self):
        status_code = '200'
        success_send = mock.Mock(return_value=status_code)
        with mock.patch('client.send_request', success_send):
            self.assertEqual(client.visit_baidu(), status_code)

    def test_fail_request(self):
        status_code = '404'
        fail_send = mock.Mock(return_value=status_code)
        with mock.patch('client.send_request', fail_send):
            self.assertEqual(client.visit_baidu(), status_code)

    def runTest(self):
        pass

if __name__ == "__main__":
    tc = Client_demo()
    tc.test_success_request()
    tc.test_fail_request()
    tc.test_call_send_request_with_right_arguments()

    tc2 = TestClient_2()
    tc2.test_success_request()
    tc2.test_fail_request()
    tc2.test_call_send_request_with_right_arguments()
