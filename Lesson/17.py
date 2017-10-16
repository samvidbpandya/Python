__author__ = 'Bryan Cairns'

# Struct
# https://docs.python.org/3.0/library/struct.html

from struct import *

strfile = r'/home/rootshell/Documents/test.txt'
strformat = 'iid'

packed = pack(strformat,1,2,3.14)

print(packed)
print("writing file")

with open(strfile,'bw') as f:
    f.write(bytes(packed))

print("reading the file")

with open(strfile,'br') as f:
    buffer = f.read()
    unpacked = unpack(strformat,buffer)
    print(unpacked)
