import pandas as pd

# ========== Sample Data ==========

# Genres/Emotions
emotions = [
    "Action Sci-Fi",
    "Animation Comedy Family",
    "Thriller",
    "Animation Adventure Drama",
    "Crime Drama",
    "Action Sci-Fi Thriller"
]

# Movies dataset
movies_data = {
    "title": [
        "The Matrix", "Toy Story", "Jaws", "The Lion King", "Pulp Fiction", "Inception",
        "Inside Out", "Zootopia", "The Dark Knight", "Finding Nemo"
    ],
    "genre": [
        "Action Sci-Fi", "Animation Comedy Family", "Thriller", "Animation Adventure Drama",
        "Crime Drama", "Action Sci-Fi Thriller",
        "Animation Comedy Family", "Animation Comedy Family", "Action Sci-Fi Thriller", "Animation Adventure Drama"
    ],
    "director": [
        "Lana Wachowski & Lilly Wachowski", "John Lasseter", "Steven Spielberg", "Roger Allers & Rob Minkoff",
        "Quentin Tarantino", "Christopher Nolan",
        "Pete Docter", "Byron Howard & Rich Moore", "Christopher Nolan", "Andrew Stanton & Lee Unkrich"
    ],
    "release_year": [
        1999, 1995, 1975, 1994, 1994, 2010, 2015, 2016, 2008, 2003
    ]
}
movies_df = pd.DataFrame(movies_data)

# Books dataset
books_data = {
    "title": [
        "Dune", "The Martian", "Gone Girl", "Harry Potter and the Sorcerer's Stone",
        "Sherlock Holmes", "Ender's Game", "Wonder", "The Lightning Thief",
        "The Girl with the Dragon Tattoo", "The Godfather"
    ],
    "genre": [
        "Action Sci-Fi", "Action Sci-Fi", "Thriller", "Animation Adventure Drama",
        "Crime Drama", "Action Sci-Fi Thriller",
        "Animation Comedy Family", "Animation Adventure Drama",
        "Thriller", "Crime Drama"
    ],
    "author": [
        "Frank Herbert", "Andy Weir", "Gillian Flynn", "J.K. Rowling",
        "Arthur Conan Doyle", "Orson Scott Card",
        "R.J. Palacio", "Rick Riordan",
        "Stieg Larsson", "Mario Puzo"
    ],
    "published_year": [
        1965, 2011, 2012, 1997, 1887, 1985, 2012, 2005, 2005, 1969
    ]
}
books_df = pd.DataFrame(books_data)

# ========== User Interaction & Recommendation Logic ==========

# 1. Show emotion/genre list
print("Select your emotion/genre of the day:")
for idx, emotion in enumerate(emotions, start=1):
    print(f"{idx}. {emotion}")

# 2. Take user emotion input
while True:
    try:
        emotion_choice = int(input("Enter the number corresponding to your emotion/genre: "))
        if 1 <= emotion_choice <= len(emotions):
            selected_emotion = emotions[emotion_choice - 1]
            break
        else:
            print("Please enter a valid number from the list.")
    except ValueError:
        print("Please enter a number.")

# 3. Ask for movies or books
while True:
    type_choice = input("Would you like recommendations for movies or books? (Enter 'movies' or 'books'): ").strip().lower()
    if type_choice in ["movies", "books"]:
        break
    else:
        print("Please enter 'movies' or 'books'.")

# 4. Filter dataset and show recommendations
if type_choice == "movies":
    results = movies_df[movies_df["genre"] == selected_emotion][["title", "director", "release_year"]]
    print(f"\nRecommended MOVIES for '{selected_emotion}':")
    if not results.empty:
        print(results.to_string(index=False, header=['Title', 'Director', 'Year']))
    else:
        print("No movies found for the selected emotion/genre.")

elif type_choice == "books":
    results = books_df[books_df["genre"] == selected_emotion][["title", "author", "published_year"]]
    print(f"\nRecommended BOOKS for '{selected_emotion}':")
    if not results.empty:
        print(results.to_string(index=False, header=['Title', 'Author', 'Published Year']))
    else:
        print("No books found for the selected emotion/genre.")

# ========== END ==========