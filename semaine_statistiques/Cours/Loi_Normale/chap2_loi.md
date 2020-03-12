# Loi de Probabilité

## Loi de Bernoulli & Binomiale

La loi de Bernoulli en probabilité est une loi de probabilité discrète. Qui prend la valeur 1 avec la probabilité p et 0 avec la probabilité 1 - p. C'est une loi de probabilité qui n'a que deux issues possibles. Par exemple si on lance une pièce de monaie alors il n'y a que deux issues possibles : Pile ou Face. La probabilité d'obtenir Pile est 1/2 et Face 1/2, si la pièce est parfaitement équilibrée.

## Exercice d'application

Créez en Python la fonction de la loi de bernouilli.

```python
import random as r

def bernoulli(p):
    pass

```

## Expérience aléatoire

Si on prend l'expérience suivante : on lance successivement 10 fois une pièce de monnaie parfaitement équilibrée. Quelle est la probabilité d'obtenir 3 piles sur ces 10 lancers ?

L'événement élémentaire ici n'a que deux issues possibles : pile ou face. Comme la pièce est équilibrée on a autant de chance d'obtenir pile que face, donc la probabilité p est p = 0.5 et la probabilité de l'événement contraire est q = p - 1 = 0.5. Cet expérence est donc un expérience de Bernoulli (deux issues possibles).

Un événement possible est : **P**F**PP**FFFFFF, mais il y en a beaucoup d'autres ... Rappelons que le calcul de la probabilité est le rapport du nombre de cas favorables sur le nombre de cas possibles.

Il faut remarquer pour la suite que les événements sont indépendants entre eux.

Si on cherche à calculer la probabilité suivante : avoir 3 piles au trois premiers lancers et que des faces pour le reste des 10 lancers alors la probabilité recherchée est :

$p^3\times(1-p)^7$

Mais dans notre expérience nous n'avons pas la notion d'ordre.

Il nous reste donc à compter combien de combinaison de 3 piles possibles parmi 10 lancers nous avons. Ce problème est un problème de dénombrement connu. Nous donnons ci-dessous la formule combinatoire pour compter le nombre de combinaisons possibles :

${n\choose k} = \frac{n!}{k!\times(n-k)!} = \frac{n\times(n-1) ... \times 1}{k\times(k-1) ...\times1 \times (n-k)\times(n-k+1) ... \times1}$

Où **n** est dans notre cas le nombre de lancers et **k** le nombre de succès, obtenir un pile.

On a donc :

$\frac{10!}{3!\times7!} = \frac{10 \times ...\times 8 \times 7!}{3!\times7!}=\frac{10\times9\times8}{3\times2\times1} = \frac{10\times3\times4}{1}= 120$

Pour obtenir la probabilité recherché on appliquera la formule générale suivante :

${n\choose k} \times p^k \times(1-q)^{n-k}$

## Exercice d'application Binomiale

1. Créez une fonction **experience(n,p)** qui permet de simuler un lancer à l'aide de la fonction bernoulli.

2. On répète un grand nombre de fois cette expérience, comptez alors le nombre de fois que l'on obtient une combinaison de 3 piles parmi 10 lancers :

```python
experience(n,p) == 3
```

3. Donnez la probabilité recherchée.

4. Utilisez maintenant la méthode binomial de numpy elle renvoie une valeur représentant une réalisation de la loi binomiale. Il s'agit donc du nombre de succès à l'issue de n tentatives avec une probabilité p de succès à chaque fois. Il existe un troisième paramètre facultatif ici N dans l'exemple ci-dessous, permettant de générer un tableau de taille N. Cela permet de générer autant de valeurs que nécessaire. En utilisant cette méthode calculez la probabilité de la question 2.

```python
import numpy as np
n, p  N = 10, 0.5, 1000

np.random.binomial(n,p,N)
```

5. Tracez maintenant un histogramme pour les valeurs de n suivantes n = 2, 3, 4, 10, 100, 1000 avec une pièce truquée ayant comme probabilité p = 0.7 de tomber sur la pile. Utilisez seaborn et la méthode distplot, mettez le paramètre kde à True pour que seaborn trace une fonction d'interpollation sur le graphe. Que constatez-vous ?

## Loi Normale

Lorsque le paramètre n augmente, dans l'expérience de la loi Binomiale, l'asymétrie de la loi est contrariée, **elle a une forme en cloche.**

![loi binomiale](images/loi_normale_01.png)

\newpage

C'est le mathématicien français de Moivre qui découvrit que la loi Binomiale avait une forme Normale lorsque n était assez grand et ceci quelque soit la probabilité p.

Mais, ce qui es plus générale est en fait le théorème suivant, dit centrale limite :

"Des données qui dépendent de nombreux petits effets aléatoires indépendants sont approximativement distribués de manière Normale".

Ceci explique pourquoi on trouve la loi Normale partout : fluctuation des marchés financiers, moyennes des températures sur une année, maladies, etc.

La loi Normale est une loi de probabilité dite de densité, son intégrale de -infiny à +infiny vaut 1. **Et toute probabilité est une portion de l'aire de la loi Normale inférieur à 1.**

## Cas où X suit une loi Normale

- Soit X une variable aléatoire. Alors X suivra une loi Normale si :

