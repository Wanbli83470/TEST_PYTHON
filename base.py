import unittest

# Modèle 1 Basique :

def fun(x) :
    return x + 1
    
class Modeltest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
     
# Perso 1 Basique :

def perso(t="Python") :
    return t.lower()
    
class Mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(perso("Java"), "java")


# Modèle 2 : Doctest :
def carré(x):
    """Je commente mon test"
    >>> carré(2)
    4
    >>> carré(8)
    64
    """
    
    return x * x
    
# Perso 2 : Doctest :

def cube(y):
    """
    >>> cube(5)
    125
    >>> cube(10)
    1000
    """
    return y*y*y

def _doctest():
    import doctest
    doctest.testmod()
    
if __name__ == '__main__':
    _doctest()
    unittest.main()
