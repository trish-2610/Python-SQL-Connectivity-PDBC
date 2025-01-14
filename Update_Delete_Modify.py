import mysql.connector as myconn
try : 
    db = myconn.connect(
        user = "root",
        password = "mysql2610",
        host = "localhost",
        port = 3306,
        database = "pdbc"
    )
    if db.is_connected():
        print("Successfully Connected")
except : 
    print("Connection failed")

cur = db.cursor()
try :
    sql1 = "Update tutorial set video_name = 'updated' where Video_id = 3;"
    sql2 = "Delete from tutorial where Video_id = 7 "
    cur.execute(sql1)
    db.commit()
    print(f"{cur.rowcount} : rows updated")
    cur.execute(sql2)
    db.commit()
    print(f"{cur.rowcount} : rows deleted")
except Exception as e :
    print("Modification Failed")
    db.rollback()

cur.close()
db.close()
    