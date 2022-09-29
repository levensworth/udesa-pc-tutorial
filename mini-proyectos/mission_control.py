from song_recommendation.main import run_train_model_loop
from song_recommendation.knn import run_inference

FEATURES = [
    'danceability',
    'energy',
    'key',
    'loudness',
    'mode',
    'speechiness',
    'acousticness',
    'instrumentalness',
    'liveness',
    'valence',
    'tempo',
    'duration_ms',
    'time_signature',
    ]
    
LABEL = 'genre'

CSV_PATH = 'mini-proyectos/datasets/genres_v2.csv'


if __name__ == '__main__':
    model = run_train_model_loop(
        data_path=CSV_PATH, 
        feature_list=FEATURES, 
        label_col=LABEL
    )
    
    
    

