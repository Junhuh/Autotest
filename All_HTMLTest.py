#coding=utf-8
import unittest
#加载模块TestBaidu,TestSogou,PythonOrg
import TestSogou
import PythonOrg
import TestBaidu

import time
import HTMLTestRunner

testunit=unittest.TestSuite()
#将测试用例加入到测试容器中
testunit.addTest(unittest.makeSuite(TestSogou.TestSogou))
testunit.addTest(unittest.makeSuite(PythonOrg.PythonOrgSearch))
testunit.addTest(unittest.makeSuite(TestBaidu.TestBaidu))

#runner=unittest.TextTestRunner()
#runner.run(testunit)

#导入当前时间，使用time模块的相关函数
now=time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
#将测试结果写入到result.html中
fp=open(now+"result.html",'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Report',description=u'Result:')
runner.run(testunit)
fp.close()