#criptare e decriptare un testo shiftando le lettere


def encrypt (s, n):
    ''' Ritorna un testo criptato con caratteri shiftati di n
    >>> encrypt('aaa', 1)
    'bbb'
    >>> encrypt('ZAZbvd  s',2)
    'BCBdxf  u'
    '''
    
    res = ""
    for c in s:
        if ord(c) >= 65 and ord(c) <= 90:
            res += chr((((ord(c)-65) + n)%26)+65) #me lo porto tra 0 e 26, effettuo la modifica e lo riporto in ascii
        elif ord(c) >= 97 and ord(c) <= 122:
            res += chr((((ord(c)-97) + n)%26)+97)
        else:
            res += c
    return res



def decrypt (s, n):
    ''' Ritorna un testo decriptato con caratteri shiftati di n
    >>> decrypt('bbb', 1)
    'aaa'
    >>> decrypt('BCBdxf  u',2)
    'ZAZbvd  s'
    '''
    res = ""
    for c in s:
        if ord(c) >= 65 and ord(c) <= 90:
            res += chr((((ord(c)-65) - n)%26)+65)
        elif ord(c) >= 97 and ord(c) <= 122:
            res += chr((((ord(c)-97) - n)%26)+97)
        else:
            res += c
    
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
