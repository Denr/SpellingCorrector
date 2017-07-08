import logging
import re
import nltk
from gensim.models.word2vec import Word2Vec
from gensim.models.word2vec import LineSentence
from gensim.models.keyedvectors import KeyedVectors
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = LineSentence('txt/source.txt')
model = Word2Vec(sentences, min_count=3, size=10, window=300)
word_vectors = model.wv
word_vectors.save('model)
model = KeyedVectors.load('model')
