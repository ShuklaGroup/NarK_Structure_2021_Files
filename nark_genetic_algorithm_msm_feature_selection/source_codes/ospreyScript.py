import os

def generateOspreyscript(folder,jobname):
        f_sge=open('sge.osprey.'+folder,'wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q*"+'\n'
+"#$ -pe orte 5"+'\n'
+"#$ -o "+os.getcwd()+"/osprey_"+folder+".log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N osprey_"+folder+"_"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"osprey worker config_osprey.yaml -n 24"+'\n'
)
        f_sge.close()

def submitOspreyscript1(input_file,jobname):
        f_sge=open('osprey_tot1','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q all.q@compute-0-4.local"+'\n'
+"#$ -t 1-2"+'\n'
+"#$ -o "+os.getcwd()+"/osprey_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N osprey_tot_1"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge.osprey."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitOspreyscript2(input_file,jobname):
        f_sge=open('osprey_tot2','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q all.q@compute-0-5.local"+'\n'
+"#$ -t 3-4"+'\n'
+"#$ -o "+os.getcwd()+"/osprey_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N osprey_tot_2"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge.osprey."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitOspreyscript3(input_file,jobname):
        f_sge=open('osprey_tot3','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q all.q@compute-0-9.local"+'\n'
+"#$ -t 5-6"+'\n'
+"#$ -o "+os.getcwd()+"/osprey_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N osprey_tot_3"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge.osprey."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitOspreyscript4(input_file,jobname):
        f_sge=open('osprey_tot4','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q all.q@compute-0-10.local"+'\n'
+"#$ -t 7-8"+'\n'
+"#$ -o "+os.getcwd()+"/osprey_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N osprey_tot_4"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge.osprey."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitOspreyscript5(input_file,jobname):
        f_sge=open('osprey_tot5','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q all.q@compute-0-11.local"+'\n'
+"#$ -t 9-10"+'\n'
+"#$ -o "+os.getcwd()+"/osprey_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N osprey_tot_5"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge.osprey."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitOspreyscript6(input_file,jobname):
        f_sge=open('osprey_tot6','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q all.q@compute-0-0.local"+'\n'
+"#$ -t 11-12"+'\n'
+"#$ -o "+os.getcwd()+"/osprey_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N osprey_tot_6"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge.osprey."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitOspreyscript7(input_file,jobname):
        f_sge=open('osprey_tot7','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-1-0.local"+'\n'
+"#$ -t 13-14"+'\n'
+"#$ -o "+os.getcwd()+"/osprey_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N osprey_tot_7"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge.osprey."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitOspreyscript8(input_file,jobname):
        f_sge=open('osprey_tot8','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-1-1.local"+'\n'
+"#$ -t 15-16"+'\n'
+"#$ -o "+os.getcwd()+"/osprey_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N osprey_tot_8"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge.osprey."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitOspreyscript9(input_file,jobname):
        f_sge=open('osprey_tot9','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-1-1.local"+'\n'
+"#$ -t 17-18"+'\n'
+"#$ -o "+os.getcwd()+"/osprey_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N osprey_tot_9"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge.osprey."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitOspreyscript10(input_file,jobname):
        f_sge=open('osprey_tot10','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-1-0.local"+'\n'
+"#$ -t 19-20"+'\n'
+"#$ -o "+os.getcwd()+"/osprey_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N osprey_tot_10"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge.osprey."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitOspreyscript11(input_file,jobname):
        f_sge=open('osprey_tot11','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-0-15.local"+'\n'
+"#$ -t 21-22"+'\n'
+"#$ -o "+os.getcwd()+"/osprey_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N osprey_tot_11"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge.osprey."+input_file+"_$SGE_TASK_ID"'\n'
)

def submitOspreyscript12(input_file,jobname):
        f_sge=open('osprey_tot12','wb')
        f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q@compute-0-15.local"+'\n'
+"#$ -t 23-24"+'\n'
+"#$ -o "+os.getcwd()+"/osprey_tot.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N osprey_tot_12"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"if [ \"$SGE_TASK_ID\" = \"undefined\" ]; then"+'\n'
+"   SGE_TASK_ID=0"+'\n'
+"fi"+'\n'
+"source ./"+input_file+"_$SGE_TASK_ID/"+"sge.osprey."+input_file+"_$SGE_TASK_ID"'\n'
)
