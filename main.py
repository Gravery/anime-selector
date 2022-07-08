from funcs import *
animelist = "Lists/animes.txt"
movieslist = "Lists/movies.txt"
serieslist = "Lists/series.txt"
run = 1

while run:
    choice = int(input("Choose what you want to random select:\n1 - Animes\n2 - Movies\n3 - Series\n"))

    if choice == 1:
        chooser(animelist, "anime")
    elif choice == 2:
        chooser(movieslist, "movie")
    elif choice == 3:
        chooser(serieslist, "serie")
    else:
        print("Invalid input. Try again")
        
    keep = input("Choose again? y/n")

    if keep.lower() == "n":
        run = 0