import mysql.connector

dataBase= mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ihave12$'
)

#prepare a cursor object

cursorObject=dataBase.cursor()

#create a database

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")