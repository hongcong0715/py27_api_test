import unittest
from common.handle_excel import HandleExcel
from library.myddt import ddt,data
from common.handle_config import conf
from requests import request
from common.handle_path import DATA_DIR
import os
# from common.handle_logging import log

filename = os.path.join(DATA_DIR,"apicases.xlsx")
@ddt
class LoginTestCase(unittest.TestCase):
    excel = HandleExcel(filename,"login")
    cases = excel.read_data()


    @data(*cases)
    def test_login(self,case):
        # 第一步，准备用例数据  （请求方法，请求地址，请求参数，请求头
        method = case["method"]
        url = case["url"]
        data = eval(case["data"])
        headers = eval(conf.get("env","headers"))
        expected = eval(case["expected"])
        # 用例所在行
        row = case["case_id"] + 1



        # 第二步，发送请求获取实际结果
        response = request(method=method,url=url,json=data,headers=headers)
        res = response.json()
        # print("实际结果：",res)
        # 第三步，断言
        try:

            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["msg"],res["msg"])
        except AssertionError as e:
            self.excel.write_data(row=row,column=8,value="未通过")
            raise e
        else:
            self.excel.write_data(row=row,column=8,value="通过")










