'''
Created on Oct 29, 2020

@author: nastasvi
'''
import unittest

from tagger.Tagger import Tagger
from tagger.model.FeatureExtractors import FeatureExtractors

class Test(unittest.TestCase):

    def setUp(self):
        self.filename = "../Data/file-onesent.txt"


    def testExtractFeatures(self):
        sentences = Tagger.readData(self.filename)
        s = sentences[0]
        fes = FeatureExtractors()
        for token in s.tokens:
            fes.extractFeatures(token)
        self.assertEqual(4, len(s.get(0).features))
        self.assertEqual(6, len(s.get(1).features))
        self.assertEqual(7, len(s.get(2).features))
        self.assertEqual(6, len(s.get(3).features))
        self.assertEqual(8, len(s.get(4).features))
        self.assertEqual(5, len(s.get(5).features))
        self.assertEqual(8, len(s.get(6).features))
        self.assertEqual(8, len(s.get(7).features))
        self.assertEqual(4, len(s.get(8).features))
        self.assertEqual(0, self.intersection(s.get(0).features, s.get(1).features))
        self.assertEqual(0, self.intersection(s.get(1).features, s.get(2).features))
        self.assertEqual(1, self.intersection(s.get(2).features, s.get(4).features))
        self.assertEqual(1, self.intersection(s.get(6).features, s.get(7).features))
        self.assertEqual(0, self.intersection(s.get(3).features, s.get(5).features))
        self.assertEqual(0, self.intersection(s.get(2).features, s.get(5).features))
        #print("Features: {}".format(s.get(0).features))
        
        
    def testExtractAllFeatures(self):
        
        ss = Tagger.readData(self.filename)
        FeatureExtractors().extractAllFeatures(ss)
        s = ss[0]
        self.assertEqual(4, len(s.get(0).features))
        self.assertEqual(6, len(s.get(1).features))
        self.assertEqual(7, len(s.get(2).features))
        self.assertEqual(6, len(s.get(3).features))
        self.assertEqual(8, len(s.get(4).features))
        self.assertEqual(5, len(s.get(5).features))
        self.assertEqual(8, len(s.get(6).features))
        self.assertEqual(8, len(s.get(7).features))
        self.assertEqual(4, len(s.get(8).features))
        self.assertEqual(0, self.intersection(s.get(0).features, s.get(1).features))
        self.assertEqual(0, self.intersection(s.get(1).features, s.get(2).features))
        self.assertEqual(1, self.intersection(s.get(2).features, s.get(4).features))
        self.assertEqual(1, self.intersection(s.get(6).features, s.get(7).features))
        self.assertEqual(0, self.intersection(s.get(3).features, s.get(5).features))
        self.assertEqual(0, self.intersection(s.get(2).features, s.get(5).features))



    def testWriteToFile(self):
        ss = Tagger.readData(self.filename)
        fes = FeatureExtractors()
        fes.extractAllFeatures(ss)
        fes.writeToFile(ss, "file-onesent.svmmulti")
        fes.readFromFile("file-onesent.svmmulti")
        

    def testReadFromFile(self):
        ss = Tagger.readData("../Data/tiger-2.2.train.conll09")
        fes = FeatureExtractors()
        fes.extractAllFeatures(ss)
        fes.writeToFile(ss, "../Data/file-tiger.svmmulti")
        ss = FeatureExtractors.readFromFile("../Data/file-tiger.svmmulti")
#        # // test robustness on complete tiger train set
        self.assertEqual(40472, len(ss), "Tiger train file should contain 40472 sentences")
        self.assertEqual(719530, self.countWords(ss), "Tiger train file word count should be 719530")





    def intersection(self, array1, array2):
        return len(set(array1).intersection(array2))
    
    def countWords(self, sentences):
        return sum([s.length() for s in sentences])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testExtractFeatures']
    unittest.main()
    