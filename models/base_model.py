import sklearn as sk
import sklearn.model_selection
import numpy as np

class BaseModel:

    def __init__(self, dataset: np.ndarray, labels: np.ndarray):
        self.X_train, self.X_test, self.y_train, self.y_test = sk.model_selection.train_test_split(dataset, labels, test_size = 0.2)

    def train(self):
        pass

    def test(self):
        pass


    

