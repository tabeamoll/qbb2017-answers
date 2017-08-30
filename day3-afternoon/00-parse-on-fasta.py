#!/usr/bin/env python

"""
Parse is a single FASTA record from stdin and prints it.

usage: ./00-parse-on-fasta.py <input.fa> output
"""

import sys

line = sys.stdin.readline()
# verfify it is a header line using True/False
assert line.startswith(">")

#exact identifier
# just another way of doing the following line.     ident = line.split()[0].lstrip(">")
ident = line.split()[0][1:]

sequences = []

while True :
    line = sys.stdin.readline().rstrip("\r\n")
    if line == "" or line.startswith (">"):
        break
    else:
        sequences.append(line)
        
print ident, "".join(sequences)