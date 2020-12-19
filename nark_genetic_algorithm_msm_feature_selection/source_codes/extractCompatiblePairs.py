"""
       	Extract compatiblePairs.txt file from an already score set of choices from the brute force algorithm
"""

# Add file name here
input_file=''
output_file='compatiblePairs.txt'

f=open('input_file','rb')
f1=open('output_file','wb')

for line in f:
       	cols=line.strip().split('\t')
       	if (cols[1]=='1'):
       		print cols[3], cols[4]
       		f1.write(cols[3]+'\t'+cols[4]+'\n')
