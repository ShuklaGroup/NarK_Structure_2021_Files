import os

def generateScoreScript(f_output,output_sets,jobname):
       	f_sge=open('sge.scoreScript','wb')
       	f_sge.write("#$ -S /bin/bash"+'\n'
+"#$ -q analysis.q*"+'\n'
+"#$ -pe orte 1"+'\n'
+"#$ -o "+os.getcwd()+"/score.log"+'\n'
+"#$ -e "+os.getcwd()+'\n'
+"#$ -N scoreScript_"+jobname+'\n'
+"#$ -cwd"+'\n'
+""+'\n'
+"cd "+os.getcwd()+'\n'
+""+'\n'
+"source script.sh > "+f_output+'\n'
+"paste temp_"+output_sets+"_1 temp_"+output_sets+"_2 temp_"+output_sets+"_3 > " +output_sets+'\n'
+"rm temp* extract* script.sh"+'\n'
)
       	f_sge.close()

def submitScoreScript(input_file,jobname):
       	cmd="qsub -hold_jid osprey_tot_1"+jobname+",osprey_tot_2"+jobname+",osprey_tot_3"+jobname+",osprey_tot_4"+jobname+",osprey_tot_5"+jobname+",osprey_tot_6"+jobname+",osprey_tot_7"+jobname+",osprey_tot_8"+jobname+",osprey_tot_9"+jobname+",osprey_tot_10"+jobname+",osprey_tot_11"+jobname+",osprey_tot_12"+jobname+" sge.scoreScript"
       	os.system(cmd)

def generateOutputFile(nSets,input_file,input_sets,sets,jobname):
       	ITERATION=input_sets.strip('iter').strip('_').strip('input_sets.txt')
       	output_sets='iter_'+ITERATION+'_output_sets.txt'

       	## Output file, column 1 and 2
       	f_output=open('temp_'+output_sets+'_1','wb')
       	for i in range(nSets):
       		f_output.write(str(len(sets[i]))+'\t'+str(len(sets[i])/2)+'\n')
       	f_output.close()

       	## Generate script file to calculate score
       	f_output='temp_'+output_sets+'_2'
       	count=1
       	cmd="rm -rf script.sh"
       	os.system(cmd)
       	f_script=open('script.sh','wb')
       	for i in range(nSets):
       		f_sql = open('extract_score_'+str(count)+'.sql','wb')
       		folder = input_file+"_"+str(count)
       		f_sql.write('.open '+folder+'/osprey-'+folder+'.db\n')
       		f_sql.write('select max(mean_test_score) from trials_v3;\n')
       		f_sql.close()
       		echo_line = "sqlite3 < extract_score_"+str(count)+".sql"
       		f_script.write(echo_line+'\n')
       		count +=1
       	f_script.close()

       	## Submit the script.sh file in a job, so that it can run after all the osprey jobs are finished
       	generateScoreScript(f_output,output_sets,jobname)
       	submitScoreScript(input_file,jobname)

       	## Output file, column 4 onwards
       	f_output=open('temp_'+output_sets+'_3','wb')
       	for i in range(nSets):
       		for j in range(len(sets[i])):
       			f_output.write(sets[i][j]+'\t')
       		f_output.write('\n')
       	f_output.close()
