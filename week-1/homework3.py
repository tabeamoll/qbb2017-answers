#!/usr/bin/env python

"""
Usage ./homework3.py <dSdN-info.txt> 


"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sp
import numpy as np


ratio = pd.read_csv(sys.argv[1], sep = "\t", header=None, names=["Codon", "dSdN-Ratio", "dN-dS"])

P_VAL = 0.05 # the generally used p-value


#determine x and y axis, does not work with "Codon" because not float
x = range(len(ratio))
y = ratio["dSdN-Ratio"]

#Z-value for Z test using scipy.stats > z value is measure of stddev
zvals = sp.zscore(ratio["dN-dS"])
#using z val, get p val > probabilty that value occures randomly
pvals = 2 * sp.norm.cdf(-1*np.abs(zvals))

#input the significance to data points
significant_x = [i for i in range(len(pvals)) if pvals[i] < P_VAL]
significant_y = [y[i] for i in significant_x]
nonsig_x = [i for i in range(len(x)) if not i in significant_x]
nonsig_y = [y[i] for i in nonsig_x]


plt.figure()

plt.scatter(nonsig_x, nonsig_y, s=1)
plt.scatter(significant_x, significant_y, s=1, color='red')
plt.xlabel("Codons")                 
plt.ylabel("dS/dN")
plt.title("dN/dS ratio over each Codon")

plt.savefig(sys.argv[2] + ".png")
plt.close()


