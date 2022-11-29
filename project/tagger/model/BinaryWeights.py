from ..data.Token import Token
from ..data.Sentence import Sentence
from ..data.StringMapper import StringMapper


class BinaryWeights(object):

    def __init__(self):
        self.weights = []
        #
        self.weights.append(1)
