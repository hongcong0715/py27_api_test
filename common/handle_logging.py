import logging
from common.handle_config import conf
import os
from common.handle_path import LOG_DIR


log_filepath = os.path.join(LOG_DIR,conf.get("log","filename"))

class HandleLogger:    # 这个是处理日志相关的模块
    @staticmethod
    def create_logger():
        # 第一步，创建一个日志收集器
        log = logging.getLogger("dapang")

        # 第二步，设置收集器收集的等级
        log.setLevel(conf.get("log","level"))

        # 第三步，设置输出渠道

        fh = logging.FileHandler(log_filepath, encoding="utf-8")
        fh.setLevel(conf.get("log","fh_level"))
        log.addHandler(fh)

        sh = logging.StreamHandler()
        sh.setLevel(conf.get("log","sh_level"))
        log.addHandler(sh)

        # 第四步，设置输出格式
        # formats = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        # 创建一个输出格式对象
        form = logging.Formatter(conf.get("log","formats"))

        # 将输出格式添加到输出渠道
        fh.setFormatter(form)
        sh.setFormatter(form)

        return log


log = HandleLogger().create_logger()




