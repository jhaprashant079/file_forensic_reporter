import subprocess as sp
location=input("Enter file location here : ")
#general tools
#binwalk
sp.run('binwalk -e {}'.format(location),shell=True)
wd=sp.run('pwd',shell=True,capture_output=True,text=True)
ploc=re.compile(r'/')
ext_location=wd+"/_" + ploc.split(location)[-1] + ".extracted"



#file identification using file command
def file_identifier(location):
    filecmd=sp.run('file {}'.format(location),shell=True,capture_output=True,text=True)
    return filecmd
pjpg=re.compile(r'jpg|.jpg')
ppng=re.compile(r'png|.png')



if len(pjpg.findall(filecmd)):
    import jpg.py
if len(ppng.findall(filecmd)):
    import png.py