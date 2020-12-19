import os

def generateFeaturizationFile(cont,traj_path,topology_file,trajectory_format,folder):
        f_ftr_py=open('featurize.py','wb')
        f_ftr_py.write("import numpy as np"+'\n'
+"import mdtraj as md"+'\n'
+"import glob"+'\n'
+"import os"+'\n'
+""+'\n'
+"for file in glob.glob('"+traj_path+"/*."+trajectory_format+"'):"+'\n'
+"      t = md.load(file, top='"+topology_file+"')"+'\n'
+"      dist=md.compute_contacts(t, contacts="+str(cont)+", scheme='ca')"+'\n'
+"      ftr=[np.ndarray.tolist(dist[0][i][:]) for i in range(len(dist[0]))]"+'\n'
+"      dir=os.path.dirname(file)"+'\n'
+"      filename=file.replace(dir+'/','',1)"+'\n'
+"      np.save(filename+'.npy', ftr)"+'\n'
+""+'\n'
+"from msmbuilder.utils import io"+'\n'
+""+'\n'
+"dataset=[]"+'\n'
+"for i in sorted(glob.glob('*.npy')):"+'\n'
+"      a = np.load(i)"+'\n'
+"      dataset.append(a)"+'\n'
+""+'\n'
+"io.dump(dataset,'dataset_"+folder+".pkl')"+'\n'
+"cmd='rm *.npy'"+'\n'
+"os.system(cmd)"+'\n'
)
        f_ftr_py.close()

def generateFtrScript(folder,jobname):
        f_sge=open('sge.'+folder,'wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q*"+'\n'
+"#$ -pe orte 5"+'\n'
+"#$ -o "+os.getcwd()+"/featurization_"+folder+".log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N featurization_"+folder+"_"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"python featurize.py"+'\n'
)
        f_sge.close()

def submitFtrScript1(input_file,jobname):
        f_sge=open('ftr_tot1','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-0-15.local*"+'\n'
+"#$ -t 1-2"+'\n'
+"#$ -o "+os.getcwd()+"/featurization_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N featurization_tot_1"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitFtrScript2(input_file,jobname):
        f_sge=open('ftr_tot2','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-0-15.local*"+'\n'
+"#$ -t 3-4"+'\n'
+"#$ -o "+os.getcwd()+"/featurization_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N featurization_tot_2"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitFtrScript3(input_file,jobname):
        f_sge=open('ftr_tot3','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-0-15.local*"+'\n'
+"#$ -t 5-6"+'\n'
+"#$ -o "+os.getcwd()+"/featurization_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N featurization_tot_3"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitFtrScript4(input_file,jobname):
        f_sge=open('ftr_tot4','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-0-15.local*"+'\n'
+"#$ -t 7-8"+'\n'
+"#$ -o "+os.getcwd()+"/featurization_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N featurization_tot_4"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitFtrScript5(input_file,jobname):
        f_sge=open('ftr_tot5','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-1-0.local*"+'\n'
+"#$ -t 9-10"+'\n'
+"#$ -o "+os.getcwd()+"/featurization_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N featurization_tot_5"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitFtrScript6(input_file,jobname):
        f_sge=open('ftr_tot6','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-1-0.local*"+'\n'
+"#$ -t 11-12"+'\n'
+"#$ -o "+os.getcwd()+"/featurization_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N featurization_tot_6"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitFtrScript7(input_file,jobname):
        f_sge=open('ftr_tot7','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-1-0.local*"+'\n'
+"#$ -t 13-14"+'\n'
+"#$ -o "+os.getcwd()+"/featurization_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N featurization_tot_7"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitFtrScript8(input_file,jobname):
        f_sge=open('ftr_tot8','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-1-0.local*"+'\n'
+"#$ -t 15-16"+'\n'
+"#$ -o "+os.getcwd()+"/featurization_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N featurization_tot_8"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitFtrScript9(input_file,jobname):
        f_sge=open('ftr_tot9','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-1-1.local*"+'\n'
+"#$ -t 17-18"+'\n'
+"#$ -o "+os.getcwd()+"/featurization_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N featurization_tot_9"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitFtrScript10(input_file,jobname):
        f_sge=open('ftr_tot10','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-1-1.local*"+'\n'
+"#$ -t 19-20"+'\n'
+"#$ -o "+os.getcwd()+"/featurization_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N featurization_tot_10"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitFtrScript11(input_file,jobname):
        f_sge=open('ftr_tot11','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-1-1.local*"+'\n'
+"#$ -t 21-22"+'\n'
+"#$ -o "+os.getcwd()+"/featurization_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N featurization_tot_11"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitFtrScript12(input_file,jobname):
        f_sge=open('ftr_tot12','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-1-1.local*"+'\n'
+"#$ -t 23-24"+'\n'
+"#$ -o "+os.getcwd()+"/featurization_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N featurization_tot_12"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge."+input_file+"_$SGE_TASK_ID"'\n'
)
