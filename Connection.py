## importing mysql connector 
## it creates connection between mysql and python 
import mysql.connector 

try : 
    ## conn is an object returned by connect() method 
    ## connect() is used to establish connection
    conn = mysql.connector.connect(
        user = "root",
        password = "mysql2610",
        host = "localhost",
        # host = "127.0.0.1" - IP address 
        port = 3306
    )
    print("Connected Successfully")

except Exception as obj :
    print("Connection Failed")

