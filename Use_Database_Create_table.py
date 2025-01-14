import mysql.connector 

try:
    conn = mysql.connector.connect(
        user = "root",
        password = "mysql2610",
        host = "localhost",
        port = 3306,
        database = "pdbc" ## another way to connect database 
    )
    if conn.is_connected():
        print("Successfully Connected")
except:
    print("Connection Failed")

cur = conn.cursor()

## using/selecting database 
## cur.execute("USE pdbc")

## creating table 
cur.execute("""CREATE TABLE IF NOT EXISTS tutorial1(
            Video_id INT PRIMARY KEY,
            Video_name VARCHAR(100) NOT NULL,
            Video_views INT,
            Watch_time FLOAT)""")

## output before execution 
## Empty set (0.00 sec)

## output after execution 
# +----------------+
# | Tables_in_pdbc |
# +----------------+
# | tutorial       |
# +----------------+
# 1 row in set (0.00 sec)


## Describing table (Description)
cur.execute("DESC tutorial")
for data in cur:
    print(data)
cur.close()
conn.close()
