import subprocess as sp
import re
from oletools.olevba import VBA_Parser, TYPE_OLE, TYPE_OpenXML, TYPE_Word2003_XML, TYPE_MHTML
import oletools.oleid


R=open("/home/jhaprashant079/project/README.md","a")
def data_from_doc_or_xls(loc):
    #mraptor
    s=sp.Popen("mraptor {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate[0]
    R.write(s)
    #olemeta
    a=sp.Popen("olemeta {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate[0]
    R.write(a)
    #oletime
    b=sp.Popen("oletime {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate[0]
    R.write(b)
    #olevba
    #parsing office files
    filedata = open(myfile, 'rb').read()
    vbaparser = VBA_Parser(loc, data=filedata)
    if vbaparser.detect_vba_macros():#Detect VBA macros
        #extracting vba macro source code
        for (filename, stream_path, vba_filename, vba_code) in vbaparser.extract_macros():
            R.write('-'*79 + '\n')
            R.write('Filename    :' + filename + '\n')
            R.write('OLE stream  :' + stream_path + '\n')
            R.write('VBA filename:' + vba_filename + '\n')
            R.write('- '*39 + '\n')
            R.write(vba_code + '\n')
        #analyze source code
        results = vbaparser.analyze_macros()
        for kw_type, keyword, description in results:
            R.write('type=%s - keyword=%s - description=%s' % (kw_type, keyword, description))
        #Deobfuscate VBA Macro Source Code
        R.write("Deobfuscated macro source code : \n")
        R.write(vbaparser.reveal())
    #oleid
    oid = oletools.oleid.OleID(loc)
    indicators = oid.check()
    for i in indicators:
        R.write("#OLEID:")
        R.write('Indicator id=%s name="%s" type=%s value=%s' % (i.id, i.name, i.type, repr(i.value)) + "\n")
        R.write('description:' + i.description + "\n")
    #detecting and extracting a SWF file from a Word document
    s=sp.Popen("pyxswf -o {}".format(loc),shell=True,stdout=sp.PIPE,text=True).communicate[0]
    R.write(s+'\n')
    #oledump.py worddoc.doc