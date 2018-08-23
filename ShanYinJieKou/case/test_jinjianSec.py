#coding:utf-8
import requests, unittest
import json, logging
import os
from common.logger import Log
import HTMLTestRunner

class TestjinjianSec(unittest.TestCase):
    log = Log()
    def setUp(self):
        #获得当前的目录
        #cur_path = os.path.dirname(os.path.realpath(__file__))
        self.url1 = r'http://210.22.89.58:37278/afterloanapi/'
        self.header = {'Content-Type': 'application/json'}

    def test_jinjian(self):
        '''外部资产-信托-闪银进件接口'''
        self.log.info("-----start----")
        self.jjurl = self.url1 + "openapi/receiveExternalContract"
        self.datas = {
            "transportDate": "2018-05-08 15:28:28",
            "uuid": "2018050849-lx",
            "sysId": "105",
            "amount": 2000,
            "handAmount": 2000,
            "periodCount": 2,
            "returnType": "0",
            "kazhe": "0",
            "bankAccount": "6217000830000123038",
            "returnName": "张学友",
            "bankId": "1005",
            "bankNo": "",
            "bankName": "",
            "bankProvince": "",
            "bankCity": "",
            "loanReturnType": "0",
            "loanKazhe": "0",
            "loanReturnName": "张学友",
            "loanBankAccount": "6217000830000123038",
            "loanBankId": "1005",
            "loanBankName": "",
            "loanBankNo": "",
            "loanBankProvince": "",
            "loanBankCity": "",
            "payeeIdCard": "111",
            "payeeIdNumber": "330106198006158578",
            "mortgagorType": "0",
            "mortgagorName": "张学友",
            "ccy": "CNY",
            "occurDate": "2018-03-23",
            "beginDate": "2018-03-23 12:00:00",
            "endDate": "2018-03-23 23:59:59",
            "contDate": "2018-03-23 12:00:00",
            "clientReqBeginDate": "2018-03-23",
            "loanPurposeOne": "13",
            "loanPurposeTwo": "13",
            "loanPurposeDesc": "测试",
            "currency": "CNY",
            "sevFeeFlag": "0",
            "preSrvFee": 0,
            "perSrvFee": 20.34,
            "inteRate": 0.015,
            "returnKind": "AQFXAQHB",
            "amt": 0,
            "monthRepaymentDate": 1,
            "expedited": "1",
            "contractType": "0",
            "attribut": "01",
            "idType": "111",
            "idNumber": "330106198006158578",
            "certIdRegion": "350103",
            "gender": "1",
            "birthday": "1998-08-08",
            "natiSign": "中国",
            "nativePlace": "",
            "regiSeat": "上海市世纪大道",
            "marriage": "1",
            "eduExperience": "8",
            "inhabTel": "",
            "mobile": "18721334499",
            "address": "上海市浦东新区实际大道100",
            "residentProvince": "上海市",
            "residentCity": "浦东新区",
            "email": "",
            "occupation": "020",
            "duty": "02",
            "positionName": "030",
            "workCorp": "工商银行",
            "companyNature": "银行",
            "belongType": "银行业",
            "companyAdd": "上海市浦东新区实际大道100号",
            "workYearMonth": "2015-10-10",
            "monthIncome": 1110,
            "imageUrlList": [{
                "imageUrl": "http://scimg.jb51.net/allimg/150703/14-150F3092U5202.jpg",
                "imageType": "1"
            },
                {
                    "imageUrl": "http://pic61.nipic.com/file/20150309/4614066_191939440318_2.jpg",
                    "imageType": "2"
                }
            ],
            "contactList": [{
                "contactName": "王王",
                "relationship": "1",
                "phoneNumber": "13432432423423"
            }],
            "loanCategory": "1",
            "productNo": "1231233",
            "productName": "闪银3期b类用户产品",
            "loanType": "4",
            "grade": "C",
            "serviceRate": 0.1245
        }
        self.log.info('-----开始进件-----')
        r = requests.post(url=self.jjurl, data=json.dumps(self.datas), headers=self.header)
        print(r.json())
        #返回的内容写到一个文件里
        res = r.text
        if res:self.log.info("----进件返回结果：%s-----"% res)
        cur_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path2 = cur_path + r'\file'
        try:
            if not(os.path.exists(path2 + r'\jinjianRes.txt')):
                #如果不存在,创建一个 jinjianRes.txt
                file_full = path2 + r'\jinjianRes.txt'
                file = open(file_full,'w+')
                file.close()
                print('----已经存在文件存储进件的response---')
        finally:
            with open(path2 + r'\jinjianRes.txt', 'r+') as f:
                f.writelines(res)
                self.log.info('----进件返回已经写入文件----')
                self.log.info('----进件结束--end---')

    def test_jianjinSec(self):
        '''外部资产-信托-闪银进件查询接口'''
        # 获得父级目录
        cur_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path2 = cur_path + r'\file'
        with open(path2 + r'\jinjianchaxun.txt', 'r+') as f:
            uu = f.readlines()
            uu2 = eval(uu[0])
        self.sysid = uu2["sysId"]
        self.uuid = uu2["uuid"]
        # self.url = TestjinjianSec.csh.CSH()[0] + 'openapi/queryReceive'
        # self.header = TestjinjianSec.csh.CSH()[1]
        self.url2 = self.url1 + r'openapi/queryReceive'
        data = {"sysId": self.sysid, "uuid": self.uuid}
        self.datas = json.dumps(data)
        r = requests.post(url=self.url2, data=self.datas, headers=self.header)
        #返回的是字符串，用eval函数变成字典
        RR = eval(r.text)
        logging.info(RR["msg"])
        self.assertEqual(RR["msg"], "成功", "ERROR")
        print(r.json())

    def tearDown(self):
        self.log.info('-----all the end !!!----- ')
        # pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
# if __name__ == "__main__":
#    #方法一
#     # unittest.main(verbosity=2)
#    #方法二 TestSuite
#     suite = unittest.TestSuite()
#     suite.addTest(TestjinjianSec("test_jinjian"))
#     suite.addTest(TestjinjianSec("test_jianjinSec"))
#     # 执行测试
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)



