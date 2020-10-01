import csv
import table as t
import load_save as l

class Names:
    def __init__(self, name):
        self.name = name
          
    def name_add(self, list):               
        if all(x.isalpha() or x.isspace() for x in self.name) == False:
            print("You can't add that to the database.\n")            
        elif self.name in list:
            print("That entry already exists.\nPlease enter a unique name into the database.")            
        else:   
            return list.append(self.name)

    def del_name(self, list):                
        if self.name in list:
            list.remove(self.name)             
        else:
            print("I can't find that in the database.\n")

class Song:
    def __init__(self, song):
        self.song = song

    def song_add(self, list):               
        if all(x.isalpha() or x.isspace() for x in self.song) == False:
            print("You can't add that to the database.\n")            
        elif self.song in list:
            print("That entry already exists.\nPlease enter a unique name into the database.")            
        else:   
            return list.append(self.song)

    def del_song(self, list):                
        if self.song in list:
            list.remove(self.song)             
        else:
            print("I can't find that in the database.\n")

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
        
        


        
    
        


    
    

            
            
            
            



            
            
                                       

