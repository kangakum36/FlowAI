import glob
import pandas as pd
import numpy as np
import os
from FlowCytometryTools import FCMeasurement
import pickle
import gc
import nmslib

class DataProcess():
    ''' Class for Data Cleaning

    Parameters:
    -----------
    files_path : str
        Path to all case files

    '''
    def __init__(self, files_path : str):
        self.files = glob.glob(os.path.join(files_path, '*.fcs'))
        self.files_per_case = 4;
        self.dataset = None;
        self.labels = None;
        self.cells_per_tube = 10000
        self.buffer = 5000

    def case_data_appending(self, tube, caseNum, tubeNum):
        sample = FCMeasurement(ID = 'Test Sample', datafile = tube)
        sample_numpy = sample.data.values
        channel_length = len(sample.channels) - 1
        for x in range(self.cells_per_tube):
            for y in range(channel_length):
                self.dataset[caseNum][tubeNum * self.cells_per_tube * channel_length + x * channel_length + y] = sample_numpy[self.buffer + x][y]

    def data_process(self):
        self.files.sort()
        num_cases = int(len(self.files) / self.files_per_case)
        cases = []
        for x in range(num_cases):
            cases.append([])

        for x in range(len(self.files)):
            cases[int(x/4)].append(self.files[x])


        self.labels = np.zeros((len(cases), 1,))
        for x in range(len(cases)):
            if("CLL" in cases[x][0]):
                self.labels[x][0] = 1
       
        self.dataset = np.empty((len(cases),10000*13*4,))
       
        print("Converting case data into a suitable format for training, printing progress: ")
        
        for x in range(len(cases)):
            for y in range(len(cases[0])):
                self.case_data_appending(cases[x][y], x, y)  
            print("Case: " + str(x + 1))

        with open('data/dataset.p', 'wb') as f:
             pickle.dump(self.dataset, f)

        with open('data/labels.p', 'wb') as f:
             pickle.dump(self.labels, f)




        


