import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tree import Tree
import re
import sys

nltk.download('state_union')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# VERIFICATION DES TYPES DES FICHIERS
assert(len(sys.argv) == 2)
path_in = sys.argv[1]
# ATTENTION, il faut le nom complet du path comme par exemple :
# C:\Users\user\Desktop\TAL\RepoGit\ET5_TAL\Projet\data\ne_test.txt
# Ce chemin sera donc different pour vous.

path_out = path_in + '.ne.nltk'
x = re.search("\.txt$", path_in)
if not x:
    raise ValueError("Le parametre d'entree n'est pas un .txt")

print('Nom du fichier texte en entree :', path_in) # C:\Users\user\Desktop\TAL\RepoGit\ET5_TAL\Projet\data\ne_test.txt
print('Nom du fichier de sortie :', path_out) # C:\Users\user\Desktop\TAL\RepoGit\ET5_TAL\Projet\data\ne_test.txt.ne.nltk


train_text = state_union.raw("2005-GWBush.txt")
#sample_text = state_union.raw("2006-GWBush.txt")
sample_text = state_union.raw(path_in)

f = open(path_out, "w")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)


def traitement(namedEnt):
    for line in namedEnt:
        if type(line)==Tree: # only a nltk.tree.Tree is relevant
            line_words = ""
            for i in range(0,len(line)):
                line_words += line[i][0]
                if i!=(len(line)-1):
                    line_words += " "
            f.write(line_words + "\t" + conversion(line.label()) + "\n")
        else:
            f.write(line[0] + "\t" + "O" + "\n")

def conversion(label):
    org = ["ORGANIZATION", "FACILITY"]
    pers = ["PERSON"]
    loc = ["LOCATION", "GPE", "GSP"]
    misc = ["DATE", "TIME", "MONEY", "PERCENT"] # Remarque : NLTK et STANFORD ne trouveront jamais des MISC...

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

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=False)
            traitement(namedEnt)
            #namedEnt.draw()
    except Exception as e:
        print(str(e))


process_content()
f.close()
