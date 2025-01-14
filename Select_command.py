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

cur = conn.cursor()
## select query is used to fetch all data from table 
cur.execute("select * from tutorial;")
for data in cur:
    print(list(data))

## select query is used to fetch particular columns from table 
cur.execute("select Video_id,Watch_time from tutorial;")
for data in cur:
    print(list(data))
cur.close()
conn.close()