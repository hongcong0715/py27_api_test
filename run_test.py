import unittest
from BeautifulReport import BeautifulReport
from common.handle_logging import log
from common.handle_path import CASE_DIR,REPORT_DIR

log.info("---------------------------------------开始执行测试用例---------------------")
#  创建测试套件
suite = unittest.TestSuite()
# 加载用例套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASE_DIR))


bf = BeautifulReport(suite)
bf.report("withdraw接口",filename="audit_report.html",report_dir= REPORT_DIR)
log.info("---------------------------------------测试用例执行完毕---------------------")



