#!/usr/bin/env python

"""
Usage: ./03-manhattanplot.py <plink2 file from both genotype and phenotype> <output>

"""

import sys
import numpy as np
import math
import matplotlib.pyplot as plt

gwas = open(sys.argv[1])

significant = []
non_significant = []
count = 0
length_of_file = 5 #why ever I need to make this 5 to work

for entry in gwas:
    length_of_file += 1
# print length_of_file

for entry in range(length_of_file):
    significant.append(None)
    non_significant.append(None)

gwas.seek(0)
for entry in gwas:
    fields = entry.split()
    if "CHR" in entry:
        continue
    elif "NA" in entry:
        continue
    elif float(fields[8]) <= 10e-5 :
        significant[count] = -np.log10(float(fields[8]))
        count += 1
    elif float(fields[8]) > 10e-5 :
        non_significant[count] = -np.log10(float(fields[8]))
        count += 1
        
# print significant
# print non_significant


plt.figure()
plt.scatter(range(len(significant)), non_significant, alpha = 0.5, s=7,  c="black")
plt.scatter(range(len(significant)), significant, alpha = 0.5, s=7, c="orange")
plt.xlabel("Location on Genome")
plt.ylabel("-log10(p-Value)")
plt.savefig(sys.argv[2] + "_manhattan_plot.png")
plt.close()

gwas.close()
