# Funzione che calcola la successione di fibonacci fino a n

__author__="matteo.ballarotto"
__version__="1.0.1"

def fibonacci (n):
    """Ritorna il fibonacci di n
    >>> fibonacci(3)
    2
    >>> fibonacci(8)
    21
    """

#Sono test eseguiti da testmod(), con verbose True mi mostra in maniera prolissa il test

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
