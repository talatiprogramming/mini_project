import pymysql

connection  = pymysql.connect(
        host = "localhost",
        port =  33066,
        user = "root",
        passwd = "password",
        db = "test2"
    )

cursor = connection.cursor()

f_name_input = input("Enter a first name: ").title()
# surname_input = input("Enter a last name: ").title()
# entry_string = f"\'{f_name_input}\', \'{surname_input}\'"
def insert_name_entry(string):
    try:
        cursor.execute(f"INSERT INTO Names (first_name, last_name) VALUES ({string});")
        connection.commit()
    finally:
        cursor.close()
        connection.close()

def import_name():
    try:
        cursor.execute("SELECT first_name FROM Names")
        imported_name = cursor.fetchall()
        for item in imported_name:
            print(item[0])
    finally:
        cursor.close()
        connection.close()      

def remove_name_entry(self):
    cursor.execute(f"DELETE FROM Names WHERE first_name=\'{self.name}\'")
    connection.commit()   
# insert_name_entry(entry_string)

remove_name_entry(f_name_input)
