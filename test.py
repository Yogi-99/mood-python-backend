# from joblib import load
# import pandas as pd
#
# top_n_popular_movies_model = load('movie_recommendation_models/top_n_popular_movies.joblib')
# top_genres = load('movie_recommendation_models/best_movies_filtered_genres.joblib')
#
# top_n_popular_movies_model = pd.DataFrame(top_n_popular_movies_model)
#
# top_genres = pd.DataFrame(top_genres)
#
# top_genres.head()
#
# top_genres.loc[(top_genres['Horror'] == 1)].sort_values(['score'], ascending=False).head(20)
# len(top_genres)
#
# top_genres.columns
#
# top_genres.drop_duplicates(subset='imdb_id', keep=False, inplace=True)
#
# len(top_genres)
#
