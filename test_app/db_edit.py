import pymysql  
import csv

connection = pymysql.connect(
        host = "localhost",
        port =  33066,
        user = "root",
        passwd = "password",
        db = "test"
    )

# def main(sql_command):
#     cursor = connection.cursor()
#     cursor.execute(sql_command)
    
#     cursor.close()
#     connection.close()


def open_user_file():
    list_of_data = []
    with open("Import_User_Sample_en.csv", "r", newline = "") as user_file:
        read_user = list(csv.reader(user_file))
        for i in range(1, len(read_user)):
            list_of_data.append(read_user[i])
    return list_of_data
            
def separate_data(stuff):
    new_stuff = []
    for item in stuff:        
        new_list = (item[0], item[1], item[3], item[7], item[12])
        new_stuff.append(new_list)
    return new_stuff
    

x = open_user_file()
y = separate_data(x)

def upload_data(stuff):
    cursor = connection.cursor()    
    for item in stuff:
        data_string = ""
        for x in item:            
            data_string += f"\'{x}\', "        
    sql_command = f"INSERT INTO Users (user_name, first_name, job_title, phone_no, post_code) VALUES ({data_string[:-2]})"

    cursor.execute(sql_command)
    cursor.close()
    connection.close()

upload_data(y)