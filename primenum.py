__author__ = 'devnull'

import random

def randomPrime():

    values = (5,      7,     11,     13,     17,     19,     23,     29,
         31,     37,     41,     43,     47,     53,     59,     61)


    return random.choice(values)


def getTwoRandomPrimes():

    primeOne = randomPrime()
    primeTwo = primeOne

    while primeOne == primeTwo:
        primeTwo = randomPrime()
        pass

    return (primeOne, primeTwo)
