import mysql.connector

con = mysql.connector.connect(host="localhost", database='python_mysql', user='root', password='sami')

cursor = con.cursor()
if con.is_connected():
    print("is connected to DB")
else:
    print("is not connected")
con.close()
cursor.close()
