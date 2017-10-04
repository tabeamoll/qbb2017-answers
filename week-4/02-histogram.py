#!/usr/bin/env python

"""
Usage: ./02-histogram.py <genotype file from GWAS> <histo.png>


"""

import sys
import pandas as pd
import matplotlib.pyplot as plt


genotype = open(sys.argv[1])

allele_frequency = []

for l in genotype:
    if l.startswith("#"):
        continue
    line = l.rstrip("\t\n").split()
    af_value = line[7]
    af_real = af_value[3:]
    af_end = af_real.split(",")
    for l in af_end:
        allele_frequency.append(float(l))

# print allele_frequency


plt.figure()
plt.hist(allele_frequency, bins=50, color='orange')
plt.xlabel('Allele Frequency')
plt.ylabel('Frequency')
plt.title('Histogram for Allele Frequencies of Genotype')
plt.savefig(sys.argv[2] + ".png")
plt.close()