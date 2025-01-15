import mysql.connector

## is_connection() method returns a boolean value 
## True - if connection is established 
## False - if connection is not established 
try : 
    conn = mysql.connector.connect(
        user = "root",
        password = "mysql2610",
        host = "localhost",
        port = 3306
    )
    if conn.is_connected():
        print("Successfully Connected")
except : 
    print("Connection failed")

## 1000 LOC - time consuming
conn.close()

## close() method is used to close the connection 
## and it is very important for resource consumption and prevents
## unexpected operations  
