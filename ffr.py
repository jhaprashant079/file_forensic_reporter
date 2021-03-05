import subprocess as sp
import re
import generalTools
import png
import jpg
import bmp

location=input("Enter file location here : ")

#generalTools
generalTools.genToolz(location)
#fileType and specific modules
fileType=generalTools.f_type(location)
if fileType=="png":
    png.data_from_png(location)
if fileType=="jpg:
    jpg.data_from_jpg(location)
if fileType=="bmp":
    bmp.data_from_bmp(location)
if fileType=="zip" :
    zip.data_from_zip(location)