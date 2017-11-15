__author__ = 'Bryan Cairns'

import os

def writefile(sfile):
    if os.path.exists(sfile):
        print("File already exists!")
        return

    f = open(sfile,'w')
    try:
        f.write("Hello world\r\nThis is a new line!!!")
        f.flush()

    except Exception as e:
        print(e)
    finally:
        if f is not None:
            f.close()


spath = r"/home/rootshell/test/testfile.txt"
writefile(spath)
