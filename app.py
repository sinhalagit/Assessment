import sqlite3

#constants and variables
DATABASE = "artist.db"


#functions
def print_all_artists():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM artist;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"First name        last name         stage name          genre         debut year     country")
    for artist in results:
        print(f"{artist[1]:<8} {artist[2]:<8} {artist[3]:<8} {artist[4]:<12} {artist[5]:<4} {artist[6]:<10}")

    db.close
    
def print_all_artists_Firstname_Asc():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM artist ORDER BY First_Name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for artist in results:
        print(artist)
        
def print_artists_debutyear():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT First_Name, Last_Name, DebutYear FROM artist  WHERE DebutYear < 2010;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for artist in results:
        print(artist)

def print_all_songs():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM song;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for artist in results:
        print(artist)
    db.close
    
def print_titles_ordered():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Title,Album FROM song ORDER BY Title ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for artist in results:
        print(artist)

def print_name_album_year_joint():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT artist.First_Name,song.Album,song.ReleaseYear FROM artist JOIN song ON artist.id=song.artistID;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for artist in results:
        print(artist)
    db.close
#close the db

#main code
while True:
    user_input = input ("\nPlease enter your option: \n1. Print all artists\n2. Print all artists first name\n3. Print all artists debut year\n4. Print all songs\n5. Print titles in ascending order\n6. Print name,album and released year\n")
    if user_input == "1":
        print_all_artists()
    elif user_input == "2":
        print_all_artists_Firstname_Asc()
    elif user_input == "3":
        print_artists_debutyear()
    elif user_input == "4":
        print_all_songs()
    elif user_input == "5":
        print_titles_ordered()
    elif user_input == "6":
        print_name_album_year_joint()
    elif user_input == "7":
        break
    else:
        print("That was not an option\n")


