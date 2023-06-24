import mysql.connector
import json

JSON = 'from_db.json'

mydb = mysql.connector.connect(
    host="db4free.net",
    user="searchproduct",
    password="14112000i",
    database="search_product_u"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM BVD_Parser")
results = mycursor.fetchall()

data = []
for result in results:
    data.append({
        'id': results[0],
        'name': result[1],
        'date': result[2],
        'images': result[3],
        'link': result[4],
        'description': result[5]
    })

with open('from_db.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

mydb.close()
