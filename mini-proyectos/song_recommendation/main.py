from random import choice
from typing import Dict, List

from song_recommendation.knn import run_inference
from song_recommendation.data_io import load_source, create_corpus
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




def get_recommendations(
    model: Dict, 
    labeled_data: List[Dict], 
    labels: List[str], 
    corpus: List[Dict],
    target_label: str,
    amount: int = 5
) -> List[int]:

    model = train_model(model, labeled_data, labels)
    result = []

    for _ in range(len(corpus)):
        song_vec = choice(corpus)
        label = run_inference(model, song_vec)
        if label == target_label:
            result.append(corpus.index(song_vec)) 
        
        if len(result) == amount:
            break
    
    return result
           


