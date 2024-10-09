# Hello, this is a script written in Python. See http://www.pyhon.org
#
# Snapper 1.2p
#
# This script will walk a directory (and its subdirectories) and compute
# SHA (Secure Hash Algorithm) for specific files (according to their
# extensions) and ouput a CSV file (suited for loading into a spreadsheet
# editor,a database or simply comparing with diff or ExamDiff.).
#
# You can redirect the output of this script to a file.
# eg.  python snapper.py > todayCheck.csv
#
# This script can be usefull to check system files tampering.
#
# This script is public domain. Feel free to reuse it.
# The author is:
#       Sebastien SAUVAGE
#       <sebsauvage at sebsauvage dot net>
#       http://sebsauvage.net
#
# More quick & dirty scripts are available at http://sebsauvage.net/python/
#
# Directory to scan and extensions are hardcoded below:
directoryStart = r'c:\windows'
extensionList=['.exe','.dll','.ini','.ocx','.cpl','.vxd','.drv','.vbx','.com','.bat','.src',
               '.sys','.386','.acm','.ax', '.bpl','.bin','.cab','.olb','.mpd','.pdr','.jar']

import os,string,sha,stat,sys

def snapper ( directoryStart , extensionList ) :
    os.path.walk( directoryStart, snapper_callback, extensionList )

def snapper_callback ( extensionList , directory, files ) :
    sys.stderr.write('Scanning '+directory+'\n')
    for fileName in files:
        if os.path.isfile( os.path.join(directory,fileName) ) :
            if string.lower(os.path.splitext(fileName)[1]) in extensionList :
                filelist.append(fileSHA ( os.path.join(directory,fileName) ))

def fileSHA ( filepath ) :
    sys.stderr.write('  Reading '+os.path.split(filepath)[1]+'\n')
    file = open(filepath,'rb')
    digest = sha.new()
    data = file.read(65536)
    while len(data) != 0:
        digest.update(data)
        data = file.read(65536)
    file.close()
    return '"'+filepath+'",'+str(os.stat(filepath)[6])+',"'+digest.hexdigest()+'"'

sys.stderr.write('Snapper 1.1p - http://sebsauvage.net/python/\n')
filelist = []
snapper( directoryStart , extensionList )
sys.stderr.write('Sorting...\n')
filelist.sort()
filelist.insert(0, '"File path","File size","SHA"' )
sys.stderr.write('Printing...\n')
for line in filelist:
	print line
sys.stderr.write('All done.\n')
