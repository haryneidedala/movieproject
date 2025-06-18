import random
import statistics
import matplotlib.pyplot as plt

# Initial movie database
movies = {
    "The Shawshank Redemption": 9.3,
    "The Godfather": 9.2,
    "The Dark Knight": 9.0,
    "Pulp Fiction": 8.9,
    "Fight Club": 8.8
}

def display_menu():
    print("\n********** My Movies Database **********\n")
    print("Menu:")
    print("1. List movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Update movie")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movie")
    print("8. Movies sorted by rating")
    print("9. Create Rating Histogram")
    print("10. Exit")

def add_movie():
    title = input("Enter movie title: ").strip()
    if not title:
        print("Error: Movie title cannot be empty")
        return
    
    if title in movies:
        print(f"Error: Movie '{title}' already exists in the database")
        print(f"Current rating: {movies[title]}")
        choice = input("Do you want to update the rating instead? (y/n): ").lower()
        if choice == 'y':
            new_rating = float(input("Enter new rating (1-10): "))
            if 1 <= new_rating <= 10:
                movies[title] = new_rating
                print(f"Movie '{title}' updated to rating {new_rating}")
            else:
                print("Error: Rating must be between 1 and 10")
        return
    
    try:
        rating = float(input("Enter movie rating (1-10): "))
        if 1 <= rating <= 10:
            movies[title] = rating
            print(f"Movie '{title}' added with rating {rating}")
        else:
            print("Error: Rating must be between 1 and 10")
    except ValueError:
        print("Error: Please enter a valid number for rating")

def create_rating_histogram():
    if not movies:
        print("No movies in database to create histogram")
        return
    
    ratings = list(movies.values())
    
    plt.figure(figsize=(10, 6))
    plt.hist(ratings, bins=10, range=(1, 10), edgecolor='black', color='skyblue')
    plt.title('Distribution of Movie Ratings', fontsize=14)
    plt.xlabel('Rating (1-10)', fontsize=12)
    plt.ylabel('Number of Movies', fontsize=12)
    plt.xticks(range(1, 11))
    plt.grid(axis='y', alpha=0.5)
    
    avg_rating = sum(ratings) / len(ratings)
    plt.axvline(avg_rating, color='red', linestyle='--', linewidth=1)
    plt.text(avg_rating + 0.1, plt.ylim()[1]*0.9, 
             f'Average: {avg_rating:.2f}', color='red')
    
    plt.tight_layout()
    plt.show()

def list_movies():
    print(f"\nThere are {len(movies)} movies in the database:")
    for title, rating in movies.items():
        print(f"{title}: {rating}")

def delete_movie():
    title = input("Enter movie title to delete: ")
    if title in movies:
        del movies[title]
        print(f"Movie '{title}' deleted")
    else:
        print(f"Error: Movie '{title}' not found in database")

def update_movie():
    title = input("Enter movie title to update: ")
    if title in movies:
        try:
            new_rating = float(input("Enter new rating (1-10): "))
            if 1 <= new_rating <= 10:
                movies[title] = new_rating
                print(f"Movie '{title}' updated to rating {new_rating}")
            else:
                print("Error: Rating must be between 1 and 10")
        except ValueError:
            print("Error: Please enter a valid number for rating")
    else:
        print(f"Error: Movie '{title}' not found in database")

def show_stats():
    if not movies:
        print("No movies in database")
        return
    
    ratings = list(movies.values())
    avg = sum(ratings) / len(ratings)
    print(f"\nAverage rating: {avg:.2f}")
    
    median = statistics.median(ratings)
    print(f"Median rating: {median:.2f}")
    
    max_rating = max(ratings)
    best_movies = [title for title, rating in movies.items() if rating == max_rating]
    print(f"Best movie(s) (rating {max_rating}): {', '.join(best_movies)}")
    
    min_rating = min(ratings)
    worst_movies = [title for title, rating in movies.items() if rating == min_rating]
    print(f"Worst movie(s) (rating {min_rating}): {', '.join(worst_movies)}")

def random_movie():
    if not movies:
        print("No movies in database")
        return
    
    title = random.choice(list(movies.keys()))
    print(f"\nRandom movie: {title}, {movies[title]}")

def search_movie():
    search_term = input("Enter part of movie name: ").lower()
    found = False
    
    for title, rating in movies.items():
        if search_term in title.lower():
            print(f"{title}, {rating}")
            found = True
    
    if not found:
        print("No movies found matching your search")

def movies_by_rating():
    if not movies:
        print("No movies in database")
        return
    
    sorted_movies = sorted(movies.items(), key=lambda x: x[1], reverse=True)
    print("\nMovies sorted by rating (highest first):")
    for title, rating in sorted_movies:
        print(f"{title}: {rating}")

def main():
    while True:
        display_menu()
        choice = input("\nEnter choice (1-10): ").strip()
        
        if choice == "1":
            list_movies()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            delete_movie()
        elif choice == "4":
            update_movie()
        elif choice == "5":
            show_stats()
        elif choice == "6":
            random_movie()
        elif choice == "7":
            search_movie()
        elif choice == "8":
            movies_by_rating()
        elif choice == "9":
            create_rating_histogram()
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-10.")

if __name__ == "__main__":
    main()
