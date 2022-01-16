
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances, manhattan_distances, cosine_similarity
from models.recommender_model import Recommender
# from models.seed_model import Seed

# Directory
DATA_csv = "db/data/"
# Query tracks from CSV file
CSV = ["top200-genres_RF.csv"]

class RecommenderService():
    model = None
    recommendations = None
    recommendation_ids = None

    def __init__(self):
        self.model = Recommender(DATA_csv+CSV[0])
        pass

    # Generate recommendations: cosine_dist, manhattan_dist, euclidean_dist
    def generate(self, seed, metric = "cosine_dist", items=20):
        seed_track_data = seed.data
        chart_tracks_df = self.model.tracks
        
        genre_cols = [col for col in chart_tracks_df.columns if ('predicted_' in col)&('genre' not in col)]
        cols = seed.feature_cols + genre_cols

        chart_tracks_df['manhattan_dist'] = chart_tracks_df.apply(lambda x: manhattan_distances(x[cols].values.reshape(-1, 1),\
                                                                  seed_track_data[cols].values.reshape(-1, 1))\
                                                                  .flatten()[0], axis=1)
        chart_tracks_df['euclidean_dist'] = chart_tracks_df.apply(lambda x: euclidean_distances(x[cols].values.reshape(-1, 1),\
                                                                        seed_track_data[cols].values.reshape(-1, 1))\
                                                                        .flatten()[0], axis=1)
        chart_tracks_df['cosine_dist'] = chart_tracks_df.apply(lambda x: 1-cosine_similarity(x[cols].values.reshape(1, -1),\
                                                                        seed_track_data[cols].values.reshape(1, -1))\
                                                                        .flatten()[0], axis=1)
        recommendation_df = chart_tracks_df[chart_tracks_df.track_id != seed_track_data.track_id.squeeze()]
        recommendation_df = recommendation_df.sort_values(by=metric).head(items)
        recommendation_df = recommendation_df[['track_id','track_name','artist_name','cosine_dist','predicted_genre']+cols]
        self.recommendations = recommendation_df
        self.recommendation_ids = recommendation_df['track_id'].values.tolist()

