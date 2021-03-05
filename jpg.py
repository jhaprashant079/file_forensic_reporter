import subprocess as sp
import re
from generalTools import hexdump
from generalTools import f_name
def data_from_jpg(loc)
    #hexdump
    print(hexdump(loc))
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