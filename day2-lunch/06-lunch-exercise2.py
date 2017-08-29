#!/usr/bin/env python

import sys
count = 0

for line in open (sys.argv[1]):
    if line.startswith ("@"):
        continue
    if "NM:i:0" in line:
        count += 1

print count