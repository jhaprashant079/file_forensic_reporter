import subprocess as sp
import re
from generalTools import f_name

def data_from_bmp(loc):
    #zsteg
    b=sp.Popen(r'zsteg {}'.format(loc),shell=True,text=True,capture_output=True).communicate()[0]
    R.write('\n Zsteg Result:\n'+b+"\n")
    #stegolsb
    s=sp.Popen("stegolsb steglsb -r -i {} -o steglsb_out.txt".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate[0]
    if 'Output file written' in s:
        exf=sp.Popen('exiftool steglsb_out.txt',shell=True,stdout=sp.PIPE,text=True).communicate()[0]
        p=re.compile('File Type Extension.*').findall(exf)[0]
        l=re.compile(':').split(p)[1]
        f_type=l[1:]
        sp.Popen('mv steglsb_out.txt steglsb_out.{}'.format(f_type),shell=True)
        print('Extracted file is saved as steglsb_out.{} ,Go and check it'.format(f_type))
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