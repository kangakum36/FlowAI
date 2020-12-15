from models.base_model import BaseModel
from xgboost import XGBClassifier
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

class XGB(BaseModel):

    def __init__(self, dataset: np.ndarray, labels: np.ndarray):
        super().__init__(dataset, labels)
        self.model = XGBClassifier()
        self.dataset = dataset
        self.labels = labels
    
    def train(self):
        self.model.fit(self.X_train, self.y_train)

    def test(self):
        y_pred = self.model.predict(self.X_test)
        predictions = [round(value) for value in y_pred]
        accuracy = accuracy_score(self.y_test, predictions)
        return accuracy

    def crossval(self):
        kfold = StratifiedKFold(n_splits=10, random_state=7)
        results = cross_val_score(self.model, self.dataset, self.labels, cv=kfold)
        print("CrossVal Accuracy: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))