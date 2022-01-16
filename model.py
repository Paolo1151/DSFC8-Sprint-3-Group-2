
from services.recommender_service import RecommenderService
from services.seed_service import SeedService

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
# pd.set_option("max_columns", 999)

# Create SeedService
seed_service = SeedService()

# Generate Seed track data, See seed_service.py
seed_service.get_seed(q=["0G3S4MVnjb8w30RZk04PI9"], col=["track_id"])


# Create RecommenderService
recom_service = RecommenderService()
# Generate recommendations
recom_service.generate(seed_service.seed)
# Print Recommendations
print(recom_service.recommendations)

# Generate Seed track data, See seed_service.py
seed_service.get_seed(q=["Kill This Love", "4pUCKHjJ4Ijewc37rRrvHn"], col=["track_name", "track_id"])
recom_service.generate(seed_service.seed, "cosine_dist", 10)
print("Generating top 10 recommendations for: \n", seed_service.seed.data)
print("\nList: \n", recom_service.recommendations)