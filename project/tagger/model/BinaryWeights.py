from ..data.Token import Token
from ..data.Sentence import Sentence
from ..data.StringMapper import StringMapper


class BinaryWeights(object):

    def __init__(self, integer):
        self.weights = {0: 1.0}
        #

    def score(self, featureVector):
        scalar = 0
        for i in range(len(featureVector)):
            # print(i)
            if featureVector[i] not in self.weights:
                pass
            else:
                scalar += 1 * self.weights[featureVector[i]]
        scalar += 1 * self.weights[0]
        return scalar

    def update(self, featureVector, learningRate):
        self.weights[0] = learningRate
        for i in range(len(featureVector)):
            print(featureVector[i])
            if featureVector[i] in self.weights:
                self.weights[featureVector[i]] += learningRate
            else:
                self.weights[featureVector[i]] = learningRate
