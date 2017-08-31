#!/usr/bin/env python

"""
Usage: ./02-stratify.py <seq1> <seq2>

- 
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

seq1 = pd.read_csv(sys.argv[1], sep = "\t")

seq2 = pd.read_csv(sys.argv[2], sep = "\t")

coi = ["t_name", "FPKM"]
seq1 = seq1[coi]
seq2 = seq2[coi]

#seq1_dict = seq1.set_index("t_name")["FPKM"].to_dict()

#print seq1_dict
merged = pd.merge(seq1,seq2, on=["t_name"], how="inner")
merged = merged[~(merged == 0).any(axis=1)]
merged["FPKM_x"]=np.log(merged["FPKM_x"])
merged["FPKM_y"]=np.log(merged["FPKM_y"])

print merged.head()

plt.figure()
plt.scatter(merged["FPKM_x"], merged["FPKM_y"], alpha = 0.25, s=1)
plt.xlabel("FPKM_893")                 
plt.ylabel("FPKM_915")
plt.title("Comparison FPKM of SRR072893 and SRR072915")
fitty = np.polyfit(x=merged["FPKM_x"], y=merged["FPKM_y"], deg=1)
plt.plot(merged["FPKM_x"], fitty[0]*merged["FPKM_x"] + fitty[1], "-")
plt.savefig(sys.argv[3] + ".png")
plt.close()

#plt.bar(range(len(counts)), counts.values())
#plt.xticks(range(len(counts)), counts.keys())

