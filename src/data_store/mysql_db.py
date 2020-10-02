import pymysql

def make_connection():
    return pymysql.connect(
        host = "localhost",
        port =  33066,
        user = "root",
        passwd = "password",
        db = "test2"
    )

def import_name():
    connection = make_connection()
    cursor = connection.cursor()
    name_list = []
    try:
        cursor.execute("SELECT first_name FROM Names")
        imported_name = cursor.fetchall()
        for item in imported_name:
            name_list.append(item[0])
        return name_list
    finally:
        cursor.close()
        connection.close()
    

def import_song():
    connection  = make_connection()
    cursor = connection.cursor()
    name_list = []
    try:
        cursor.execute("SELECT song_title FROM Songs")
        imported_name = cursor.fetchall()
        for item in imported_name:
            name_list.append(item[0])
        return name_list
    finally:
        cursor.close()
        connection.close()    
