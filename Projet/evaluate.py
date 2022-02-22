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
nb_lines_ref  = len(lines_ref)
nb_lines_pred = len(lines_pred)

TP = nb_lines_ref # le mot etiquette correctement par les experts (correspondant au nombre de mots en reference)
FP = 0 # le mot n a pas ete etiquette correctement
FN = 0 # le mot n a ete etiquette par aucune etiquette

def preprocessing(line):
	word,  tag  = line.split('\t')
	# On supprime les espaces ainsi que les sauts de ligne
	word  = word.replace(' ', '')
	tag   = tag.replace('\n', '')
	# On decide de remplacer les mots '' et `` par " pour eviter les potentielles erreurs
	word  = word.replace("''", '"')
	word  = word.replace("``", '"')
	return word, tag

error_counter = 0 # compteur d erreur

i_ref = 0  # identifiant des lignes du fichier de reference
i_pred = 0 # identifiant des lignes du fichier de reference
word_ref      = "" # mot analyse dans le fichier de reference
word_ref_tag  = "" # etiquette de word_ref
word_pred     = "" # mot analyse dans le fichier de prediciton
word_pred_tag = "" # etiquette de word_pred

long_word 	   = "" # mot ayant le plus de caractere entre le mot de reference et le mot de prediction
long_word_tag  = "" # etiquette de long_word
short_word 	   = "" # mot ayant le moins de caractere entre le mot de reference et le mot de prediction
short_word_tag = "" # etiquette de shor_word

word_type = 0 # entier permettant de connaitre le mot le plus grand (1 = ref ; 2 = pred)

while(i_ref < nb_lines_ref and i_pred < nb_lines_pred):
	#print('\nWord Type :', word_type)
	#print('Identifiants : ref :', i_ref, ' ; pred: ', i_pred)
	#print('Mots correspondant dans les fichiers :', lines_ref[i_ref].replace('\n',''), ' ; pred :', lines_pred[i_pred].replace('\n',''))
	if (word_type == 1):
		word_ref, word_ref_tag   = long_word, long_word_tag
		word_pred, tag_pred = preprocessing(lines_pred[i_pred])
		i_pred += 1
	elif (word_type == 2):
		word_ref, word_ref_tag   = preprocessing(lines_ref[i_ref])
		word_pred, tag_pred = long_word, long_word_tag
		i_ref += 1
	else:
		word_ref,  tag_ref  = preprocessing(lines_ref[i_ref])
		word_pred, tag_pred = preprocessing(lines_pred[i_pred])
		i_ref += 1
		i_pred += 1

	if (len(word_ref) > len(word_pred)):
		long_word, long_word_tag   = word_ref, tag_ref
		word_type = 1 # Le mot le plus long est la reference
		short_word, short_word_tag = word_pred, tag_pred
	else:
		long_word, long_word_tag   = word_pred, tag_pred
		short_word, short_word_tag = word_ref, tag_ref
		word_type = 2 # Le mot le plus long est la prediction ou les deux mots ont la meme taille

	#print('Mots analysés : ref = ', word_ref, " ; pred = ", word_pred)
	#print('Mots analysés : long = ', long_word, " ; short = ", short_word)

	if (long_word == short_word):
		if (long_word_tag != short_word_tag):
			FP += 1
		word_type = 0
	else: # long_word != short_word
		FN += 1
		try:
			assert(long_word.find(short_word) != -1)
			long_word = long_word.replace(short_word, '', 1)
		except:
			if(word_ref in ['{', '}', '(', ')']): # Ces caracteres ne sont pas conserves dans le fichier stanford
				FN += 1
				i_pred -=1
			elif ((long_word == '.') or (short_word == '.')): # Stanford rajoute parfois un "." a la fin d une phrase
				i_ref -= 1
			else: # Dans les autres cas, Stanford oublie de considerer un mot
				FN += 1
				i_pred -=1
			word_type = 0
			error_counter += 1
	
			print('Erreur au niveau de la ligne n°', i_ref, ' du fichier de reference et n°', i_pred, ' du fichier de predicition\n')
	#print('Mots mis à jour : ref = ', word_ref, " ; pred = ", word_pred)
	#print('Mots mis à jour : long = ', long_word, " ; short = ", short_word)

print(error_counter, " erreur(s) referencee(s)")


# RESULTATS
sys.stdout.write('\nPrecision = ')
sys.stdout.write(str(TP / (TP + FP)))
sys.stdout.write(' ( ')
sys.stdout.write(str(TP))
sys.stdout.write(' / ( ')
sys.stdout.write(str(TP))
sys.stdout.write(' + ')
sys.stdout.write(str(FP))
sys.stdout.write(' )')

print('')

sys.stdout.write('\nRappel = ')
sys.stdout.write(str(TP / (TP + FN)))
sys.stdout.write(' ( ')
sys.stdout.write(str(TP))
sys.stdout.write(' / ( ')
sys.stdout.write(str(TP))
sys.stdout.write(' + ')
sys.stdout.write(str(FN))
sys.stdout.write(' )\n')