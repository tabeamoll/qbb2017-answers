#!/usr/bin/env python

import sys
count = 0

for line in open (sys.argv[1]):
    if line.startswith ("@"):
        continue
    else:
        count += 1

print count