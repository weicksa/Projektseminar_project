from .Sentence import *
from .Token import *


class ConfusionMatrix(object):

    def __init__(self, data):
        self.data = data
        outer_dict = {}
        for sentence in data:
            for token in sentence.tokens:
                if token.label in outer_dict:
                    if token.prediction in outer_dict[token.label]:
                        outer_dict[token.label][token.prediction] += 1
                    else:
                        outer_dict[token.label][token.prediction] = 1
                else:
                    outer_dict[token.label] = {}
                    outer_dict[token.label][token.prediction] = 1
        self.matrix = outer_dict

        tag_value_list = []
        for key in outer_dict:
            try:
                tag_value_list.append((key, outer_dict[key][key]))
            except KeyError:
                pass
        self.sort = sorted(tag_value_list, key=lambda value: value[1], reverse=True)

    def numberErrors(self, goldLabel: str, predLabel: str) -> int:
        try:
            return self.matrix[goldLabel][predLabel]
        except KeyError:
            return 0

    def print(self, maxDim: int):
        labels = []
        labels.append("  ")
        labels.extend([key for key, val in self.sort[:maxDim]])
        print(labels)
        vals = []
        for el in labels[1:]:
            vals.append(el)
            for lab in labels[1:]:
                try:
                    vals.append(self.matrix[el][lab])
                except KeyError:
                    vals.append(0)
            print(f"{vals}")
            vals.clear()


        # dictionary[gold][dictionary[pred]]

        # for key in dict:
        #   sorted_list.append((key, dict[key][key]))

        # for el, va in sortedlist[:max_dim+1]:
        #

