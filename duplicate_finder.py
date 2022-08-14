#index a number of folders, by appending file names to list. if list.count(i) >=1 delete file

import os
from sys import argv

# before using commandline arguments, loc = "C:\\users\sexy\desktop\self1"
#current config works WITHOUT double backslash after C:


loc = argv[1] #enter the full path of the directory you want to clean
files = []
trash = []

for r, d, f in os.walk(loc):
    for i in f:
        if files.count(i) >= 1:
            i_path=r+"\\"+i
            trash.append(i)
            os.remove(i_path)
            print(i,"duplicate removed from",r,"\n")
        else:
            files.append(i)

print(trash)
