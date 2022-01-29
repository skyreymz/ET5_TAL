import sys
import nltk

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
from nltk import pos_tag

assert(len(sys.argv) == 2)


# OUVERTURE DES FICHIERS
path_in = sys.argv[1]
path_out = path_in + '.pos.nltk'

fr = open(path_in,  'r')
fw = open(path_out, 'w')

print('Nom du fichier d entree :',  path_in)  # data/wsj_0010_sample.txt
print('Nom du fichier de sortie :', path_out) # data/swj_0010_sample.txt.pos.nltk


# LECTURE DU FICHIER + TRAITEMENT
lines = fr.readlines()
fr.close()

for l in lines:
	line_tokenized = word_tokenize(l) #line_tokenized = l.split()
	line_tagged = nltk.pos_tag(line_tokenized)

	# ECRITURE DANS LE FICHIER DE SORTIE
	for couple in line_tagged:
		fw.write(couple[0] + '\t' + couple[1] + '\n')

fw.close()