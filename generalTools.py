import subprocess as sp
import re
#general tools
def genToolz(location):
    if '/' in location:
        p_name=re.compile(r'/')
        f_name=ploc.split(location)[-1]
    else :
        f_name=location
        
    #binwalk
    binchoice=input('Do you wanna use binwalk on this file,(y/n)')
    if binchoice=='y' :
        sp.run('binwalk -e {}'.format(location),shell=True)
        wd=sp.run('pwd',shell=True,capture_output=True,text=True)
        ext_location=wd+"/_" + f_name + ".extracted"
        print('Files and folders in binwalk extracted folder :')
        sp.run('tree -la {}/'.format(ext_location))
    #foremost
    forechoice=input('Do you wanna use foremost on this file,(y/n) :')
    if forechoice=='y' :
        wd=sp.run('pwd',shell=True,capture_output=True,text=True)
        sp.run('mkdir recovery_{}'.format(f_name))
        sp.run('foremost -i {} -T -o recovery_{}'.format(location,f_name))
    