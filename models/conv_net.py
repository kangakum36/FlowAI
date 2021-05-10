from models.base_model import BaseModel
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Conv1D
from tensorflow.keras.layers import MaxPooling1D
from tensorflow.keras.layers import Flatten
from sklearn.model_selection import StratifiedKFold
import numpy as np

class ConvNet(BaseModel):

    def __init__(self, dataset: np.ndarray, labels: np.ndarray):
        super().__init__(dataset, labels)
        self.model = None;

    def gen_model(self):
        model = Sequential()
        model.add(Conv1D(16, 3, activation='relu', input_shape = self.X_train.shape[1:]))
        model.add(Conv1D(16, 3, activation='relu'))
        model.add(MaxPooling1D(pool_size=2, strides=2))
        model.add(Flatten())
        model.add(Dense(30, activation='relu'))
        model.add(Dropout(0.05))
        model.add(Dense(20, input_dim=30, activation='relu'))
        model.add(Dropout(0.05))
        model.add(Dense(10, input_dim=20, activation='relu'))
        model.add(Dense(1, activation='relu'))
        return model

    def test(self):
        accuracy = self.crossval(100, self.X_train, self.y_train, self.X_test, self.y_test)
        return accuracy

    def crossval(self, n_epochs, X_train, y_train, X_test, y_test, filename = None):
        kfold = StratifiedKFold(n_splits=4, shuffle=True, random_state=0)
        bestmodel = None
        bestAcc = 0
        cvscores = []
        fold = 1
        for train, test in kfold.split(X_train, y_train):
            model = self.gen_model()
            model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
            print('------------------------------------------------------------------------')
            print(f'Training for fold {fold} ...')
            model.fit(X_train[train], y_train[train],epochs=n_epochs, verbose=1) # validation_split=0.2)
            scores = model.evaluate(X_train[test], y_train[test], verbose=1)
            print("Score for fold %d - %s: %.2f%%" % (fold, model.metrics_names[1], scores[1]*100))
            if(scores[1] > bestAcc):
                bestAcc = scores[1]
                bestmodel = model
            cvscores.append(scores[1] * 100)
            fold += 1
        print('------------------------------------------------------------------------')
        print("Avg accuracies: %.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores)))
        test_loss, test_acc = bestmodel.evaluate(X_test,  y_test, verbose=2)
        self.model = bestmodel
        return test_acc

       


        