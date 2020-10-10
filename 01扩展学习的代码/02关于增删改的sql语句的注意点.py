"""
pymysql 模块操作数据库，默认是开启了事务
所以在执行增删改的相关操作之后，一定要提交事务才会生效
"""

# 第一步，连接到数据库
import pymysql
conn = pymysql.connect(host="120.78.128.25",port=3306,user="future",password="123456",charset="utf8",cursorclass = pymysql.cursors.DictCursor)

# 第二步，创建一个游标对象
cur = conn.cursor()
# 假设这个是增删改的语句
sql = "select * from futureloan.member limit 10"

# 第三步，执行sql
cur.execute(sql)

# 第四步， 提交事务
conn.commit()