from src.data_store import mysql_db as m 
from src.core import table as t 


    

# def add_preference():
#     names_list = m.import_name()
#     t.print_table("names", names_list)
#     choice = str(input("\nSelect a name from the list\n"))
#     choice2 = str(input("Would you like to:\n[1] Assign a whole album\n[2] Individual songs?\n[3] Exit?\n"))
#     if choice2 == "1":
#         album_list = m.import_album()
#         album_stuff = []    
#         for key, value in album_list.items():
#             album_stuff.append(f"{key} {value[0]}, {value[1]}")
#         t.print_table("albums", album_stuff)
#         choice3 = str(input("Choose an album no. from the list.\n"))
#         if choice3 in album_list.keys(): 
#             album_choice = m.import_song_choice("s.song_title, a.album_name", "Songs as s, Albums as a", f"s.albumID={choice3} AND a.albumID={choice3}")
#             try:
#                 for item in album_choice:
#                     m.insert_entry("Favourites (name, song_title, album_name)", f"\'{choice}\', \'{item[0]}\', \'{item[1]}\'")
#                 print("Your preferences have been saved.")
#             except:
#                 print("There was an issue in saving your preferences.") 
#         else:
#             print("Not a valid option")
#             assign_an_album()
#     elif choice2 == "2":
#         song_data = m.import_song()
#         song_list = []
#         for key, value in song_data.items():
#             song_list.append(f"{key} {value[0]}, {value[2]} - {value[3]}")
#         t.print_table("songs", song_list)
#         choice4 = str(input("Choose a song no. from the list.\n"))
#         if choice4 in song_data.keys():
#             try:
#                 song_choice = song_data[choice4]
#                 m.insert_entry("Favourites (name, song_title, album_name)", f"\'{choice}\', \'{song_choice[0]}\', \'{song_choice[2]}\'")
#                 print("Your preferences have been saved.\n")
#             except:
#                 print("There was an issue in saving your preferences.\n")
#         else:
#             print("Not a valid option.")
#     elif choice2 == "3":
#         quit()
#     else:
#         print("Not a valid option")
#         add_preference()
    

# def del_preference():
#     fav_songs = m.import_fav_songs()
#     fav_song_list = []
#     for key, value in fav_songs.items():
#         fav_song_list.append(f"{key} {value[0]} - {value[1]}, {value[2]}")
#     t.print_table("favourites", fav_song_list)
#     choice = str(input("\nChoose an entry no. from the list.\n"))
#     if choice in fav_songs.keys():
#         try:
#             m.remove_entry("Favourites", f"favID={choice}")
#             print("Your preference was removed successfully.\n")
#         except:
#             print("There was an issue with deleting your preference.\n")
#     else:
#         print("Not a valid option.")
#         del_preference()




# def option_3():
#     choice = str(input("Would you like to:\n[1] Assign a preference?\n[2] Delete a preference?\n[3] Return to menu?\n"))
#     if choice == "1":
#         add_preference()
#         option_3()
#     elif choice == "2":
#         del_preference()
#         option_3()
#     elif choice == "3":
#         quit()
#     else:
#         print("Not a valid option")
#         option_3() 
            



# def view_fav_songs():    
#     fav_album = m.import_fav_songs()
#     fav_song_list = []
#     for value in fav_album.values():            
#         fav_song_list.append(f"{value[0]} - {value[1]}, {value[2]}")
#     t.print_table(f"Favourites", fav_song_list)
        
# view_fav_songs()

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

x = song_selector()
print(x)

        





    
            
        
        
            
            

        

    
    