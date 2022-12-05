from ..data.Token import Token
from ..data.Sentence import Sentence
from ..data.StringMapper import StringMapper
from ..model.Weights import Weights
import random


class Perceptron(object):

    def __init__(self, numClasses, numFeatures):
        self.weights = Weights(numClasses, numFeatures)

    def predict(self, token):
        # make a prediction for a tokens class based on the scoring function
        res_list = []
        # iterate over all known classes and compute the scalar for each one
        # append them to res_list in a tuple with (predicted_class, score)
        for cl in self.weights.class_map:
            if cl is not "bias":
                pred = self.weights.score(cl, token.features)
                res_list.append((cl, pred))
            else:
                continue

        # sort the results by score
        sort_res = sorted(res_list, key=lambda i: i[1], reverse=True)
        prediction = sort_res[0][0]
        # the final prediction is the class with the highest score
        token.predictedLabelIndex = prediction
        return prediction

    def train(self, trainingData, numberOfIterations):
        for i in range(numberOfIterations + 1):
            # randomly iterate over sentences and tokens
            for a in random.sample(range(len(trainingData)), len(trainingData)):
                for b in random.sample(list(range(trainingData[a].length())), trainingData[a].length()):
                    token = trainingData[a].tokens[b]
                    pred = self.predict(token)
                    # check wether the prediction is correct,
                    # if it's too small , increase weights for the right class and decrease them for the
                    # wrong prediction
                    # if it's too big, decrease weights for the right class and increase them for
                    # the wrong prediction
                    if pred != float(token.correctLabelIndex):
                        if pred > token.correctLabelIndex:
                            self.weights.update(pred, token.correctLabelIndex, token.features, -1)
                        else:
                            self.weights.update(pred, token.correctLabelIndex, token.features, 1)
