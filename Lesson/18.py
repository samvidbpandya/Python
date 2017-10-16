__author__ = 'Bryan Cairns'

#serialize object

import pickle

class person(object):
    name = ""
    age = 0

    def __int__(self, name = "unknown"):
        self.name = name

    def hello(self):
        print("Hello my name is %s" % self.name)

#test our object
p = person()
p.name = 'Bryan'
p.age = 40
p.hello()

strfile = r'/home/rootshell/Documents/test.txt'

with open(strfile, 'bw') as f:
    pickle.dump(p,f)

print("The pickle has landed")

with open(strfile, 'br') as f:
    o = pickle.load(f)

    print(o)

    #https://www.jetbrains.com/pycharm/help/type-hinting-in-pycharm.html
    if isinstance(o,person):
        print(o.hello())




