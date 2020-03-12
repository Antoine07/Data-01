## Corrections exercices fréquence

```python
import pandas as pd
students = pd.read_csv('./data/students.csv')
students.head()

```

On peut renommer les colonnes du dataframe :

```python
students = students.rename(columns={'Couleur des yeux': 'eye_color', 'Mention au Bac': 'mention'})
```

On regroupe maintenant par couleur des yeux :

```python
# Création d'un objet groupby les [[]]  permette d'avoir un nouveau DataFrame
df = students.groupby("eye_color")[['eye_color']].count()
# On renomme la colonne eye_color
df.columns = ['Effectif']
```

Création d'une nouvelle colonne pour la fréquence :

```python
df['frequence'] = df/df.sum()
df['pourcentage'] = df['frequence'] * 100
df = df.round(2)
```

Puis on représente le Dataframe en diagramme en secteur. Pour finir définissez une variable colors et précisez chacune des couleurs.

```python
%matplotlib notebook
import matplotlib.pyplot as plt
plt.pie(df['Effectif'].values, labels=df.index.values,
        autopct='%1.1f%%')

plt.axis('equal')

plt.savefig('eye_color.png')
plt.show()
```

## Exercice Quartile notes

 Soit la série suivantes : 10; 25; 30; 40; 41; 42; 50; 55; 70; 101; 110; 111

 On a 12 valeurs ordonnées.

 1. Déterminez le troisième quartile.

  12*0.75 = 9, donc 70.

 2. La médiane.

 Comme la longueur de la série statistique est pair on prend la valeur moyenne suivante : $\frac{42 + 50}{2} = 46$ sixième et septième valeurs divisées par 2.

 3. L'intervalle interquartile.

 $Q_3 - Q_1 = 70 - 30$ le premier quartile est trouvé en faisant $0.25 \times 12$.

Même exercice avec la série statistique suivante, répondez aux 3 questions :

Soit la série suivantes : 10; 25; 30; 40; 41; 42; 50; 55; 70; 101; 110; 111, 208.

1. 

13*0.75 = 9.75 donc on prend la 10 valeur, donc 101.

2. 

La série est impair donc on prend la valeur dont la position dans la série est 13//2 = 6. Donc 50.

3.

$Q_3 - Q_1 = 101 - 40 = 61$

13*0.25 = 3.25 donc pour $Q_1 = 40$.

## Exercice calcul de la variance

Script permettant de calculer la variance

```python
import numpy as np

s = np.array( [7, 9, 11, 12, 13, 15])
m = s.mean()

var = np.sum( (a - a.mean())**2) / len(a)

```

2. Soit le tableau de notes d'une classe suivant :

| Note             |     Effectif             |
| -------------    |  ----------------------: |
| 7                |        5                 |
| 9                |        4                 |
| 11               |        21                |
| 12               |        35                |
| 13               |        32                |
| 15               |        3                 |

2.1 Calculez la moyenne des notes de cette classe.

```python
notes = np.array([7,9,11, 12, 13, 15])
effectifs = np.array( [5, 4, 21, 35, 32, 3])

neff = notes * effectifs

m = np.sum(neff) / np.sum(effectifs)
# 11.83

```

2.2 Déterminez la médiane

```python

def median(l):
        ln = len(l)
        if len(l) % 2 == 0:
                return (l[ln//2] + l[ln//2 + 1])/2

        return l[ln//2]

# On crée un tableau avec toutes les valeurs notes
ser = []
for i, note in enumerate(notes):
        ser = ser + [note] * effectifs[i]

# 12
print( median(ser) )
```

2.3 Déterminez la variance

```python
import numpy as np

ser = np.array(ser)
# var = 2.64
var = np.sum( (ser - ser.mean())**2) / len(ser)
```

2.4 On définit l'écart type comme étant la racine de la variance. Calculez l'écart type des notes de cette classe.

```python
import maths as m

# std = 1.78
std = m.sqrt(var)
```

Augmentation de 1 point

La moyenne change + 1

```python

notes = np.array([7,9,11, 12, 13, 15]) + 1
effectifs = np.array( [5, 4, 21, 35, 32, 3])

neff = notes * effectifs

m = np.sum(neff) / np.sum(effectifs)

```

La médiane + 1

La variance et l'écart type change faiblement. Mesure de dispertion.
