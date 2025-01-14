## commit() - to save changes 
## rollback() - to undo changes , in case of any error or exception 
## connection object is related to connection 
## cursor object is related to cursor
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

## inserting data 
## inserting single data
sql = "Insert into tutorial(Video_id,Video_name,Video_views,Watch_time) values(2,'Bye',500,4.5);"
## inserting multiple data ( comma separated values )
sql = """Insert into tutorial(Video_id,Video_name,Video_views,Watch_time)
        values(7,'A',300,9.7) ,(8,'B',450,10.4) ,(9,'C',200,6.5);"""
try:
    cur.execute(sql)
    ## data will not get inserted until it gets committed 
    conn.commit()
    print("Successfully committed(data inserted)")
    ## rowcount() method is used to print no. of rows affected 
    print(f"{cur.rowcount} : rows affected(inserted)")
except Exception as e : 
    conn.rollback()
    ## rollback executes in case of any exception 
    print(e," ","Failed commit")
cur.close()
conn.close()