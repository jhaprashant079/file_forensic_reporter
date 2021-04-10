import subprocess as sp
import re
import hashlib
from generalTools import md5hash
from generalTools import sha1hash
from generalTools import sha256hash
R=open("Report.md","a")
def data_from_pdf(loc):
    #exiftool
    #hash
    R.write("md5 hash of the file is--> "+md5hash(loc)+"\n")
    R.write("sha1 hash of the file is--> "+sha1hash(loc)+"\n")
    R.write("sha256 hash of the file is--> "+sha256hash(loc)+"\n")
    a=sp.Popen("perl /JohnTheRipper/run/pdf2john.pl {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    if "not encrypted" in a:
        R.write("PDf is not encrypted .\n")
    else:
        R.write("Pdf is password encrypted and Password hash of "+a+"\n")
    #pdf-parser
    b=sp.Popen("pdf-parser -a {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    R.write(b+" \n")
    #pdfid
    c=sp.Popen("pdfid {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    R.write(c+" \n")
    R.close()