from typing import Dict, List
from song_recommendation.data_io import load_source, create_corpus

from song_recommendation.utils import transform_row_vector
from song_recommendation.metrics import get_accuracy
from song_recommendation.knn import train_model, create_knn

def run_train_model_loop(data_path: str, feature_list: List[str], label_col: str) -> Dict:
    
    train_set, test_set = load_source(data_path)
    train_corpus, train_labels = create_corpus(train_set, feature_list, label_col)

    # train the model
    knn = create_knn()
    knn = train_model(knn, train_corpus, train_labels)

    # create test set for evaluation
    test_corpus, test_lables = create_corpus(test_set, feature_list, label_col)
    # get metrics
    accuracy = get_accuracy(knn, test_corpus, test_lables)
    # show metrics
    print(f'the accuracy for this model is {accuracy} over {len(test_corpus)} samples.')

    return knn




