from src.data_store import mysql_db as m 
from src.core import table as t 

# x = m.import_songID()
# t.print_table("songs", x)



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
            quit()
           
    else:
        print("That name doesn't exist.")
        assign_a_song()
            
        

def option():
    fav_songs = m.return_fav_songs()
    t.print_table("fav songs", fav_songs)
    choice = input("\nWould you like to update this list?\ny or n?\n").lower()
    if choice == "y":
        assign_a_song()
        option()
    elif choice == "n":
        quit()
    else:
        print("Not a valid option.")
        option()

option() 


