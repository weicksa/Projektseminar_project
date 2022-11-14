'''
Created on Oct 29, 2020

@author: nastasvi
'''

import io

from .data.Token import Token
from .data.Sentence import Sentence


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
        token_counter = 0
        with open(filename) as source:
            lines = source.readlines()
            length = len(lines) - 1
            sent_list = []
        for line in lines:
            length -= 1
            spl = line.split()
            try:
                if len(spl) > 0:
                    tok = Token(word=spl[1], label=spl[4], prediction=spl[5])
                    sent_list.append(tok)
                else:
                    token_counter += len(sent_list)
                    copy_sent_list = sent_list.copy()
                    sent = Sentence(tokens=copy_sent_list)
                    res_list.append(sent)
                    sent_list.clear()
                    i += 1
                    tok = Token(word=spl[1], label=spl[4], prediction=spl[5])
                    sent_list.append(tok)
            except IndexError:
                pass
        print(token_counter)
        return res_list
    # this is a comment made by Sandro

# comment by tana
