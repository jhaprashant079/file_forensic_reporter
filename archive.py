import subprocess as sp
import re
import generalTools
R=open("/home/jhaprashant079/project/README.md","a")
def data_from_zip(loc):
    sp.Popen("unzip {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    R.write("Zip file has been unzipped.\n")
    a=sp.Popen("zip2john {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    if "not encrypted" in a:
        R.write("Zip is not encrypted .\n")
    else:
        R.write("Zip is password encrypted and Password hash of "+a+"\n")
def data_from_7z(loc):
    sp.Popen("7z e {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    R.write("7z file has been unarchived.\n")
def data_from_bz2(loc):
    sp.Popen("bzip2 -d {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    R.write("bzip2 file has been unarchived.\n")
def data_from_gz(loc):
    sp.Popen("gzip -d {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    R.write("gzip file has been unarchived.\n")
def data_from_tar(loc):
    sp.Popen("tar -xf {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    R.write("tar file has been unarchived.\n")
