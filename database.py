import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Check if connection is successful
if mydb.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect to MySQL database")

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Execute SQL query to create a database
mycursor.execute("CREATE DATABASE IF NOT EXISTS python_db")

# Query to get the list of databases
mycursor.execute("SHOW DATABASES")

# Fetch all databases
databases = mycursor.fetchall()

# Check if the newly created database exists in the list of databases
if ("python_db",) in databases:
    print("Database 'python_db' created successfully")
else:
    print("Failed to create database 'python_db'")

# Displaying all databases
for db in mycursor:
    print(db)