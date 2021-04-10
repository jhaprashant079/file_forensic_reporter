import subprocess as sp
import re
import os
import sys

import generalTools
import png
import jpg
import bmp
import rtf
import office_files
import pdf
import archive

file=sys.argv[1]
location= os.path.abspath(file)
R=open("Report.md","w")
R.write('')
R.close()
#generalTools
generalTools.genToolz(location)
#fileType and specific modules
fileType=generalTools.f_type(location)
if fileType=="png":
    png.data_from_png(location)
if fileType=="jpg":
    jpg.data_from_jpg(location)
if fileType=="bmp":
    bmp.data_from_bmp(location)
if fileType=="wav":
    wav.data_from_bmp(location)
if fileType=="txt":
    txt.data_from_txt(location)
if fileType=="rtf" :
    rtf.data_from_rtf(location)
if fileType=="docx" or fileType=="docm" or fileType=="xlsx":
    office_files.data_from_officeFile(location)
if  fileType=="pdf" :
    pdf.data_from_pdf(location)
if fileType=="zip" :
    archive.data_from_zip(location)
if fileType=="tar" :
    archive.data_from_tar(location)
if fileType=="bz2" :
    archive.data_from_bz2(location)
if fileType=="gz" :
    archive.data_from_gz(location)
if fileType=="7z" :
    archive.data_from_7z(location)