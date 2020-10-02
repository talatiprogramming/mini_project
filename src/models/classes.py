import csv
import pymysql
from src.core import table as t
from src.data_store import load_save as l

connection  = pymysql.connect(
        host = "localhost",
        port =  33066,
        user = "root",
        passwd = "password",
        db = "test2"
        )
cursor = connection.cursor()

class Names:
    def __init__(self, name):
        self.name = name

    def insert_name_entry(self):
        connection  = pymysql.connect(
        host = "localhost",
        port =  33066,
        user = "root",
        passwd = "password",
        db = "test2"
        )
        cursor = connection.cursor()
        try:
            cursor.execute(f"INSERT INTO Names (first_name) VALUES (\'{self.name}\');")
            connection.commit()
        finally:
            cursor.close()
            connection.close()
        
    def remove_name_entry(self):
        connection  = pymysql.connect(
        host = "localhost",
        port =  33066,
        user = "root",
        passwd = "password",
        db = "test2"
        )
        cursor = connection.cursor()
        try:
            cursor.execute(f"DELETE FROM Names WHERE first_name=\'{self.name}\'")
            connection.commit()
        finally:
            cursor.close()
            connection.close() 

    # def name_add(self, list):               
        # if all(x.isalpha() or x.isspace() for x in self.name) == False:
        #     print("You can't add that to the database.\n")            
        # elif self.name in list:
        #     print("That entry already exists.\nPlease enter a unique name into the database.")            
    #     else:   
    #         return list.append(self.name)

    # def del_name(self, list):                
    #     if self.name in list:
    #         list.remove(self.name)             
    #     else:
    #         print("I can't find that in the database.\n")
         


class Song:
    def __init__(self, song):
        self.song = song

    def insert_song_entry(self):
        connection  = pymysql.connect(
        host = "localhost",
        port =  33066,
        user = "root",
        passwd = "password",
        db = "test2"
        )
        cursor = connection.cursor()
        try:
            cursor.execute(f"INSERT INTO Songs (song_title) VALUES (\'{self.song}\');")
            connection.commit()
        finally:
            cursor.close()
            connection.close()
        
    def remove_song_entry(self):
        connection  = pymysql.connect(
        host = "localhost",
        port =  33066,
        user = "root",
        passwd = "password",
        db = "test2"
        )
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"DELETE FROM Songs WHERE song_title=\'{self.song}\'")
                connection.commit()
        finally:
            connection.close() 
            



class RequestMaker:
    def __init__(self, aux_guy=None, name=None, song=None, request_list=[]):
        self.name = name
        self.song = song
        self.aux_guy = aux_guy
        self.request_list = request_list

    def appoint_an_aux_guy(self):
        self.request_list.append(self.aux_guy) 

    def create_a_request(self,):
        self.request_list.append(f"{self.name} requested {self.song}")
        t.print_round(f"{self.request_list[0]} has the aux cable.", self.request_list)
              
    def load_order(self):
        x = l.load_stuff("requests.csv")
        return x + self.request_list
        
    def save_order(self):
        l.save_stuff("requests.csv", self.request_list)
        
        


        
    
        


    
    

            
            
            
            



            
            
                                       

