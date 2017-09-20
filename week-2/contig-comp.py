#!/usr/bin/env python

"""
Usage
./contig-comp.py <contig file>

this script allows to perform basic stats on the generated contigs files


"""


import sys
import fasta


contigFile = open(sys.argv[1])
contig_length = []


for dnaIdent, contig in fasta.FASTAReader(contigFile): 
    contig_length.append(len(contig))
    
maxi_result = max(contig_length)
mini_result = min(contig_length)
contig_number = len(contig_length)
contig_average_length = sum(contig_length) / float(contig_number)
contig_half_length = sum(contig_length) // 2
sorted_contigs = sorted(contig_length, reverse = True)
contig_count = 0
n50 = None

for l in sorted_contigs:
    contig_count += l
    if contig_count >= contig_half_length:
        n50 = l
        break
   
print "Contig Minimum {} \nContig Maximum {} \nAmount of Contigs {} \nAverage Length of Contigs {} \nN50 {}".format(mini_result, maxi_result, contig_number, contig_average_length, n50)
   
   
   
   
    
