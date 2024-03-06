import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "python_db"
)

mycursor = mydb.cursor()

sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
val = [
  ('Peter', 22),
  ('Amy', 23),
  ('Hannah', 21),
  ('Michael', 22),
  ('Sandy', 20),
  ('Betty', 25),
  ('Richard', 28),
  ('Susan', 34),
  ('Vicky', 24),
  ('Ben', 28),
  ('William', 20),
  ('Chuck', 34),
  ('Viola', 21)
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


# Close the connection
mydb.close()