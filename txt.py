import subprocess as sp
R=open("/home/jhaprashant079/project/README.md","a")
def data_from_txt(loc):
    #stegsnow
    a=sp.Popen("stegsnow -C {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate()[0]
    R.write(a+"\n")
    R.close()