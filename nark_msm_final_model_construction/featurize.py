import numpy as np
import mdtraj as md
import glob
import os

for file in glob.glob('/home/jf8/NarK-MD/strip-trajs-combined/NarK_stripped_dcd/*.dcd'):
      t = md.load(file, top='/home/jf8/NarK-MD/strip-trajs-combined/NarK-strip.pdb')
      dist=md.compute_contacts(t, contacts=[[112, 333], [249, 377], [54, 85], [125, 213], [54, 67], [133, 423], [358, 371], [220, 371], [109, 419], [193, 374], [35, 245], [9, 198], [62, 335], [123, 183], [280, 325], [225, 326], [25, 117], [4, 359], [383, 397], [208, 234], [9, 164], [157, 291], [162, 420], [124, 439], [48, 171], [241, 320], [52, 147], [29, 436], [53, 445], [125, 155], [294, 392], [99, 189], [230, 274], [92, 128], [91, 151], [97, 338], [356, 425], [200, 444], [351, 439], [138, 197], [42, 169], [234, 425], [110, 331], [36, 43], [240, 347], [160, 245], [6, 50], [293, 396], [287, 299], [25, 158], [13, 233], [22, 321], [210, 369], [29, 204], [230, 421], [256, 275], [205, 424], [237, 313], [117, 146], [34, 63], [377, 443]], scheme='ca')
      ftr=[np.ndarray.tolist(dist[0][i][:]) for i in range(len(dist[0]))]
      dir=os.path.dirname(file)
      filename=file.replace(dir+'/','',1)
      np.save(filename+'.npy', ftr)

from msmbuilder.utils import io

dataset=[]
for i in sorted(glob.glob('*.npy')):
      a = np.load(i)
      dataset.append(a)

io.dump(dataset,'dataset_nark.best_nonredu.pkl')
cmd='rm *.npy'
os.system(cmd)
