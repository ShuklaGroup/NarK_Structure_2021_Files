# GeneticAlgorithm

### Extract all compatible pairs
<li> This script is a little heavy and may take long depending on the size of the dataset
<li> Genrates a file named compatiblePairs.txt
<li> Requires the input file as input
```ipython <sourceCodePath>/generatePairs.py <path-to-input-file>```

### To do the rest of the analysis, use the wrapper script, run 
<li> Make sure you have the compatiblePairs.txt already generated and in the current folder
<li> Requires the input file as input
```source <sourceCodePath>/run <path-to-input-file>```

### Clean your directory 
<li> After running the program, you can clean your directory of temporary file using the following this script, but it may erase certain log files that you could want to look at later
```source <sourceCodePath>/clean```

### Format for input file
<li> Do not tinker much with the white spaces, the bash scripts are extremely fastidious about these things
```
# Source code path
sourceCodePath='/Softwares/optimalProbes'

# Job Identifiers
jobname = "test-01"

# Genetic Algorithm Parameters
N_ITERATIONS=20
populationSize=20
percentMutation=50
percentCrossover=20

# Experiment Constraints
DEER_low = 1.8
DEER_up = 6.0
min_probes=2
max_probes=10

# Trajectory Information
topology_file = "/home/trajectories/test.pdb"
traj_path = "/home/trajectories"
trajectory_format = "dcd"

# Protein Topology Information
elements=[range(0,5),range(5,37),range(37,44),range(44,73),range(73,81)]
not_allowed=range(8,34)+range(47,70)
intra=range(21,58)+range(97,137)
extra=range(0,21)+range(58,97)

# Osprey Parameters
clusters=200
lagtime=500
```
