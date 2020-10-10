"""
主机：120.78.128.25
port：3306
用户：future
密码：123456


"""
# 第一步，连接到数据库
import pymysql
conn = pymysql.connect(host="120.78.128.25",port=3306,user="future",password="123456",charset="utf8",cursorclass = pymysql.cursors.DictCursor)

# 第二步，创建一个游标对象
cur = conn.cursor()

sql = "select * from futureloan.member limit 10"

# 第三步，执行sql语句
res = cur.execute(sql)
print(res)

# 第四步，获取查询到的结果
data = cur.fetchone()
print(data)

# data2 = cur.fetchall()
# print(data2)