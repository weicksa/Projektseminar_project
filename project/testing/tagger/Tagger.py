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

        with open(filename) as source:
            lines = source.readlines()
            for line in lines:
                spl = line.split()
                print(spl)


    # this is a comment made by Sandro

# comment by tana