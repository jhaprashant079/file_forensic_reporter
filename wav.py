import subprocess as sp
import re
from generalTools import f_type
r=open('Report.md','a')
def data_from_wav(loc):
    #spectrogram
    try:
        sp.Popen(r"sox {} -n spectogram".format(loc),shell=True)
        R.write("Spectogram in spectogram.png file.")'
    except:
        continue
    #wavsteg
    s=sp.Popen('stegolsb wavsteg -r -i {} -o wavsteg_out.txt -n 1 -b 1000'.format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    if 'Written output file' in s:
        ex=f_type(loc)
        sp.Popen('mv wavsteg_out.txt wavsteg_out.{}'.format(ex),shell=True)
        R.write('Extracted file is saved as wavsteg_out.{} ,Go and check it'.format(ex))
    #stegseek
    try:
        p=sp.Popen(r'stegseek {} /usr/share/wordlist/rockyou.txt'.format(loc),shell=True,text=True,capture_output=True).communicate()[0]
        if "not find" in p:
            R.write("Stegseek passphrase not found so either the password is not bruteforceable or maybe there is no hidden data.")
        else:
            R.write("Stegseek output file is in {}.out".format(f_name(loc)))

    except:
        R.write("No embedded data found using stegseek")