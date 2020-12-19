import glob
import mdtraj as md
import numpy as np
import os
import sys
from msmbuilder.utils import io
if __name__ == "__main__":
    #log file
    f_log=open("generatePairs.log","wb")
    if len(sys.argv)==2:
       f=open(sys.argv[1],'rb')
       for line in f:
           exec line
       f.close()
    cmd="ls "+traj_path+"/*."+trajectory_format+" > temp_trajectories.txt"
    os.system(cmd)
    with open('temp_trajectories.txt', 'rb') as f:
 	sample_traj_file = f.readline().strip('\n')

    #read topology
    R=0
    f_log.write("Loading topology ...\n")
    topology=md.load(sample_traj_file,top=topology_file).topology
    f_log.write("Defining constants ...\n")
    R=447

    #genearate all the possible residue pairs
    f_log.write("Generating all the residue pairs ...\n")
    f1 = open("compatiblePairs.txt", "w")
    tot_pair = []
    for i in range(1,R):
    	for j in range(i+1, R):
                tot_pair.append([i,j])
    		f1.write(str(i) + "\t "+str(j)+'\n')
    f_log.write('%s\n' %str(np.shape(tot_pair)[0]==int(R)*(int(R)-1)/2.0))
    f1.close()
    f_log.close()
