import random as r

def bernouilli(p):

    if r.random() > p :
        return 0
        
    return 1

print( bernouilli(.5) )