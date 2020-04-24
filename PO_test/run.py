#coding=utf-8
import unittest
import os
from datetime import datetime
from base.HTMLTestRunner import HTMLTestRunner

path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(path,'case')

if __name__ == '__main__':
    reportdir = os.path.join(path,"report")
    print (reportdir)
    report_file = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.html'
    reportpath = reportdir+'\\'+report_file
    f = open(reportpath,'w',encoding='utf-8')
    testsuit = unittest.defaultTestLoader.discover(case_path,'*case*.py')
    with open(reportpath,'w',encoding='utf-8') as f:
        runner = HTMLTestRunner(stream=f, title='flie report',description='flie report')
        runner.run(testsuit)
