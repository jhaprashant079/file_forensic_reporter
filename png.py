import subprocess as sp
# from ffr.py import location
# sp.run('zsteg {}'.format(location))
def data_from_png(loc) :
    #exiftool
    print("Exiftool data : ")
    sp.run('exiftool {}'.format(location))
    #hexdump and strings
    hexchoice=input("Do you wanna see hexdump and strings of the file (y/n):")
    svchoice=input('Do you wanna save it in a file (y/n):')
    if hexchoice=='y' :
        print("Hexdump of the file: ")
        sp.run(r'hexdump -C {}'.format(loc),shell=True,text=True)
        if svchoice=='y' :
            print(r'The hexdump is saved in file "{}_hexdump"'.format(loc))
            sp.run(r'hexdump -C {} > {}_hexdump',format(loc,loc),shell=True)
        sp.run(r'strings {}'.format(loc),shell=True)
    #zsteg
    print("The data found with zsteg tool: ")
    sp.run('zsteg {}'.format(loc),shell=True,text=True)
    #stegseek
    stegseek_choice=input("Do you wann use stegseek on ur file (y/n) :")
    if stegseek_choice=='y' :
        w_list=input(r"which wordlist to use? 'd' for rockyou.txt(or you can youself specify its path in case of error) and complete location for others :")
        if w_list=='d' :
            sp.run(r'stegseek {} /home/jhaprashant079/Downloads/tools/rockyou.txt'.format(loc),shell=True)
        else :
            sp.run(r'stegseek {} {}'.format(loc,w_list),shell=True)
    
    
    
