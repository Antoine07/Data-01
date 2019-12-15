
from argparse import ArgumentParser

# Initialisation de l'analyseur syntaxique
parser = ArgumentParser()

# Description des valeurs attendues dans la ligne de commande
# on definit deux variables obligatoires
parser.add_argument(dest="temperature", type=float, help="Premier parametre temperature")
parser.add_argument(dest="unit", type=str, help="Second parametre unite")

# Analyse de la commande
input_args = parser.parse_args()

# print(input_args.temperature, input_args.unit)

FLAG_UNIT = input_args.unit
temperature = input_args.temperature

# logique métier 

def celsiusToFahren(celsius):
    tempfahren=celsius*1.8 + (32)

    return tempfahren

def fahrenCelsius(fahren):
    tempcelsius=(fahren - 32) * 5 / 9

    return tempcelsius

if FLAG_UNIT == 'celsius':
    print("la température fahrenheit de", temperature, "c", "est:", celsiusToFahren(temperature), "f")

if FLAG_UNIT == "fahrenheit":
    print ("la température celsius de", temperature, "f",  "est:",  fahrenCelsius(temperature), "c")

if FLAG_UNIT != "celsius" and FLAG_UNIT !="fahrenheit":
    print( "erreur: vous devez renseigner l'unité, uniquement celsius ou fahrenheit")