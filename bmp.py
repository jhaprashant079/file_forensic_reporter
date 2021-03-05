import subprocess as sp
import re
from generalTools import hexdump
from generalTools import f_name

def data_from_bmp(loc):
    #hexdump
    hexdump(loc)
    #zsteg
    print("The data found with zsteg tool: ")
    sp.run('zsteg {}'.format(loc),shell=True,text=True)
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
    stegseek_choice=input("Do you wanna use stegseek on ur file (y/n) :")
    if stegseek_choice=='y' :
        try:
            w_list=input(r"which wordlist to use? 'd' for rockyou.txt(or you can youself specify its path in case of error) and complete location for others :")
            if w_list=='d' :
                p=sp.run(r'stegseek {} /home/jhaprashant079/Downloads/tools/rockyou.txt'.format(loc),shell=True,text=True,capture_output=True).communicate()[0]
            else :
                p=sp.run(r'stegseek {} {}'.format(loc,w_list),shell=True,text=True,capture_output=True).communicate()[0]
            if "not find" in p:
                print("passphrase not found so try changing wordlist ,if problem persists then the password is not bruteforceable or maybe there is no hidden data.")
            else:
                print("output file is in {}.out".format(f_name(loc)))

        except:
            print("No embedded data found")
    