#!/usr/bin/env python

"""
Usage: ./01-histo.py <dif_filtered_freebayes> <histo.png>


"""

import sys
import pandas as pd
import matplotlib.pyplot as plt


freebayes = open(sys.argv[1])

allele_frequency = []

for l in freebayes:
    if l.startswith("#"):
        continue
    line = l.rstrip("\t\n").split()
    af_value = line[7].split(";")
    af_real = af_value[3][3:]
    af_end = af_real.split(",")
#    print af_real
    for l in af_end:
        allele_frequency.append(float(l))
        
       
    # need to take AD value which is number of reads for each SNP
# look at DP which is total number of reads for that variant at that SNP


plt.figure()
plt.hist(allele_frequency, bins=30)
plt.xlabel('Allele Frequency')
plt.ylabel('Frequency')
plt.savefig(sys.argv[2] + ".png")
plt.close()