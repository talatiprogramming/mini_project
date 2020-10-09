from src.data_store import mysql_db as m 
from src.core import table as t 

# x = m.import_songID()
# t.print_table("songs", x)

# x = m.import_album()
# for item in x:
#     print(item)

def album_option():
    album_list = m.import_album()
    for key, value in album_list.items():
        print(f"{key} {value[0]} - {value[1]}")
    try:
        choice = int(input("\nSelect an album to view or enter 0 to return to menu.\n"))
        for key in album_list.keys():
            if choice == 0:
                continue
            if choice == key:
                song_list = m.import_song(f"WHERE albumID={choice}")
                for item in song_list:
                    print(item)
                input("\nWAIT\n")
                album_option()
            if choice not in album_list.keys():
                print("\nNot a valid option.\n")
                album_option()
    except ValueError:
        print("\nNot a valid option.\n")
        album_option()

def song_option():
    song_list = m.import_song()
    t.print_table("songs", song_list)
    input("\nWAIT\n")

def option_2():
    choice = str(input("\nWould you like to:\n[1] View all albums?\n[2] View all songs?\n[3] Exit?\n"))
    if choice == "1":
        album_option()
        option_2()
    elif choice == "2":
        song_option()
        option_2()
    elif choice == "3":
        quit()
    else:
        print("Not a valid option.")
        option_2()

option_2()





    
            
        
        
            
            
album_option()
        

    
    