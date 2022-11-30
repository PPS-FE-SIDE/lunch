from flask import Flask, Response
import pymysql
import json
from flask_cors import CORS

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db="lunch_db")
cur = conn.cursor()

cur.execute("select store.name, menu.name, menu.price from store join menu on store.name = menu.store")
result = cur.fetchall()


obj = {}
for data in result:
    if data[0] in obj:
        obj[data[0]].append({ "menu": data[1], "price": data[2] } )

    else:
        obj[data[0]] = [{"menu": data[1], "price": data[2]}]

response_json = json.dumps(obj)
print(response_json)


app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def home():
    return Response(response_json, mimetype="application/json", status=200)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
