A = input("The value of A : 1) T 2) F \n")


B = input("The value of B : 1) T 2) F \n")

if( A == "T" and  B == "T"):

    print ("False")

elif(A == "T" and B == "F"):

    print ("True")

elif(A == "F" and B == "T"):

    print ("True")

elif(A == "F" and B == "F"):

    print ("False")

else:

    print ("Check value of A or B")


def XOR(A,B):
    return (A^B)

import unittest

class XORING(unittest.TestCase):

    def test_XOR(self):
        print("Test is ON")
        self.assertEqual( XOR(0,0), 0)
        self.assertEqual( XOR(0,1), 1)
        self.assertEqual( XOR(1,0), 1)
        self.assertEqual( XOR(1,1), 0)
        print("Oh What Hapiness you passed the test")
unittest.main()




    
    
