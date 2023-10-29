import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'YourDatabasePassword'

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE CompDataBase")

print("All Done!")
