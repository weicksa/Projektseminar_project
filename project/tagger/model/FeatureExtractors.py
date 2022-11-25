from ..data.Token import Token
from ..data.Sentence import Sentence
from ..data.StringMapper import StringMapper


class FeatureExtractors(object):

    def extractFeatures(self, token):
        # call extract(prev/next/current)word, extractSuffices
        # store results in one list
        mapper = StringMapper()
        features = []
        features.append((extractPrevWord(mapper, token)))
        features.append(extractCurrentWord(mapper, token))
        features.append(extractNextWord(mapper, token))
        features.append((extractSuffices(mapper, token)))
        token.features = features
        print(features)
        print(mapper.map)
        # token.features -> overwrite with new feature list
    def extractAllFeatures(self, corpus):
        # run through whole corpus, use extractFeatures on every token
        # return lists in list?
        for sentence in corpus:
            for token in sentence.tokens:
                extractFeatures(token)

        pass


def extractPrevWord(mapper, token) -> int:  # input: Token
    # iterate over sentences, get previous word
    # if prev word not there (sentence start) create pseudo token
    # use string mapper
    if token.previous is None:
        return mapper.lookup("$begin")
    else:
        return mapper.lookup(token.previous)


def extractNextWord(mapper, token) -> int:  # input: Token
    # iterate over sentences, get current word
    # use string mapper
    if token.next is None:
        return mapper.lookup("final$")
    else:
        return mapper.lookup(token.next)


def extractCurrentWord(mapper, token) -> int:  # input: Token
    # iterate over sentences, get next word
    # if prev word not there (sentence end) create pseudo token
    # use string mapper
    return mapper.lookup(token.word)


def extractSuffices(mapper, token):
    # Eingabe: ein Token:
    #   if len(token) >= 6:
    #       use str slicing
    #   else (Länge wort -1):
    #       use str slicing
    word = token.word

    if len(word) >= 6:
        for i in range(1, 6):
            a = len(word) - i
            mapper.lookup("suf=" + word[a:])
    else:
        for i in range(1, len(word)):
            a = len(word) - i
            mapper.lookup(("suf=" + word[a:]))



