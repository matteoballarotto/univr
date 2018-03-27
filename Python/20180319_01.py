# Funzione potenza senza operatore **

__author__="matteo.ballarotto"
__version__="1.0.1"

def powerof (base, exp):
    """Ritorna base elevato ad exp
    >>> powerof(2,5)
    32
    >>> powerof(3,4)
    81
    """

#Sono test eseguiti da testmod(), con verbose True mi mostra in maniera prolissa il test
    
    result = 1;


    for _ in range(exp):
        result *= base
    
    return result;

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
