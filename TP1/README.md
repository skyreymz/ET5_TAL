# TP1

## Pré-requis

### Installer NLTK et numpy
```bash
pip install --user -U NLTK
pip install --user -U numpy
```

### Télécharger averaged_perceptron_tagger et punkt
```bash
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
```


## Question 1. Evaluation de l’analyse morpho-syntaxique de la plateforme NLTK

### Question 1.1 : Désambiguïsation morpho-syntaxique
data/wsj_0010_sample.txt => data/wsj_0010_sample.txt.pos.nltk
```bash
python q1_1.py data/wsj_0010_sample.txt
```


### Question 1.2 : Evaluation à l'aide des étiquettes Penn TreeBank (PTB)
data/wsj_0010_sample.txt.pos.nltk et data/wsj_0010_sample.pos.ref => data/wsj_0010_sample_corrected.txt.pos.nltk et data/wsj_0010_sample_corrected.pos.ref
```bash
python q1_2.py data/wsj_0010_sample.txt.pos.nltk data/wsj_0010_sample.pos.ref
```

Faire l'évaluation :
```bash
python evaluate.py data/wsj_0010_sample_corrected.txt.pos.nltk data/wsj_0010_sample_corrected.pos.ref
```
Résultats :
- Word precision: 0.944954128440367
- Word recall: 0.944954128440367
- Tag precision: 0.944954128440367
- Tag recall: 0.944954128440367
- Word F-measure: 0.944954128440367
- Tag F-measure: 0.944954128440367


### Question 1.3 : Evaluation à l'aide des étiquettes universelles
data/wsj_0010_sample_corrected.txt.pos.nltk et data/wsj_0010_sample_corrected.pos.ref => data/wsj_0010_sample_corrected_universal.txt.pos.nltk et data/wsj_0010_sample_corrected_universal.pos.ref
```bash
python q1_3.py data/wsj_0010_sample_corrected.txt.pos.nltk data/wsj_0010_sample_corrected.pos.ref data/POSTags_PTB_Universal_Linux.txt
```

Faire l'évaluation :
```bash
python evaluate.py data/wsj_0010_sample_corrected_universal.txt.pos.nltk data/wsj_0010_sample_corrected_universal.pos.ref
```
Résultats :
- Word precision: 0.963302752293578
- Word recall: 0.963302752293578
- Tag precision: 0.963302752293578
- Tag recall: 0.963302752293578
- Word F-measure: 0.963302752293578
- Tag F-measure: 0.963302752293578

Réponse à la question 1.3.c :
A partir des résultats des deux évaluations effectuées ci-dessus, nous pouvons voir que nous obtenons de meilleurs taux dans le cas où nous prenons des étiquettes universelles, ce qui est cohérent.


## Question 2 : Utilisation de la plateforme NLTK pour l'analyse syntaxique
Le fichier data/wsj_0010_sample.txt.grammar contient les structures syntaxiques desirees.
data/wsj_0010_sample.txt => data/wsj_0010_sample.txt.chk.nltk
```bash
python q2.py data/wsj_0010_sample.txt data/wsj_0010_sample.txt.grammar
```


## Question 3 : Utilisation de la plateforme NLTK pour l’extraction d’entités nommées

### Question 3.1
data/wsj_0010_sample.txt => data/wsj_0010_sample.txt.ne.nltk
REMARQUE IMPORTANTE: pour la commande bash suivante, il faut indiquer VOTRE chemin complet du fichier wsj_0010_sample.txt
```bash
python q3_1.py C:\Users\user\Desktop\TAL\RepoGit\ET5_TAL\TP1\data\wsj_0010_sample.txt
```

### Question 3.2 et 3.3
data/formal-tst.NE.key.04oct95_sample.txt => data/formal-tst.NE.key.04oct95_sample.txt.ne.nltk
REMARQUE IMPORTANTE: pour la commande bash suivante, il faut indiquer VOTRE chemin complet du fichier formal-tst.NE.key.04oct95_sample.txt
```bash
python q3_2et3.py C:\Users\user\Desktop\TAL\RepoGit\ET5_TAL\TP1\data\formal-tst.NE.key.04oct95_sample.txt
```


## Exemples et documentations
- https://www.guru99.com/pos-tagging-chunking-nltk.html
- https://www.nltk.org/_modules/nltk/tree.html
- https://www.nltk.org/howto/tree.html