
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load the movie dataset
movies = pd.read_csv("movies.csv")

# Step 2: Handle missing values
movies = movies.fillna("")

# Step 3: Combine movie information
movies["combined_features"] = (
    movies["genre"] + " " + movies["description"]
)

# Step 4: Convert text into numerical features
vectorizer = TfidfVectorizer(stop_words="english")

feature_matrix = vectorizer.fit_transform(
    movies["combined_features"]
)

# Step 5: Calculate similarity between movies
similarity_matrix = cosine_similarity(feature_matrix)


# Step 6: Create recommendation function
def recommend_movies(movie_name, number=5):
    movie_name = movie_name.strip().lower()

    matches = movies[
        movies["title"].str.lower() == movie_name
    ]

    if matches.empty:
        print("\nMovie not found in the dataset.")
        print("Please enter a movie title from the dataset.")
        return

    movie_index = matches.index[0]

    similarity_scores = list(
        enumerate(similarity_matrix[movie_index])
    )

    # Sort movies by similarity score
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Movies:")
    count = 0

    for index, score in similarity_scores:
        if index == movie_index:
            continue

        print(
            f"{count + 1}. {movies.iloc[index]['title']}"
            f" (Similarity: {score:.2f})"
        )

        count += 1

        if count == number:
            break


# Step 7: Run the program
print("===================================")
print("     MOVIE RECOMMENDATION ENGINE")
print("===================================")

while True:
    movie_name = input(
        "\nEnter a movie name (or type exit): "
    )

    if movie_name.strip().lower() == "exit":
        print("Thank you for using the system!")
        break

    recommend_movies(movie_name)
