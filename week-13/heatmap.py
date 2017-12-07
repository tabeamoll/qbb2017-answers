#!/usr/bin/env python

"""
Usage
./heatmap.py <abundance_table.tab>




"""


import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

abundance = pd.read_csv( sys.argv[1], sep='\t', index_col=0 )[['SRR492183','SRR492186','SRR492188','SRR492189','SRR492190','SRR492193','SRR492194','SRR492197']]

BIN_dictionary = { 'bin.1': 'Staphylococcus haemolyticus','bin.2': 'Leuconostoc citreum','bin.3': 'Staphylococcus lugdenensis','bin.4': 'Enterococcus faecalis', 'bin.5': 'Cutibacterium avidum', 'bin.6': 'Staphylococcus epidermidis', 'bin.7': 'Staphylococcus aureus', 'bin.8': 'Anaerococcus prevotii' }

genomes = [ BIN_dictionary[ bin ] for bin in abundance.index ]
#print abundance



plt.figure()
plt.imshow(abundance, aspect = 'auto', interpolation = 'nearest')
plt.title('Abundance Heatmap')
plt.yticks( [ x for x in range( len( genomes ))], genomes )
plt.xticks( [ x for x in range( len( abundance.columns ))], abundance.columns, rotation='vertical' )
plt.colorbar()
plt.tight_layout()
plt.savefig("abundance_heatmap.png")
plt.close()