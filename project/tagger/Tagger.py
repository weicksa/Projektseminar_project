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
                # assumption: token, gold, and prediction are in second, third and fourth column of CoNLL
                res_list.append(spl[1:4])
        return res_list
    # this is a comment made by Sandro

# comment by tana