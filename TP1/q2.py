import sys
import nltk

# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')

assert(len(sys.argv) == 3)


# VERIFICATION DES TYPES DES FICHIERS
path_in_text    = sys.argv[1]
path_in_grammar = sys.argv[2]
path_out        = path_in_text + '.chk.nltk'

assert(path_in_grammar.find('grammar') != 1)


# OUVERTURE DES FICHIERS
fr_text    = open(path_in_text,    'r')
fr_grammar = open(path_in_grammar, 'r')
fw         = open(path_out,        'w')

print('Nom du fichier texte en entree :',                   path_in_text)    # data/wsj_0010_sample.txt
print('Nom du fichier contenant la grammaire en entree :',  path_in_grammar) # data/wsj_0010_sample.txt.grammar
print('Nom du fichier de sortie :',                         path_out)        # data/swj_0010_sample.txt.chk.nltk


# LECTURE DU TEXTE ET DE LA GRAMMAIRE
lines = fr_text.readlines()
fr_text.close()

grammars = fr_grammar.readlines()
fr_grammar.close()


# TRAITEMENTS
def extract_compound_words(text, grammar, file):
    grammar_name = grammar[0:grammar.find(':')]
    
    for l in text:
        line_tokenized = nltk.word_tokenize(l) #line_tokenized = l.split()
        line_tagged = nltk.pos_tag(line_tokenized)
        cp = nltk.RegexpParser(grammar)
        tree = cp.parse(line_tagged)
        #print(tree)
        #print(tree.pretty_print())

        # ECRITURE DANS LE FICHIER DE SORTIE
        for subtree in tree.subtrees():
            if(subtree.label() == grammar_name):
                #print(subtree)
                file.write(grammar_name + ': ')
                
                # DISTINCTION ENTRE LE MOT ET SON ETIQUETTE
                for i in range(len(subtree)):
                    file.write(subtree[i][0] + '/' + subtree[i][1] + ' ')
                file.write('\n')

for g in grammars:
    extract_compound_words(lines, g.replace('\n', ''), fw)

fw.close()