import sys

assert(len(sys.argv) == 3)


# VERIFICATION DES TYPES DES FICHIERS
path_in = sys.argv[1]
path_out = sys.argv[2]
assert(path_in.find( '.txt.pos.stanford') != -1)
assert(path_out.find('.txt.pos.stanford') != -1)


# OUVERTURE DES FICHIERS
fr = open(path_in,  'r')
fw = open(path_out, 'w')

print('Nom du fichier d entree :',  path_in)  # data/stanford/stanford-postagger-2018-10-16/resultats/pos_test.txt.pos.stanford
print('Nom du fichier de sortie :', path_out) # data/pos_test.txt.pos.stanford


# LECTURE DU FICHIER + TRAITEMENT
lines = fr.readlines()
fr.close()


# ECRITURE DANS LE FICHIER DE SORTIE
for l in lines:
	elements = l.split()
	for couple in elements:

		c = couple.split('_')
		if(len(c) >= 2):
			fw.write(c[0] + '\t' + c[1] + '\n')
		else:
			fw.write('\n')

fw.close()