#!/usr/bin/env python

import sys

f = open(sys.argv[1])

for line in f:
#    line = line.rstrip("\r\n")
    
    if "DROME" not in line:
        continue
        
    else:
        row = line.split()

        print row[-1], "\t", row[-2]
        
