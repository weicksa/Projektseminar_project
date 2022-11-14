'''
Created on Oct 29, 2020

@author: nastasvi
'''

import io

from .data.Token import *
from .data.Sentence import *


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
        i = 1
        with open(filename) as source:
            lines = source.readlines()
            length = len(lines)-1
            print(length)
            sent_list = []
        for line in lines[143:182]:
            length -= 1
            spl = line.split()
            print(spl)
            try:
                print(int(spl[0]))
                print(i)
                if int(spl[0]) == int(i):
                    tok = Token(word=spl[1], label=spl[4], prediction=spl[5])
                    sent_list.append(tok)
                else:
                    print("in else")
                    sent = Sentence(sent_list)
                    res_list.append(sent)
                    sent_list.clear()
                    i += 1
                    tok = Token(word=spl[1], label=spl[4], prediction=spl[5])
                    sent_list.append(tok)
            except IndexError:
                pass

        return res_list
    # this is a comment made by Sandro

# comment by tana
