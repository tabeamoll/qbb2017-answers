#!/usr/bin/env python

"""
Parse every FASTA record from a file and print
"""

import sys

class FASTAReader(object):
    def __init__(self, input_file):
        self.file = input_file
        self.last_ident = None
        
    def __iter__(self):
        return self
    
    def next(self):
        #if this is the first call
        if self.last_ident is None:
    
            line = self.file.readline()
            # verfify it is a header line using True/False
            assert line.startswith(">")

            #exact identifier
            # just another way of doing the following line.     ident = line.split()[0].lstrip(">")
            ident = line.split()[0][1:]
        #if it was called before
        else:
            ident = self.last_ident
            
            
        sequences = []

        while True :
            line = self.file.readline().rstrip("\r\n")
            if line.startswith (">"):
                self.last_ident = line.split ()[0][1:]
                break
            elif line == "":
                raise StopIteration
            else:
                sequences.append(line)
        
        return ident, "".join(sequences)
        
#what I want

reader = FASTAReader (sys.stdin)

for ident, sequence in reader :
    print ident, sequence