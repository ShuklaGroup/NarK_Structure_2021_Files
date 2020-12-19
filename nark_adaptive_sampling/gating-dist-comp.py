import mdtraj as md
import glob
import numpy as np
filename = 'Nark-rnd'+str(run)+'-'+str(group)+'*strip.mdcrd'
error_trajs = []
for i in sorted(glob.glob(filename)):
    try:
        traj = md.load(i, top='NarK-strip.pdb')
        a = np.loadtxt('gating_index.txt')
        distance = md.compute_distances(traj, a)
        name1 = i.strip('.mdcrd')
        np.save(name1, distance)
    except:
        error_trajs.append(i)
        print("error: " + i)
if error_trajs:
    np.save("error_trajs_group_"+str(group), error_trajs)
