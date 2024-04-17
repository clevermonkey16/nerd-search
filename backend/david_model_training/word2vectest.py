import nltk
import gensim
from gensim.models import KeyedVectors
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings


model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

print('done')
print(model.similarity("engine", "engines"))
