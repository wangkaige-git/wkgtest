import  unittest,os
from datetime import datetime
from HTMLTestRunner import HTMLTestRunner
path="E:\\auto_test\\PO_test"
print (path)
case_path=path+'\\case'
if __name__ == '__main__':
    reportdir = os.path.join("E:\\auto_test\PO_test\\report")
    report_file = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.html'
    reportpath = reportdir+'\\'+report_file
    f = open(reportpath,'w',encoding='utf-8')
    testsuit = unittest.defaultTestLoader.discover(case_path,'*case*.py')
    with open(reportpath,'w',encoding='utf-8') as f:
        runner = HTMLTestRunner(stream=f, title='flie report',description='flie report')
        runner.run(testsuit)
