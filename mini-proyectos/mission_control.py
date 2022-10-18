from random import randint

from song_recommendation.user_controller import show_recomendations
from song_recommendation.knn import create_knn
from song_recommendation.data_io import load_source, create_corpus
from song_recommendation.user_controller import show_user_welcome_message, get_song_name
from song_recommendation.main import run_train_model_loop, get_recommendations
from song_recommendation.data_io import load_csv
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
    
LABEL = 'song_name'

CSV_PATH = 'mini-proyectos/datasets/genres_v2.csv'

NUMBER_OF_SONGS = 5

LIKE_LABEL = 'liked'
DISLIKED_LABEL = 'dislike'


if __name__ == '__main__':
    # model = run_train_model_loop(
    #     data_path=CSV_PATH, 
    #     feature_list=FEATURES, 
    #     label_col=LABEL
    # )

    knn = create_knn()

    
    songs = load_csv(CSV_PATH)

    corpus, song_names = create_corpus(songs, FEATURES, label_col=LABEL)

    show_user_welcome_message()
    
    labeled_songs = []
    labels  = []
    #  create a small labeled set for training
    for i in range(NUMBER_OF_SONGS):
        song_idx = get_song_name(song_names)
        labeled_songs.append(corpus[song_idx])
        labels.append(LIKE_LABEL)
        labeled_songs.append(corpus[randint(0, len(songs))])
        labels.append(DISLIKED_LABEL)
        

    recomendations = get_recommendations(
        knn, 
        labeled_data=labeled_songs,
        labels=labels,
        corpus=corpus,
        target_label=LIKE_LABEL,
        amount=NUMBER_OF_SONGS
    )

    rec_names = [songs[rec][LABEL] for rec in recomendations]
    show_recomendations(rec_names)
    

    
    
    
    
    
    
    
    

    
    
    

