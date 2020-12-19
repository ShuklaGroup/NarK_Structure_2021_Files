import glob
import numpy as np
traj_list = np.load('./traj_list.npy')

dir_mdcrd = "/home/jf8/ds02/unstripped/NarK-MD/revision/"
run = 85
start = 0
for i in range(len(traj_list)):
    frame_index=int(traj_list[i][1])+1
    traj_name = traj_list[i][0].split('.mdcrd')[0] + '.xtc'
    print (i, traj_name, frame_index)
    j = i + start
    f = open('ccpASample_revision_' +str(run) +'_'+ str(j), 'w')
    f.write('parm NarK-strip.prmtop' + '\n')
    f.write('trajin ' + dir_mdcrd + traj_name  + '\n')
    #f.write('parmbox alpha 90 beta 90 gamma 90\n')
    f.write('trajout Nark-rnd'+str(run)+'-' + str(j) + '.rst restart onlyframes ' + str(frame_index) +'\n')
    f.write('run \n')
    f.write('quit')
    f.close()