import subprocess as sp
import re
from generalTools import f_name
from generalTools import f_type

R=open('Report.md','a')
def data_from_png(loc):
    #pngcheck
    a=sp.Popen(r'pngcheck {}'.format(loc),shell=True,text=True,capture_output=True).communicate()[0]
    R.write("pngcheck result:\n"+a+"\n")
    #zsteg
    b=sp.Popen(r'zsteg {}'.format(loc),shell=True,text=True,capture_output=True).communicate()[0]
    R.write('\n Zsteg Result:\n'+b+"\n")
    #stegolsb
    s=sp.Popen("stegolsb steglsb -r -i {} -o steglsb_out.txt".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    if 'Output file written' in s:
        ex=f_type(loc)
        sp.Popen('mv steglsb_out.txt steglsb_out.{}'.format(ex),shell=True)
        R.write('Extracted file is saved as steglsb_out.{} ,Go and check it'.format(ex))
    #stegseek
    try:
        p=sp.Popen(r'stegseek {} /usr/share/wordlist/rockyou.txt'.format(loc),shell=True,text=True,capture_output=True).communicate()[0]
        if "not find" in p:
            R.write("Stegseek passphrase not found so either the password is not bruteforceable or maybe there is no hidden data.")
        else:
            R.write("Stegseek output file is in {}.out".format(f_name(loc)))

    except:
        R.write("No embedded data found using stegseek")
    R.close()