from models.base_model import BaseModel
from sklearn.tree import DecisionTreeClassifier
import numpy as np
class DecisionTreeModel(BaseModel):

    def __init__(self, dataset: np.ndarray, labels: np.ndarray):
        super().__init__(dataset, labels)
        self.model = DecisionTreeClassifier(random_state=0) 
        
    def train(self):
        self.model.fit(self.X_train, self.y_train.ravel())

    def test(self):
        accuracy = self.model.score(self.X_test, self.y_test.ravel())
        return accuracy


