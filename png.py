import subprocess as sp
import re
from generalTools import hexdump
from generalrTools import f_name
from generalTools import f_type

def data_from_png(loc):
    #hexdump
    print(hexdump(loc))
    #zsteg
    print("The data found with zsteg tool: ")
    sp.run('zsteg {}'.format(loc),shell=True,text=True)
    #stegolsb
    s=sp.Popen("stegolsb steglsb -r -i {} -o steglsb_out.txt".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    if 'Output file written' in s:
        ex=f_type(loc)
        sp.Popen('mv steglsb_out.txt steglsb_out.{}'.format(ex),shell=True)
        print('Extracted file is saved as steglsb_out.{} ,Go and check it'.format(ex))