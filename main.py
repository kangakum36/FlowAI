import argparse
import pickle
from utils.data_process import DataProcess
from models.random_forest_classifier import RandomForestModel
from models.decision_tree_classifier import DecisionTreeModel
from models.neural_net import NeuralNet

def parse_args(parser):
    parser.add_argument('-m', '--model', type = str, choices=['rfc', 'dtc', 'nn'], help = "specify a model type", required = True)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parse_args(parser)
    model_tag = args.model
    model = None

    files_path = 'data/FlowCasesDeidentify120519'
#    dp = DataProcess(files_path)
#    dp.data_process()
    dataset = pickle.load( open( "data/dataset.p", "rb" ))
    labels = pickle.load( open( "data/labels.p", "rb" ))


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
        model.train()
        accuracy = model.test()


    print("Selected model accuracy is: " + str(accuracy))

