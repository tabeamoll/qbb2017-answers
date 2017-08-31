#!/usr/bin/env python

"""
Usage: ./00-reorder.py <ctab_file> <prefix>

- create a file that has chr start end t_name FPKM width
- calculate mean and std dev of width
- visualize distribution
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv(sys.argv[1], sep = "\t")
coi = ["chr", "start", "end", "t_name", "FPKM", "width" ]
df["width"] = df["end"]-df["start"]+1

print df[coi].head()

print "Mean %d, Std.dev %d" % (df["width"].mean(), df["width"].std())

plt.figure()
plt.hist(df["width"], bins=100, range=[0,10000])
plt.savefig(sys.argv[2] + ".png")
plt.close()