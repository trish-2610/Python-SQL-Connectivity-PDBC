## cursor object allows you to execute SQL command in database 
## cursor actually points to data , result(list , tuple format) , etc.

## execute() method is used to execute SQL query by using cursor object 
## Query should be in the form of string only (mandatory argument)

import mysql.connector 
try : 
    conn = mysql.connector.connect(
        user = "root",
        password = "mysql2610",
        host = "localhost",
        port = 3306
    )
    if conn.is_connected():
        print("Connected")
except : 
    print("Not Connected")

## creating cursor using cursor() method that returns cursor object 
cur = conn.cursor()

## calling execute method using this cursor object to execute query 
cur.execute("CREATE DATABASE PDBC")

## close the cursor object 
cur.close()

## OUTPUT BEFORE 

# mysql> show databases ;
# +--------------------+
# | Database           |
# +--------------------+
# | information_schema |
# | mysql              |
# | performance_schema |
# | practice           |
# +--------------------+
# 4 rows in set (0.00 sec)

## OUTPUT AFTER 

# mysql> show databases ;
# +--------------------+
# | Database           |
# +--------------------+
# | information_schema |
# | mysql              |
# | pdbc               |
# | performance_schema |
# | practice           |
# +--------------------+
# 5 rows in set (0.00 sec)
