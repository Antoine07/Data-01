# Descriptive généralites

Une variable statistique est dite :

## Quantitative

- **quantitative** : lorsqu'elle est mesurée par un nombre (les Notes des Etudiants à l'Examen de Statistique, le Chiffre d'Affaire par PME, le Nombre d'Enfants par Ménage, . . . ).

On distingue 2 types de variables quantitatives :

- les variables quantitatives discrètes
- Les variables quantitatives continues.

Par exemple le nombre d'enfants par ménage ne peut être que 0, ou 1, ou 2, ou 3, . . .C'est une variable quantitative discrète.

Les variables **quantitatives continues** peuvent prendre toute valeur dans un intervalle. Par exemple, le chiffre d'affaire par PME, le temps d'attente à un arrêt de bus.

## Qualitative

Lorsque les modalités (ou les valeurs) qu'elle prend sont désignées par des noms. Par exemples, les modalités d'une variable Sexe peuvent être : Masculin et Féminin.

On distingue deux types de variables qualitatives : les variables qualitatives ordinales et les variables qualitatives nominales.

Plus précisément une variable qualitative est dite **ordinale**, lorsque ses modalités peuvent être classées dans un certain ordre naturel (c'est par exemple le cas d'une variable commen Mention au Bac).

Une variable qualitative est dite **nominale**, lorsque ses modalités ne peuvent être classées de façon naturelle (c'est par exemple le cas d'une variable comme Couleur des Yeux ou encore de la variable Sexe).

## Exercice fréquence

Récupérez le dataset dans student.csv, dans le dossier data et étudiez le critère couleur des yeux.

1. Créez un tableau avec une colonne supplémentaire des fréquences de la couleur des yeux. Arrondissez à deux décimales les valeurs. Quelle est le type de la variable "Couleur des yeux" ?

2. Créez à partir du tableau précédent un diagramme en secteur.

## Exercice notes en statistique

Récupérez le dataset note_statistiques.csv et faite un diagramme en baton des notes en statistiques.

Renommez la colonne Notes examen de statistiques en Notes.

1. Que constatez-vous pour ce diagramme ?

2. Quelle est le type de la variable notes ?

3. Faites maintenant des classes d'étendue de largeur 4 pour les notes et faites un diagramme en baton représentant les notes.

La classe modale est la classe dont la fréquence par unité d'amplitude est la plus élevée.

Cette classe correspond donc au rectangle le plus haut de l'histogramme des fréquences.

Trouvez la classe modale de notre dataset notes statistiques.


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
