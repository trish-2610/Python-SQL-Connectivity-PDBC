import mysql.connector

## creating connection using dictionary 
config = { 
    "user" : "root",
    "password" : "mysql2610",
    "host" : "localhost",
    "port" : 3306
}

try : 
    conn = mysql.connector.connect(**config) ## variable arguments
    print("Connected Successfully")
except :
    print("Connection Failed")


## creating it's function 
def connect(u,p,h,po) :
    config = {
        "user" : u ,
        "password" : p,
        "host" : h,
        "port" : po
    }
    try : 
        conn = mysql.connector.connect(**config) ## variable arguments
        print("Connected Successfully")
    except :
        print("Connection Failed")
## function calling 
connect("root","mysql2610","localhost",3306)