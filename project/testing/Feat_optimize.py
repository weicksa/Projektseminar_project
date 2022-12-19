import unittest

from ..tagger.Tagger import *


class Feat_optimize(unittest.TestCase):

	def setUp(self):
		self.path = "project/Data/"
		self.tagger = Tagger()
		self.training = self.tagger.readCoNLL(self.path + "wsj_train.conll09")
		self.develop = self.tagger.readCoNLL(self.path + "wsj_dev.conll09")
		self.extractor = FeatureExtractors()
		print("done with reading data")

	def test_pipeline(self):

		self.extractor.extractAllFeatures(self.training)
		self.extractor.extractAllFeatures(self.develop)
		print("done with extraction")
		feature_count = 0
		for key in self.extractor.mapper.map:
			feature_count += 1

		class_mapper = self.extractor.class_mapper
		model = Perceptron(class_mapper, feature_count)

		for i in range(1, 11):
			print(f"currently on iteration: {i}")
			model.train(self.training, 1)
			for sentence in self.develop:
				for token in sentence.tokens:
					model.predict(token)
			print(f"Evaluation and ConfusionMatrix for iteration {i}")
			matrix = ConfusionMatrix(self.develop)
			accuracy = Evaluation.accuracy(self.develop)
			accuracy_train = Evaluation.accuracy(self.training)
			matrix.print(10)
			print(f"accuracy on development data: {accuracy}")
			print(f"Accuracy on training data: {accuracy_train}")



if __name__ == "__main__":
	# import sys;sys.argv = ['', 'Test.testName']
	unittest.main()
