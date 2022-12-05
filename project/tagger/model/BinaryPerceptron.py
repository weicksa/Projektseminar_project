from ..data.Token import Token
from ..data.Sentence import Sentence
from ..data.StringMapper import StringMapper
from ..model.BinaryWeights import BinaryWeights
import random


class BinaryPerceptron(object):

    def __init__(self, num):
        self.weights = BinaryWeights(num)

    def predict(self, token):
        pred = self.weights.score(token.features)
        token.predictedLabelIndex = pred
        return pred

    def train(self, trainingData, numberOfIterations):
        for i in range(numberOfIterations + 1):
            print(random.choices(range(len(trainingData))))
            for a in random.choices(range(len(trainingData))):
                print(trainingData[a].length)
                for b in random.sample(list(range(trainingData[a].length))):
                    token = trainingData[a].tokens[b]
                    pred = self.predict(token)
                    if pred != token.correctLabelIndex:
                        if pred > token.correctLabelIndex:
                            self.weights.update(token.features, -0.5)
                        else:
                            self.weights.update(token.features, 0.5)
