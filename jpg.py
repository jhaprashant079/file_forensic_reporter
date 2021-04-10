import subprocess as sp
import re
from generalTools import f_name
R=open("Report.md",'a')
def data_from_jpg(loc):
    #stegseek
    try:
        p=sp.Popen(r'stegseek {} /usr/share/wordlist/rockyou.txt'.format(loc),shell=True,text=True,capture_output=True).communicate()[0]
        if "not find" in p:
            R.write("Stegseek passphrase not found so either the password is not bruteforceable or maybe there is no hidden data.")
        else:
            R.write("Stegseek output file is in {}.out".format(f_name(loc)))

    except:
        R.write("No embedded data found using stegseek")
    #outguess
    sp.Popen("outgues -r {}  outguessResult.txt".format(loc),shell=True,stdout=sp.PIPE,text=True)
    R.write("Outguess extracted file is outguessResult.txt")
    #
    R.close()