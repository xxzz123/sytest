#coding:utf-8
import os, time
import unittest
import HTMLTestRunner

#当前脚本所在文件的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
# print(cur_path)
# cur_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# path2 = cur_path + r'\file'

def add_case(caseName="case", rule='test_*.py'):
    ''' 第一步：加载所有的测试案例 '''
    case_path = os.path.join(cur_path, caseName)
    if not os.path.exists(case_path): os.mkdir(case_path)
    print('case path:%s'% (case_path+'\\'))
    #定义discover方法的参数
    testunit = unittest.TestSuite()
    # discover = unittest.defaultTestLoader.discover(case_path+"\\", pattern=rule, top_level_dir=None)
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            print(test_case)
            testunit.addTests(test_case)
            print(testunit)
    return testunit

    # return discover

#生成测试报告
def run_case(all_case,reportName="testReport"):
    '''第二步：执行所有的用例，并把结果HTML测试报告中'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path=os.path.join(cur_path,reportName)
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path,now+"result.html")
    print("report path:%s"%report_abspath)
    fp=open(report_abspath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'闪银接口测试报告',description='用例执行情况')
    #调用 all——case 返回值
    runner.run(all_case)
    fp.close()


if __name__ == "__main__":
    all_case = add_case() #1记载测试用例
    print('********all_case***********', all_case)
    run_case(all_case)    #2执行用例
    report_path =os.path.join(cur_path,"testReport")