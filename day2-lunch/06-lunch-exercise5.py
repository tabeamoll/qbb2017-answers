#!/usr/bin/env python

import sys
count = 0
mapq = 0

for line in open (sys.argv[1]):
    if line.startswith ("@"):
        continue
    cols = line.split()    
    mapq += int(cols[4])
    count += 1
    
print mapq/float(count)
