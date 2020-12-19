import mdtraj as md
import os, glob
import numpy as np
import pandas as pd
import pickle
import glob
from msmbuilder.featurizer import ContactFeaturizer
from msmbuilder.dataset import dataset
from msmbuilder.decomposition import tICA
from msmbuilder.cluster import MiniBatchKMeans
from msmbuilder.msm import MarkovStateModel
from msmbuilder.utils import verbosedump,verboseload

file='dataset_nark.best_nonredu.pkl'
alpha=pickle.load(open(file))
print ('#_trajs:'+ str(np.shape(alpha)[0])+'\n' '#_CA_contacts:'+str(np.shape(alpha[0])[1]))
tica_model=tICA(n_components=10,lag_time=1)
tica_trajs=tica_model.fit_transform(alpha)
clusterer =MiniBatchKMeans(n_clusters=400)
clustered_trajs = clusterer.fit_transform(tica_trajs)
msm =MarkovStateModel(lag_time=150, n_timescales=5)
assignments = msm.fit_transform(clustered_trajs)
data = np.concatenate(tica_trajs, axis=0)
pi_0 = msm.populations_[np.concatenate(assignments, axis=0)]


name=file[:-4]
verbosedump(tica_model, name+"-GA-tica_model.pkl")
verbosedump(tica_trajs, name+"-GA-tica_trajs.pkl")
verbosedump(clusterer, name+"-GA-mbkm_mdl.pkl")
verbosedump(clustered_trajs, name+"-GA-clustered_trajs.pkl")
verbosedump(msm,name+"-GA-msm.pkl")
verbosedump(assignments,name+"-GA-assignments.pkl")
verbosedump(data,name+"-GA-weighted-msme-tica-data.pkl")
verbosedump(pi_0,name+"-GA-weighted-msme-tica-pi.pkl")
