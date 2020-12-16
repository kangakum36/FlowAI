from models.base_model import BaseModel
from xgboost import XGBClassifier
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score

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
        scoring = {'accuracy' : make_scorer(accuracy_score), 
           'precision' : make_scorer(precision_score),
           'recall' : make_scorer(recall_score), 
           'f1_score' : make_scorer(f1_score)}
        kfold = StratifiedKFold(n_splits=10, random_state=7)
        results = cross_validate(self.model, self.dataset, self.labels, cv=kfold, scoring=scoring)
        print(results)

        print("CrossVal Accuracy: %.2f%% (%.2f%%)" % (results['accuracy'].mean()*100, 
                results['accuracy'].std()*100))

        print("F1 Score: %.2f (%.2f%%)" % (results['f1_score'].mean()*100, 
                results['f1_score'].std()*100))