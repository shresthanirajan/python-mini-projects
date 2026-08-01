

def view_movie():
    if not movies_list:
        print("Movie List Empty, Please add Movies")
    else:
        for movie in movies_list:
            for movie_name, movie_rating in movie.items():
                print(f"Movie: {movie_name}, Rating: {movie_rating}")


def add_movie():
    movie_name = input("What movie do you wanna add: ").lower()
    movie_rating = int(input("Movie Rating: "))

    movies_list.append({movie_name:movie_rating, "watched": False})
    print(f"{movie_name} Successfully Added with rating: {movie_rating}")


def search_movie():
    if not movies_list:
        print("No Movies to Search")
    else:
        movie_search = input("Enter movie name you wanna Search: ").lower()
        for movie in movies_list:
            if movie_search in movie:
                print(f"Movie is: {movie_search}")
                break
            else:
                print(f"{movie_search} Doesn't exist")

def mark_watched():
    if not movies_list:
        print("You haven't watched any Movies Please Add a Movie!")
    else:
        movie_watched = input("Name a movie you have watched: ").lower()

        for watch_movie in movies_list:

            if movie_watched in watch_movie:
                check_if_watched = watch_movie["watched"]
                if check_if_watched:
                    print(f"{movie_watched} has already been added to your watch List.")
                    break
                else:
                    watch_movie["watched"] = True
                    print(f"{movie_watched} Has been added to your watched List!")
                    break

        else:
            print(f"Doesn't Exist, Please Add {movie_watched} to Movie List First.")
            return

def remove_movie():
    if not movies_list:
        print("No Movies to remove!")
    else:
        remove_name = input("Enter the movie you wanna remove: ").lower()
        for movie_remove in movies_list:
            if remove_name in movie_remove:
                movies_list.remove(movie_remove)
                print(f"{remove_name} Successfully Removed!")
                break
            else:
                print(f"{remove_name} Doesn't Exist. couldn't remove")


def view_watched_list():
    if not movies_list:
        print("No Movies Added to Watched List")
    else:
        found_watched = False
        for movie in movies_list:
            movie_watched = movie["watched"]
            if movie_watched:

                for movie_watch, rating in movie.items():
                    if movie_watch != "watched":
                        print(f"Movie: {movie_watch} | Rating: {rating}")
                found_watched = True
                #TODO FIX ISSUES HERE !


        if found_watched == False:
            print("No Watched Movies! Please Add movies to Watched List")

movies_list = [

]

while True:
    user_input = input( "1. View Movies\n2. Add movie\n3. Search Movie\n4. Mark Movie as Watched\n5. Remove movie\n6. View Watched Movie\n7.Exit\nChoose an Option: ")
    if user_input == "1":
        view_movie()
    elif user_input == "2":
        add_movie()
    elif user_input == "3":
        search_movie()
    elif user_input == "4":
        mark_watched()
    elif user_input == "5":
        remove_movie()
    elif user_input == "6":
        view_watched_list()
    elif user_input == "7":
        print("Exit")
        break

    else:
        print("Invalid Input")


