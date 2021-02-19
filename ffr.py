import subprocess as sp
import re
import png
# import jpg
# import bmp
# import .
# . 
# .


location=input("Enter file location here : ")
#general tools
#binwalk
binchoice=input('Do you wanna use binwalk on this file,(y/n)')
if binchoice=='y' or binchoice=='Y' :
    sp.run('binwalk -e {}'.format(location),shell=True)
    wd=sp.run('pwd',shell=True,capture_output=True,text=True)
    ploc=re.compile(r'/')
    ext_location=wd+"/_" + ploc.split(location)[-1] + ".extracted"
    print('Files and folders in binwalk extracted folder :')
    sp.run('tree -la {}/'.format(ext_location))
    



#file identification using file command
def file_identifier():
    filecmd=sp.run('file {}'.format(location),shell=True,capture_output=True,text=True)
    return filecmd
fileType=file_identifier()
print(fileType)
pjpg=re.compile(r'jpg',re.IGNORECASE)
ppng=re.compile(r'png',re.IGNORECASE)

# if len(pjpg.findall(str(fileType)))!=0:
#     import jpg.py
if len(ppng.findall(str(fileType)))!=0:
    png.data_from_png(location)