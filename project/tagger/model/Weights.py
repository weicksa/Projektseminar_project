from ..data.Token import Token
from ..data.Sentence import Sentence
from ..data.StringMapper import StringMapper


class Weights(object):
    def __init__(self, numClasses, numFeatures):
        # initialize class map with bias = 1.0
        self.class_map = {"bias": 1.0}
        # create initial entries in class map, based on numClasses and numFeatures
        for a in range(numClasses):
            self.class_map[a] = {}
            for b in range(numFeatures):
                self.class_map[a][b] = 0

    def score(self, classID, featureVector):
        # compute score as scalar for a specific class for a feature vector
        scalar = 0
        for feat in featureVector:
            if classID not in self.class_map:
                pass
            if feat not in self.class_map[classID]:
                pass
            else:
                scalar += 1 * self.class_map[classID][feat]
        # always add the bias value to score
        scalar += 1 * self.class_map["bias"]
        return scalar

    def update(self, prediction, correctLabelIndex, features, learningRate):
        # always set bias to learningRate
        self.class_map["bias"] = learningRate

        # if the prediction is not correct, decrease weights for wrongly predicted class
        # and increase weights for correct class
        if prediction != correctLabelIndex:
            for al in features:
                if prediction not in self.class_map:
                    self.class_map[prediction] = {al: -learningRate}
                elif al in self.class_map[prediction]:
                    self.class_map[prediction][al] -= learningRate
                else:
                    self.class_map[prediction][al] = -learningRate

            for el in features:
                if correctLabelIndex not in self.class_map:
                    self.class_map[correctLabelIndex] = {el: learningRate}
                elif el in self.class_map[correctLabelIndex]:
                    self.class_map[correctLabelIndex][el] += learningRate
                else:
                    self.class_map[correctLabelIndex][el] = learningRate
