import mdtraj as md
import numpy as np
import glob
filename = 'Nark-rnd'+str(run)+'-'+str(group)+'*strip.mdcrd'
error_trajs = []
for i in sorted(glob.glob(filename)):
     try: 
        traj = md.load(i, top='NarK-strip.pdb')
     except:
        error_trajs.append(i)
        continue
     a = [1240, 4559]
     dist_no2_list=[]
     dist_no3_list=[]
     for k in range(traj.n_frames):
         p1 = traj.xyz[k, a[0], :]
         p2 = traj.xyz[k, a[1], :]
         cx=(p1[0]+p2[0])*0.5
         cy=(p1[1]+p2[1])*0.5
         cz=(p1[2]+p2[2])*0.5
         c=[cx,cy,cz]
         dist_no2_0 = 10000
         dist_no3_0 = 10000
         for j in range(6845, 6927, 3):
             no2 = traj.xyz[k, j, :]
             if abs(dist_no2_0) < np.linalg.norm(c-no2):
                dist_no2 = dist_no2_0
             elif no2[2] > c[2]:
                dist_no2 = 0-np.linalg.norm(c-no2)
             else:
                dist_no2 =np.linalg.norm(c-no2)
             dist_no2_0 = dist_no2
         for j in range(6929, 7038, 4):
             no3 = traj.xyz[k, j, :]
             if abs(dist_no3_0) < np.linalg.norm(c-no3):
                dist_no3 = dist_no3_0
             elif no3[2] > c[2]:
                dist_no3 = 0-np.linalg.norm(c-no3)
             else:
                dist_no3 =np.linalg.norm(c-no3)
             dist_no3_0 = dist_no3
         dist_no2_list.append(dist_no2)
         dist_no3_list.append(dist_no3)
     name = i
     name1 = name.strip('.mdcrd') + '_no2'
     name2 = name.strip('.mdcrd') + '_no3'
     np.save(name1, dist_no2_list)
     np.save(name2, dist_no3_list)
if error_trajs:
    np.save("error_trajs_ions_group_"+str(group), error_trajs)
