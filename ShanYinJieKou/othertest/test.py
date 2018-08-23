# coding:utf-8

import requests, unittest
import json, logging
import HTMLTestRunner
'''
# 进件查询
url = 'http://210.22.89.58:37278/afterloanapi/openapi/queryReceive'
data = json.dumps({"sysId": "105", "uuid": "2018041725-lx"})

headers = {'Content-Type': 'application/json'}
#方法一
r = requests.post(url, data=data, headers=headers)
print(r.text)
#方法二
response = requests.request("POST", url, data=data, headers=headers)
print(response.json())
'''


class TestJJapi(unittest.TestCase):

    def setUp(self):
        self.url = 'http://210.22.89.58:37278/afterloanapi/openapi/queryReceive'
        self.header = {'Content-Type': 'application/json'}

    def test_jj(self):
        data = {"sysId": "105", "uuid": "2018041725-lx"}
        r = requests.post(url=self.url, data=json.dumps(data), headers=self.header)
        # 返回的是字符串，用eval函数转成字典
        RR = eval(r.text)
        logging.info(RR["msg"])
        self.assertEqual(RR["msg"], "成功", "ERROR")
        print(r.json())
        print('**************test_jj******************')

    def tearDown(self):
        pass


if __name__ == '__main__':
    print('1122232334')
    # report_dir = 'result.html'
    # print(report_dir)
    # re_open = open(report_dir,'wb')
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestJJapi)
    # runner = HTMLTestRunner.HTMLTestRunner(
    #         stream=re_open,
    #         title=u'闪银-进件接口查询',
    #         description='进件接口查询详情')
    # runner.run(suite)
    # re_open.close()

    # 定义一个测试容器
    test = unittest.TestSuite()
    # 将测试用例，加入到测试容器中
    test.addTest(TestJJapi("test_jj"))
    # 定义个报告存放的路径，支持相对路径
    file_path = "result.html"
    file_result = open(file_path, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result,
                                           title=u"闪银-进件接口查询",
                                           description="进件接口查询详情"
                                           )

    # 运行测试用例
    runner.run(test)
    file_result.close()