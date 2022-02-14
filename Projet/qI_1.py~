# -*- coding: utf-8 -*-

import sys

assert(len(sys.argv) == 2)

path_in = sys.argv[1]
ident = path_in.find('_reference.txt.lima')
assert(ident != -1)
path_out = path_in[:ident] + '_test.txt'

fr = open(path_in,  'r')
fw = open(path_out, 'w')

print('Nom du fichier d entree :',  path_in)  # data/pos_reference.txt.lima
print('Nom du fichier de sortie :', path_out) # data/pos_test.txt


# LECTURE DU FICHIER + TRAITEMENT
lines = fr.readlines()
fr.close()

text = ""
beginning = True # detection des debuts de phrase
for l in lines:
	elements = l.split('\t')
	if (len(elements) == 2):
		if(beginning):
			beginning = False
		else:
			if(elements[0] not in [",", "."]): # on ne met pas d espace devant les points et les virgules
				fw.write(" ")

		fw.write(elements[0])

		if(elements[0] == "."):
			beginning = True
			fw.write(" ") # espace pour le debut de la prochaine phrase

fw.close()
