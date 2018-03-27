# Funzione che calcola la successione di fibonacci fino a n

__author__="matteo.ballarotto"
__version__="1.0.1"

import math
import random

def pi (n):
    """Ritorna un'approssimazione di pigreco
    """
    
    ni = 0
    
    for _ in range (1,n+1):
        x = random.random()
        y = random.random()

        dist = math.sqrt(x*x + y*y) #distanza del punto dall'origine

        if dist < 1 :
            ni = ni +1

    
    return ni/n*4

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)

    print(pi(90000000))
