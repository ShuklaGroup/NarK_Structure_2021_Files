# script make a cluster based on tICs and pick the less populated clusters, and find
# the frames in those clusters, the make a input file for Cpptraj to extract them
##########################################################################################
from msmbuilder.dataset import dataset
import numpy as np
from msmbuilder.cluster import KMeans
import pickle
import asFunctions
import glob

myn_clusters = 5000
n_samples = 200
topFile='NarK-strip.pdb'

dataset = [] 
ls = []
for i in sorted(glob.glob('*.npy')):
	a = np.load(i)
	b = np.array(a)
	dataset.append(b)
	ls.append(i)
	print(i)
np.save('list', ls)

#trajs = [np.load('data.npy')]
# make cluster of the tICs trajectories
cluster = KMeans(n_clusters=myn_clusters)
cluster.fit(dataset)
l = cluster.labels_

T = []
for trj in glob.glob('*strip.mdcrd'):
	T.append(trj)
T.sort()

# Write the output file, which have the information about population of each cluster, 
# trajectory name and frame number of corresponding frame 	
asFunctions.writeOPF(l, T, myn_clusters, n_samples)

# Based on information in output file, build the cpptraj input file
asFunctions.CpptrajInGen_commonTop(topFile)
#pickle.dump( cluster , open( "tICCluster.pkl", "wb"))
