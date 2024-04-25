'''
Write a Python function, sscount0,

Author: Elias C
Title: sscount
Credit: viet
'''

import doctest

def sscount0(needle, haystack):
    '''
    
    (needle: str, haystack: str) -> int
    Counts the number of times that a su
    
    >>> sscount0('ss','assesses')
    2
    >>> sscount0('!!', '!!!!!!')
    5
    >>> sscount0('aa', 'aabbaaaa')
    4

    
    '''
    ctr = 0

    n = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i+n] == needle:
            ctr += 1

    return ctr

print(doctest.testmod())