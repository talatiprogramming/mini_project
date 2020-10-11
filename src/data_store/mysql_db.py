import pymysql

def make_connection():
    return pymysql.connect(
        host = "localhost",
        port =  33066,
        user = "root",
        passwd = "password",
        db = "metal_db",
        autocommit = True
    )

def import_name():
    connection = make_connection()
    cursor = connection.cursor()
    name_list = []
    try:
        cursor.execute("SELECT name FROM Names")
        imported_name = cursor.fetchall()
        for item in imported_name:
            name_list.append(item[0])
        return name_list
    finally:
        cursor.close()
        connection.close()
    
def import_song_title(condition=None):
    connection  = make_connection()
    cursor = connection.cursor()
    name_list = []
    try:
        cursor.execute(f"SELECT song_title FROM Songs {condition};")
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
    name_list = {}
    try:
        cursor.execute("SELECT * FROM Songs")
        imported_name = cursor.fetchall()
        for item in imported_name:
            name_list.update({str(item[0]): [item[1], item[2], item[3], item[4]]})
        return name_list
    finally:
        cursor.close()
        connection.close()

def import_album():
    connection  = make_connection()
    cursor = connection.cursor()
    name_list = {}
    try:
        cursor.execute("SELECT * FROM Albums")
        imported_name = cursor.fetchall()
        for item in imported_name:
            name_list.update({str(item[0]): [item[1], item[2]]})
        return name_list
    finally:
        cursor.close()
        connection.close()


def insert_entry(string1, string2):
        connection  = make_connection()
        cursor = connection.cursor()
        try:            
            cursor.execute(f"INSERT INTO {string1} VALUES ({string2});")            
        finally:
            cursor.close()
            connection.close()

def remove_entry(string1, string2):
        connection = make_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(f"DELETE FROM {string1} WHERE {string2};")
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

def import_fav_songs(string1=""):
    connection = make_connection()
    cursor = connection.cursor()
    table_list = {}
    try:
        cursor.execute(f"SELECT * FROM Favourites{string1}")
        joined_tables = cursor.fetchall()
        for item in joined_tables:        
            table_list.update({str(item[0]): [item[1], item[2], item[3]]})
        return table_list
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def import_song_choice(string1, string2, string3):
    connection = make_connection()
    cursor = connection.cursor()
    table_list = []
    try:
        cursor.execute(f"SELECT {string1} FROM {string2} WHERE {string3};")
        joined_tables = cursor.fetchall()
        for item in joined_tables:        
            table_list.append([item[0], item[1]])
        return table_list
        connection.commit()
    finally:
        cursor.close()
        connection.close() 


def inner_join(string1, string2, string3, string4):
    connection = make_connection()
    cursor = connection.cursor()
    table_list = []
    try:
        cursor.execute(f"SELECT {string1} FROM {string2} INNER JOIN {string3} ON {string4};")
        joined_tables = cursor.fetchall()
        for item in joined_tables:
            table_list.append([item])
        return table_list
        connection.commit()
    finally:
        cursor.close()
        connection.close() 

