#!/usr/bin/env python

import sys
count = 0

for line in open (sys.argv[1]):
    if line.startswith ("@"):
        continue
    cols = line.split()    
    count += 1
    print cols[2]
    if count > 9:
        break
