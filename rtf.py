import subprocess as sp
import re
def data_from_rtf(loc):
    #rtfobj
    b=sp.Popen("rtfobj {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    print(b.splitlines()[3:])
    #pyxswf
    a=sp.Popen("pyxswf -xf {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    print(a)