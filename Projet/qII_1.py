# -*- coding: utf-8 -*-

import sys

assert(len(sys.argv) == 3)

# OUVERTURE DES FICHIERS
path_in  = sys.argv[1]
path_out = sys.argv[2]

id_type = path_in.find('.txt.conll.txt')
assert(id_type != -1)


fr = open(path_in,  'r')
fw = open(path_out, 'w')

print('Nom du fichier d entree :',  path_in)  # data\ne_reference.txt.conll.txt
print('Nom du fichier de sortie :', path_out) # data\ne_test.txt


# LECTURE DU FICHIER
lines = fr.readlines()
fr.close()


# TRAITEMENT et ECRITURE DANS LE FICHIER DE SORTIE
beginning = True
for l in lines:
	if (l.strip() != ""):
		elements = l.split('\t')
		if(elements[0] not in [",", "."]): # on ne met pas d espace devant les points et les virgules
			if not beginning:
				fw.write(" ")
			else:
				beginning = False
		fw.write(elements[0])
	else:
		fw.write("\n") # retour à la ligne pour la prochaine phrase
		beginning = True

fw.close()
