import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123654",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
