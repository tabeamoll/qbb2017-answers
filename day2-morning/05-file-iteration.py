#!/usr/bin/env python

import sys

fh = sys.stdin

for line in fh:
   #start and end are in columns 3 and 4
    if line.startswith ("t_id"):
        continue
    fields = line.split("\t")
    print int (fields [4]) - int(fields [3])