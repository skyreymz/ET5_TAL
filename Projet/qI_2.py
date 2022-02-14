import sys

assert(len(sys.argv) == 4)

path_in_lima     = sys.argv[1]
path_in_LIMA_PTB = sys.argv[2]
path_in_PTB_UNIV = sys.argv[3]
ident = path_in_lima.find('.txt.lima')
assert(ident != -1)

# OUVERTURE ET LECTURE DES FICHIERS D ENTREE
lines_lima = []
with open(path_in_lima, 'r') as f:
    lines_lima = f.readlines()

lines_LIMA_PTB = []
with open(path_in_LIMA_PTB, 'r') as f:
    lines_LIMA_PTB = f.readlines()

lines_PTB_UNIV = []
with open(path_in_PTB_UNIV) as f:
    lines_PTB_UNIV = f.readlines()    

print('Nom de notre fichier en entree :', 	 	      		  path_in_lima)     # data/pos_reference.txt.lima
print('Nom de la table de correspondance LIMA -> PTB :',      path_in_LIMA_PTB) # data/ POSTags_LIMA_PTB_Linux.txt
print('Nom de la table de correspondance PTB -> Universal :', path_in_PTB_UNIV) # data/POSTags_PTB_Universal_Linux.txt


# OUVERTURE / CREATION DU FICHIER DE SORTIE
path_out = path_in_lima[:ident] + '.txt.univ'
fw = open(path_out, 'w')
print('Nom de notre fichier en sortie :', path_out)


# ENREGISTREMENT DES TABLES DE CORRESPONDANCE DANS DES TABLEAUX
tags_LIMA 	  = [] # tags LIMA de la table de correspondance LIMA -> PTB
tags_PTB  	  = [] # tags PTB  de la table de correspondance LIMA -> PTB
tags_PTB2 	  = [] # tags PTB  de la table de correspondance PTB  -> UNIV
tags_UNIV	  = [] # tags UNIV de la table de correspondance PTB  -> UNIV
tags_PTB_UNIV = [] # tags UNIV permettant la correspondance  LIMA -> PTB -> UNIV

for line in lines_LIMA_PTB:
	line = line.split()
	line = [l.replace('\n', '') for l in line]
	tags_LIMA.append(line[0])
	tags_PTB.append(line[1])

for line in lines_PTB_UNIV:
	line = line.split()
	line = [l.replace('\n', '') for l in line]
	tags_PTB2.append(line[0])
	tags_UNIV.append(line[1])

for tag_PTB in tags_PTB:
	index = tags_PTB2.index(tag_PTB)
	if (index == -1):
		raise ValueError("L etiquette " + tag_PTB + " de la table de correspondance LIMA -> PTB n est pas presente dans la table PTB -> Universal")
	tags_PTB_UNIV.append(tags_UNIV[index])


# CONVERSION DES TAGS LIMA EN UNIV
for line in lines_lima:
	line = line.replace('\n', '').split('\t')
	if (len(line) == 2):
		fw.write(line[0] + '\t' + tags_PTB_UNIV[tags_LIMA.index(line[1])] + '\n')

fw.close()