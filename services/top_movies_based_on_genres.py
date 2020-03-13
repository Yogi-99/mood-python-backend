import pandas as pd
import json
from joblib import load

top_n_popular_movies_model = load('movie_recommendation_models/top_n_popular_movies.joblib')
top_genres = load('movie_recommendation_models/best_movies_filtered_genres.joblib')

top_genres.drop_duplicates(subset='imdb_id', keep=False, inplace=True)
top_n_popular_movies_model.drop_duplicates(subset='imdb_id', keep=False, inplace=True)

top_genres_return_fields = ['imdb_id', 'original_title', 'overview', 'tagline']
top_popular_return_fields = ['imdb_id', 'original_title', 'overview', 'tagline']


top_n_popular_movies_model = top_n_popular_movies_model.fillna('')
top_genres = top_genres.fillna('')


def get_top_n_popular_movies(top_n):
    return top_n_popular_movies_model[top_popular_return_fields].head(top_n).to_dict()


def get_top_movies_filtered_by_genres(genre, top_n):
    return pd.DataFrame(
        top_genres.loc[(top_genres[genre] == 1)].sort_values(['score'], ascending=False))[
        top_genres_return_fields].head(top_n).to_dict()


