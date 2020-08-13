from models.base_model import BaseModel
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
import numpy as np

class NeuralNet(BaseModel):

    def __init__(self, dataset: np.ndarray, labels: np.ndarray):
        super().__init__(dataset, labels)
        self.model = Sequential()

    def train(self):
        self.model.add(Dense(30, input_dim=520000, activation='tanh'))
        self.model.add(Dropout(0.05))
        self.model.add(Dense(20, input_dim=30, activation='tanh'))
        self.model.add(Dense(10, input_dim=20, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.model.fit(self.X_train, self.y_train, epochs=50, batch_size=10)

    def test(self):
        _, accuracy = self.model.evaluate(self.X_test, self.y_test)
        return accuracy
