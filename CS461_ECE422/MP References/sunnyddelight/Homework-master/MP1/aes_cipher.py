__author__ = 'Sunny'
import base64
import array
from Crypto.Cipher import AES
key='06f2495ff34a9e6c7d0f00090c6493f62751f7746d41e09482da8fff20ddd828'.decode('hex')
iv='e29c65ce63dd7d3b3cc66ae121712211'.decode("hex")
text='ea44186cc4c2adb968d126aa5f1471b31ae5f51683b31f65394f245de00ceb23dcef4061e7242d171c5b847d52ea10f306bab7e24638709fe1f5005f9927d7b056ba14b14703a32ea21c3cb7120f600ad688499123252c80d89c5c68c6ad104b'.decode("hex")
mode=AES.MODE_CBC
decryptor=AES.new(key,mode,iv)
print decryptor.decrypt(text)
