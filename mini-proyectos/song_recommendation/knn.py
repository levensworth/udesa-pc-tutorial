import math
from itertools import count
from typing import Dict, List, Tuple


def create_knn(amount_of_neighbours: int = 5) -> Dict:
    return {
        'n_neighbours': amount_of_neighbours,
        'corpus': None,
        'n_feature': None,
        'labels': None
    }


def train_model(knn: Dict, data: List[List[float]], labels: List[str]) -> Dict:
    
    if len(data) != len(labels):
        raise ValueError('seems as if the amount of datapoints and labels does not match.')
    knn['labels'] = labels
    knn['corpus'] = data
    knn['n_features'] = len(data[0])
    return knn


def run_inference(knn: Dict, target: List[float]) -> str:
    # sanity check
    if knn.get('lables'):
        raise ValueError('the given knn seems as if it wasn\'t trained, try calling the train_model method first')
    if knn.get('n_feature') == len(target):
        raise ValueError('seems as if the amount of features in the model differs from the target datapoint')

    
    top_distances = get_neighbours(knn.get('corpus'), knn.get('n_neighbours'), target)
    # decide lable
    labels = {}
    for datapoint in top_distances:
        current_label = knn.get('labels')[datapoint[0]]
        labels.setdefault(current_label, 0) # this only works the first time the label appears
        labels[current_label] += 1  

    winner_label_tuple: Tuple[str, int] = max(labels.items(), key=lambda t: t[1])
    return winner_label_tuple[0]



def get_distance(from_vec: List[float], to_vec: List[float]) -> float:
    
    result = 0
    for feature_idx in range(len(from_vec)):
        result += (from_vec[feature_idx] - to_vec[feature_idx]) ** 2
        
    return result ** 0.5
        

def get_neighbours(
    corpus: List[List[float]], 
    n_neighbours: int, 
    target: List[float]
) -> List[Tuple[int, float]]:
    
    top_distances: List[Tuple[int, float]] = [(-1, math.inf)]* n_neighbours

    for idx, datapoint in enumerate(corpus):
        current_distnace = get_distance(datapoint, target)
        # finds the least near datapoint to our target
        min_top_datapoint = max(top_distances, key=lambda t: t[1])
        
        if current_distnace <= min_top_datapoint[1]:
            # if the current datapoint it nearer, then we add this as new neighbour and delete the prev.
            top_distances.remove(min_top_datapoint)
            top_distances.append((idx, current_distnace))
        
    return top_distances
    


    

    