* X suit l'influence d'un grand nombre de facteurs.

* Lorsque ces facteurs influençant cette variable sont tous indépendants entre eux.

* Pris isolément ils contribuent très faiblement à faire varier la quantité X.

Alors X suit une loi Normale.

### Exemple de variable X suivant une loi Normale

Si on s'intéresse par exemple au diamètre X (variable aléatoire) d'une pièce de voiture fabriquée par une machine. Alors la mesure de ces diamètres suit une loi Normale.

### Expérience mathématique

L'espérance de X est la valeur que l'on peut espérer obtenir, pour X, en moyenne, sur un grand nombre d'expériences. Elle est définie comme suit :

$E(X) = \sum_{0}^{n}X_i \times p_i$ où $p_i$ est la probabilité associée à la variable aléatoire $X_i$.

L'espérance mesure la moyenne d'obtenir un succès. Dans l'exemple précédent, des 10 lancers de pièce successifs, l'espérance mathématique mesure la moyenne d'obtenir un succès, **c'est-à-dire d'obtenir un pile**.

L'espérance mathématique d'une loi Binomiale est :

$E(X) = n \times p$

Cette propriété sera admise. Voir la partie démonstration à la fin ci cela vous intéresse.

### Présentation de la loi Normale

La loi normale est déterminée par deux paramètres : sa **moyenne** et son **écart-type**. Lorsque sa moyenne est égale à 0 et que son écart type est égale à 1 alors on dira qu'elle **est centrée réduite**.

Elle est définie par **la densité de probabilité** f suivante :

$f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\times (\frac{x - \mu}{\sigma})^2}$

La loi normale, dans la littérature, est notée : $\mathcal{N}(\mu,\,\sigma^{2})$

#### Représentation graphique

![loi binomiale](images/loi_normale_02.png)

\newpage

### Loi Normale centrée réduite

Une loi Normale ayant une moyenne différente de zéro et un écart-type quelconque peut être par changement de variable transformée en Loi Normale centrée réduite :

![loi binomiale](images/loi_normale_03.png)

\newpage

Preuve :

$Z = \frac{X-\mu}{\sigma}$ où $\mu$ et $\sigma$ sont respectivement la moyenne et l'écart type.

$E(Z) = \frac{E(X) -E(\mu)}{\sigma} = \frac{\mu - \mu}{\sigma} = 0$

On supposera admis la propriété sur la variance suivante :

$V(aX + b) = a^2 \times V(X)$

$V(X - \mu) = V(X)$

D'où :

$E(\frac{X-\mu}{\sigma}) = \frac{1}{\sigma^2} \times V(X- \mu) = \frac{V(X)}{\sigma^2}= \frac{\sigma^2}{\sigma^2}=1$

Dans ce cas la densité, centrée réduite, de probabilité est définie par :

$f(z)=\frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}\times z^2}$

## Règles des 3 sigmas

En statistique, la règle 68-95-99,7 indique que pour une loi Normale, presque toutes les valeurs se situent dans un intervalle centré autour de la moyenne.

- Environ 68,27% des valeurs se situent à moins de un écart-type de la moyenne.

- Environ 95,45% des valeurs se situent à moins de 2 écarts-types de la moyenne.

- Et la quasi-totalité 99,73% des valeurs se situent à moins de 3 écarts-types de la moyenne.

$P(\mu-\sigma \le x \le \mu+\sigma) \approx 0.6827$
$P(\mu-2\sigma \le x \le \mu+2\sigma) \approx 0.9545$
$P(\mu-3\sigma \le x \le \mu+3\sigma) \approx 0.6827$


![valeurs remarquables](images/regles_3_sigma.png)

\newpage

## Exercice lecture de la table

Trouvez les probabilités, de la variable aléatoire Z centrée réduite suivantes. Utilisez la table Normale centrée réduite ci-dessous :

- $P(Z \leq 2.53)$

- $P(Z \leq 0.56)$

- $P(Z \leq 1)$

## Centrer réduire

En pratique on a une table de valeurs pour la loi Normale centrée réduite. En connaissant la moyenne et l'écart type, d'une variable aléatoire X suivant une loi Normale, on peut passer de la loi Normale à la loi Normale réduite facilement par changement de variable :

$Z=\frac{X - \mu}{\sigma}$

Les tables donnent les probabilités pour la fonction de répartition suivante : $F(a) = P( X \leq a )$. $F(a)$ donne la probabilité que X soit inférieur ou égal au paramètre a.

## Exercice théorique & pratique

Soit X une variable aléatoire qui suit la loi Normale $\mathcal{N}(500,\,20^{2})$

- Calculez la probabilité : $P(X \leq 520)$

## Exercice poids dans une population

Exemple, soit les poids des Hommes, supposons que la moyenne des poids soit égale à 68 kg et que l'écart-type soit égale à 9. Alors quelle est la probabilité de peser plus de 70kg, on notera cette probabilité $P(X \geq 70)$.

Justifiez que le poids des Hommes suit une loi Normale.

Essayez en vous aidant d'une table Normale de calculer cette probabilité. Pensez à centrer réduire.

## Table Normale centrée réduite

![table normale](images/table_normale.png)
