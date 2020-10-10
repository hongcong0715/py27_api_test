import random
from common.handle_db import HandleMysql

db = HandleMysql()


def random_phone():
    """
    生成一个数据里里面未注册的手机号
    :return:
    """
    while True:
        phone = "155"
        for i in range(8):
            r = random.randint(0,9)
            phone += str(r)
        sql = "select * from futureloan.member where mobile_phone = {}.format(phone)"
        res = db.find_count(sql)
        if res == 0:
            return phone

res = random_phone()
print(res)