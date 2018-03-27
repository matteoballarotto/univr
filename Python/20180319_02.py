# Funzione che calcola il fattoriale

__author__="matteo.ballarotto"
__version__="1.0.1"

def factorial (n):
    """Ritorna il fattoriale di n
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """

#Sono test eseguiti da testmod(), con verbose True mi mostra in maniera prolissa il test
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
