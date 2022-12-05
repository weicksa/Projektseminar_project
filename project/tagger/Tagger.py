'''
Created on Oct 29, 2020

@author: nastasvi
'''

from .data.Token import Token
from .data.Sentence import Sentence
from .data.StringMapper import StringMapper


class Tagger(object):
    '''
    classdocs
    '''

    @staticmethod
    def extractInstances(data, goldLabel, predLabel):
        res_list = []
        for sentence in data:
            for i in range(sentence.length()):
                token = sentence.get(i)
                if token.label == goldLabel and token.prediction == predLabel:
                    try:
                        for a in range(i-3,i):
                            print(f"{sentence.get(a).word}\t{sentence.get(a).label}\t{sentence.get(a).prediction}")
                    except IndexError:
                        pass
                    print(f"*{token.word}*\t{token.label}\t{token.prediction}")
                    try:
                        for b in range(i+1,i+4):
                            print(f"{sentence.get(b).word}\t{sentence.get(b).label}\t{sentence.get(b).prediction}")
                    except IndexError:
                        pass
                    print("*******************")


    @staticmethod
    def readCoNLL(filename):
        class_map = StringMapper()
        res_list = []
        i = 1
        token_counter = 0
        word_prev = None
        word_next = None
        with open(filename) as source:
            lines = source.readlines()
            length = len(lines) - 1
            sent_list = []
        for line in lines:
            length -= 1
            spl = line.split()
            try:
                if len(spl) > 0:
                    tok = Token(word=spl[1], label=spl[4], prediction=spl[5], correctLabelIndex=class_map.lookup(spl[4]))
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

        for sent in res_list:
            for i in range(sent.length()):
                current_token = sent.get(i)
                try:
                    current_token.previous = sent.get(i-1).word
                except IndexError:
                    current_token.previous = None
                try:
                    current_token.next = sent.get(i+1).word
                except IndexError:
                    current_token.next = None

        try:
            print(f"from tagger: {res_list[-1].toString()}")
        except IndexError:
            pass
        return res_list
    # this is a comment made by Sandro

# comment by tana
