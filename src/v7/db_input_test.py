from src.data_store import mysql_db as m 
from src.core import table as t 

# def assign_a_song():
#     x = m.import_name()
#     t.print_table("names", x)
#     name_input = input("Choose a name from the list: ").title()
#     if name_input in x:    
#         choice = input("Would you like to choose from the:\n[1] Album list\n[2] Song list?\n[3]Exit?\n")
#         if choice == "1":
#             album_list = m.import_album()
#             album_stuff = []    
#             for key, value in album_list.items():
#                 album_stuff.append(f"{key} {value[0]}, {value[1]}")
#             t.print_table("albums", album_stuff)
#             choice2 = input("Select an album number from the list.\n")
#             selected_album = album_list[choice2]

x = m.import_fav_songs("song_title, album_name", "Songs as s, Albums as a", "s.albumID=1 AND a.albumID=1")
print(x)





    
            
        
        
            
            

        

    
    