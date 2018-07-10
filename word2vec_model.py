# -*- coding: utf-8 -*-

import logging
import os.path
import sys
import argparse
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence, Text8Corpus

parser = argparse.ArgumentParser(description = 'word2vec_model.py')

parser.add_argument("-text", required = True, help = 'Path to the Corpus.')
parser.add_argument("-vector", default = 'wiki.en.text.vector', help = 'Name of the Vector Output.')
parser.add_argument("-core", type=int, default = multiprocessing.cpu_count(), help = 'Number of cores of cpu while running in multiprocessing.')

opt = parser.parse_args()

if __name__ == '__main__':
	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)

	logging.basicConfig(format = '%(asctime)s: %(levelname)s: %(message)s')
	logging.root.setLevel(level = logging.INFO)
	logger.info("running %s" % ' '.join([sys.argv[0], opt.text, opt.vector]))

	inpt, vect = opt.text, opt.vector
	sentences = Text8Corpus(inpt)

	model = Word2Vec(sentences, size=300, window = 10, min_count = 50, workers = 8 , sg = 1, negative=7)
	model.wv.save_word2vec_format(vect, binary = False)
	logger.info("MSG : Finished Save!")
