####################
# WORK IN PROGRESS #
####################

import sys
import re

assert(len(sys.argv) == 3)

path_in_pred = sys.argv[1]
path_in_ref  = sys.argv[2]


# VERIFICATION DES TYPES DES FICHIERS
assert(bool(re.search(".txt.pos.*.univ$", path_in_pred)))
assert(bool(re.search(".txt.univ$", 	  path_in_ref)))


# OUVERTURE ET LECTURE DES FICHIERS D ENTREE
lines_pred = []
with open(path_in_pred, 'r') as f:
    lines_pred = f.readlines()

lines_ref = []
with open(path_in_ref, 'r') as f:
    lines_ref = f.readlines()

print('Nom de notre fichier en entree :', 		 path_in_pred) # data/pos_test.txt.pos.stanford.univ data/pos_test.txt.pos.nltk.univ
print('Nom du fichier de reference en entree :', path_in_ref)  # data/pos_reference.txt.univ


# EVALUATION
def preprocessing1(line):
	word,  tag  = line.split('\t')
	word  = word.replace(' ', '')
	tag   = tag.replace('\n', '')
	# On decide de remplacer les mots '' et `` par " pour eviter les potentielles erreurs
	word  = word.replace("''", '"')
	word  = word.replace("``", '"')
	return word, tag

def preprocessing2(word):
	return (((word_ref.find('"') != -1) or (word_ref.find("'") != -1) or \
		     (word_ref.find("`") != -1) or (word_ref.find(".") != -1)    	 \
		    ) and (len(word_ref) <= 2))

nb_lines_ref  = len(lines_ref)
nb_lines_pred = len(lines_pred)

TP = nb_lines_ref # le mot etiquette correctement par les experts
FP = 0 # le mot n a pas ete etiquette correctement
FN = 0 # le mot na ete etiquette par aucune etiquette

i_ref = 0
i_pred = 0
while(i_ref < nb_lines_ref and i_pred < nb_lines_pred):
	word_ref,  tag_ref  = preprocessing1(lines_ref[i_ref])
	word_pred, tag_pred = preprocessing1(lines_pred[i_pred])

	if (word_ref == word_pred):
		if (tag_ref != tag_pred):
			FP += 1

	elif (preprocessing2(word_ref) and preprocessing2(word_pred)):
		FN += 1

	else: # word_ref != word_pred

		print('')
		print(i_ref, i_pred)
		print(word_ref, tag_ref)
		print(word_pred, tag_pred)

		if (len(word_ref) > len(word_pred)):
			FN += 1
			try:
				#assert(bool(re.search("^" + word_pred, word_ref)))
				assert(word_ref.find(word_pred) != -1)
			except:
				print(word_ref, word_pred)
				raise ValueError('oui')
			word_ref = word_ref.replace(word_pred, '', 1)

			while(word_ref != ""):
				i_pred += 1
				word_pred, _ = preprocessing1(lines_pred[i_pred])
				word_pred = word_pred.replace(' ', '')

				if(preprocessing2(word_pred)):
					break

				try:
					#assert(bool(re.search("^" + word_pred, word_ref)))
					assert(word_ref.find(word_pred) != -1)

				except:
					print(word_ref, tag_ref)
					print(word_pred, tag_pred)
					raise ValueError('oui')
				word_ref = word_ref.replace(word_pred, '', 1)

		elif (len(word_ref) < len(word_pred)):
			FN += 1
			try:
				assert(bool(re.search("^" + word_ref, word_pred)))
			except:
				print(word_ref, tag_ref)
				print(word_pred, tag_pred)
				raise ValueError('oui')
			word_pred = word_pred.replace(word_ref, '', 1)

			while(word_pred != ""):
				FN += 1
				i_ref += 1
				word_ref, _ = preprocessing1(lines_ref[i_ref])
				word_ref  = word_ref.replace(' ', '')

				if(preprocessing2(word_ref)):
					break

				assert(bool(re.search("^" + word_ref, word_pred)))
				word_pred = word_pred.replace(word_ref, '', 1)
		else: # Les deux mots ont la meme taille mais sont differents
			print(i_ref, i_pred)
			raise ValueError('Les deux mots ont la meme taille mais sont differents :', word_pred, word_ref)
	i_ref += 1
	i_pred += 1

# RESULTATS
sys.stdout.write('Precision = ')
sys.stdout.write(str(TP / (TP + FP)))
sys.stdout.write(' ( ')
sys.stdout.write(str(TP))
sys.stdout.write(' / ( ')
sys.stdout.write(str(TP))
sys.stdout.write(' + ')
sys.stdout.write(str(FP))
sys.stdout.write(' )')

print('')

sys.stdout.write('Rappel = ')
sys.stdout.write(str(TP / (TP + FN)))
sys.stdout.write(' ( ')
sys.stdout.write(str(TP))
sys.stdout.write(' / ( ')
sys.stdout.write(str(TP))
sys.stdout.write(' + ')
sys.stdout.write(str(FN))
sys.stdout.write(' )')