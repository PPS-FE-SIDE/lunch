import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db="lunch_db")
cur = conn.cursor()

cur.execute('INSERT INTO store (name) VALUES ("이도곰탕 본점");')
conn.commit()
print(cur.execute("select * from store"))
