from ..data.Token import Token
from ..data.Sentence import Sentence
from ..data.StringMapper import StringMapper


class FeatureExtractors(object):

    def __init__(self):
        self.mapper = StringMapper()
        self.inverse_mapper = {}

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
        # return lists in list?
        for sentence in corpus:
            for token in sentence.tokens:
                self.extractFeatures(token)

        pass

    def writeToFile(self, sent, filename: str):
        """
         <line> .=. <target> <feature>:<value> <feature>:<value> ... <feature>:<value> # <info>
        <target> .=. <integer>
        <feature> .=. <integer>
        <value> .=. <float>
        <info> .=. <string>
        3 1:0.43 3:0.12 9284:0.2 # abcdef
        """
        with open(filename, "w") as file:
            target_mapper = StringMapper()
            # increasse iterations by one -> IndexError
            for i in range(len(sent)):
                sentence = sent[i]
                for token in sentence.tokens:
                    self.inverse_mapper[target_mapper.lookup(token.word)] = token.word
                    line = f"{target_mapper.lookup(token.word)}"
                    sort_features = sorted(token.features)
                    for feature in sort_features:
                        line += f" {feature}:1"

                    line += f" # {i} \n"
                    file.write(line)

    def readFromFile(self, filename: str):

        sentence_counter = 0
        sentences_indexes = []
        res_list = []
        with open(filename) as source:
            sent_list = []
            sent_index = 0

            lines = source.readlines()
            print(f"from read: {lines[-1]}")
            line_null = lines[0]
            split_null = line_null.split()
            sent_index = split_null[-1]
            for line in lines:
                spl = line.split()

                if spl[-1] == sent_index:
                    # add features
                    tok_features = []
                    for index in range(1,len(spl)-2):
                        feat_spl = spl[index].split(":")
                        tok_features.append(int(feat_spl[0]))
                    tok = Token(word=spl[0], features=tok_features)
                    sent_list.append(tok)
                else:
                    copy_sent_list = sent_list.copy()
                    sent = Sentence(tokens=copy_sent_list)
                    res_list.append(sent)
                    sentences_indexes.append((sent_index, spl[-1]))
                    # print(f"sent_index: {sent_index}, split[-1]: {spl[-1]}")
                    sentence_counter += 1

                    sent_list.clear()
                    sent_index = spl[-1]
                    tok_features = []
                    for index in range(1, len(spl) - 2):
                        feat_spl = spl[index].split(":")
                        tok_features.append(int(feat_spl[0]))
                    tok = Token(word=spl[0], features=tok_features)
                    sent_list.append(tok)

                    # sent = Sentence(tokens=copy_sent_list)
                    # res_list.append(sent)
            copy_sent_list = sent_list.copy()
            sentence = Sentence(tokens=copy_sent_list)
            res_list.append(sentence)

            sent = res_list[-1]
            last_sent = []
            """
            for token in sent.tokens:
                last_sent.append(self.inverse_mapper[int(token.word)])
            """
            print(f"feature: {last_sent}")
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
