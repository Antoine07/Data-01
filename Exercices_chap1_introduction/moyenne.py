#! /usr/bin/env python
"""
    Calculateur de moyenne
    ======================

    Ce programme admet un nombre arbitraire d'arguments.
    Il affiche la moyenne de toutes les valeurs.
 """

from argparse import ArgumentParser
from statistics import mean

parser = ArgumentParser()
parser.add_argument(dest="nombres", type=int, nargs='*', help="entier")
input_args = parser.parse_args()

nombres = input_args.nombres

print(nombres)
resultat = mean(nombres)
print("La moyenne de la série de nombres est : {}".format(resultat))