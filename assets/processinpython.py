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
from nltk.corpus import stopwords


#Stemming the document
def stem_document(document):
	from nltk.stem import LancasterStemmer
	stemmer = LancasterStemmer()
	return stemmer.stem(document)

#Lemmatizing the documennt
def lemmatize_document(document):
	from nltk.stem import WordNetLemmatizer
	lemmatizer = WordNetLemmatizer()
	return lemmatizer.lemmatize(document)


#Can implement babblefish here for language translation

def translate_document(source_lang,target_lang,document):
	from nltk.misc import babelfish
	return babelfish.translate(document,source_lang,target_lang)

def regex_replacer_document(document):
	from replacers import RegexpReplacer
	replacer = RegexpReplacer()
	return replacer.replace(document)

def repeat_replacer_document(document):
	from replacers import RepeatReplacer
	replacer = RepeatReplacer()
	return replacer.replace(document)

def spelling_replacer(document):
	from replacers import SpellingReplacer
	replacer = SpellingReplacer()
	return replacer.replace(document)

def antonym_dealer(document):
	from replacers import AntonymReplacer
	replacer = AntonymReplacer()
	return replacer.replace_negations(document)

def filter_sent(sent):
	from transforms import filter_insignificant
	from transforms import correct_verbs
	from transforms import swap_verb_phrase
	from transforms import swap_infinitive_phrase
	from transforms import singularize_plural_noun
	from transforms import swap_noun_cardinal

	#print filter_insignificant(sent)
	return singularize_plural_noun(swap_infinitive_phrase(swap_noun_cardinal(swap_verb_phrase(correct_verbs(filter_insignificant(sent))))))


number_of_words =  len(sys.argv)-1
print number_of_words
content = ""




for i in range(1,number_of_words):
	content = content+sys.argv[i]  + " "

#content contains raw data till this point
document = content

document = stem_document(document)
document = lemmatize_document(document)
document = regex_replacer_document(document)
#document = spelling_replacer(document)
#document = antonym_dealer(document)

sentences = nltk.sent_tokenize(document)
words = [nltk.word_tokenize(sent) for sent in sentences]
words = [w for w in words if not w in stopwords.words('english')]

document = regex_replacer_document(document)






grammar1 = r"""
  NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
      {<NNP>+}                # chunk sequences of proper nouns
"""	

grammar2 = r"""
  NP: {<DT|JJ|JJS|CD|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*>} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
  """

def traverse (t):
	if isinstance (t, nltk.tree.Tree):
		if t.node == 'NP' or t.node == 'VP':
			print t.node
			#print t
			temp= ''
			for child in t:
				temp = temp +child[0] + " "
			print temp	
			for child in t:
				traverse(child)
		else:
			for child in t:
				traverse (child)





def ie_preprocess(document):
	sentences = nltk.sent_tokenize(document)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	return sentences



cp1 = nltk.RegexpParser(grammar1)
cp2 = nltk.RegexpParser(grammar2)

document = ie_preprocess(document)

for sent in document:
	print(sent)
	
	result = cp2.parse(sent)
	traverse(result)




# def ie_preprocess(document):
# 	sentences = nltk.sent_tokenize(document)
# 	sentences = [nltk.word_tokenize(sent) for sent in sentences]
# 	sentences = [nltk.pos_tag(sent) for sent in sentences]
# 	return sentences

# content = ie_preprocess(content)

# grammar = r"""
#   NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
#       {<NNP>+}                # chunk sequences of proper nouns
# """	

# grammar2 = r"""
#   NP: {<DT|JJ|JJS|CD|NN.*>+}          # Chunk sequences of DT, JJ, NN
#   PP: {<IN><NP>}               # Chunk prepositions followed by NP
#   VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
#   CLAUSE: {<NP><VP>}           # Chunk NP, VP
#   """

# def traverse (t):
# 	if isinstance (t, nltk.tree.Tree):
# 		if t.node == 'NP' or t.node == 'VP':
# 			print t.node
# 			print t
# 			temp= ''
# 			for child in t:
# 				temp = temp +child[0] + " "
# 			print temp	
# 			for child in t:
# 				traverse(child)
# 		else:
# 			for child in t:
# 				traverse (child)




# cp = nltk.RegexpParser(grammar)
# cp2 = nltk.RegexpParser(grammar2)

# for sent in content:
# 	result = cp2.parse(sent)
# 	#print(result)
# 	traverse(result)






#do with this
# for sent in content:
# 	result = cp.parse(sent)
# 	print(result)
# 	#result.draw()


# print content;
