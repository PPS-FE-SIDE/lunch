import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db="lunch_db")
cur = conn.cursor()

cur.execute("select * from store")
result = cur.fetchall()

print(result)
