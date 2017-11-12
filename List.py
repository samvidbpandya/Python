l1 = [5,3,1,6,7]

l1.append(33)

l1.insert (3,12)

print (l1)

l2 = l1[1:3]

print (l2)

l3 = [[1,2,3,4,5], [6,7,8], 9]

print (l3)

print (l3[0][1])

l4 = [1,2,3,4,5,9,9,9]

l5 = [9,99,19]

l4.append(l5)

print (l4)

l4.extend(l5)

print (l4)

print (l4[0:5])
print (l4[5])
print (l4[6:])

l4.remove([9,99,19])

print (l4)

a = l4.count(9)

print (a)

len(l1)
