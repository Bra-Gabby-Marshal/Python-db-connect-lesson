import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM students")

mycursor.execute(("SELECT name from students WHERE age=22"))
myresult = mycursor.fetchall()

for row in myresult:
    print(row)


# Close the connection
mydb.close()