import sys
import re

assert(len(sys.argv) == 3)

path_in_nltk = sys.argv[1]
path_in_ref = sys.argv[2]


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

print('Nom de notre fichier en entree :', 		 path_in_nltk) # data/wsj_0010_sample.txt.pos.nltk
print('Nom du fichier de reference en entree :', path_in_ref)  # data/wsj_0010_sample.pos.ref


# OUVERTURE / CREATION DES FICHIERS DE SORTIE
path_out_nltk = path_in_nltk[0:id_type_nltk] + '_corrected.txt.pos.nltk'
path_out_ref  = path_in_ref[0:id_type_ref]   + '_corrected.pos.ref'

f_nltk = open(path_out_nltk, 'w')
f_ref  = open(path_out_ref,  'w')

print('Nom de notre fichier en sortie :', 		 path_out_nltk)
print('Nom du fichier de reference en sortie :', path_out_ref)


# ANALYSE ET MISE A JOUR VERS LES FICHIERS DE SORTIE
nb_lines_ntlk = len(lines_nltk)
nb_lines_ref  = len(lines_ref)

i = 0
j = 0
while(i < nb_lines_ntlk and j < nb_lines_ref):
	if (lines_nltk[i].strip() != ""):
		if (lines_ref[j].strip() != ""):
			if (lines_nltk[i].split()[0] == lines_ref[j].split()[0]):
				f_nltk.write(lines_nltk[i])
				f_ref.write(lines_ref[j])
			i += 1
			j += 1
		else:
			j += 1
	else:
		i += 1

f_nltk.close()
f_ref.close()