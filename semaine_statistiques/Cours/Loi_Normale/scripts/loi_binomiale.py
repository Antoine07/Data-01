import random as r
import numpy as np
import matplotlib.pyplot as plt

def bernouilli(p):

    if r.random() > p:
        return 0

    return 1

p, n, N = 0.7, 10, 2000

def experience(n, p):
    count = 0
    for _ in range(n):
        if bernouilli(p) == 1:
            count += 1

    return count

print(np.random.binomial(n,p, N))

count = 0
NB_SEARCH = 3
for _ in range(N):
    if experience(n, p) == NB_SEARCH:
        count += 1

print(count/N)
print( sum(np.random.binomial(n,p, N) == NB_SEARCH)/N )


plt.hist(np.random.binomial(n,p, N), bins=range(11))

plt.show()
