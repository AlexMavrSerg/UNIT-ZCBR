import mysql.connector
import json

mydb = mysql.connector.connect(
    host="db4free.net",
    user="searchproduct",
    password="14112000i",
    database="search_product_u"
)

mycursor = mydb.cursor()

with open('output.json', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    sql = "SELECT * FROM BVD_Parser WHERE name = %s"
    val = (item['name'],)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if not result:
        sql = "INSERT INTO BVD_Parser (name, date, images, link, description) VALUES (%s, %s, %s, %s, %s)"
        val = (item['name'], item['date'], item['images'], item['link'], item['description'])
        mycursor.execute(sql, val)
        mydb.commit()

mydb.close()
