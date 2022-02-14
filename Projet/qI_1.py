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

for l in lines:
	elements = l.split('\t')
	if (len(elements) == 2):
		if(elements[0] not in [",", "."]): # on ne met pas d espace devant les points et les virgules
			fw.write(" ")
		fw.write(elements[0])
	elif (len(elements) == 1):
		fw.write("\n") # retour à la ligne pour la prochaine phrase
	else:
		raise ValueError('Il y a une erreur dans le fichier ' + path_in)

fw.close()
