__author__ = 'Bryan Cairns'

from os import path

strPath = r"/home/rootshell/PycharmProjects/videos"

print("The current directory is: %s" % strPath)
print("abspath = %s" % path.abspath(strPath))
print("dirname = %s" % path.dirname(strPath))
print("basname = %s" % path.basename(strPath))
print("exists = %s" % path.exists(strPath))
print("isdir = %s" % path.isdir(strPath))
print("isfile = %s" % path.isfile(strPath))
