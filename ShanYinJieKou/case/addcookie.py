#coding:utf-8

import requests

loginUrl = 'http://10.36.40.213:5151/afterloanmgr/login.html'
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
           }  # get方法其它加个User-Agent就可以了
s = requests.session()
r = s.get(url=loginUrl, headers=headers, verify=False)
print(s.cookies)
#添加登陆需要的两个cookie
c = requests.cookies.RequestsCookieJar()
#登陆之后，使用fillder
c.set('AFTERLOANSHIROSESSIONID','afterloan-shiro-session-ec53a244-d9cc-4c20-b738-e274a5d87c75')
c.set('NGCAPTCHAID', '1524206733329fa0a638d298e43ed97b21eb07b2e93c1')
s.cookies.update(c)
print(s.cookies)

#新增保证金流水
url2 = "http://10.36.40.213:5151/afterloanmgr/mgr/doAddWecashBailFlow.jspx"
# http://10.36.40.213:5151/afterloanmgr/view/addOrEditWecashBailFlow.html?parameter_ =%7B%22width%22:640,%22height%22:520%7D&fid = gridMainFrame&id =& oid = % 5Biframe_wecashBailFlowMgr%5BwecashBailFlowFrame%5D%5D
body = {"bailTermId": "2",
        "dealAmount": "88.77",
        "dealDate": "2018-04-20",
        "remark": "python测试",
        "trustId": "AF002",
        "id": ""}
r2 = s.post(url=url2, data=body, verify=False)
# print(r.content)
print("*************************")
print(r2.content)
print(r2.text)