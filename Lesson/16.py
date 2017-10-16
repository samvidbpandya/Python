__author__ = 'Bryan Cairns'

# Binary files

lst = [12,34,200,255]

strfile = r'/home/rootshell/Documents/test.txt'
buffer = bytes(lst)

print(buffer)

with open(strfile,'bw') as f:
    f.write(buffer)

print('File written, reading it back')

with open(strfile,'br') as f:
    buffer = f.read(16)
    print("Length of buffer is %d" % len(buffer))

    for i in buffer:
        print(int(i))

