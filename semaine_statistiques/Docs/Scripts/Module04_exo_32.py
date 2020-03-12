import math

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,3,4,7,9,11,16,20,23,31]

average_x = sum(x)/10
average_y = sum(y)/10

print(average_x)
print(average_y)

# variance
variance_x = 0
for xi in x:
    # cumuler les effectifs salaires
    variance_x = variance_x + (xi - average_x)**2

variance_y = 0
for yi in y:
    # cumuler les effectifs salaires
    variance_y = variance_y + (yi - average_y)**2

# variances x et y
variance_x = round(variance_x/10,2)
variance_y = round(variance_y/10,2)

# variances
print(variance_x)
print(variance_y)

# covariance
covariance_xy = 0
for i in range(10):
    covariance_xy += x[i] * y[i]

covariance_xy = (covariance_xy)/10 - average_x*average_y

print(covariance_xy)

# coefficient directeur de D et ordonnée à l'origine de D
coeff_D = round(covariance_xy/variance_x,2)
print(coeff_D)

ordonnee_origine = round(average_y - coeff_D*average_x,2)
print(ordonnee_origine)




