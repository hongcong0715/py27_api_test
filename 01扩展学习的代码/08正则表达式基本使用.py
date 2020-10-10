import re
"""
1、re 模块
findall :查找所有符合规范的数据
第一个参数，匹配规则
第二个参数，被查找的字符串


返回值，是一个列表（list),所有符合规范的数据。找不到时返回的是空列表！

-------------------------------------------------------------------

2、search
-------------------------------------------------------------------
3、match

-------------------------------------------------------------------
4、sub

"""
# s1 = "ggjlagjajg13310006789jjjklljllj13310006789hhouhooippi13310006789hghiuiggghf13310006789"
# res1 = re.findall("13310006789",s1)
# print(res1)           #  ['13310006789', '13310006789', '13310006789', '13310006789']
# print(type(res1))     #  <class 'list'>


# -------------------------正则表达式的匹配规则------------------------------------------
# s2 = "111aaa\t"
# . 表示除\n之外的任意字符>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# res2 = re.findall(".",s2)
# print(res2)


# []   表示举例多个字符  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# s3 = "111aaajgalgjgjgjj444222444ggjggk"
# res3 = re.findall("[0-9a-zA-Z]",s3)
# print(res3)


# \d  表示0-9 ， >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s4 = "5678hhh"
# res4 = re.findall("\d",s4)
# print(res4)      # ['5', '6', '7', '8']


# \D 表示非数字（0-9除外，其他的都匹配）  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s5 = "56789qazwsx"
# res5 = re.findall("\D",s5)
# print(res5)    #  ['q', 'a', 'z', 'w', 's', 'x']


# \s 表示空白键  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s6 = "  67 hj"
# res6 =re.findall("\s",s6)
# print(res6)     #  [' ', ' ', ' ']


# \S 表示非空白键  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s7 = "  67 hj"
# res7 = re.findall("\S",s7)
# print(res7)   ['6', '7', 'h', 'j']



# \w 表示单词字符（数字、字母、下划线、中文特殊）  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s8 = "pa123_?*&%$#@~你好"
# res8 = re.findall("\w",s8)
# print(res8)   # ['p', 'a', '1', '2', '3', '_', '你', '好']


# \W 表示非单词字符  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s9 = "pa123_?*&%$#@~你好"
# res9 = re.findall("\W",s9)
# print(res9)   # ['?', '*', '&', '%', '$', '#', '@', '~']




# -----------------------------------表示数量----------------------------
# {n}: 表示前一个字符出现n次，>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s1 = "ggjlagjajg13310006788jjjklljllj13310006789hhouhooippi13310006789hghiuiggghf13310006790"
# res1 = re.findall("\d{11}",s1)
# print(res1)     # ['13310006788', '13310006789', '13310006789', '13310006790']

# {n,m }:  表示前一个字符出现n-m次，>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# s2 = "abc111df123456hhhhhhhh789000"
# res2 = re.findall("\d{3,5}",s2)
# print(res2)    # ['111', '12345', '78900']


# 贪婪模式，符合匹配的规范之内，尽可能匹配更多的内容
# 非贪婪模式，符合匹配的规范之内，尽可能匹配更少的内容


# {m,}  表示一个字符 至少出现m次，>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# *   表示前一个字符串出现0次或者n次（0次以上），>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s3 = "abc123"
# res3 = re.findall("\d*",s3)
# print(res3)    # ['', '', '', '123', '']


# +  表示前一个字符出现1次n次（1次以上），>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# s4 = "abc123"
# res4 = re.findall("\d+",s4)
# print(res4)   # ['123']

# -----------------------------------表示边界----------------------------
# 单词边界  ，>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s1= "python123 python456 python"
# res1 = re.findall(r"\bpython",s1)
# print(res1)    # ['python', 'python', 'python']

# 非单词边界 ，>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s2 = "python123python456python"
# res2 = re.findall(r"\Bpython",s2)
# print(res2)      # ['python', 'python']


# 字符串开头^  字符串开头 ，>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s3 = "python123java"
# res3 = re.findall("^python",s3)
# print(res3)    # ['python']

# 字符串结尾  $  字符串结尾 ，>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s4 = "python123java"
# res4 = re.findall("java$",s4)
# print(res4)  #  ['java']

# |   匹配多个规范
# s5 = "phone1234pwd456"
# res5 = re.findall("phone|pwd|456",s5)
# print(res5)   # ['phone', 'pwd', '456']


# ()  表示匹配分组

# data = '{"user":#user#,"pwd":#pwd#,"name":#name#,"age":##}'
# res = re.findall("#.*?#",data)
# print(res)

from common.handle_config import conf


data = '{"user":#user#,"pwd":#pwd#,"name":#name#,"age":#age#}'


def replace_data(data):
    while re.search("#(.*?)#",data):

        res = re.search("#(.*?)#",data)
        # print(res)   # <re.Match object; span=(8, 14), match='#user#'>  返回的是一个匹配对象
        key = res.group()
        # print(key)   #  --#user#
        item = res.group(1)
        # print(item)  #   user

        value = conf.get("musen",item)  # item = user   ；value = python

        data = data.replace(key,value)  #  key ==  #user#
        # print(data)             # {"user":python,"pwd":#pwd#,"name":#name#,"age":#age#}
    return data


# a = replace_data(data = '{"user":#user#,"pwd":#pwd123#,"name":#name#,"age":#age#}')
# print(a)
