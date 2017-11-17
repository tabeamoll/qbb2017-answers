#!/usr/bin/env python


"""
./01-heatmap-dendrogram.py <hema_data.txt>


"""


import sys
import pandas as pd
import scipy.cluster as sp
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans




raw_data = pd.read_csv(sys.argv[1], delimiter="\t")
values_of_raw = raw_data.as_matrix()[:,1:].astype(float)

#This extracts the values for the heatmap rows
link_data = sp.hierarchy.linkage(values_of_raw, method="average", metric="euclidean")


#This gets the info for the dendrogram -> transpose
link_data_cols = sp.hierarchy.linkage(values_of_raw.T, method="average", metric="euclidean")
index_heatmap = sp.hierarchy.leaves_list(link_data)
cleaned_data = values_of_raw[index_heatmap,:]
dendrite_label = ["CFU", "poly", "unk", "int", "mys", "mid"]

#heatmap plot
plt.figure()
plt.pcolor(cleaned_data, cmap="plasma")
plt.savefig("heatmap.png")
plt.close()

#dendrogram plot
plt.figure()
sp.hierarchy.dendrogram(link_data_cols, labels=dendrite_label)
plt.savefig("dendrogram.png")
plt.close()

#Make the k-clusters and plot as heatmap 
kmeans = KMeans(n_clusters=5, random_state=0)
kmeans.fit(values_of_raw)
labels = kmeans.predict(values_of_raw)
data_matrix = pd.merge(pd.DataFrame(values_of_raw, columns = ['CFU', 'poly', 'unk', 'int', 'mys', 'mid']), pd.DataFrame( labels, columns=['cluster'] ), left_index=True, right_index=True )
k_clustered = data_matrix.sort_values('cluster')[['CFU', 'poly', 'unk', 'int', 'mys', 'mid']].values

plt.figure()
plt.imshow(k_clustered, aspect='auto', interpolation='nearest')
plt.grid( False )
plt.savefig("k_mean_map.png")
plt.close()