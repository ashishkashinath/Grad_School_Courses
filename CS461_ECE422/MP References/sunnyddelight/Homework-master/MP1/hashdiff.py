__author__ = 'Sunny'
from Crypto.Hash import SHA256
string1='UNDER THE NAME TASTES GOOD TASTES HAPPY THIS US BRAND MADE ITS DEBUT IN CHINA'
string2='UNDER THE NAME TASTES COOD TASTES HAPPY THIS US BRAND MADE ITS DEBUT IN CHINA'
h1=SHA256.new(data=string1)
h2=SHA256.new(data=string2)
hash1=h1.hexdigest()
hash2=h2.hexdigest()
count=0
decodeArray=[0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]
for i in range(0,len(hash1)):
    count+=decodeArray[int(hash1[i],16) ^ int(hash2[i],16)]
print count