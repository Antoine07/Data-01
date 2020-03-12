import math

students = [5,5,4,6,2]
notes = [9,13,14,17,18]

# somme la liste students, effectif total
N = sum(students)

# calculer la moyenne des salaires
average = 0
for i in range(5):
    # cumuler les effectifs salaires
    average =  average + students[i]*notes[i]

# afficher la moyenne
average = average/N
print(round(average,2))

# calculer la variance et l'écart type

variance = 0
for i in range(5):
    # cumuler les effectifs salaires
    variance = variance + students[i]*(notes[i] - average)**2

# variance
variance = variance/N
print(variance)

# écart type
print(math.sqrt(variance))


# calcul de la médiane
if N % 2 == 0 :
    mediane = N / 2
else:
    mediane = (N+1) / 2

print(mediane)

sum = 0
for i, e in enumerate(students):
    sum = sum + e
    if sum >= mediane:
        print(notes[i])
        break
    