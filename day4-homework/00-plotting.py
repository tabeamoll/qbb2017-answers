#!/usr/bin/env python

"""
Making a boxplot
Usage: ./00-plotting.py <samples.cvs> <ctab.dir> <replicates.cvs>

- Boxplot distribution of Sxl in female
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_samples = pd.read_csv(sys.argv[1])

soi_f = df_samples["sex"] == "female"
transcript = "FBtr0331261"


fpkms_f = []
for sample in df_samples["sample"][soi_f]:
    fname_f = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname_f, sep = "\t")
    roi_f = df["t_name"] == transcript
    fpkms_f.append((df[roi_f]["FPKM"]).values)
#print fpkms_f

soi_m = df_samples["sex"] == "male"

fpkms_m = []
for sample in df_samples["sample"][soi_m]:
    fname_m = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname_m, sep = "\t")
    roi_m = df["t_name"] == transcript
    fpkms_m.append((df[roi_m]["FPKM"]).values)
#print fpkms_m

#FOLLOWING ARE THE REPLICATES
df_replicates = pd.read_csv(sys.argv[3])

soi_fr = df_replicates["sex"] == "female"

fpkms_fr = [None, None, None, None]
for replicate in df_replicates["sample"][soi_fr]:
    fname_fr = os.path.join(sys.argv[2], replicate, "t_data.ctab")
    df = pd.read_csv(fname_fr, sep = "\t")
    roi_fr = df["t_name"] == transcript
    fpkms_fr.append((df[roi_f]["FPKM"]).values)

soi_mr = df_replicates["sex"] == "male"


fpkms_mr = [None, None, None, None]
for replicate in df_replicates["sample"][soi_mr]:
    fname_mr = os.path.join(sys.argv[2], replicate, "t_data.ctab")
    df = pd.read_csv(fname_mr, sep = "\t")
    roi_mr = df["t_name"] == transcript
    fpkms_mr.append((df[roi_mr]["FPKM"]).values)    



plt.figure()
plt.plot(fpkms_f, c="red", lw=3)
plt.plot(fpkms_m, c="blue", lw=3)
plt.plot(fpkms_fr, 'o', c="red", markersize=10)
plt.plot(fpkms_mr, 'o', c="blue", markersize =10)
plt.xticks(range(len(fpkms_f)), df_samples["stage"], rotation = 90)
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (RPKM)")
plt.title("Sxl \n")
ax = plt.gca()
ax.tick_params(direction='out', top = 'off', right = 'off')
art =[]
plt.legend(['females', 'males', 'female replicates', 'male replicates'], loc='center right', bbox_to_anchor =(1.5,0.5), frameon = False, numpoints = 1) 
plt.savefig("plot.png", additional_artists=art, bbox_inches="tight")
plt.close()