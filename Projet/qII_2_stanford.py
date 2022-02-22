import sys

assert(len(sys.argv) == 3)
path_in  = sys.argv[1]
path_out  = sys.argv[2]
id_type = path_in.find('.ne.stanford')
assert(id_type != -1)


# OUVERTURE DES FICHIERS
fr = open(path_in,  'r')
fw = open(path_out, 'w')
print('Nom du fichier d entree :',  path_in)  # data\stanford\stanford-ner-2018-10-16\resultats\ne_test.txt.ne.stanford
print('Nom du fichier de sortie :',  path_out)  # data\ne_test.txt.ne.stanford


# LECTURE DU FICHIER
lines = fr.readlines()
fr.close()


def conversion(label):
	org = ["ORGANIZATION", "FACILITY"]
	pers = ["PERSON"]
	loc = ["LOCATION", "GPE", "GSP"]
	misc = ["DATE", "TIME", "MONEY", "PERCENT"] # Remarque : STANFORD et NLTK ne trouveront jamais des MISC...

	if label in org:
		return "ORG"
	elif label in pers:
		return "PER"
	elif label in loc:
		return "LOC"
	elif label in misc:
		return "MISC"
	else:
		raise ValueError("Etiquette non reconnue")


# TRAITEMENT et ECRITURE DANS LE FICHIER DE SORTIE
for l in lines:
	entities = l.split()
	tag = ""
	b_entity = False

	for entity in entities:
		couple = entity.split("/")
		if (len(couple) == 2):
			if (couple[1] != "O"):
				if not b_entity:
					fw.write(couple[0])
					tag = couple[1]
					b_entity = True
				else:
					if couple[1] == tag:
						fw.write(" " + couple[0])
					else:
						fw.write("\t" + conversion(tag) + "\n")
						fw.write(couple[0])
						tag = couple[1]
						b_entity = True
			else:
				if b_entity:
					fw.write("\t" + conversion(tag) + "\n")
				b_entity = False
				fw.write(couple[0] + "\t" + couple[1] + "\n") # couple[1] == "O" ici
		else:
			raise ValueError("L'entite nommee possède un caractère / dans son nom")

fw.close()
