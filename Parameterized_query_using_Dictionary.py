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

## using dictionary - order need not to be maintained 
## when using keyword arguments don't use prepared statement
cur = conn.cursor()
sql = "Insert into tutorial(Video_id,Video_name,Video_views,Watch_time) values(%(Video_id)s,%(Video_name)s,%(Video_views)s,%(Watch_time)s)"
n = int(input("Enter number of values : "))
# for i in range(n):
#     id = int(input("Enter id : "))
#     name = input("Enter name : ")
#     views = int(input("Enter views : "))
#     watch_time = float(input("Enter watch time : "))
#     cur.execute(sql,{"Video_id" : id , "Video_views" : views ,"Video_name" : name , "Watch_time" : watch_time})
#     conn.commit()

## using while loop - no limit
while(True):
   id = int(input("Enter id : "))
   name = input("Enter name : ")
   views = int(input("Enter views : "))
   watch_time = float(input("Enter watch time : "))
   cur.execute(sql,{"Video_id" : id , "Video_views" : views ,"Video_name" : name , "Watch_time" : watch_time})
   conn.commit()
   ans = input("Do you want to continue ? y/n").lower()
   if ans != "y":
       break
   conn.commit()

cur.close()
conn.close()
