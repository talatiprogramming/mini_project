import csv
import pymysql
from src.core import table as t
from src.data_store import load_save as l
from src.data_store import mysql_db as m

class Names:
    def __init__(self, name):
        self.name = name

    def insert_name_entry(self):
        m.insert_entry("Names (name)", f"(\'{self.name}\')")
        
    def remove_name_entry(self):
        m.remove_entry("Names", f"name=\'{self.name}\'") 

class Song:
    def __init__(self, song):
        self.song = song

    def insert_song_entry(self):
        m.insert_entry("Songs (song_title)", self.song)

    def remove_song_entry(self):
         m.remove_entry("Songs", "song_title", self.song) 
            
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
        t.print_requests(f"{self.aux_guy} has the aux cable.", self.request_list)
              
    def load_order(self):
        x = l.load_stuff("requests.csv")
        return x + self.request_list
        
    def save_order(self):
        l.save_stuff("requests.csv", self.request_list)
        



        


        
    
        


    
    

            
            
            
            



            
            
                                       

