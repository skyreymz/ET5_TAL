# TP2


## I. Installation et évaluation de l’outil de désambiguïsation morphosyntaxique de l’université de Stanford

### I.1 Installation

#### Question I.1.d : Analyser le texte du fichier "simple-input.txt"
Analyse du texte du fichier "simple-input.txt" :
data/wsj_0010_sample.txt => data/wsj_0010_sample.txt.pos.nltk
```bash
cd stanford/stanford-postagger-2018-10-16
./stanford-postagger.sh models/english-left3words-distsim.tagger sample-input.txt > sample-input.txt.pos
```
Le fichier de résultat _sample-input.txt.pos_ se trouve dans le dossier _/stanford/stanford-postagger-2018-10-16/resultats_


### I.2 Evaluation

#### Question I.2.a : Lancer le POS tagger sur le fichier « wsj_0010_sample.txt »
```bash
cd stanford/stanford-postagger-2018-10-16
./stanfordpostagger.sh models/english-left3words-distsim.tagger wsj_0010_sample.txt > wsj_0010_sample.txt.pos.stanford
```
Le fichier de résultat _wsj_0010_sample.txt.pos.stanford_ se trouve dans le dossier _/stanford/stanford-postagger-2018-10-16/resultats_

#### Question I.2.b : Ecrire un programme Python qui permet de convertir le fichier de référence _wsj_0010_sample.pos.ref_ au format de la sortie du Stanford POS tagger
wsj_0010_sample.pos.ref => wsj_0010_sample.pos.stanford.ref
```bash
python qI_2_b wsj_0010_sample.pos.ref
```

#### Question I.2.c : Calculer la précision de ce POS tagger en utilisant les étiquettes PTB
Faire l'évaluation :
```bash
python evaluate.py stanford/stanford-postagger-2018-10-16/resultats/wsj_0010_sample.txt.pos.stanford wsj_0010_sample.pos.stanford.ref
```
Résultats :
- Word precision: 0.990909090909091
- Word recall: 0.990909090909091
- Tag precision: 0.9727272727272728
- Tag recall: 0.9727272727272728
- Word F-measure: 0.990909090909091
- Tag F-measure: 0.9727272727272728

#### Question I.2.d : Remplacer à l’aide d’un programme Python les étiquettes Penn TreeBank des fichiers par les étiquettes universelles en utilisant la table de correspondance « POSTags_PTB_Universal.txt »
stanford/stanford-postagger-2018-10-16/resultats/wsj_0010_sample.txt.pos.stanford et wsj_0010_sample.pos.stanford.ref POSTags_PTB_Universal.txt => stanford/stanford-postagger-2018-10-16/resultats/wsj_0010_sample.txt.pos.univ.stanford wsj_0010_sample.pos.univ.stanford.ref
```bash
python qI_2_d.py stanford/stanford-postagger-2018-10-16/resultats/wsj_0010_sample.txt.pos.stanford wsj_0010_sample.pos.stanford.ref POSTags_PTB_Universal.txt
```

#### Question I.2.e : Calculer la précision de ce POS tagger en utilisant les étiquettes universelles
```bash
python evaluate.py stanford/stanford-postagger-2018-10-16/resultats/wsj_0010_sample.txt.pos.univ.stanford wsj_0010_sample.pos.univ.stanford.ref
```
Résultats :
- Word precision: 0.990909090909091
- Word recall: 0.990909090909091
- Tag precision: 0.9727272727272728
- Tag recall: 0.9727272727272728
- Word F-measure: 0.990909090909091
- Tag F-measure: 0.9727272727272728

#### Question I.2.f : Quelles conclusions peut-on avoir à partir de ces deux évaluations ? 
Nous nous attendions à ce que les résultats s'améliorent dans le cas où on prend les étiquettes universelles mais les résultats sont identiques.

En effet :
- le mot "manufacturing" (ligne 1) est considéré comme un nom (NOUN) par le POS tagger alors que dans la référence il est considéré comme un verbe (VERB)
- le mot "more" est considéré comme un adverbe (ADV) par le POS tagger alors que dans la référence il est considéré comme un adjectif (ADF)

Pour chacun de ces deux mots, le POS tagger détermine une étiquette trop éloignée de l'étiquette de référence. De ce fait, même en prenant les étiquettes universelles, on obtient également des étiquettes différentes. Il est donc cohérent que les résultats ne s'améliorent pas dans ce cas.