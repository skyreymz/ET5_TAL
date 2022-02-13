import sys

assert(len(sys.argv) == 3)

path_in = sys.argv[1]

id_type = path_in.find('.ne.stanford')

assert(id_type != -1)


# OUVERTURE DES FICHIERS
path_in  = sys.argv[1]
path_out = sys.argv[2]

fr = open(path_in,  'r')
fw = open(path_out, 'w')

print('Nom du fichier d entree :',  path_in)  # data/formal-tst.NE.key.04oct95_small.txt.ne.stanford
print('Nom du fichier de sortie :', path_out) # votre nom de fichier choisi


# LECTURE DU FICHIER
lines = fr.readlines()
fr.close()


# TRAITEMENT
global_counter = 0
entity_dictionary = {}

for l in lines:
	entities = l.split()
	for entity in entities:
		couple = entity.split("/")
		if (len(couple) == 2):
			if (couple[1] != "O"):
				global_counter += 1
				if (entity_dictionary.__contains__(couple[0])):
					entity_dictionary[couple[0]] = (entity_dictionary[couple[0]][0], entity_dictionary[couple[0]][1] + 1)
				else:
					entity_dictionary[couple[0]] = (couple[1], 1)
		else:
			raise ValueError("L'entite nommee possède un caractère / dans son nom")


# ECRITURE DANS LE FICHIER DE SORTIE
fw.write("Entite nommee\tType\tNombre d’occurrences\tProportion dans le texte (%)\n\n")
for item in entity_dictionary.items():
	fw.write(item[0] + '\t' + item[1][0] + '\t' + str(item[1][1]) + '\t' + str(item[1][1]/global_counter) + " (" + str(item[1][1]) + "/" + str(global_counter) + ")\n")

fw.close()


# VERIFICATION DU NOMBRE D'ENTITES NOMMEES
assert(sum([x[1] for x in entity_dictionary.values()]) == global_counter)