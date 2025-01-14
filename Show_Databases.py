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

cur = conn.cursor()
cur.execute("SHOW DATABASES")
## cur object only points to result , it works as pointer only 
## to print the result use for loop 
for data in cur:
    print(data[0])
## output - all databases name 

for data in cur:
    print(data[0])
## NO output : because cur object only print the result one time 
## and after execution(printing) it deletes the result 

cur.close()
conn.close()