import pymysql


class HandleMysql:
    def __init__(self):
        # 初始化方法中，连接到数据库，建立连接
        self.conn = pymysql.connect(host="120.78.128.25",
                                    port=3306,
                                    user="future",
                                    password="123456",
                                    charset="utf8",
                                    cursorclass=pymysql.cursors.DictCursor)
        # 创建一个游标对象
        self.cur = self.conn.cursor()

    def find_all(self,sql):
        """
        查询sql语句返回的所有数据
        :param sql:  查询的sql
        :return: 查询到的所有数据
        """
        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_one(self,sql):
        """
        查询sql语句返回的一条数据
        :param sql: 查询的sql
        :return: 查询到的一条数据
        """
        self.cur.execute(sql)
        return self.cur.fetchone()

    def update(self,sql):
        """
        增删改操作的方法
        :param sql: 增删改的sql语句
        :return:
        """
        self.cur.execute(sql)
        self.conn.commit()


if __name__ == '__main__':
    db = HandleMysql()
    sql = "select * from futureloan.member limit 10"
    res = db.find_one(sql)
    print(res)

