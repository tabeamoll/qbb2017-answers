#!/usr/bin/env python

"""
Usage: ./00-reorder.py <csv_file> <tsv_file>
- remove header
- reorder columns: sex, sample, stage
- subset "female" in sex column
- convert delimeter from comma to tab
"""

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
#specify desired column order
coi = ["sex", "sample", "stage"]
#print df[coi]
roi = df["sex"]=="female"

df[coi][roi].to_csv(sys.argv[2],sep="\t", index=False, header=False)