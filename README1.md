
# Movie Recommendation Engine

## 1. Project Overview
The Movie Recommendation Engine is a Python-based machine learning project that recommends movies based on their genres and descriptions.

It uses Content-Based Filtering to find movies similar to the movie entered by the user.

## 2. Objectives
- Recommend movies based on similarity.
- Analyze movie genres and descriptions.
- Use machine learning techniques for recommendations.
- Provide a simple, interactive console interface.

## 3. Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

## 4. Project Structure

Movie_Recommendation_Project/
- movie_recommendation.py
- movies.csv
- README.md

## 5. Installation

Install the required Python libraries using:

```bash
python -m pip install pandas scikit-learn
```

## 6. How to Run

1. Download or create the project files.
2. Keep `movie_recommendation.py` and `movies.csv` in the same folder.
3. Open `movie_recommendation.py` using Python IDLE.
4. Select Run → Run Module or press F5.
5. Enter a movie title, such as Avatar.
6. View the recommended movies.
7. Type `exit` to close the program.

## 7. Sample Input

Avatar

## 8. Sample Output

Recommended Movies:
- Interstellar
- Jurassic Park
- Avengers Endgame
- Iron Man

Note: Actual recommendations depend on the movie dataset and similarity scores.

## 9. Algorithm Used

### TF-IDF Vectorizer
Converts text data, including movie genres and descriptions, into numerical vectors.

### Cosine Similarity
Measures the similarity between movie feature vectors.

### Content-Based Filtering
Recommends movies based on their content and characteristics.

## 10. Advantages
- Easy to understand and implement.
- Provides quick recommendations.
- Does not require user ratings.
- Can be extended with a larger movie dataset.

## 11. Limitations
- Recommendations are limited to the available dataset.
- It does not learn individual user preferences.
- Results depend on the quality of movie descriptions.

## 12. Future Enhancements
- Add thousands of movies.
- Develop a graphical user interface.
- Integrate movie posters and ratings.
- Build a web application using Flask or Streamlit.
- Include user ratings and personalized recommendations.

## 13. Conclusion
The Movie Recommendation Engine demonstrates how machine learning and
natural language processing techniques can be used to recommend movies.
TF-IDF and Cosine Similarity help identify movies with similar content.