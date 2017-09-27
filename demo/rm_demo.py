# coding=utf-8
# __author__='wujide'

from mymodule import rm
import os.path
import tempfile
import unittest
import mock


class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.tmpfilepath, "wb") as f:
            f.write("Delete me!")

    def test_rm(self):
        # remove the file
        rm(self.tmpfilepath)
        # test that it was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")

    @mock.patch('mymodule.os')
    def test_rm_mock(self, mock_os):
        rm("any path")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")
        print "called"


if __name__ == "__main__ ":
    rm_test = RmTestCase()
    rm_test.test_rm_mock()
