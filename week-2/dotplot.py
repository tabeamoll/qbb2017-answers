#!/usr/bin/env python

"""
./dotplot.py <_lastz.tsv>
"""

import sys
import fasta
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

contigs = open(sys.argv[1])


count = 0

plt.figure()

for i in contigs:
    if "start1" in i:
        continue
    else:
        fields = i.split("\t")
        plt.plot([count,count+int(fields[1])],[int(fields[0]),int(fields[2])])
        count += int(fields[1])


plt.xlabel("Contig Names")
plt.ylabel("Position")
plt.xlim(0, 310000)
plt.ylim(0, 400000)
#make some sort of tick mark with low font
plt.savefig( "spades_better_align" + ".png")
plt.close()