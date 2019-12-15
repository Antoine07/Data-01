def permuteNumber(a, b, c):
    a, b, c = b, c, a
    # str permet de transformer un nombre en chaine de caractères
    # il faut le faire car sinon Python ne voudra pas concaténer a, b et c avec 
    # la chaine de caractères ci-dessous 
    return "a : " + str( a ) + " b : " + str( b ) + " c : " + str(c)
permuteNumber(1,2,3)
