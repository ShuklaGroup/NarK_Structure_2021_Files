import pickle
import numpy as np
import matplotlib
matplotlib.use('Agg')
from msmbuilder.msm import MarkovStateModel
from msmbuilder.msm import implied_timescales
import pylab as plt
import matplotlib as mpl

file='dataset_nark.best_nonredu.pkl'
name=file[:-4]
cl = pickle.load(open(name+"-GA-mbkm_mdl.pkl"))
n_timescales=5

lag_times=range(5,225,5)

ts=np.zeros([n_timescales,len(lag_times)])
ns_lt=np.ndarray.tolist(np.array(lag_times))
index = 0

for i in lag_times:
 msm=MarkovStateModel(lag_time=i, n_timescales=n_timescales)
 clL = cl.labels_
#clL10 = [clL[i][::0] for i in range(len(clL))]
 msm.fit_transform(clL)
 print(msm.timescales_)
 len(msm.timescales_)
 ts[:,index]=msm.timescales_
 index=index+1

np.save('nark_best_nonredu_ts10_cl400_ns_lt',ns_lt)
np.save('nark_best_nonredu_ts10_cl400_ts',ts)

