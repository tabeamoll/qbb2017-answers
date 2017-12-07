#!/usr/bin/env python

"""
Usage
./help.py <.kraken files>




"""


import sys



kraken_files = open(sys.argv[1])


kraken_files_count = {}

for line in kraken_files:
    strip_it = line.rstrip("\n").split("\t")
    #col1 = strip_it[0]
    col2 = strip_it[1]
    #print col2
    
    
    if col2 not in kraken_files_count:
        kraken_files_count[col2] = 1
    else:
        kraken_files_count[col2] +=1
            
for i in kraken_files_count:
    print str(kraken_files_count[i]) + "\t" + "\t".join(i.split(";"))

   
   
    
