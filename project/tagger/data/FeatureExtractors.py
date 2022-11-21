class FeatureExtractor(object):

    def extractPrevWord(self): #input: Token
        # iterate over sentences, get previous word
        # if prev word not there (sentence start) create pseudo token
        # use string mapper
        pass

    def extractNextWord(self): #input: Token
        # iterate over sentences, get current word
        # use string mapper
        pass
    def extractCurrentWord(self): #input: Token
        # iterate over sentences, get next word
        # if prev word not there (sentence end) create pseudo token
        # use string mapper
        pass

    def extractSuffices(self):
        # Eingabe: ein Token:
        #   if len(token) >= 6:
        #       use str slicing
        #   else:
        #       use str slicing
        pass

    def extractFeatures(self):
        # call extract(prev/next/current)word, extractSuffices
        # store results in one list
        pass

    def extractAllFeatures(self):
        # run through whole corpus, use extractFeatures on every token
        # return lists in list?
        pass