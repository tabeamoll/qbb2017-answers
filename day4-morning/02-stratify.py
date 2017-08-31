#!/usr/bin/env python

"""
Usage: ./02-stratify.py <ctab> <prefix>

- visualize for transcripts on chr (barplot)
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1], sep = "\t")

chrs = ["2L", "2R", "3L", "3R", "4", "X", "Y"]

counts = {}

for item in chrs:
    roi = df["chr"] == item
    #to only get the rows that are True
    counts[item] = len(df[roi])
    
print counts

plt.figure()
plt.bar(range(len(counts)), counts.values())
plt.xticks(range(len(counts)), counts.keys())
plt.savefig(sys.argv[2] + ".png")
plt.close()