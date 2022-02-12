import sys

assert(len(sys.argv) == 4)

path_in_exp = sys.argv[1]
path_in_ref = sys.argv[2]
path_univ   = sys.argv[3] # Table de correspondance

id_type_exp = path_in_exp.find('.txt.pos.stanford')
id_type_ref = path_in_ref.find('.pos.stanford.ref')
assert(id_type_exp != -1)
assert(id_type_ref != -1)


# OUVERTURE ET LECTURE DES FICHIERS D ENTREE
lines_exp = []
with open(path_in_exp, 'r') as f:
    lines_exp = f.readlines()

lines_ref = []
with open(path_in_ref, 'r') as f:
    lines_ref = f.readlines()

lines_univ = []
with open(path_univ) as f:
    lines_univ = f.readlines()    

print('Nom de notre fichier en entree :', 		 path_in_exp) # wsj_0010_sample.txt.pos.stanford
print('Nom du fichier de reference en entree :', path_in_ref) # wsj_0010_sample.pos.stanford.ref
print('Nom de la table de correspondance :',	 path_univ)   # POSTags_PTB_Universal_Linux.txt


# OUVERTURE / CREATION DES FICHIERS DE SORTIE
path_out_exp = path_in_exp[0:id_type_exp] + '.txt.pos.univ.stanford '
path_out_ref = path_in_ref[0:id_type_ref] + '.pos.univ.stanford.ref'

f_exp = open(path_out_exp, 'w')
f_ref = open(path_out_ref,  'w')

print('Nom de notre fichier en sortie :', 		 path_out_exp)
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
        couples = l.split()
        for c in couples:
            element, tag = c.split('_')
            outfile.write(element + '_' + tags_univ[tags_ptb.index(tag)] + ' ')
        outfile.write('\n')

replace_tags(lines_exp, f_exp)
replace_tags(lines_ref, f_ref)