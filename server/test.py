import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db="lunch_db")
cur = conn.cursor()

cur.execute("select store.name, menu.name, menu.price from store join menu on store.name = menu.store")
result = cur.fetchall()

print(result)
