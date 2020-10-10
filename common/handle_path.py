import os
# 打印当前模块所在目录
# print(os.path.abspath(__file__))    # /Users/momo/Documents/py27_api_test/common/handle_path.py
# 获取项目所在的绝对路径

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)   # /Users/momo/Documents/py27_api_test



# 用例模块所在的目录路径；
CASE_DIR = os.path.join(BASE_DIR,"testcases")
# 用例数据所在的目录路径；
DATA_DIR = os.path.join(BASE_DIR,"data")

# 配置文件所在的目录路径；
CONF_DIR = os.path.join(BASE_DIR,"conf")

# 测试报告所在的目录路径；
REPORT_DIR = os.path.join(BASE_DIR,"reports")

# 日志文件的绝对路径
LOG_DIR = os.path.join(BASE_DIR,"logs")


