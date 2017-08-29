#!/usr/bin/env python

import sys
count = 0

genome_map = open(sys.argv[1])

ctab = open(sys.argv[2])

#create a dictionary with the created genome map
gene_dic = {}
for line in genome_map:
    genome_map_fields = line.rstrip("\r\n").split("\t")
    gene_dic[genome_map_fields[0].rstrip(" ")] = genome_map_fields[1]

#to check if my dic works  
#for key, value in gene_dic.iteritems():
#    print key, value
#    count +=1
#    if count >5:
#        break

#get rid of the header first
for line in ctab:
    if line.startswith ("t_id"):
        continue
#take the gene_name from the ctab    
    else:
        ctab_fields = line.rstrip("\r\n").split("\t")
        gene_name_ctab = ctab_fields[8]
        
        if gene_name_ctab in gene_dic:
            uniprot_id = gene_dic[gene_name_ctab]
            print line, uniprot_id  
            
        else:
            #continue   # just leaves the ones out that don't have a value
            print line, "whatever I chose"

print line[:100]