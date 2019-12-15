"""
Correction de l'exercice somme des prix ttc
"""

# Définition d'une TVA

TVA = 0.2

def priceTTC(*prices):

    if len(prices) == 0:

        print("Attention vous devez donner des prix")

        return

    return sum(prices) * ( TVA + 1 )


total = priceTTC(12, 100, 50, 35)

print(f"votre total est {total}")
