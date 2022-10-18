
from typing import Dict, List

from song_recommendation.knn import run_inference

def get_accuracy(
    knn: Dict, 
    test_corpus: List[List[float]], 
    test_labels: List[str]
) -> float:
    """calculate the accuracy of a knn model
    Accuracy is the amount of currect results from the total predictions.
    Ie: You make 100 predictions and only get 75 right, the your accuracy is
    75% or 0.75.

    
    Args:
        knn (Dict): a trained knn model.
        test_corpus (List[List[float]]): an unseen subset of datapoint that should not be in the training set.
        test_labels (List[str]): the labels for the above datapoints.

    Returns:
        float: the accurcy measure between [0 - 1]
    """
    # eval model
    predicted = []
    for row in test_corpus:
        predicted.append(run_inference(knn, row))
        
    # calculate accuracy
    correct_results = 0
    for correct_label, predicted_label in zip(test_labels, predicted):
        if correct_label == predicted_label:
            correct_results += 1

        
    return correct_results / len(test_labels)




