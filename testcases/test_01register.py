import unittest
import random
from common.handle_excel import HandleExcel
from library.myddt import ddt,data
from common.handle_config import conf
from requests import request
from common.handle_logging import log
from common.handle_path import DATA_DIR
import os
from common.handle_db import HandleMysql
filename = os.path.join(DATA_DIR,"apicases.xlsx")
@ddt
class RegisterTestCase(unittest.TestCase):
    excel = HandleExcel(filename,"register")
    cases = excel.read_data()
    db = HandleMysql()


    @data(*cases)
    def test_register(self,case):
        # 第一步，准备用例数据  （请求方法，请求地址，请求参数，请求头
        # 请求方法
        method = case["method"]
        # 请求url
        url = case["url"]
        # 请求参数是否有手机号需要替换
        # 判断
        if "#phone#" in case["data"]:
            phone = self.random_phone()
            case["data"] = case["data"].replace("#phone#",phone)

        data = eval(case["data"])
        headers = eval(conf.get("env","headers"))
        expected = eval(case["expected"])
        # 用例所在行
        row = case["case_id"] + 1


        # 第二步，发送请求获取实际结果
        response = request(method=method,url=url,json=data,headers=headers)
        res = response.json()
        # print("实际结果：",res)

        print("预期结果：", expected)
        print("实际结果：", res)

        # 第三步，断言
        try:

            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["msg"],res["msg"])
            # 判断是否需要进行sql校验
            if case["check_sql"]:
                sql = case["check_sql"].replace("#phong#",data["mobile_phone"])

                res = self.db.find_count(sql)
                self.assertTrue(1,res)

        except AssertionError as e:
            # ---------------------将结果回写excel  中
            log.error("用例---- {}----执行未通过".format(case["title"]))
            log.info("预期结果：",expected)
            log.info("实际结果：",res)
            log.exception(e)
            # log.error(e）
            log.exception(e)   # 这样可以异常情况打印到日志文件中！
            self.excel.write_data(row=row,column=8,value="未通过")
            raise e
        else:
            # ----------------------将结果回写excel  中
            log.error("用例---- {}----执行通过".format(case["title"]))

            self.excel.write_data(row=row,column=8,value="通过")

    @classmethod
    def random_phone(self):
        """
        生成一个数据里里面未注册的手机号
        :return:
        """
        while True:
            phone = "155"
            for i in range(8):
                r = random.randint(0, 9)
                phone += str(r)
            sql = "select * from futureloan.member where mobile_phone = {}".format(phone)
            res = self.db.find_count(sql)
            if res == 0:
                return phone













