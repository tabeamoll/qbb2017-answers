#!/usr/bin/env python

"""
Usage ./homework2.py <alignment_nuc.fa> > <safe it>


"""
import sys
import numpy as np

dnaAlignment = open(sys.argv[1])
            #comparisonFile = open("s-n-values.txt", "w")



# found online the codon table generator, use that code
bases = ['T', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

# define a
def codon_splitter(sequence, k):
    return [sequence[i:i+k] for i in range(0, len(sequence), k)]
    
#skip header in first line
dnaAlignment.readline()
#take out first sequence and store it as reference, in steps of 3 store the codons
firstLine = codon_splitter(dnaAlignment.readline(), 3)

#define the dS and dN
dS = np.zeros(len(firstLine))
dN = np.zeros(len(firstLine))

# for loop to a) skip is the same or --- b) append dS when different code and same AA c) append dN when different code and different AA

for line in dnaAlignment:
    #skips the header
    if line[:2] == "gi":
        continue
    for index, (codon, ref) in enumerate(zip(codon_splitter(line, 3), firstLine)):
        if codon == ref:
            continue
            
        if not codon in codon_table or not ref in codon_table:
            continue
            
        if codon_table[codon] == codon_table[ref]:
            dS[index] += 1
        else:
            dN[index] += 1
            
           
differences_list = dN - dS


#three columns 1) codon 2) dN/dS 3) dN-dS.
for i in range(len(firstLine)):
    if dS[i] > 0:
        print("{}\t{}\t{}".format(firstLine[i], float(dN[i])/dS[i], differences_list[i]))
 
 
 
 
 
        
        
