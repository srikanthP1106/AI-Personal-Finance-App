import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Manasa@123",
    database="ai_finance"
)

cursor = connection.cursor()

print("Database Connected Successfully!")