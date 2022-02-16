import sys
import re

assert(len(sys.argv) == 3)

path_in   = sys.argv[1]
path_univ = sys.argv[2] # Table de correspondance

assert(path_in.find('.pos') != -1)


# OUVERTURE ET LECTURE DES FICHIERS D ENTREE
lines_in = []
with open(path_in, 'r') as f:
    lines_in = f.readlines()

lines_univ = []
with open(path_univ) as f:
    lines_univ = f.readlines()    

print('Nom du fichier en entree :', 		 path_in)   # data/pos_test.txt.pos.stanford / data/pos_test.txt.pos.nltk
print('Nom de la table de correspondance :', path_univ) # data/POSTags_PTB_Universal_Linux.txt


# OUVERTURE / CREATION DES FICHIERS DE SORTIE
path_out = path_in + '.univ'

fw = open(path_out, 'w')

print('Nom du fichier en sortie :', path_out) # data/pos_test.txt.pos.stanford.univ / data/pos_test.txt.pos.nltk.univ


# ENREGISTREMENT DE LA TABLE DE CORRESPONDANCE DANS UN TABLEAU
tags_ptb = []
tags_univ = []

for line in lines_univ:
    line = line.split()
    tags_ptb.append(line[0])
    tags_univ.append(line[1])


# REMPLACEMENT DES ETIQUETTES DES FICHIERS ET ECRITURE VERS LES FICHIERS DE SORTIE
lines_error = []
for l in lines_in:
    try:
        element, tag = l.split()
        fw.write(element + '\t' + tags_univ[tags_ptb.index(tag)] + '\n')
    except :
        lines_error.append(l.replace('\n', ''))
fw.close()

if (len(lines_error) > 0):
    print("\nLes lignes suivantes n ont pas pu etre traitees :")
    for l in lines_error:
        print(l)