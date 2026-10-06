# Number of friends giving suggestions
n = int(input("Enter the number of friends: "))

if n <= 0:
    print("\n0 friends? Damn, go make some friends first, loser! 💀🍿")
else:
    movies = []

    # Accept movie suggestions
    for i in range(n):
        print("\nEnter details of Movie", i + 1)

        title = input("Movie Title: ")
        rating = float(input("Movie Rating (out of 10): "))
        duration = input("Time Period (e.g. 2 hrs 15 mins): ")
        price = float(input("Ticket Price (₹): "))

        movies.append({
            "Title": title,
            "Rating": rating,
            "Duration": duration,
            "Price": price
        })

    # Display all suggestions
    print("\n------ Movie Suggestions ------")
    for movie in movies:
        print("Title       :", movie["Title"])
        print("Rating      :", movie["Rating"])
        print("Duration    :", movie["Duration"])
        print("Ticket ₹    :", movie["Price"])
        print()

    # Find the best movie
    best_movie = movies[0]

    for movie in movies[1:]:
        if movie["Rating"] > best_movie["Rating"]:
            best_movie = movie
        elif movie["Rating"] == best_movie["Rating"]:
            if movie["Price"] < best_movie["Price"]:
                best_movie = movie

    # Display the selected movie
    print("===================================")
    print(" Best Movie for Weekend Night ")
    print("===================================")
    print("Movie Title   :", best_movie["Title"])
    print("Rating        :", best_movie["Rating"])
    print("Duration      :", best_movie["Duration"])
    print("Ticket Price  : ₹", best_movie["Price"])
    print("\nEnjoy your movie night with friends!")