from typing import Any, Dict, List, Tuple
from random import sample

def transform_row_vector(row: Dict[str, Any], keys: List[str]) -> List[float]:
    """transformation from the human understandable dictionary to a 
    mathematical vector used in the knn model.

    Args:
        row (Dict[str, Any]): a datapoint
        keys (List[str]): the features names you want to use the mathematical vector.

    Returns:
        List[float]: the mathematical vector.
    """
    return [row[key] for key in keys]


def split_train_test(corpus: List[Dict], train_ratio: float = 0.7) -> Tuple[List, List]:
    """generate a train and test corpus from an original dataset.
    This process is necessary for later evaluation.
    the datapoints are taken by a random (uniform distribution) sampling.
    
    Args:
        corpus (List[Dict]): The dataset.
        train_ratio (float, optional): The percentage of the corpus to use for training. Defaults to 0.7.

    Returns:
        Tuple[List, List]: _description_
    """
    amount_of_samples = len(corpus)
    
    amount_in_train = int(amount_of_samples * train_ratio)

    train_indexes = sample(range(amount_of_samples), amount_in_train)
    
    test_indexes = set(range(amount_of_samples)) - set(train_indexes)
    
    train_set = [corpus[idx] for idx in train_indexes]
    test_set = [corpus[idx] for idx in test_indexes]

    return (train_set, test_set)
    
    
    
    
    


