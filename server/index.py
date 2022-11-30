from flask import Flask, Response
import pymysql
import json

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db="lunch_db")
cur = conn.cursor()

cur.execute("select * from store")
result = cur.fetchall()
response_data = []

for data in result:
    response_data.append({"name": data[1]})

response_json = json.dumps({"store": response_data})
print(response_json)


app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return Response(response_json, mimetype="application/json", status=200)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
