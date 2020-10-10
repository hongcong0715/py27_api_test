from configparser import ConfigParser
from common.handle_path import CONF_DIR
import os


class HandleConfig(ConfigParser):
    def __init__(self,filename):
        super().__init__()
        self.read(filename,encoding="utf8")


conf = HandleConfig(os.path.join(CONF_DIR, "config.ini"))
