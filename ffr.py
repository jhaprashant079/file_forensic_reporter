import subprocess as sp
import re
import generalTools
import png
# import jpg
# import bmp
# import .
# . 
# .

location=input("Enter file location here : ")

#generalTools
generalTools.genToolz(location)

#file identification using file command
def file_identifier():
    filecmd=sp.run('file {}'.format(location),shell=True,capture_output=True,text=True)
    return filecmd
fileType=file_identifier()
print(fileType)
pjpg=re.compile(r'jpg',re.IGNORECASE)
ppng=re.compile(r'png',re.IGNORECASE)

if len(ppng.findall(str(fileType)))!=0:
    png.data_from_png(location)