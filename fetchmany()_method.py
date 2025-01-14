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

## fetchmany() method fetches specified no. of records (returns a list of rows)
cur = conn.cursor()
sql = "SELECT * FROM tutorial"
cur.execute(sql)
n = int(input("enter"))
try:
    data = cur.fetchmany(n)
    print(data)
    cur.close()
except :
    print("Unread result found")
conn.close()