def cube(n):
    return n**3


def triarea(base,height):
    return base * height 

def sqrt(n):
    return n**0.5


import unittest

class Testing(unittest.TestCase):
    
    def test_cube(self):
        self.assertEqual( cube(2), 8)
        self.assertEqual( cube(4), 64)
        self.assertEqual( cube(8), 512)
        self.assertEqual( cube(7), 343)
        self.assertEqual( cube(6), 216)
        self.assertEqual( cube(9), 729)
        self.assertEqual( cube(11), 1331)
        self.assertEqual( cube(1), 1)

    def test_triarea(self):
        self.assertEqual( triarea(2,2), 2 )
        self.assertEqual( triarea(10,2), 10 )
        self.assertEqual( triarea(5,6), 15 )
        self.assertEqual( triarea(7,8), 28 )
        self.assertEqual( triarea(10,6), 30 )
        self.assertEqual( triarea(20,25), 250 )
        self.assertEqual( triarea(200,20), 2000 )

    def test_sqrt(self):
        self.assertEqual( sqrt(9), 3 )
        self.assertEqual( sqrt(81), 9 )
        self.assertEqual( sqrt(64), 8 )
        self.assertEqual( sqrt(900), 30 )
        self.assertEqual( sqrt(729), 27 )
        self.assertEqual( sqrt(121), 11 )
        self.assertEqual( sqrt(169), 13 )
        self.assertEqual( sqrt(256), 16 )
        self.assertEqual( sqrt(576), 24 )
        self.assertEqual( sqrt(676), 26 )
    

unittest.main()
        
