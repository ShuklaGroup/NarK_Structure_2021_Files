import glob
dir_mdcrd = "/home/jf8/ds02/unstripped/NarK-MD/revision/run85/"
for f in glob.glob(dir_mdcrd + '*.mdcrd'):
    a = f.split('/')[-1]
    name = a.strip('.mdcrd')
    filename = 'cpp_'+name+'.in'
    f = open(filename, 'w')
    f.write('parm NarK-MD.prmtop \n')
    f.write('trajin ' + dir_mdcrd +  name+ '.mdcrd\n')
    f.write('strip :PA\n')
    f.write('strip :PC\n')
    f.write('strip :OL\n')
    f.write('strip :WAT\n')
    f.write('center origin\n')
    f.write('autoimage origin\n')
    f.write('trajout ' + name +'_strip.mdcrd\n')
    f.write('run \n')
    f.write('quit')
