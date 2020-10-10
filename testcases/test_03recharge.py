import unittest
from library.myddt import ddt,data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
import os
from common.handle_config import conf
from requests import request
import jsonpath
from common.handle_logging import log
from common.handle_db import HandleMysql
import decimal
from common.handle_data import EnvData,replace_data



@ddt
class RechargeTestCase(unittest.TestCase):
    # 创建一个操作excel的对象
    excel = HandleExcel(os.path.join(DATA_DIR,"apicases.xlsx"),"recharge")
    cases = excel.read_data()
    db = HandleMysql()


    @classmethod
    def setUpClass(cls):
        """
        用例执行的前置条件，登录
        :return:
        """
        # 准备登录的相关数据
        url = conf.get("env","url") + "/member/login"
        data = {
            "mobile_phone":conf.get("test_data","phone"),
            "pwd":conf.get("test_data","pwd")
        }
        headers = eval(conf.get("env","headers"))
        response = request(method="post",url=url,json=data,headers=headers)
        res = response.json()
        member_id = str(jsonpath.jsonpath(res,"$..id")[0])  # 下标取值
        # print("提取到的用户id为：",cls.member_id)
        # print(type(cls.member_id))

        # token_type = jsonpath.jsonpath(res,"$..token_type")   # 获取到的是Bearer
        # # print(token_type,type(token_type))

        token = "Bearer" + " " + jsonpath.jsonpath(res,"$..token")[0]
        setattr(EnvData,"member_id",member_id)
        setattr(EnvData,"token",token)






    @data(*cases)
    def test_recharge(self,case):
        # 第一步 ，准备用例
        url = conf.get("env","url") + case["url"]
        method = case["method"]


        # 准备用例参数
        # 替换参数中用户的ID
        # case["data"] = case["data"].replace("#member_id#",self.member_id)


        # 转换为字典
        data = eval(replace_data(case["data"]))
        headers = eval(conf.get("env","headers"))
        # 准备请求头
        headers["Authorization"] = getattr(EnvData,"token")
        expected = eval(case["expected"])
        row = case["case_id"] + 1

        # 判断该用例是否需要数据库校验,获取充值之前的账户余额
        if case["check_sql"]:
            # sql = case["check_sql"].format(self.member_id)
            sql = replace_data(case["check_sql"])
            start_money = self.db.find_one(sql)["leave_amount"]
            print("充值之前的金额：",start_money)

        # 第二步， 发送请求，获取实际结果
        response = request(method=method,url=url,json=data,headers=headers)
        res = response.json()
        print("预期结果：",expected)
        print("实际结果：",res)


        # 获取充值后的账户余额
        if case["check_sql"]:
            # sql = case["check_sql"].format(self.member_id)
            sql = replace_data(case["check_sql"])

            end_money = self.db.find_one(sql)["leave_amount"]
            print("充值后的金额：",end_money)

        # 第三步，断言预期结果和实际结果
        try:
            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["msg"],res["msg"])
            # 判断是否需要sql校验：
            if case["check_sql"]:
                recharge_money = decimal.Decimal(str(data["amount"]))
                self.assertEqual(recharge_money,end_money - start_money)
        except AssertionError as e:
            # 将结果回写excel  中
            log.error("用例-- {}--执行未通过".format(case["title"]))
            # log.debug("预期结果：".format(expected))
            # log.debug("实际结果：".format(res))
            log.exception(e)    # 这样可以异常情况打印到日志文件中！
            self.excel.write_data(row=row, column=8, value="未通过")
            raise e
        else:
            # 将结果回写excel  中
            log.error("用例--{}--执行通过".format(case["title"]))

            self.excel.write_data(row=row, column=8, value="通过")


