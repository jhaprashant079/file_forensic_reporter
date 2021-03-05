import subprocess as sp
import re
#general tools
def f_name(location) :
    if '/' in location:
        ploc=re.compile(r'/')
        name=ploc.split(location)[-1]
    else :
        name=location
    return name
def f_type(location):
    exf=sp.Popen('exiftool {}'.format(location),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    p=re.compile('File Type Extension.*').findall(exf)[0]
    l=re.compile(':').split(p)[1]
    return l[1:]
def genToolz(location):
    #exiftool
    print("Exifdata : ")
    exifdata=sp.run('exiftool {}'.format(location),shell=True,capture_output=True,text=True)
    #..
    
    #binwalk
    binchoice=input('Do you wanna use binwalk on this file,(y/n)')
    if binchoice=='y' :
        sp.run('binwalk {}'.format(location),shell=True)
        savebin=input("Do you wanna extract the files (y/n):")
        if savebin=='y':
            wd=sp.run('pwd',shell=True,capture_output=True,text=True)
            ext_location=wd+"/_" + f_name(location) + ".extracted"
            print('Files and folders in binwalk extracted folder :')
            sp.run('tree -la {}/'.format(ext_location))
    #foremost
    forechoice=input('Do you wanna use foremost on this file,(y/n) :')
    if forechoice=='y' :
        wd=sp.run('pwd',shell=True,capture_output=True,text=True)
        sp.run('mkdir recovery_{}'.format(f_name(location)))
        sp.run('foremost -i {} -T -o recovery_{}'.format(location,f_name(location)),shell=True,c)
        print("Recovered files are saved in recovery_{} directory.".format(f_name))
#hexdump & string
def hexdump(location):
    hexchoice=input("Do you wanna see hexdump of the file (y/n):")
    strchoice=input("Do you wanna see strings of the file (y/n),if u r searching for particular word type that after space with y:")
    svchoice=input('Do you wanna save it in a file (y/n):')
    if hexchoice=='y' :
        print("Hexdump of the file: ")
        sp.run(r'hexdump -C {}'.format(loc),shell=True,text=True)
        if strchoice=='y':
            s=sp.Popen('string {} | grep -i {}'.format(location,strchoice[2:]),stdout=sp.PIPE,shell=True,text=true).communicate()[0]
        if svchoice=='y' :
            print(r'The hexdump is saved in file "{}_hexdump"'.format(loc))
            sp.run(r'hexdump -C {} > {}_hexdump',format(loc,loc),shell=True)
        sp.run(r'strings {}'.format(loc),shell=True)  
    if hexchoice!='y' or hexchoice!='n' :
        print("Please give valid response!")