import mysql.connector
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

## Prepared is used to check query syntax , privileges (only one time)
## query is processed only one time and then same query is used for multiple times without checking any syntax
## Improved speed
## Prevent SQL Injection 
## Save time

cur = conn.cursor(prepared = True)
sql = "Insert into tutorial(Video_id,Video_name,Video_views,Watch_time) values(%s,%s,%s,%s)"
n = int(input("Enter number of values : "))
for i in range(n):
    id = int(input("Enter id : "))
    name = input("Enter name : ")
    views = int(input("Enter views : "))
    watch_time = float(input("Enter watch time : "))
    cur.execute(sql,(id,name,views,watch_time))
    ## when using tuple order should be maintained
    conn.commit()
cur.close()
conn.close()
