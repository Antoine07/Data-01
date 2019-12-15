from argparse import ArgumentParser

# Initialisation de l'analyseur syntaxique
parser = ArgumentParser()
# Description des valeurs attendues dans la ligne de commande
parser.add_argument(dest="nombre_1", type=int, help="Premier nombre dividende")
parser.add_argument(dest="nombre_2", type=int, help="Second nombre est le diviseur")

# Analyse de la commande
input_args = parser.parse_args()

# print(input_args.nombre_1)

# print(input_args)

# Import des valeurs dans le programme
nombre_1 = input_args.nombre_1
nombre_2 = input_args.nombre_2

resultat = nombre_1 % nombre_2

if not ( bool(resultat) ) :
    print("Le nombre ", nombre_1, " est divisible par", nombre_2)

else:
    print("Le nombre ", nombre_1, " n'est pas divisible par", nombre_2)