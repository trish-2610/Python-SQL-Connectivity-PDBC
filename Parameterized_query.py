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

## Parameterized Query - %s
cur = conn.cursor()
sql = "Update tutorial set Video_views = %s where Video_id = %s"
# cur.execute(sql,(790,11))
id = int(input("Enter id : "))
views = int(input("Enter views : "))
cur.execute(sql,(views,id))
conn.commit()
cur.close()
conn.close()
