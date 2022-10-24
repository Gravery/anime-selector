from ast import Add
from funcs import *
animelist = "Lists/animes.txt"
movieslist = "Lists/movies.txt"
serieslist = "Lists/series.txt"
run = 1

while run:
    choice = int(input("1 - Get random thing to watch\n2 - Add something to watch on the list\n"))

    if choice == 1:
        choice = int(input("Choose what you want to random select:\n1 - Animes\n2 - Movies\n3 - Series\n"))

        if choice == 1:
            chooser(animelist, "anime")
        elif choice == 2:
            chooser(movieslist, "movie")
        elif choice == 3:
            chooser(serieslist, "serie")
        else:
            print("Invalid input. Try again")

    elif choice == 2:
        choice = int(input("Which file you want to add things:\n1 - Animes\n2 - Movies\n3 - Series\n"))

        if choice == 1:
            add(animelist)
        elif choice == 2:
            add(movieslist)
        elif choice == 3:
            add(serieslist)
        else:
            print("Invalid input. Try again")
            
    else:
        print("Invalid input. Try again")

    keep = input("Choose again? y/n\n")

    if keep.lower() == "n":
        run = 0