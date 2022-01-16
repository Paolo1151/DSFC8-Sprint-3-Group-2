import pandas as pd
import numpy as np

import joblib as j
from sklearnex import patch_sklearn
patch_sklearn()



# Directory
DATA_clf = "db/clf_models/"
DATA_tra = "db/transformers/"

# Class Classifier
class Classifier():
    # Init variables
    model=None

    # Initialize
    def __init__(self, model="XGB"):
        self.load_model(model)

    # Load model
    def load_model(self, i="XGB"):
        dir = DATA_clf+"{0}_optimal.mdl".format(i)
        self.model = j.load(dir)

    # Predict
    def predict(self, seed):
        seed_track_data = seed.data
        le = j.load(DATA_tra+"genre.mdl")
        pred = self.model.predict(seed_track_data[seed.feature_cols])[0]

        # Generate genre prediction columns
        if "all_genre_prob" not in seed_track_data.columns.tolist():
            seed_track_data["genre_label"] = pred
            seed_track_data["genre"] = le.inverse_transform([pred])
            seed_track_data['predicted_genre_id'] = seed_track_data.apply(lambda x: self.model.predict(x[seed.feature_cols].values.reshape(1,-1))[0]\
                                                , axis=1)
            seed_track_data['predicted_genre'] = le.inverse_transform(seed_track_data['genre_label'])
            seed_track_data['predicted_genre_prob'] = seed_track_data.apply(lambda x:  np.max(self.model.predict_proba(x[seed.feature_cols].values.reshape(1,-1)))\
                                                                , axis=1)
            seed_track_data['all_genre_prob'] = seed_track_data.apply(lambda x:  self.model.predict_proba(x[seed.feature_cols].values.reshape(1,-1))[0]\
                                                                , axis=1)
            # Explode genre data
            charts_predicted_genre_prob = pd.DataFrame(seed_track_data["all_genre_prob"].to_list(),
                                           columns=['predicted_'+g+'_prob' for g in le.classes_.tolist()])
            charts_predicted_genre_prob['track_id'] = seed_track_data['track_id']
            seed_track_data = pd.merge(seed_track_data,charts_predicted_genre_prob, how='left', on='track_id')

        del pred, le
        return seed_track_data