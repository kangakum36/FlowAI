import argparse
import pickle
from utils.data_process import DataProcess
from models.random_forest_classifier import RandomForestModel
from models.decision_tree_classifier import DecisionTreeModel
from models.neural_net import NeuralNet
from models.conv_net import ConvNet
from models.xgb import XGB

def parse_args(parser):
    parser.add_argument('-m', '--model', type = str, choices=['rfc', 'dtc', 'nn', 'cnn', 'xgb'], help = "specify a model type", required = True)
    parser.add_argument('-p', '--pickle', type = str, choices=['load'], help = "specify to use pickled files")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    print("Starting")
    parser = argparse.ArgumentParser()
    args = parse_args(parser)
    model_tag = args.model
    model = None
    dataset = None
    labels = None
    conv_dataset = None
    accuracy = 0

    if(args.pickle != None):
        dataset = pickle.load( open( "data/dataset.p", "rb" ))
        labels = pickle.load( open( "data/labels.p", "rb" ))
        conv_dataset = pickle.load( open( "data/conv_dataset.p", "rb" ))

    else:
        files_path = 'data/FlowCasesDeidentify120519'
        print("Starting Data Process")
        dp = DataProcess(files_path)
        dp.data_process()
        dp.conv_process()
        dataset = dp.dataset
        labels = dp.labels
        conv_dataset = dp.conv_dataset


    if model_tag == 'rfc':
        model = RandomForestModel(dataset, labels)
        model.train()
        accuracy = model.test()

    elif model_tag == 'dtc':
        model = DecisionTreeModel(dataset, labels)
        model.train()
        accuracy = model.test()

    elif model_tag == 'nn':
        model = NeuralNet(dataset, labels)
        accuracy = model.test()

    elif model_tag == 'cnn':
        model = ConvNet(conv_dataset, labels)
        accuracy = model.test()

    elif model_tag == 'xgb':
        model = XGB(dataset, labels)
        model.train()
        accuracy = model.test()
        model.crossval()
        # model.gridSearch()




    # print("Selected model accuracy is: " + str(accuracy))

