import subprocess as sp
import re
from oletools.olevba import VBA_Parser, TYPE_OLE, TYPE_OpenXML, TYPE_Word2003_XML, TYPE_MHTML
import oletools.oleid


R=open("Report.md","a")
def data_from_officeFile(loc):
    #mraptor
    s=sp.Popen("mraptor {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    s=re.sub("^(.*\n.*\n)",'',s)
    R.write("\nData from mraptor:\n:"+s+"\n")
    #olevba
    a=sp.Popen("olevba --reveal --decode {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    a=re.sub("^(.*\n)",'',a)
    R.write("Data from olevba:\n"+a+"\n")
    #oleid
    a=sp.Popen("oleid {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    a=re.sub("^(.*\n.*\n.*\n)",'',a)
    z=re.findall('OLE format.*',a,re.MULTILINE)[0]
    R.write("Data from oleid:\n"+a+"\n")
    #msodde
    a=sp.Popen("msodde -a {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    a=re.sub("^(.*\n.*\n.*\n)",'',a)
    R.write("Data from msodde:\n"+a+"\n")
    #detecting and extracting a SWF file from a Word document
    if "False" not in z:
        s=sp.Popen("pyxswf -o {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
        R.write("Data from pyxwf:\n"+s+'\n')
    #oleobj
    a=sp.Popen("oleobj {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    a=re.sub("^(.*\n.*\n.*\n)",'',a)
    R.write("Data from olevbj:\n"+a+"\n")
    #olemeta
    if "False" not in z:
        a=sp.Popen("olemeta {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
        a=re.sub("^(.*/n.*/n)",'',a)
        R.write("Data from olemeta:\n"+a+"\n")
    R.close()