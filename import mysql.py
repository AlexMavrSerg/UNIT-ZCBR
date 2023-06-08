import mysql.connector

# connect to the database
cnx = mysql.connector.connect(user='your_username', password='your_password',
                              host='127.0.0.1', database='searchproducts')

# print a confirmation message
if cnx.is_connected():
    print('Connected to the MySQL database "searchproducts"')

# close the connection when finished
cnx.close()
