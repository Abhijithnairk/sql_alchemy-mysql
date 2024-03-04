import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "abhijith_user",
    password = "Abhi@1212",
    database = "GROCERY_STORE"
)

cursor = mydb.cursor()

#cursor.execute("CREATE TABLE WORKERS(ID INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(255),AGE INT)")

query = "INSERT INTO WORKERS(NAME,AGE) VALUES(%s,%s)"
values = [('john',35),
          ('alice',25),
          ('bob',30),
          ('diana',20)
]

cursor.executemany(query,values)
mydb.commit()

cursor.execute("SELECT * FROM WORKERS")
result = cursor.fetchall()
for row in result:
    print(row)
    
cursor.close()
mydb.close()
