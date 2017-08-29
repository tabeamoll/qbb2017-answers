#!/usr/bin/env python

import sys
count_rev = 0
count_fwd = 0

for line in open (sys.argv[1]):
    if line.startswith ("@"):
        continue
    cols = line.split()    
    rev_strand = int(cols[1])
    
    if rev_strand == 16:
        count_rev += 1
    else:
        count_fwd += 1
    
    
print count_rev
print count_fwd
