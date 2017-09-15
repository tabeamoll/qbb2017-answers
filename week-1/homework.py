#!/usr/bin/env python

"""
Usage ./homework.py <1000_homologs.fa> <alignment_prot.fa>

writes the new file into alignment_nuc.fa

"""
import itertools
import sys
import fasta

dnaFile = open(sys.argv[1])
aminoFile = open(sys.argv[2])
alignmentFile = open("alignment_nuc.fa", "w")

for (dnaIdent, dnaSeq), (aminoIdent, aminoSeq) in itertools.izip(fasta.FASTAReader(dnaFile),
                                                                 fasta.FASTAReader(aminoFile)): 
    alignmentFile.write(dnaIdent + "\n")
    for amino in aminoSeq:
        if amino == "-":
            alignmentFile.write("---")
        else:
            alignmentFile.write(dnaSeq[:3])
            dnaSeq = dnaSeq[3:]

    alignmentFile.write("\n")
            
        