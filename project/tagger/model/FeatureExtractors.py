from ..data.Token import Token
from ..data.Sentence import Sentence
from ..data.StringMapper import StringMapper


class FeatureExtractors(object):

    def __init__(self):
        self.mapper = StringMapper()
        self.inverse_mapper = {}
        self.class_mapper = StringMapper()

    def extractFeatures(self, token):
        # call extract(prev/next/current)word, extractSuffices
        # store results in one list
        features = []
        features.append((extractPrevWord(self.mapper, token)))
        features.append(extractCurrentWord(self.mapper, token))
        features.append(extractNextWord(self.mapper, token))
        features.extend((extractSuffices(self.mapper, token)))
        token.features = features
        # token.features -> overwrite with new feature list

    def extractAllFeatures(self, corpus):
        # run through whole corpus, use extractFeatures on every token
        for sentence in corpus:
            for token in sentence.tokens:
                self.extractFeatures(token)
                token.correctLabelIndex = self.class_mapper.lookup(token.label)

    def writeToFile(self, sent, filename: str):
        """
         <line> .=. <target> <feature>:<value> <feature>:<value> ... <feature>:<value> # <info>
        <target> .=. <integer>
        <feature> .=. <integer>
        <value> .=. <float>
        <info> .=. <string>
        3 1:0.43 3:0.12 9284:0.2 # abcdef
        """
        # save Sentence(es) to svmmulti file, the digit after the # indicates the sentence
        with open(filename, "w") as file:
            target_mapper = StringMapper()
            for i in range(len(sent)):
                sentence = sent[i]
                for token in sentence.tokens:
                    line = f"{target_mapper.lookup(token.word)}"
                    for feature in token.features:
                        line += f" {feature}:1"
                    line += f" # {i} \n"
                    file.write(line)

    def readFromFile(self, filename: str):
        sentence_counter = 0
        sentences_indexes = []
        res_list = []
        # read a file in the smvmulti format
        with open(filename) as source:
            sent_list = []
            sent_index = 0
            lines = source.readlines()
            line_null = lines[0]
            split_null = line_null.split()
            # initialize sent_index with the first sent_index value from file
            sent_index = split_null[-1]

            for line in lines:
                spl = line.split()
                # check wether the current line still belongs to the same sentence
                if spl[-1] == sent_index:
                    # add features
                    tok_features = []
                    for index in range(1, len(spl) - 2):
                        feat_spl = spl[index].split(":")
                        tok_features.append(int(feat_spl[0]))
                    tok = Token(word=spl[0], features=tok_features)
                    sent_list.append(tok)

                # if the current line belongs to a new sentence, add the old sentence to
                # the res_list
                else:
                    copy_sent_list = sent_list.copy()
                    sent = Sentence(tokens=copy_sent_list)
                    res_list.append(sent)
                    sentences_indexes.append((sent_index, spl[-1]))
                    sentence_counter += 1

                    # add the new token to a fresh sentence
                    sent_list.clear()
                    sent_index = spl[-1]
                    tok_features = []
                    for index in range(1, len(spl) - 2):
                        feat_spl = spl[index].split(":")
                        tok_features.append(int(feat_spl[0]))
                    tok = Token(word=spl[0], features=tok_features)
                    sent_list.append(tok)

            # add the last sentence to the res_list
            copy_sent_list = sent_list.copy()
            sentence = Sentence(tokens=copy_sent_list)
            res_list.append(sentence)

            return res_list


def extractPrevWord(mapper, token) -> int:  # input: Token
    # get previous word
    # if prev word not there (sentence start) create pseudo token
    # use string mapper
    if token.previous is None:
        return mapper.lookup("prev=$begin")
    else:
        return mapper.lookup("prev=" + token.previous)


def extractNextWord(mapper, token) -> int:  # input: Token
    # get next word
    # if next word is None use pseudo token
    # use string mapper
    if token.next is None:
        return mapper.lookup("next=final$")
    else:
        return mapper.lookup("next=" + token.next)


def extractCurrentWord(mapper, token) -> int:  # input: Token
    # get current word
    # use string mapper
    return mapper.lookup(token.word)


def extractSuffices(mapper, token):
    # Eingabe: ein Token:
    #   if len(token) >= 6:
    #       use str slicing
    #   else (Länge wort -1):
    #       use str slicing
    word = token.word
    suf_list = []

    if len(word) >= 6:
        for i in range(1, 6):
            a = len(word) - i
            suf_list.append(mapper.lookup("suf=" + word[a:]))
    else:
        for i in range(1, len(word)):
            a = len(word) - i
            suf_list.append(mapper.lookup("suf=" + word[a:]))

    return suf_list
