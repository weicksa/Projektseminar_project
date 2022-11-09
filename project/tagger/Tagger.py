'''
Created on Oct 29, 2020

@author: nastasvi
'''

import io

from .data import Sentence
from .data import Token

class Tagger(object):
    '''
    classdocs
    '''

      
    @staticmethod
    def extractInstances(data, goldLabel, predLabel):
        pass

    @staticmethod
    def readCoNLL(filename):
        res_list = []
        with open(filename) as source:
            lines = source.readlines()
            for line in lines:
                # split could be changed to split at \t if needed
                spl = line.split()
                # CoNLL has form: second,third and fourth column are wordforms, then gold(?), then pred(?)
                res_list.append(Sentence(spl[1:6]))
        return res_list
    # this is a comment made by Sandro

# comment by tana