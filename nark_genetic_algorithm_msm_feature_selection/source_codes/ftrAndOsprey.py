"""
       	Run as
       	<code name featurize.py> <input filename> <iteration input file iter_1_input_sets.txt >
"""

import os
import sys
from ospreyScript import *
from ftrScript import *
from scoreScript import *

input_file=sys.argv[1]
input_sets=sys.argv[2]

if __name__ == "__main__":

       	## Log file
        f_log=open("featurization.log","wb")

       	## Reading input file
        if len(sys.argv)==3:
                f=open(input_file,'rb')
                for line in f:
                        exec line
                f.close()
        else:
                print "This script needs exactly "+str(len(sys.argv)-1)+" arguments, aborting"
                f_log.write("This script needs exactly "+str(len(sys.argv)-1)+" arguments, aborting\n")
                sys.exit()

       	## Read iteration input sets
       	f=open(input_sets,'rb')
       	sets=[]
       	for line in f:
       		columns=line.split()
       		sets.append(columns)
       	f.close()

       	nSets=len(sets)

       	count=1
       	for i in range(nSets):
       		folder = input_file+"_"+str(count)
       		cmd="rm -rf "+folder
       		os.system(cmd)
       		cmd="mkdir "+folder
       		os.system(cmd)
       		rel_path_of_main_folder = sys.argv[0].replace('ftrAndOsprey.py','',1)
       		cmd="cp "+ rel_path_of_main_folder+"write_config.py ."
       		os.system(cmd)
                cmd="cp "+ rel_path_of_main_folder+"tica_write_config.py ."
                os.system(cmd)
       		os.chdir(folder)
       		n=len(sets[i])/2       	## Number of distances to calculate
       		cont=[]
       		temp_count=0
       		for j in range(n):
       			cont.append([int(sets[i][temp_count]),int(sets[i][temp_count+1])])
       			temp_count +=2
       		generateFeaturizationFile(cont[:],traj_path,topology_file,trajectory_format,folder)
       		generateFtrScript(folder,jobname)
                if n < 5:
                     cmd="python ../write_config.py "+str(clusters)+" "+str(lagtime)+" "+folder
       		     os.system(cmd)
                else:
                     cmd="python ../tica_write_config.py "+str(clusters)+" "+str(lagtime)+" "+str(tica_lagtime)+" "+str(tica_components)+" "+folder
                     os.system(cmd)
       		generateOspreyscript(folder,jobname)
       		count +=1
       		os.chdir('..')

        submitFtrScript1(input_file,jobname)
        submitOspreyscript1(input_file,jobname)
        submitFtrScript2(input_file,jobname)
        submitOspreyscript2(input_file,jobname)
        submitFtrScript3(input_file,jobname)
        submitOspreyscript3(input_file,jobname)
        submitFtrScript4(input_file,jobname)
        submitOspreyscript4(input_file,jobname)
        submitFtrScript5(input_file,jobname)
        submitOspreyscript5(input_file,jobname)
        submitFtrScript6(input_file,jobname)
        submitOspreyscript6(input_file,jobname)
        submitFtrScript7(input_file,jobname)
        submitOspreyscript7(input_file,jobname)
        submitFtrScript8(input_file,jobname)
        submitOspreyscript8(input_file,jobname)
        submitFtrScript9(input_file,jobname)
        submitOspreyscript9(input_file,jobname)
        submitFtrScript10(input_file,jobname)
        submitOspreyscript10(input_file,jobname)
        submitFtrScript11(input_file,jobname)
        submitOspreyscript11(input_file,jobname)
        submitFtrScript12(input_file,jobname)
        submitOspreyscript12(input_file,jobname)
        cmd="qsub ftr_tot1"
        os.system(cmd)
        cmd="qsub ftr_tot2"
        os.system(cmd)
        cmd="qsub ftr_tot3"
        os.system(cmd)
        cmd="qsub ftr_tot4"
        os.system(cmd)
        cmd="qsub ftr_tot5"
        os.system(cmd)
        cmd="qsub ftr_tot6"
        os.system(cmd)
        cmd="qsub ftr_tot7"
        os.system(cmd)
        cmd="qsub ftr_tot8"
        os.system(cmd)
        cmd="qsub ftr_tot9"
        os.system(cmd)
        cmd="qsub ftr_tot10"
        os.system(cmd)
        cmd="qsub ftr_tot11"
        os.system(cmd)
        cmd="qsub ftr_tot12"
        os.system(cmd)
        cmd="qsub -hold_jid featurization_tot_1"+jobname+" osprey_tot1"
        os.system(cmd)
        cmd="qsub -hold_jid featurization_tot_2"+jobname+" osprey_tot2"
        os.system(cmd)
        cmd="qsub -hold_jid featurization_tot_3"+jobname+" osprey_tot3"
        os.system(cmd)
        cmd="qsub -hold_jid featurization_tot_4"+jobname+" osprey_tot4"
        os.system(cmd)
        cmd="qsub -hold_jid featurization_tot_5"+jobname+" osprey_tot5"
        os.system(cmd)
        cmd="qsub -hold_jid featurization_tot_6"+jobname+" osprey_tot6"
        os.system(cmd)
        cmd="qsub -hold_jid featurization_tot_7"+jobname+" osprey_tot7"
        os.system(cmd)
        cmd="qsub -hold_jid featurization_tot_8"+jobname+" osprey_tot8"
        os.system(cmd)
        cmd="qsub -hold_jid featurization_tot_9"+jobname+" osprey_tot9"
        os.system(cmd)
        cmd="qsub -hold_jid featurization_tot_10"+jobname+" osprey_tot10"
        os.system(cmd)
        cmd="qsub -hold_jid featurization_tot_11"+jobname+" osprey_tot11"
        os.system(cmd)
        cmd="qsub -hold_jid featurization_tot_12"+jobname+" osprey_tot12"
        os.system(cmd)
       	generateOutputFile(nSets,input_file,input_sets,sets,jobname)
       	cmd="rm write_config.py"
       	os.system(cmd)
        cmd="rm tica_write_config.py"
        os.system(cmd)
       	f_log.close() 
