import sys

assert(len(sys.argv) == 2)

path_in = sys.argv[1]

id_type = path_in.find('.pos.ref')

assert(id_type != -1)


# OUVERTURE DES FICHIERS
path_in = sys.argv[1]
path_out = path_in[:id_type] + '.pos.stanford.ref'

fr = open(path_in,  'r')
fw = open(path_out, 'w')

print('Nom du fichier d entree :',  path_in)  # data/wsj_0010_sample.pos.ref
print('Nom du fichier de sortie :', path_out) # data/wsj_0010_sample.pos.stanford.ref


# LECTURE DU FICHIER + TRAITEMENT
lines = fr.readlines()
fr.close()

# ECRITURE DANS LE FICHIER DE SORTIE
for l in lines:
	couple = l.split()
	if(len(couple) >= 2):
		fw.write(couple[0] + '_' + couple[1] + ' ')
	else:
		fw.write('\n')
fw.close()