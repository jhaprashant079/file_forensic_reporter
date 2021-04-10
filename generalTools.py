import subprocess as sp
import re
import hashlib
#general tools
R=open("Report.md","a")
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
    a=sp.Popen('exiftool {}'.format(location),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    exifdata=re.sub(r'(File Permissions.*\n)|(ExifTool Version Number.*\n)','',a)
    R.write("Exifdata======================\n"+exifdata)
    
    #hexdump & string
    b=sp.Popen(r'xxd {} | head'.format(location),shell=True,text=True,stdout=sp.PIPE).communicate()[0]
    c=sp.Popen(r'xxd {} | tail'.format(location),shell=True,text=True,stdout=sp.PIPE).communicate()[0]
    d=sp.Popen(r'strings {} | tail'.format(location),shell=True,text=True,stdout=sp.PIPE).communicate()[0] 
    R.write("Head of hexdump:\n"+b+"\nTail of hexdump:\n"+c+"\nLast lines of Readable characters from file:\n"+d+"\n")
    
    #binwalk
    try:
        e=sp.Popen('binwalk {}'.format(location),shell=True,text=True,stdout=sp.PIPE).communicate()[0]
        f=re.sub(r'(-{80}\n)|(.*Zlib.*)|(^0\s.*\n)','',e,re.MULTILINE)
        if len(re.findall(r'.+',f))>0:
            l=sp.Popen('binwalk -e {}'.format(location),shell=True,text=True,stdout=sp.PIPE).communicate()[0] 
            wd=sp.Popen('pwd',shell=True,stdout=sp.PIPE,text=True).communicate()[0]
            ext_location=wd+"/_" + f_name(location) + ".extracted"
            R.write('Binwalk extracted result in '+ ext_location+'/n')
        #foremost
        g=sp.Popen(r'foremost {}'.format(location),shell=True,text=True,stdout=sp.PIPE).communicate()[0]
        if len(re.findall(r'^.*\n\|\*\|',g,re.MULTILINE))==0 :
            wd=sp.run('pwd',shell=True,capture_output=True,text=True)
            sp.run('mkdir recovery_{}'.format(f_name(location)),shell=True)
            sp.run('foremost -i {} -T -o recovery_{}'.format(location,f_name(location)),shell=True)
            R.write("Recovered files are saved in recovery_{} directory.".format(f_name))
    except:
        R.write('binwalk and foremost failed.')
def md5hash(filename):
    h = hashlib.md5()
    with open(filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()
def sha1hash(filename):
    h = hashlib.sha1()
    with open(filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()
def sha256hash(filename):
    h = hashlib.sha256()
    with open(filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()
    R.close()