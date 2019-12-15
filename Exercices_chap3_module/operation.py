#! /usr/bin/env python
"""
    module d'opérations mathématiques
"""

import math


def isEven (x):
    """
    Teste si un nombre est pair ou non

    :param x: un nombre entier
    :type x: int
    :return: Le résultat du test
    :rtype: bool

    :Example:

    >>> isEven(6)
    True
    """
    return x % 2 == 0

def isOdd (x):
    """
    Teste si un nombre est impair ou non

    La fonction isOdd est définie comme la négation de isEven

   :param x: un nombre entier
    :type x: int
    :return: Le résultat du test
    :rtype: bool

    :Example:

    >>> isOdd(75)
    True
    """
     return not isEven(x)

def isMultiple(x, y):
    """
    Teste si un nombre est multiple d'un autre nombre

    La fonction utilise la fonction gcd du module math.
    Celle-ci calcule le PGCD des deux nombres.

   :param x: un nombre entier
    :type x: int
   :param y: un nombre entier
    :type y: int
    :return: Le résultat du test
    :rtype: bool

    :Example:

    >>> isMultiple(18, 3)
    True
    """
    return math.gcd(x, y) == y

def isALetterCode(x):
    """
     Teste si un nombre correspond au code ASCII d'une lettre

    :param x: un nombre entier
     :type x: int
     :return: Le résultat du test
     :rtype: bool

     :Example:

     >>> isALetterCode(112)
     True
     """
    return (x >= 65 and x <= 90) or (w >= 97 and x <= 122)
