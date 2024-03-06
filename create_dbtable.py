import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "python_db"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

# Check if the table creation was successful
mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)
tables = mycursor.fetchall()
if ("students",) in tables:
    print("Table 'students' created successfully")
else:
    print("Failed to create table 'students'")

# Close the connection
mydb.close()