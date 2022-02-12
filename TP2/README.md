# TP2

## I. Installation et évaluation de l’outil de désambiguïsation morphosyntaxique de l’université de Stanford

### I.1 Installation

#### Question I.1.d : Analyser le texte du fichier "sample-input.txt"
data/stanford/stanford-postagger-2018-10-16/sample-input.txt => data/stanford/stanford-postagger-2018-10-16/resultats/sample-input.txt.pos
```bash
cd data/stanford/stanford-postagger-2018-10-16
./stanford-postagger.sh models/english-left3words-distsim.tagger sample-input.txt > sample-input.txt.pos
```
Le fichier de résultat _sample-input.txt.pos_ se trouve dans le dossier _data/stanford/stanford-postagger-2018-10-16/resultats_


### I.2 Evaluation

#### Question I.2.a : Lancer le POS tagger sur le fichier « wsj_0010_sample.txt »
```bash
cd data/stanford/stanford-postagger-2018-10-16
./stanfordpostagger.sh models/english-left3words-distsim.tagger wsj_0010_sample.txt > wsj_0010_sample.txt.pos.stanford
```
Le fichier de résultat _wsj_0010_sample.txt.pos.stanford_ se trouve dans le dossier _/stanford/stanford-postagger-2018-10-16/resultats_

#### Question I.2.b : Ecrire un programme Python qui permet de convertir le fichier de référence _wsj_0010_sample.pos.ref_ au format de la sortie du Stanford POS tagger
data/wsj_0010_sample.pos.ref => data/wsj_0010_sample.pos.stanford.ref
```bash
python qI_2_b data/wsj_0010_sample.pos.ref
```

#### Question I.2.c : Calculer la précision de ce POS tagger en utilisant les étiquettes PTB
Faire l'évaluation :
```bash
python evaluate.py data/stanford/stanford-postagger-2018-10-16/resultats/wsj_0010_sample.txt.pos.stanford data/wsj_0010_sample.pos.stanford.ref
```
Résultats :
- Word precision: 0.990909090909091
- Word recall: 0.990909090909091
- Tag precision: 0.9727272727272728
- Tag recall: 0.9727272727272728
- Word F-measure: 0.990909090909091
- Tag F-measure: 0.9727272727272728

#### Question I.2.d : Remplacer à l’aide d’un programme Python les étiquettes Penn TreeBank des fichiers par les étiquettes universelles en utilisant la table de correspondance « POSTags_PTB_Universal.txt »
data/stanford/stanford-postagger-2018-10-16/resultats/wsj_0010_sample.txt.pos.stanford et data/wsj_0010_sample.pos.stanford.ref POSTags_PTB_Universal.txt => data/stanford/stanford-postagger-2018-10-16/resultats/wsj_0010_sample.txt.pos.univ.stanford data/wsj_0010_sample.pos.univ.stanford.ref
```bash
python qI_2_d.py data/stanford/stanford-postagger-2018-10-16/resultats/wsj_0010_sample.txt.pos.stanford data/wsj_0010_sample.pos.stanford.ref data/POSTags_PTB_Universal.txt
```

#### Question I.2.e : Calculer la précision de ce POS tagger en utilisant les étiquettes universelles
```bash
python evaluate.py data/stanford/stanford-postagger-2018-10-16/resultats/wsj_0010_sample.txt.pos.univ.stanford data/wsj_0010_sample.pos.univ.stanford.ref
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


## II. Installation et utilisation de l’outil de reconnaissance d’entités nommées
de l’université de Stanford

### II.1 Installation

#### Question II.1.j : Analyser le texte du fichier "sample-input.txt"
Ne pas oublier de placer le fichier _sample-input.txt_ dans le bon répertoire !
sample-input.txt => data/stanford/stanford-ner-2018-10-16/resultats/sample-input.txt.output
```bash
cd data/stanford/stanford-ner-2018-10-16
java -mx600m -cp stanford-ner.jar:lib/* edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier classifiers/english.all.3class.distsim.crf.ser.gz -textFile sample-input.txt > sample-input.txt.output
```
Le fichier de résultat _sample-input.txt.output_ se trouve dans le dossier _data/stanford/stanford-ner-2018-10-16/resultats_


### II.2 Extraction d'entités nommées

#### Question II.2.a : Lancer l'extracteur d'entités nommées sur le fichier "formal-tst.NE.key.04oct95_small.txt"
Ne pas oublier de placer le fichier _formal-tst.NE.key.04oct95_small.txt_ dans le bon répertoire !
```bash
cd data/stanford/stanford-ner-2018-10-16
java -mx600m -cp stanford-ner.jar:lib/* edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier classifiers/english.all.3class.distsim.crf.ser.gz -textFile formal-tst.NE.key.04oct95_small.txt > formal-tst.NE.key.04oct95_small.txt.ne.stanford
```
Le fichier de résultat _formal-tst.NE.key.04oct95_small.txt.ne.stanford_ se trouve dans le dossier _data/stanford/stanford-ner-2018-10-16/resultats_

