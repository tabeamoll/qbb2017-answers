#!/usr/bin/env python


"""
things we need to do: 
    1) strip the query of its lines and remove the header
    2) kmer input on terminal
    3) creat dic on query -> index for searching
    
        kmer_matcher.py <target.fa> <query.fa> <k>
    *) output target_sequence_name    target_start    query_start   k-mer
"""

import sys
import fasta

target = open(sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3])
#k=10

kmer_dict = {}

for ident, sequence, in fasta.FASTAReader (target):
    sequence = sequence.upper()
    for i in range(0, len(sequence)-k):
        kmer = sequence [i:i+k]
        if kmer not in kmer_dict:
            kmer_dict[kmer] = [(ident,i)]
        else:
            kmer_dict[kmer].append((ident,i))



#for kmer, count, in kmer_dict.iteritems():
    #print kmer, count
    
    
    
ident, sequence_q = fasta.FASTAReader (query).next()
sequence_q = sequence_q.upper()
for j in range(0, len(sequence_q)-k):
    kmer_query = sequence_q [j:j+k]
    if kmer_query in kmer_dict:
        result=kmer_dict[kmer_query]
        for item in result:
            print item[0], "\t", item[1], "\t", j, "\t", kmer_query
        
        
        
        
        
        