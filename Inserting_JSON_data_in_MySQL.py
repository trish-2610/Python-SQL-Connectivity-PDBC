## Write a program for inserting given json data into MySQL table

import json
import mysql.connector

## loading/reading json data file 
with open("data.json","r") as f :
    data = json.load(f)
print(data)

## creating connection 
try : 
    conn = mysql.connector.connect(
        user = "root",
        password = "mysql2610",
        host = "localhost",
        port = 3306,
        database = "pdbc"
    )
    if conn.is_connected():
        print("Successfully Connected")
except : 
    print("Connection failed")

## writing json data into data table 
cur = conn.cursor()
for item in data :
    print(item)
    sql = "Insert into data values(%s,%s,%s)"
    cur.execute(sql,(item["name"],item["age"],item["salary"]))
    conn.commit()
    print(cur.rowcount," rows inserted")   
cur.close()
conn.close()