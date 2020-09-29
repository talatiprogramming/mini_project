import pymysql  

connection = pymysql.connect(
        host = "localhost",
        port = 33066,
        user = "root",
        passwd = "password",
        db = "test_db"
    )

cursor = connection.cursor()
cursor.execute("SELECT * FROM musicians")
connection.commit()
rows = cursor.fetchall()
cursor.close()
connection.close()

for row in rows:
    print(row)