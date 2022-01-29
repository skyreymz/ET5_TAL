import sys
import re

assert(len(sys.argv) == 4)

path_in_nltk = sys.argv[1]
path_in_ref  = sys.argv[2]
path_univ    = sys.argv[3] # Table de correspondance

# VERIFICATION DES TYPES DES FICHIERS
#assert(bool(re.search("nltk$", path1)) ^ bool(re.search("nltk$", path2)))
#assert(bool(re.search("ref$", path1))  ^ bool(re.search("ref$", path2)))

id_type_nltk = path_in_nltk.find('.txt.pos.nltk')
id_type_ref = path_in_ref.find('.pos.ref')
assert(id_type_nltk != -1)
assert(path_in_ref != -1)


# OUVERTURE ET LECTURE DES FICHIERS D ENTREE
lines_nltk = []
with open(path_in_nltk, 'r') as f:
    lines_nltk = f.readlines()

lines_ref = []
with open(path_in_ref, 'r') as f:
    lines_ref = f.readlines()

lines_univ = []
with open(path_univ) as f:
    lines_univ = f.readlines()    

print('Nom de notre fichier en entree :', 		 path_in_nltk) # data/wsj_0010_sample.txt.pos.nltk
print('Nom du fichier de reference en entree :', path_in_ref)  # data/wsj_0010_sample.pos.ref
print('Nom de la table de correspondance :',	 path_univ)    # data/POSTags_PTB_Universal_Linux.txt


# OUVERTURE / CREATION DES FICHIERS DE SORTIE
path_out_nltk = path_in_nltk[0:id_type_nltk] + '_universal.txt.pos.nltk'
path_out_ref  = path_in_ref[0:id_type_ref]   + '_universal.pos.ref'

f_nltk = open(path_out_nltk, 'w')
f_ref  = open(path_out_ref,  'w')

print('Nom de notre fichier en sortie :', 		 path_out_nltk)
print('Nom du fichier de reference en sortie :', path_out_ref)


# ENREGISTREMENT DE LA TABLE DE CORRESPONDANCE DANS UN TABLEAU
tags_ptb = []
tags_univ = []

for line in lines_univ:
    line = line.split()
    tags_ptb.append(line[0])
    tags_univ.append(line[1])

# REMPLACEMENT DES ETIQUETTES DES FICHIERS ET ECRITURE VERS LES FICHIERS DE SORTIE
def replace_tags(lines, outfile):
	for l in lines:
		element, tag = l.split()
		outfile.write(element + '\t' + tags_univ[tags_ptb.index(tag)] + '\n')

replace_tags(lines_nltk, f_nltk)
replace_tags(lines_ref, f_ref)