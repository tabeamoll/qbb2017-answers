#!/usr/bin/env python

"""


usage ./03-pca-components.py <all.csv> <base>
"""

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1], sep="\t")

roi_fwd = df["strand"] == "+"
coi_fwd=["chr", "start", "t_name"]

df_gene_plus = df[roi_fwd][coi_fwd]
df_gene_plus["prom-start"] = df_gene_plus["start"] - 500
df_gene_plus["prom-start"][df_gene_plus["prom-start"]<0]=1
df_gene_plus["prom-end"] = df_gene_plus["start"] + 500

cp = ["chr", "prom-start", "prom-end", "t_name"]

#for the minus strand
roi_rvs = df["strand"] == "-"
coi_rvs=["chr", "end", "t_name"]

df_gene_minus = df[roi_rvs][coi_rvs]
df_gene_minus["prom-start"] = df_gene_minus["end"] - 500
df_gene_minus["prom-start"][df_gene_minus["prom-start"]<0]=1
df_gene_minus["prom-end"] = df_gene_minus["end"] + 500

cm = ["chr", "prom-start", "prom-end", "t_name"]


frames = [df_gene_plus[cp], df_gene_minus[cm]]
result = pd.concat(frames)

result.to_csv("assignment1.bed", sep="\t", header=None, index=False)