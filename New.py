#Create a List from the function
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

"""------------------------------"""
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]


# find number in 1000 to 5001 in which every digit in number can be divisible by 2
values = []
for i in range(1000, 5001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print (','.join(values))

## Chinese Puzzle ## Laugh Out Loud

print ("The Starting of Chinese Puzzle")
def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=50
numlegs=150
solutions=solve(numheads,numlegs)
print (solutions)

## Interview Kind of Question


