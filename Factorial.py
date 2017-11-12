################################################

#Python program to find the factorial of a number.

num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

################################################

# Python program to display the Fibonacci sequence up to n-th term using recursive functions

def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


################################################

#NEW
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)


n = 10

################################################

#Sorting

y = [9,4,5,6,1]

for x in range(0, len(y)):

    for z in range(x+1, len(y)):
      if(y[x]>y[z]):
        temp = y[z]
        y[z] = y[x]
        y[x] = temp
print (y)

################################################

# find number in 1000 to 5001 in which every digit in number can be divisible by 2
values = []
for i in range(1000, 5001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print (','.join(values))

################################################

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

################################################

#Create a List from the function
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

################################################

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]

################################################
x="abcdefg"


for y in x:
        print (y)
    

################################################


x="abcdabcab"

y = {}
for i in range(0,len(x)):
    if (y.get(x[i])):
        y[x[i]]+=1
    else:
        y[x[i]] = 1
print(y)
        
################################################
        
x = "H1e2l3l4o5  w6o7r8l9d"

x = x[::2]
print (x)

################################################

import itertools
print (list(itertools.permutations([1,2,3])))

################################################


def pypart(n):
     
    
    for i in range(0, n):
     
         for j in range(0, i+1):
            print("* ",end="")

         print("\r")
n = int(input("Enter Value of n"))
pypart(n)

################################################

# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern
def pypart2(n):
     
    # number of spaces
    k = 2*n - 2
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 2
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ", end="")
     
        # ending line after each row
        print("\r")
 
# Driver Code
n = int(input("Enter Value of n"))
pypart2(n)

################################################

def numpat(n):
     
    # initialising starting number 
    num = 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # re assigning num
        num = 1
     
        # inner loop to handle number of columns
            # values changing acc. to outer loop
        for j in range(0, i+1):
         
                # printing number
            print(num, end=" ")
         
            # incrementing number at each column
            num = num + 1
     
        # ending line after each row
        print("\r")
 
# Driver code
n = int(input("Enter Value of n"))
numpat(n)


################################################

def numpat(n):
     
    # initialising starting number 
    num = 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        
     
        # inner loop to handle number of columns
            # values changing acc. to outer loop
        for j in range(0, i+1):
         
                # printing number
            print(num, end=" ")
         
            # incrementing number at each column
            num = num + 1
     
        # ending line after each row
        print("\r")
 
# Driver code
n = int(input("Enter Value of n"))
numpat(n)

################################################


def alphapat(n):
     
    # initializing value corresponding to 'A' 
    # ASCII value
    num = 65
 
    # outer loop to handle number of rows
    # 5 in this case
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # explicitely converting to char
            ch = chr(num)
         
            # printing char value 
            print(ch, end=" ")
     
        # incrementing number
        num = num + 1
     
        # ending line after each row
        print("\r")
 
# Driver Code
n = int(input("Enter Value of n"))
alphapat(n)

################################################


def alphapat(n):
     
    # initializing value corresponding to 'A' 
    # ASCII value
    num = 65
 
    # outer loop to handle number of rows
    # 5 in this case
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # explicitely converting to char
            ch = chr(num)
         
            # printing char value 
            print(ch, end=" ")
     
           # incrementing number
            num = num + 1
     
        # ending line after each row
        print("\r")
 
# Driver Code
n = int(input("Enter Value of n"))
alphapat(n)
