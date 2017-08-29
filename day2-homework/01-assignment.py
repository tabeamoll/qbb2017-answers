#!/usr/bin/env python

import sys

f = open(sys.argv[1])

#filter out all the lines that do not contain DROME
for line in f:
    
    if "DROME" not in line:
        continue
#split those lines        
    else:
        row = line.split()
#get only the last and the second to last column, separated by a tab
        print row[-1], "\t", row[-2]
        
