from src.data_store import load_save as l 
from src.core import table as t
from src.models import classes as c
#defines expected commands
GET_NAMES = "1"
GET_SONGS = "2"
ASSIGN_SONGS = "3"
VIEW_FAV_SONGS = "4"
REMOVE_SONG_PREF = "5"
CREATE_A_REQUEST = "6"
VIEW_REQUESTS = "7"
RUN_AWAY = "0"
MENU = f"""
Welcome to METAL MASTER!
Create a list of your mates requests and shit on them for being posers!
Please select a database to choose from:

[{GET_NAMES}] People 
[{GET_SONGS}] Songs
[{ASSIGN_SONGS}] Assign favourite songs
[{VIEW_FAV_SONGS}] View favourite songs
[{REMOVE_SONG_PREF}] Remove favourite songs
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
    return str(input("Who's in charge of the aux cable?\n"))
    
def name_selector():
    t.print_table("names", name_list)
    person_select = str(input("Please type a name from the database:\n")).title()        
    if person_select in name_list:
        return person_select 
    else:
        print("\nOne of your options is not in the database.\n")
        name_selector()
    

def song_selector():
    t.print_table("songs", song_list)
    song_select = str(input("Please assign a song from the database:\n")).title()
    if song_select in song_list:
        return song_select
    else:
        print("\nOne of your options is not in the database.\n")
        song_selector()  

def make_a_combo():
    choice1 = name_selector()
    choice2 = song_selector() 
    return choice1 + " - " + choice2   

def option_1():
    t.print_table("names", name_list)
    add_name_option = str(input("\nWould you like to edit this database?\n[1] Add name\n[2] Remove name\n[3] Return to menu\n"))
    if add_name_option == "1":
        x = name_input()
        name_to_add = c.Names(x)
        name_to_add.name_add(name_list)
        option_1()      
    elif add_name_option == "2":
        y = name_input()
        name_to_del = c.Names(y)
        name_to_del.del_name(name_list)
        option_1()
    elif add_name_option == "3":        
        wait()
    else:
        print("That's not a valid option.")
        option_1()
        

def option_2():
    t.print_table("songs", song_list)
    add_drink_option = str(input("\nWould you like to edit this database?\n[1] Add song\n[2] Remove song\n[3] Return to menu\n"))
    if add_drink_option == "1":
        x = song_input()
        drink_to_add = c.Song(x)
        drink_to_add.song_add(song_list)
        option_2()
    elif add_drink_option == "2":
        y = songx = song_input()
        drink_to_del = c.Song(y)
        drink_to_del.del_song(song_list)
        option_2()            
    elif add_drink_option == "3":
        wait()
    else:
        print("That's not a valid option.")
        option_2()

def option_3():
    assigned_song = make_a_combo()
    if assigned_song not in fav_songs_list:
        fav_songs_list.append(assigned_song)
        t.print_table("fav songs", fav_songs_list)
    else:
        print("That combination has already been done.")
        option_3() 

def option_4():
    t.print_table("fav songs", fav_songs_list)
    del_assigned_song = make_a_combo()
    if del_assigned_drink in fav_songs_list:
        delete_item(fav_songs_list, del_assigned_song)
        l.save_stuff("favsongs.csv", fav_songs_list)
    else:
        print("That combination does not exist.")
        option_4()

def option_5():
    t.print_table("fav songs", fav_songs_list)
    del_assigned_song = make_a_combo()
    if del_assigned_song in fav_songs_list:
        delete_item(fav_songs_list, del_assigned_song)        
    else:
        print("That combination does not exist.")
        option_5()

def option_6():
    t.print_table("fav songs", fav_songs_list)
    wait()

def option_7():    
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
        print("That ain't a valid command buster.")
        option_7()
    
def option_8():
    round_list = l.load_stuff("src/data/requests.csv")
    server = requests_list[0]    
    t.print_round(f"{server} has the aux cable", requests_list)
    wait() 
 
 
     
        
name_list = l.load_stuff("src/data/metalheads.csv")
song_list = l.load_stuff("src/data/songlist.csv")
fav_songs_list = l.load_stuff("src/data/favsongs.csv")
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
            l.save_stuff("src/data/favsongs.csv", fav_songs_list)
            ultimate_menu()                
                                
        elif user_selection == REMOVE_SONG_PREF:              
            option_5()
            l.save_stuff("src/data/favsongs.csv", fav_songs_list)
            wait()
            ultimate_menu()
                    
        elif user_selection == VIEW_FAV_SONGS:          
            option_6()
            ultimate_menu()

        elif user_selection == CREATE_A_REQUEST:
            option_7()
            l.save_stuff("src/data/requests.csv", requests_list)            
            ultimate_menu()
        
        elif user_selection == VIEW_REQUESTS:
            option_8()
            ultimate_menu()        

        elif user_selection == RUN_AWAY:
            l.save_stuff("src/data/metalheads.csv", name_list)
            l.save_stuff("src/data/songlist.csv", song_list)
            print("We hope you enjoyed your stay.")
            exit()     
        else:
            print(f"{str(user_selection)} is not a valid command.\n")
            wait()
            ultimate_menu()

ultimate_menu()
                    


    




                    