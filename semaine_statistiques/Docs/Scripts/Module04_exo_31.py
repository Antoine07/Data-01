import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,3,4,7,9,11,16,20,23,31]

plt.scatter(x,y)

plt.title('Nuage de points')
plt.plot([0, 10], [-4.39, 26.5]) # Droite D
plt.xlabel('x')
plt.ylabel('y')
plt.show()