from models.base_model import BaseModel
from xgboost import XGBClassifier
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.model_selection import GridSearchCV
import pickle

class XGB(BaseModel):

    def __init__(self, dataset: np.ndarray, labels: np.ndarray):
        super().__init__(dataset, labels)
        self.model = XGBClassifier(max_depth=3)
        self.dataset = dataset
        self.labels = labels
    
    def train(self):
        self.model.fit(self.X_train, self.y_train)

    def test(self):
        y_pred = self.model.predict(self.X_test)
        predictions = [round(value) for value in y_pred]
        accuracy = accuracy_score(self.y_test, predictions)
        print(classification_report(self.y_test, predictions))
        return accuracy

    def crossval(self):
        scoring = {'accuracy' : make_scorer(accuracy_score), 
           'precision' : make_scorer(precision_score),
           'recall' : make_scorer(recall_score), 
           'f1_score' : make_scorer(f1_score)}
        kfold = StratifiedKFold(n_splits=10, random_state=7, shuffle=True)
        results = cross_validate(self.model, self.dataset, self.labels, cv=kfold, scoring=scoring)
        print(results)

        print("CrossVal Accuracy: %.2f%% (%.2f%%)" % (results['test_accuracy'].mean()*100, 
                results['test_accuracy'].std()*100))

        print("F1 Score: %.2f (%.2f%%)" % (results['test_f1_score'].mean()*100, 
                results['test_f1_score'].std()*100))

    def gridSearch(self):
        scoring = {'accuracy' : make_scorer(accuracy_score)}

                
        kfold = StratifiedKFold(n_splits=10, random_state=7)
        search_space = [
                        {"n_estimators": [100, 200, 300, 400], 
                         "max_depth": [3, 4, 5, 6],
                         "learning_rate": [0.3, 0.1, 0.01, 1.0],
                         "colsample_bytree": [1.0, 0.9]}
                        ]
        grid = GridSearchCV(estimator=self.model, param_grid = search_space, cv=kfold, scoring='accuracy', verbose=1)
        grid.fit(self.X_train, self.y_train)
        with open('grid.p', 'wb') as f:
             pickle.dump(grid, f) 
        best = grid.best_estimator
        y_pred = best.predict(self.X_test)                                   
        predictions = [round(value) for value in y_pred]
        accuracy = accuracy_score(self.y_test, predictions)
        print("Accuracy is: "+ accuracy)

        print(grid.results)
        print(grid.best_estimator)
        print(grid.best_score)
        print(grid.best_params)        
         
