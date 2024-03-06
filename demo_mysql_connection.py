import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",     # Your host, usually localhost
    user="root",          # Your username
    passwd="",            # Your password
    database="python_db" # Your database name
)

# Check if connection is successful
if connection.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect to MySQL database")

# Perform database operations here...

# Close the connection
connection.close()
