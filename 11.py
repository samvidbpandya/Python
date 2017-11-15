__author__ = 'Bryan Cairns'

# Classes Continued

class Animal(object):
    name = "Not Named" # Static

    def __init__(self):
        print("Animal Constructed")

class Reptile(Animal):
    hasScales = True # Static

    def __init__(self):
        super(Reptile,self).__init__() # Must init the super
        print("Reptile Constructed")

class Mammal(Animal):
    hasHair = True # Static

    def __init__(self):
        super(Mammal,self).__init__() # Must init the super
        self.hasBackBone = True
        print("Mammal Constructed")

class Dragon(Reptile,Mammal):
    hasWings = True # Static

    def __init__(self,dragonage = 50):
        super(Dragon,self).__init__() # Must init the super
        self.age = dragonage
        print("Dragon Constructed and is %d years old" % self.age)

    def __del__(self):
        print(self.__class__.__name__ + " destroyed")

print("Start")

myDragon1 = Dragon(100)
myDragon1.name = "Sam"

myDragon2 = Dragon()
myDragon2.name = "Smog"

print("Hair = %s" % myDragon1.hasHair)
print("BackBone = %s" % myDragon1.hasBackBone)
print("%s is %d years old" % (myDragon1.name, myDragon1.age))


print("Finished")
