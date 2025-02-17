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

## fetchone() method fetches rows one by one 
cur = conn.cursor()
sql = "SELECT * FROM tutorial"
cur.execute(sql)
try:
    # data1 = cur.fetchone() ## fetches 1st row
    # print(data1)
    # data2 = cur.fetchone() ## fetches 2nd row
    # print(data2) 
    # data3 = cur.fetchone() ## fetches 3rd row
    # print(data3)
    # cur.close()

    ## 2nd way
    # n = int(input("Enter the number of rows : "))
    # for i in range(n):
    #     data = cur.fetchone()
    #     if data == None:
    #         continue
    #     print(data)
    # cur.close()

    ## 3rd way
    while(True): ## fetch all records
        data = cur.fetchone()
        if data == None:
            break
        print(data)
    cur.close()
except :
    print("Unread result found")
conn.close()
