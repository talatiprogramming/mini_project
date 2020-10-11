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
Create a shared music queue with your mates and dunk on them for being posers!
Please select a database to choose from:

[{GET_NAMES}] People 
[{GET_SONGS}] Songs
[{ASSIGN_SONGS}] Edit favourite songs
[{CREATE_A_REQUEST}] Create a music queue
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
    input("\nPress ENTER to continue\n")

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
    song_data = m.import_song()
    song_list = []
    for key, value in song_data.items():
        song_list.append(f"{key} {value[0]}, {value[2]}")
    t.print_table("songs", song_list)
    song_select = str(input("Please assign a song no. from the list:\n"))
    if song_select.isnumeric() == True:
        for key in song_data.keys():
            if song_select == key:
                x = song_data[song_select]                
                return f"{x[0]}, {x[2]}"
            
    else:
        print("\nNot a valid option.\n")
        song_selector()             


def view_fav_songs():    
    fav_album = m.import_fav_songs()
    fav_song_list = []
    for value in fav_album.values():            
        fav_song_list.append(f"{value[0]} - {value[1]}, {value[2]}")
    t.print_table(f"Favourites", fav_song_list)

def add_preference():
    names_list = m.import_name()
    t.print_table("names", names_list)
    choice = str(input("\nSelect a name from the list\n")).title()
    choice2 = str(input("Would you like to:\n[1] Assign a whole album\n[2] Individual songs?\n[3] Exit?\n"))
    if choice2 == "1":
        album_list = m.import_album()
        album_stuff = []    
        for key, value in album_list.items():
            album_stuff.append(f"{key} {value[0]}, {value[1]}")
        t.print_table("albums", album_stuff)
        choice3 = str(input("Choose an album no. from the list.\n"))
        if choice3 in album_list.keys(): 
            album_choice = m.import_song_choice("s.song_title, a.album_name", "Songs as s, Albums as a", f"s.albumID={choice3} AND a.albumID={choice3}")
            try:
                for item in album_choice:
                    m.insert_entry("Favourites (name, song_title, album_name)", f"\'{choice}\', \'{item[0]}\', \'{item[1]}\'")
                print("Your preferences have been saved.")
            except:
                print("There was an issue in saving your preferences.") 
        else:
            print("Not a valid option")
            assign_an_album()
    elif choice2 == "2":
        song_data = m.import_song()
        song_list = []
        for key, value in song_data.items():
            song_list.append(f"{key} {value[0]}, {value[2]} - {value[3]}")
        t.print_table("songs", song_list)
        choice4 = str(input("Choose a song no. from the list.\n"))
        if choice4 in song_data.keys():
            try:
                song_choice = song_data[choice4]
                m.insert_entry("Favourites (name, song_title, album_name)", f"\'{choice}\', \'{song_choice[0]}\', \'{song_choice[2]}\'")
                print("Your preferences have been saved.\n")
            except:
                print("There was an issue in saving your preferences.\n")
            choice5 = str(input("Would you like to save another preference?:\n[1] Yes\n[2] No\n"))
            if choice5 == "1":
                add_preference()
            elif choice5 == "2":
                ultimate_menu()
            else:
                print("Not a valid option")
                del_preference()
        else:
            print("Not a valid option.")
            add_preference()
    elif choice2 == "3":
        ultimate_menu()
    else:
        print("Not a valid option")
        add_preference()

def del_preference():
    fav_songs = m.import_fav_songs()
    fav_song_list = []
    for key, value in fav_songs.items():
        fav_song_list.append(f"{key} {value[0]} - {value[1]}, {value[2]}")
    t.print_table("favourites", fav_song_list)
    choice = str(input("\nChoose an record no. from the list.\n"))
    if choice in fav_songs.keys():
        try:
            m.remove_entry("Favourites", f"favID={choice}")
            print("Your preference was removed successfully.\n")
        except:
            print("There was an issue with deleting your preference.\n")
        choice2 = str(input("Would you like to delete another record?\n[1] Yes\n[2] No\n"))
        if choice2 == "1":
            del_preference()
        elif choice2 == "2":
            ultimate_menu()
        else:
            print("Not a valid option")
            del_preference()
    else:
        print("Not a valid option.")
        del_preference()

        
def song_option():
    song_data = m.import_song()
    song_list = []
    for item in song_data.values():
        song_list.append(f"{item[0]}, {item[2]} - {item[3]}")
    t.print_table("songs", song_list)
    wait()

def album_option():
    album_list = m.import_album()
    album_stuff = []    
    for key, value in album_list.items():
        album_stuff.append(f"{key} {value[0]}, {value[1]}")
    t.print_table("albums", album_stuff)
    choice = input("\nSelect an album to view or enter x to return to menu.\n")
    for key in album_list.keys():
        if choice == "x":
            ultimate_menu()
        elif choice == key:
            song_list = m.import_song_title(f"WHERE albumID={choice}")
            x = album_list[choice]
            t.print_table(f"{x[0]}", song_list)                
            wait()
            album_option()
        elif choice not in album_list.keys():
            print("\nNot a valid option.\n")
            album_option()

def option_1():
    name_list = m.import_name()
    t.print_table("names", name_list)
    add_name_option = str(input("\nPlease select an option:\n[1] Add name\n[2] Remove name\n[3] Return to menu\n"))
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
        ultimate_menu()
    else:
        print("That's not a valid option.")
        option_1()    
    

def option_2():
    choice = str(input("Please select an option:\n[1] View all albums\n[2] View all songs\n[3] Return to menu\n"))
    if choice == "1":
        album_option()
        option_2()
    elif choice == "2":
        song_option()
        option_2()
    elif choice == "3":
        ultimate_menu()
    else:
        print("Not a valid option.")
        option_2()

def option_3():
    view_fav_songs()
    choice = str(input("Please select an option:\n[1] Assign a preference\n[2] Delete a preference\n[3] Return to menu\n"))
    if choice == "1":
        add_preference()
        option_3()
    elif choice == "2":
        del_preference()
        option_3()
    elif choice == "3":
        ultimate_menu()
    else:
        print("Not a valid option")
        option_3() 


def option_4():    
    aux_guy = aux_manager()
    name1 = name_selector()
    song1 = song_selector()
    order1 = c.RequestMaker(aux_guy, name1, song1, requests_list)
    order1.appoint_an_aux_guy()
    order1.create_a_request()
    exit_selection = str(input("\nWould you like to continue?\n[1] Yes\n[2] No\n"))
    if exit_selection == "1" or exit_selection == "2":
        while exit_selection != "2":
            name2 = name_selector()
            song2 = song_selector()
            order2 = c.RequestMaker(aux_guy, name2, song2, requests_list)
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
                   


    




                    