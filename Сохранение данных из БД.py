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
        'name': result[0],
        'date': result[1],
        'images': result[2],
        'link': result[3],
        'description': result[4]
    })

with open('from_db.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

mydb.close()
