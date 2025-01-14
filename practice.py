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
try : 
    cur.execute("Insert into tutorial values(11,'Z',290,2.4);")
    conn.commit()
    print(f"{cur.rowcount} : row successfully inserted")
except Exception as e:
    conn.rollback()
    print(e," ","Failed Insertion of records")
cur.execute("Select * from tutorial;")
for data in cur:
    print(list(data))
