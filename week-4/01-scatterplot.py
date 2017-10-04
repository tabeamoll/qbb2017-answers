#!/usr/bin/env python

"""
Usage: ./01-scatterplot.py <pca file> <output>

"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

pca = pd.read_csv(sys.argv[1], sep = "\t")


plt.figure()
plt.scatter(pca["PC1"], pca["PC2"], s=7, c="orange")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA Analysis for Genotypes")
plt.savefig(sys.argv[2] + ".png")
plt.close()

