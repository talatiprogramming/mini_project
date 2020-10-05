from src.data_store import mysql_db as m
from src.data_store import load_save as l 
from src.core import table as t
from src.models import classes as c

#defines expected commands
GET_NAMES = "1"
GET_SONGS = "2"
ASSIGN_SONGS = "3"
CREATE_A_REQUEST = "4"
VIEW_REQUESTS = "5"
RUN_AWAY = "0"
MENU = f"""
Welcome to METAL MASTER!
Create a list of your mates requests and dunk on them for being posers!
Please select a database to choose from:

[{GET_NAMES}] People 
[{GET_SONGS}] Songs
[{ASSIGN_SONGS}] Assign favourite songs
[{CREATE_A_REQUEST}] Makes some requests
[{VIEW_REQUESTS}] View the queue
[{RUN_AWAY}] Exit
"""


def selection_screen():
    print(MENU)

# Separate functions to ensure names don't end up in the drinks list and vice versa.
def user_input():
    return str(input())  

def name_input():
    return str(input("Please enter a name:\n")).title()

def song_input():
    return str(input("Please enter a song:\n")).title()
   
# Pauses the script in the middle of the while loop
def wait():
    input("Press ENTER to continue\n")

# Deletes item from a list
def delete_item(list, item):
    list.remove(item)

def aux_manager():
    name_list = m.import_name()
    x = str(input("Who's in charge of the aux cable?\n")).title()
    if x in name_list:
        return x
    else:
        print("Not a valid name.\n")
        aux_manager()
    
def name_selector():
    name_list = m.import_name()
    t.print_table("names", name_list)
    person_select = str(input("Please type a name from the list:\n")).title()        
    if person_select in name_list:
        return person_select 
    else:
        print("\nNot a valid option.\n")
        name_selector()
    

def song_selector():
    song_list = m.import_songID()
    t.print_table("songs", song_list)
    song_select = str(input("Please assign a song no. from the list:\n"))
    if song_select.isnumeric() == True:
        for item in song_list:
            if song_select == item[0]:                
                return item[2:]
            
    else:
        print("\nNot a valid option.\n")
        song_selector()  
            

 
def assign_a_song():
    x = m.import_name()
    t.print_table("names", x)
    name_input = input("Choose a name from the list: ").title()
    if name_input in x:    
        y = m.import_songID()
        t.print_table("songs", y)
        song_input = str(input("Choose a song number from the list: "))
        for item in y:
            while song_input == item[0]:
                continue
            m.update_entry("Names", f"fav_songID={song_input}", f"first_name='{name_input}'")
            option_3()
           
    else:
        print("That name doesn't exist.")
        assign_a_song()

def option_1():
    name_list = m.import_name()
    t.print_table("names", name_list)
    add_name_option = str(input("\nWould you like to edit this database?\n[1] Add name\n[2] Remove name\n[3] Return to menu\n"))
    if add_name_option == "1":
        x = name_input()
        if x.isnumeric == True:
            print("You can't add that to the database.\n")
            option_1()            
        elif x in name_list:
            print("That entry already exists.\nPlease enter a unique name into the database.\n")
            option_1()
        else:        
            name_to_add = c.Names(x)
            name_to_add.insert_name_entry()        
            option_1()      
    elif add_name_option == "2":
        y = name_input()
        name_to_del = c.Names(y)
        if y in name_list:
            name_to_del.remove_name_entry()
            option_1()
        else: 
            print("That name does not exist")
            option_1()
    elif add_name_option == "3":        
        wait()
    else:
        print("That's not a valid option.")
        option_1()
        

def option_2():
    song_list = m.import_song()
    t.print_table("songs", song_list)
    song_option = str(input("\nWould you like to edit this database?\n[1] Add song\n[2] Remove song\n[3] Return to menu\n"))
    if song_option == "1":
        x = song_input()
        if x.isnumeric == True:
            print("You can't add that to the database")
            option_2()
        elif x in song_list:
            print("That song already exist. Add a new one.")
            option_2()
        else:
            song_to_add = c.Song(x)
            song_to_add.insert_song_entry()
            option_2()
    elif song_option == "2":
        y = song_input()
        if y in song_list:
            song_to_del = c.Song(y)
            song_to_del.remove_song_entry()
            option_2()
        else:
            print("That song does not exist.")
            option_2()            
    elif song_option == "3":
        wait()
    else:
        print("That's not a valid option.")
        option_2()

def option_3():
    fav_songs = m.return_fav_songs()
    t.print_table("fav songs", fav_songs)
    choice = input("\nWould you like to update this list?\ny or n?\n").lower()
    if choice == "y":
        assign_a_song()
        option()
    elif choice == "n":
        ultimate_menu()
    else:
        print("Not a valid option.")
        option()


def option_4():    
    aux_guy = aux_manager()
    name1 = name_selector()
    drink1 = song_selector()
    order1 = c.RequestMaker(aux_guy, name1, drink1, requests_list)
    order1.appoint_an_aux_guy()
    order1.create_a_request()
    exit_selection = str(input("\nWould you like to continue?\n[1] Yes\n[2] No\n"))
    if exit_selection == "1" or exit_selection == "2":
        while exit_selection != "2":
            name2 = name_selector()
            drink2 = song_selector()
            order2 = c.RequestMaker(aux_guy, name2, drink2, requests_list)
            order2.create_a_request()
            exit_selection = str(input("\nWould you like to continue?\n[1] Yes\n[2] No\n"))
    else:
        print("That's not a valid option.")
        option_4()
    
def option_5():
    requests_list = l.load_stuff("src/data/requests.csv")
    server = requests_list[0]    
    t.print_requests(f"{server} has the aux cable", requests_list)
    wait() 


load_requests = l.load_stuff("src/data/requests.csv")
requests_list = c.RequestMaker().request_list

def ultimate_menu():
    while True:           
        selection_screen()
        user_selection = user_input()
        # Organises arguments based on user input
        if user_selection == GET_NAMES:        
            option_1()
            ultimate_menu()

        elif user_selection == GET_SONGS:        
            option_2()   
            ultimate_menu()

        elif user_selection == ASSIGN_SONGS:
            option_3()            
            ultimate_menu()                

        elif user_selection == CREATE_A_REQUEST:
            option_4()
            l.save_stuff("src/data/requests.csv", requests_list)            
            ultimate_menu()
        
        elif user_selection == VIEW_REQUESTS:
            option_5()
            ultimate_menu()        

        elif user_selection == RUN_AWAY:
            print("We hope you enjoyed your stay.")
            exit()     
            
        else:
            print(f"{str(user_selection)} is not a valid command.\n")
            wait()
            ultimate_menu()
            
                                


ultimate_menu()
                   


    




                    