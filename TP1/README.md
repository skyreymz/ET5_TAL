# TP1

## 1. Evaluation de l’analyse morpho-syntaxique de la plateforme NLTK

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


### Question 1.3 : Evaluation à l'aide des étiquettes universelles
data/wsj_0010_sample_corrected.txt.pos.nltk et data/wsj_0010_sample_corrected.pos.ref => data/wsj_0010_sample_corrected_universal.txt.pos.nltk et data/wsj_0010_sample_corrected_universal.pos.ref
```bash
python q1_3.py data/wsj_0010_sample_corrected.txt.pos.nltk data/wsj_0010_sample_corrected.pos.ref data/POSTags_PTB_Universal_Linux.txt
```

Faire l'évaluation :
```bash
python evaluate.py data/wsj_0010_sample_corrected_universal.txt.pos.nltk data/wsj_0010_sample_corrected_universal.pos.ref
```
