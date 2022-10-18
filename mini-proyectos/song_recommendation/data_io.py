from typing import Dict, List, Tuple
from song_recommendation.text_processing import load_csv
from song_recommendation.utils import transform_row_vector, split_train_test


def load_source(csv_path: str) -> Tuple[List, List]:
    table = load_csv(csv_path)
    train_set, test_set = split_train_test(table, train_ratio=0.7) 

    train_set = train_set[: 1500]
    test_set = test_set[:200]
    
    return train_set, test_set


def create_corpus(dataset: List[Dict], feature_list: List[str], label_col: str) -> Tuple[List, List]:
    
    corpus = []
    labels = []
    for row in dataset:
        corpus.append(transform_row_vector(row, feature_list))
        labels.append(row[label_col])
        
    return corpus, labels
