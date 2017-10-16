str = "Hello World I am Samvid Pandya and this is my String Manipulation Script"

#String Length
print("The string is %d bytes long " % len(str))

#Make Upper Case
print(str.upper())

#Make lower Case
print(str.lower()) 

#Find the index of the number
print("The index of o is %d" % str.index('o'))

#print("The index of o is %d" % str.index('O'))


print("The index of o is %d" % str.upper().index("O"))

#Count the number of I's in String using tupple
print("There are %d letter I's in '%s'" %(str.upper().count("I"),str) )

#Slicing of the script
print (str[17])
print (str[1:56])
print (str[1:len(str)])

#Split the String

name = "Samvid Bhargav Pandya"
mylist = name.split(" ")
print (mylist)
print ("My Fisrt name is '%s' My middle name is '%s' and my last name is '%s'" % (mylist[0],mylist[1],mylist[2]))
