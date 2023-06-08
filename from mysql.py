from mysql.connector import connect, Error
hosts="db4free.net"
users= "searchproduct"
databases="search_product_u"
passwords="14112000i"
with connect(host=hosts, user=users, password=passwords, database=databases, use_unicode=True, charset='utf8') as connection:
        connection.autocommit = True
        radiusshops = []
        select_movies_query = """SELECT * FROM Browser_data;"""
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            result = cursor.fetchall()
print(result)