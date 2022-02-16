# PROJET de Traitement Automatique des Langues

# Sujet 1 : Evaluation de deux palteformes open source d'analyse linguistique

## I. Evaluation de l’analyse morpho-syntaxique

### Question I.1 : Utiliser le corpus annoté "pos_reference.txt.lima" pour extraire les phrases ayant servi pour produire ce corpus annoté et sauvegarder le résultat dans le fichier "pos_test.txt"
<u>Entrée :</u> data/pos_reference.txt.lima
<u>Sortie :</u> data/pos_test.txt
```bash
python qI_1.py data/pos_reference.txt.lima
```


### Question I.2 : Convertir les tags du corpus annoté "pos_reference.txt.lima" en tags universels et sauvegarder le résultat dans le fichier "pos_reference.txt.univ"
<u>Entrées :</u> data/pos_reference.txt.lima et data/POSTags_LIMA_PTB_Linux.txt et data/POSTags_PTB_Universal_Linux.txt
<u>Sortie :</u> data/pos_reference.txt.univ
```bash
python qI_2.py data/pos_reference.txt.lima data/POSTags_LIMA_PTB_Linux.txt data/POSTags_PTB_Universal_Linux.txt
```


### Question I.3 : Lancer les deux POS taggers sur le fichier "pos_test.txt"
#### POS tagger de Stanford
<u>Entrée :</u> data/pos_test.txt
<u>Sortie :</u> data/stanford/stanford-postagger-2018-10-16/resultats/pos_test.stanford
```bash
cd data/stanford/stanford-postagger-2018-10-16
./stanfordpostagger.sh models/english-left3words-distsim.tagger ../../pos_test.txt > resultats/pos_test.txt.pos.stanford
```
Le fichier de resultat _pos_test.txt.pos.stanford_ se trouve dans le dossier _data/stanford/stanford-postagger-2018-10-16/resultats_

On met le fichier _pos_test.txt.pos.stanford_ sous le même format que le corpus anoté _pos_reference.txt.lima_ (2 colonnes séparées par une tabulation) grace au script suivant :
<u>Entrée :</u> data/stanford/stanford-postagger-2018-10-16/resultats/pos_test.txt.pos.stanford
<u>Sortie :</u> data/pos_test.txt.pos.stanford
```bash
python qI_3.py data/stanford/stanford-postagger-2018-10-16/resultats/pos_test.txt.pos.stanford data/pos_test.txt.pos.stanford
```

#### POS tagger avec NLTK
Pour cette question, on réutilise le script du TP1 : q1_1_TP1.py
<u>Entrée :</u> data/pos_test.txt
<u>Sortie :</u> data/pos_test.txt.pos.nltk
```bash
python q1_1_TP1.py data/pos_test.txt
```


### Question I.4 : Convertir les résultats des deux POS taggers en utilisant les étiquettes universelles (Annexe 1)
Pour cette question, on réutilise le script du TP1 : q1_3_TP1.py

<u>Entrées :</u> data/pos_test.txt.pos.stanford et data/POSTags_PTB_Universal_Linux.txt
<u>Sortie :</u> data/pos_test.txt.pos.stanford.univ
```bash
python q1_3_TP1.py data/pos_test.txt.pos.stanford data/POSTags_PTB_Universal_Linux.txt
```

<u>Entrées :</u> data/pos_test.txt.pos.nltk et data/POSTags_PTB_Universal_Linux.txt
<u>Sortie :</u> data/pos_test.txt.pos.nltk.univ
```bash
python q1_3_TP1.py data/pos_test.txt.pos.nltk data/POSTags_PTB_Universal_Linux.txt
```


### Question I.5 : Calculer la précision de ce POS tagger en utilisant les étiquettes universelles

<u>Entrées :</u> data/pos_test.txt.pos.stanford.univ et data/pos_reference.txt.univ
```bash
python evaluate.py data/pos_test.txt.pos.stanford.univ data/pos_reference.txt.univ
```

<u>Entrées :</u> data/pos_test.txt.pos.nltk.univ et data/pos_reference.txt.univ
```bash
python evaluate.py data/pos_test.txt.pos.nltk.univ data/pos_reference.txt.univ
```


## II. Evaluation de la reconnaissance d’entités nommées 