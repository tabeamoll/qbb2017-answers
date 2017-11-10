#!/usr/bin/env python

"""
Usage: ./01-CTCF-heat.py <ctcf_peaks.tsv> <Nora_Primers.bed>

"""

import sys
import numpy as np
import math

heat = np.load("5Cenriched_good.heat.npz")
forward = heat['0.forward']
reverse = heat['0.reverse']
enrichment = heat['0.enrichment']

#for key in heat:
#    print key, heat[key]

# get the position of the CTCF binding on only the x chromosome    
ctcf = open(sys.argv[1])
ctcf_binding = []

for line in ctcf:
    line = line.rstrip('\r\n').split('\t')
    if line [0] == 'chrX':
        ctcf_binding.append(line[1])
#print ctcf_binding

ctcf_forward = []
for i, each in enumerate(forward):
    start, stop = each[0], each[1]
    #print type(start), stop
    for position in ctcf_binding:
        if int(position) >= start and int(position)<= stop:
            ctcf_forward.append(i)
            break #stops it when you found your position once

ctcf_reverse = []
for i, each in enumerate(reverse):
    start, stop = each[0], each[1]
    #print type(start), stop
    for position in ctcf_binding:
        if int(position) >= start and int(position)<= stop:
            ctcf_reverse.append(i)
            break #stops it when you found your position once

#print ctcf_forward, ctcf_reverse

#now get the enrichment info for these

ctcf_enrichment = enrichment[ctcf_forward,:][:,ctcf_reverse]

#print ctcf_enrichment
col_maximum = np.argmax(ctcf_enrichment, axis = 0)
row_maximum = np.argmax(ctcf_enrichment, axis = 1)

#print col_maximum, row_maximum
count = 0
print " top forward interactions"
for i in row_maximum:
    #print i
    top_reverse = reverse[ctcf_reverse[i]]
    top_forward = forward[ctcf_forward[count]]
    count += 1
    print  'Forward = %s, Reverse = %s' % (top_forward, top_reverse)

count = 0

print "\n top reverse interactions"
for i in col_maximum:
    #print i
    top_forward = forward[ctcf_forward[i]]
    top_reverse = reverse[ctcf_reverse[count]]
    count += 1
    print 'Reverse = %s, Forward = %s' % (top_reverse, top_forward)
    
    
#Create that dictionary of primers
# primers = open(sys.argv[2])
# primer_dict = {}
#
# for line in primers:
#     line = line.rstrip('\r\n').split('\t')
#     if line[0] == '#chr':
#         continue
#     else:
#         primer_dict[line[1]] = [line[2]]
#print primer_dict
