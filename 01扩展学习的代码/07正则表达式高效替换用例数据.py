user = "python"
pwd = "lemonban"
name = "dapang"
age = 16

data = '{"user":#user#,"pwd":#pwd#,"name":#name#,"age":#age#}'

# 使用字符串的方法进行替换，缺点 >>>>>每次只能替换一个数据，效率太低
data = data.replace("#user#",user)
data = data.replace("#pwd#",pwd)
data = data.replace("#name#",name)
data = data.replace("#age#",str(age))

print(data)   # {"user":python,"pwd":lemonban,"name":dapang,"age":16}


# 通过正则表达式进行数据替换




