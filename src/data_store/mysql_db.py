import pymysql

def make_connection():
    return pymysql.connect(
        host = "localhost",
        port =  33066,
        user = "root",
        passwd = "password",
        db = "metal_db"
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

def import_songID():
    connection  = make_connection()
    cursor = connection.cursor()
    name_list = []
    try:
        cursor.execute("SELECT * FROM Songs")
        imported_name = cursor.fetchall()
        for item in imported_name:
            name_list.append(f"{item[0]} {item[1]}")
        return name_list
    finally:
        cursor.close()
        connection.close()

def insert_entry(string1, string2):
        connection  = make_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(f"INSERT INTO {string1} VALUES (\'{string2}\')")
            connection.commit()
        finally:
            cursor.close()
            connection.close()

def remove_entry(string1, string2, string3):
        connection = make_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(f"DELETE FROM {string1} WHERE {string2}=\'{string3}\'")
            connection.commit()
        finally:
            cursor.close()
            connection.close() 

def update_entry(string1, string2, string3):
    connection = make_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(f"UPDATE {string1} SET {string2} WHERE {string3};")
        connection.commit()
    finally:
        cursor.close()
        connection.close() 

def return_fav_songs():
    connection = make_connection()
    cursor = connection.cursor()
    table_list = []
    try:
        cursor.execute(f"SELECT n.first_name, s.song_title FROM Names as n INNER JOIN Songs as s ON n.fav_songID=s.songID;")
        joined_tables = cursor.fetchall()
        for item in joined_tables:
            table_list.append(f"{item[0]} - {item[1]}")
        return table_list
        connection.commit()
    finally:
        cursor.close()
        connection.close() 

