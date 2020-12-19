##
#      	Usage: ipython <codename> <n_clusters> <int_lagtime frames> <dataset number>
##

import sys
import os

##
f_log=open("write_config.log","wb")

if len(sys.argv)!=6:
       	print "This script needs exactly "+str(len(sys.argv)-1)+" arguments, aborting"
       	f_log.write("This script needs exactly three arguments, aborting\n")
       	print "Usage: ipython <codename> <n_clusters> <int_lagtime>"
       	f_log.write("Usage: ipython <codename> <n_clusters> <int_lagtime>\n")
       	sys.exit()

## Writing the osprey config file
f_log.write("Writing config file\n")
config_filename="config_osprey.yaml"

f_config=open(config_filename,"wb")

f_config.write("# osprey configuration file."+'\n'
+"#---------------------------"+'\n'
+"# usage:"+'\n'
+"#  osprey worker config.yaml"+'\n'
+"estimator:"+'\n'
+"    eval: |"+'\n'
+"        Pipeline(["+'\n'
+"                ('tica', tICA()),"+'\n'
+"                ('cluster', MiniBatchKMeans()),"+'\n'
+"                ('msm', MarkovStateModel(n_timescales=5, verbose=False)),"+'\n'
+"        ])"+'\n'
+'\n'
+"# for eval, a python package containing the estimator definitions"+'\n'
+"    eval_scope: msmbuilder"+'\n'
+'\n'
+'\n'
+"strategy:"+'\n'
+"    name: random # or moe, hyperopt_tpe"+'\n'
+'\n'
+"search_space:"+'\n'
+'\n'
)

f_config.write("  tica__n_components:"+'\n'
+"    choices:"'\n'
+"      - 2"+'\n'
+"      - 5"+'\n'
+"      - 10"+'\n'
+"      - 15"+'\n'
+"    type: enum"+'\n'
+'\n'
)

f_config.write("  tica__lag_time:"+'\n'
+"    min: "+sys.argv[3]+'\n'
+"    max: "+sys.argv[3]+'\n'
+"    type: int"+'\n'
+'\n'
)

f_config.write("  cluster__n_clusters:"+'\n'
+"    choices:"'\n'
+"      - 200"+'\n'
+"      - 400"+'\n'
+"      - 500"+'\n'
+"      - 600"+'\n'
+"      - 800"+'\n'
+"      - 1000"+'\n'
+"    type: enum"+'\n'
+'\n'
)

f_config.write("  msm__lag_time:"+'\n'
+"      min: "+sys.argv[2]+'\n'
+"      max: "+sys.argv[2]+'\n'
+"      type: int"+'\n'
+'\n'
)

f_config.write("cv:"+'\n'
+"  name: shufflesplit"+'\n'
+"  params:"+'\n'
+"    n_iter: 5"+'\n'
+"    test_size: 0.5"+'\n'
+'\n'
+"dataset_loader:"+'\n'
+"  name: joblib"+'\n'
)

f_config.write("  params:"+'\n'
+"    filenames: dataset_"+sys.argv[5]+".pkl"+'\n'
+'\n'
)

f_config.write("trials:"+'\n'
+"  uri: sqlite:///osprey-"+sys.argv[5]+".db"+'\n'
)

f_config.close()

f_log.close()
