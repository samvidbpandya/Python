__author__ = 'Bryan Cairns'

# List dir contents

import os

spath = r"/home/rootshell/Python-3.4.3"

# Everything
print(os.listdir(spath))

#Get everything split
#for roots, dirs, files in os.walk(spath):
#    for file in files:
#        print("File = %s" % file)

#Only the roots
roots = next(os.walk(spath))[0]
print("Roots = %s" % roots)

#Only the dirs
dirs = next(os.walk(spath))[1]
print("Dirs = %s" % dirs)

#Only the files
files = next(os.walk(spath))[2]
print("Files = %s" % files)