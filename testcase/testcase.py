# coding:utf-8
import requests
import unittest
import warnings


class Test_pinglun(unittest.TestCase):
    def setUp(self):  # 前置
        warnings.simplefilter("ignore", ResourceWarning)
        self.url = "https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=315793&count=10&page=0&filter_rating=0&bkn=2055178255&r=0.1307198157821292"
        self.par = {'Referer': 'https://ke.qq.com/course/315793?taid=2540133853483409'}
        self.s = requests.session()

    def test_pinglun(self):
        # 发出请求
        r = self.s.get(self.url, params=self.par)
        c = r.status_code
        self.assertEqual(c, 200)
        # print(r.url)

    def test_01(self):
        a = 1
        b = 2
        c = a + b
        self.assertEqual(c, 3)

    def test_02(self):
        str1 = "ab"
        str2 = "c"
        str3 = str1 + str2
        self.assertEqual(str3, 'abc')


if __name__ == "__main__":
    unittest.main()

