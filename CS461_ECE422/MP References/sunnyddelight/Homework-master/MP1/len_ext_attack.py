__author__ = 'Sunny'
from pymd5 import md5,padding
import urllib
import sys
f=file(sys.argv[1],'r')
o=file('query_updated.txt','w')
orig=f.readline()
outString='http://cs461ece422.org/project1/api?token='
#orig='http://cs461ece422.org/project1/api?token=b301afea7dd96db3066e631741446ca1&user=admin&command1=ListFiles&command2=NoOp'
h=md5(state=orig[6:38].decode("hex"), count=512)
h.update('&command3=DeleteAllFiles')
outString+=h.hexdigest()
outString+=orig[39:]
outString+=urllib.quote(padding(len(orig[39:])*8))
outString+='&command3=DeleteAllFiles'
o.write(outString)