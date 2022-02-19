# Question II-2 : Conversion du fichier "ne_test.txt.ne.stanford" obtenu par STANFORD, sous le format du fichier "ne_reference.txt.conll.txt"
# Question II-3 : Conversion en étiquettes CoNLL-2003
# Nous sommes contraints à réaliser ces deux questions en meme temps pour STANFORD, contrairement pour NLTK où cela peut se faire séparément
#   puisque STANFORD ne détecte pas les entités nommées avec un arbre syntaxique, contrairement à NLTK.
# En effet, nous ne pouvons pas en déduire facilement les débuts d'entités (ex: B-ORG) des suites d'entités (ex: I-ORG)
#   puisqu'une ligne du fichier à produire pour la question 2 n'aura au maximum qu'un seul token associé à une étiquette,
#   contrairement à NLTK où une ligne du fichier pour la question 2 (ne_test.txt.ne.nltk) peut avoir plus d'un token associé(s) à une étiquette
#   grace a son systeme de détection avec un arbre syntaxique.
# Donc pour la question 3, pour NLTK, il suffit juste d'analyser ligne par ligne le fichier obtenu à la question 2.
# Néanmoins, cela n'est pas possible pour STANFORD.
# Ainsi, la stratégie pour pourvoir en déduire les débuts d'entités (ex: B-ORG) et les suites d'entités (ex: I-ORG)
#   pour STANFORD sera donc de détecter la première occurence d'une entité et d'analyser le token qui suit :
#   - si le token qui suit est une entité avec la meme étiquette de celle de la 1ere occurence, alors ce token est une suite de l'entité
#   - si le token qui suit est une entité mais avec une étiquette différente de celle la 1ere occurence, alors ce token est une autre entité
#   - sinon (cad si le token est un "Other"), le token n'est pas une entité.
# Cette stratégie n'est correcte que si l'on considère que deux entités différentes mais qui ont la meme étiquette
#   (par exemple deux entités différentes mais qui sont toutes deux des personnes), sont au moins séparées par un token qui n'est pas une entité, dans le texte.

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
print('Nom du fichier de sortie :',  path_out)  # data\ne_test.txt.ne.stanford.conll.txt


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
					fw.write(couple[0] + "\t" + "B-" + conversion(couple[1]) + "\n")
					tag = couple[1]
					b_entity = True
				else:
					if couple[1] == tag:
						fw.write(couple[0] + "\t" + "I-" + conversion(couple[1]) + "\n")
					else:
						fw.write(couple[0] + "\t" + "B-" + conversion(couple[1]) + "\n")
						tag = couple[1]
						b_entity = True
			else:
				b_entity = False
		else:
			raise ValueError("L'entite nommee possède un caractère / dans son nom")

fw.close()
