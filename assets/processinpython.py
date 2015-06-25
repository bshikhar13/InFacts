import nltk
nltk.data.path.append('/home/shikhar/Documents/Shikhar/namo/nltk_data')
import  re, pprint
from nltk.corpus import stopwords
from nltk.chunk import *
from nltk.chunk.util import *
from nltk.chunk.regexp import *
from nltk import Tree
from nltk.chunk import RegexpParser
from nltk.corpus import conll2000
import sys


number_of_words =  len(sys.argv)-1
print number_of_words
content = ""




for i in range(1,number_of_words):
	content = content+sys.argv[i]  + " "

#content contains raw data till this point

def ie_preprocess(document):
	sentences = nltk.sent_tokenize(document)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	return sentences

content = ie_preprocess(content)

grammar = r"""
  NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
      {<NNP>+}                # chunk sequences of proper nouns
"""	

grammar2 = r"""
  NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
  """

cp = nltk.RegexpParser(grammar)
cp2 = nltk.RegexpParser(grammar2)

for sent in content:
	result = cp2.parse(sent)
	print(result)




#do with this
# for sent in content:
# 	result = cp.parse(sent)
# 	print(result)
# 	#result.draw()


# print content;
