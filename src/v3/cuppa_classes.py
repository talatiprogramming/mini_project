import csv
import table as t
import load_save as l

class Names:
    def __init__(self, name):
        self.name = name
          
    def name_add(self, list):               
        if self.name.isalpha() == False:
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

class Drink:
    def __init__(self, drink):
        self.drink = drink

    def drink_add(self, list):               
        if self.drink.isalpha() == False:
            print("You can't add that to the database.\n")            
        elif self.drink in list:
            print("That entry already exists.\nPlease enter a unique name into the database.")            
        else:   
            return list.append(self.drink)

    def del_drink(self, list):                
        if self.drink in list:
            list.remove(self.drink)             
        else:
            print("I can't find that in the database.\n")

class RoundMaker:
    def __init__(self, name, drink):
        self.name = name
        self.drink = drink
        self.round_list = []
           
    def create_an_order(self, server):
        self.server = server
        self.round_list.append(f"{self.name} ordered {self.drink}")
        t.print_table(f"{self.server} is making the round", self.round_list)
        continue_option = str(input("\nWould you like to continue?\n[1] Y\n[2] N\n"))
        while continue_option == "1":
            exit()

    
    def save_order(self):
        l.save_stuff("drinksround.csv", self.round_list)
    

            
            
            
            



            
            
                                       

