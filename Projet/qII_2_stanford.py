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

def replace(token):
	if (token == "-LRB-"):
		return "("
	elif (token == "-RRB-"):
		return ")"
	elif (token == "-RSB-"):
		return "]"
	else:
		raise ValueError("Stanford ne devrait pas retenir les acolades { et }")


# TRAITEMENT et ECRITURE DANS LE FICHIER DE SORTIE
unrelated_characters = ["-LCB-", "-RCB-", "-LRB-", "-RRB-", "-RSB-"] # il s'agit des caracteres {, }, (, ) et ]

for l in lines:
	entities = l.split()
	tag = ""
	b_entity = False

	for entity in entities:
		couple = entity.split("/")
		if (len(couple) == 2):
			if (couple[0] in unrelated_characters):
				couple[0] = replace(couple[0])
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
			raise ValueError("L'entite nommee possede un caractère / dans son nom")

fw.close()



"""
Description de l'algorithme :

Les entités nommées obtenues par le NE recognizer de STANFORD ne sont pas données sous forme d’arbre syntaxique, contrairement au NE recognizer de NLTK.
En effet, pour STANFORD, nous obtenons à la suite des tokens avec leur étiquette respective au lieu d'avoir une structure en arbre syntaxique pouvant être composé de plusieurs tokens à la fois pour une seule même étiquette.
Par exemple, "Paul Itteck" est décomposé en deux tokens “Paul” et “Itteck” distincts ayant chacun pour étiquette PERSON, au lieu d'être décomposé comme un arbre syntaxique possédant les deux tokens “Paul” et “Itteck” en tant que nœuds de l’arbre et l’étiquette PERSON en tant que racine de l’abre.
Ainsi, pour NLTK, il suffit de récupérer les nœuds de l’arbre pour obtenir les différents mots de l’entité nommée.
Le NE recognizer de STANFORD se contente quant à lui d’associer à un token, une étiquette d’une entité nommée s’il le juge comme telle, sans faire de lien entre les précédents tokens alors qu’ils pourraient ensemble, représenter une seule même entité nommée. 
Ainsi, pour les résultats obtenus avec le NE recognizer de STANFORD, nous ne pouvons pas en déduire à vue d’œil les débuts d'entités (ex: B-ORG) des suites d'entités (ex: I-ORG).

Il faudra donc trouver une stratégie afin de convertir les étiquettes actuelles par les étiquettes CoNLL-2003 nous permettant de voir si le token s’agit d’un début d’entité nommée (B-) ou de sa suite (I-).
Cette stratégie sera donc de détecter lorsqu’une entité nommée est rencontrée puis d'analyser le token qui suit :
- (*) Si le token qui suit est une entité avec la même étiquette que la précédente, alors ce token est une suite de l'entité précédemment rencontrée
- Si le token qui suit est une entité mais avec une étiquette différente de la précédente, alors ce token est une autre entité
- Sinon (donc si le token est étiqueté en tant que "OTHER"), le token n'est pas une entité.
(*) Cette stratégie n'est correcte que si l'on considère de plus, que deux entités différentes mais qui ont la même étiquette (par exemple, deux PERSON différentes mais qui sont donc deux entités avec la meme etiquette), sont au moins séparées par un token qui n'est pas une entité. 
"""
