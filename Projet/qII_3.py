import sys

assert(len(sys.argv) == 2)


# OUVERTURE DES FICHIERS
path_in  = sys.argv[1]
path_out = path_in + '.conll.txt'

fr = open(path_in,  'r')
fw = open(path_out, 'w')

print('Nom du fichier d entree :',  path_in)  # data\ne_test.txt.ne.nltk , data\ne_test.txt.ne.stanford
print('Nom du fichier de sortie :', path_out) # data\ne_test.txt.ne.nltk.conll.txt , data\ne_test.txt.ne.stanford.conll.txt


# LECTURE DU FICHIER
lines = fr.readlines()
fr.close()


# TRAITEMENT et ECRITURE DANS LE FICHIER DE SORTIE
for l in lines:
	couple = l.split("\t")
	if (len(couple) != 2):
		raise ValueError("Il n'y a pas que 2 colonnes dans votre jeu de données")
	if(couple[1]=="O\n"):
		fw.write(l)
	else :
		entities = couple[0].split()
		fw.write(entities[0] + "\t" + "B-" + couple[1])
		if (len(entities) != 1):
			for i in range(1,len(entities)):
				fw.write(entities[i] + "\t" + "I-" + couple[1])

fw.close()
